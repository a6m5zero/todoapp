from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import ToDoItem
from tasks.forms import AddTaskForm, TodoItemForm, TodoItemExportForm
from django.views import View
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return HttpResponse("HELLO BITCH. I AM RUNNIG THIS SHEAT СУКА БЛЯТЬ")     

def task_list(request):
    all_tasks = ToDoItem.objects.all()
    return render(request, 'tasks/list.html', {'tasks': all_tasks})

def delete_task(request,uid):
    print(f'DELETE {uid}')
    ToDoItem.objects.filter(id = uid).delete()
    messages.warning(request, "Задача удалена")
    return redirect("/tasks/list/")


def complete_task(request,uid):
    print (f'COMPLETE {uid}')
    t = ToDoItem.objects.get(id = uid)
    t.is_completed = True
    t.save()
    return HttpResponse('OK')

def task_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return reverse("tasks:list")
    else:
        form = TodoItemForm()
    return render(request, "tasks/create.html", {"form": form})

def add_task(request):
    if request.method == "POST":
        desc = request.POST["description"]
        t = ToDoItem(description=desc)
        t.save()
    return HttpResponseRedirect(reverse("tasks:list"))


class TaskListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"

    def get_queryset(self):
        u = self.request.user
        return u.tasks.all()


class TaskListView_c(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pass
    def get(self, request, *args, **kwargs):
        tasks = ToDoItem.objects.all()
        




class TaskCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.owner = request.user
            new_task.save()
            return HttpResponseRedirect(reverse("tasks:list"))
        return render(request, "tasks/create.html", {"form": form})
    
    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return render(request, "tasks/create.html", {"form": form})

class TaskDetailsView(DetailView):
    model = ToDoItem
    template_name = 'tasks/details.html'

# class izmenenia zadachi
class TaskEditView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        t = ToDoItem.objects.get(id = pk)
        form = TodoItemForm(request.POST, instance = t)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.owner = request.user
            new_task.save()
            return HttpResponseRedirect(reverse("tasks:list"))
        return render(request, "tasks/edit.html", {"form": form, "task": t})
    
    def get(self, request, pk, *args, **kwargs):
        t = ToDoItem.objects.get(id = pk)
        form = TodoItemForm(instance=t)
        return render(request, "tasks/edit.html", {"form": form, "task": t})


# class exporta zadach po e-mail
class TaskExportView(LoginRequiredMixin, View):
    def generate_body(self, user, priorities):
        q = Q()
        if priorities["prio_high"]:
            q = q | Q(priority = ToDoItem.PRIORITY_HIGH)
        if priorities["prio_med"]:
            q = q | Q(priority = ToDoItem.PRIORITY_MEDIUM)
        if priorities["prio_low"]:
            q = q | Q(priority = ToDoItem.PRIORITY_LOW)
        tasks = ToDoItem.objects.filter(owner=user).filter(q).all()

        body = "Ваши задачи и приоритеты:\n"
        for t in list(tasks):
            if t.is_completed:
                body += f"[X] {t.description} ({t.get_priority_display()})\n"
            else:
                body += f"[ ] {t.description} ({t.get_priority_display()})\n"
    
        return body
    
    def post(self, request, *args, **kwargs):
        form = TodoItemExportForm(request.POST)
        if form.is_valid():
            email = request.user.email
            body = self.generate_body(request.user, form.cleaned_data)
            send_mail("Задачи", body, settings.EMAIL_HOST_USER, [email])
            messages.success(request, "Задачи были отправлены на почту %s" % email)
        else:
            messages.error(request, "Что-то пошло не так, попробуйте ещё раз")
        return redirect(reverse("tasks:list"))
    
    def get(self, request, *args, **kwargs):
        form = TodoItemExportForm()
        return render(request, "tasks/export.html", {"form": form})



