from django.shortcuts import render, get_object_or_404, redirect
from .models import Sprint
from .forms import SprintCreateForm
from .forms import SprintUpdateForm

def sprint_list(request):
    sprints = Sprint.objects.all()
    if request.method == 'POST':
        form = SprintCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprint_list')
    else:
        form = SprintCreateForm()  # Substitua SprintForm por SprintCreateForm aqui

    return render(request, 'core/sprint_list.html', {'sprints': sprints, 'form': form})

    return render(request, 'core/sprint_list.html', {'sprints': sprints, 'form': form})

def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = SprintUpdateForm(request.POST, instance=sprint)
            if form.is_valid():
                form.save()
                return redirect('sprint_detail', pk=sprint.pk)
        elif 'delete' in request.POST:
            sprint.delete()
            return redirect('sprint_list')
    else:
        form = SprintUpdateForm(instance=sprint)

    return render(request, 'core/sprint_detail.html', {'sprint': sprint, 'form': form})

def sprint_create(request):
    if request.method == 'POST':
        form = SprintCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprint_list')
    else:
        form = SprintCreateForm()
    return render(request, 'core/sprint_create.html', {'form': form})