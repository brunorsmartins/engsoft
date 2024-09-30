from django.shortcuts import render, get_object_or_404, redirect
from .models import Sprint
from .forms import SprintCreateForm, SprintUpdateForm, DailyForm

def sprint_list(request):
    sprints = Sprint.objects.all()
    if request.method == 'POST':
        form = SprintCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprint_list')  # Use redirect para evitar re-submissão de formulário
    else:
        form = SprintCreateForm()  # Substitua SprintForm por SprintCreateForm aqui

    return render(request, 'core/sprint_list.html', {'sprints': sprints, 'form': form})

def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    dailys = sprint.daily_set.all()  # Pegar todas as Dailys associadas à Sprint

    # Lidar com a criação de uma nova Daily
    if request.method == 'POST':
        daily_form = DailyForm(request.POST)
        if daily_form.is_valid():
            daily = daily_form.save(commit=False)
            daily.sprint = sprint
            daily.save()
            return redirect('sprint_detail', pk=sprint.pk)
    else:
        daily_form = DailyForm()

    media_notas = sprint.calcular_media()

    return render(request, 'core/sprint_detail.html', {
        'sprint': sprint,
        'form': SprintUpdateForm(instance=sprint),
        'daily_form': daily_form,
        'dailys': dailys,
        'media_notas': media_notas
    })

def sprint_create(request):
    if request.method == 'POST':
        form = SprintCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprint_list')  # Redirecionar após criar a sprint
    else:
        form = SprintCreateForm()
    return render(request, 'core/sprint_create.html', {'form': form})

def home_redirect(request):
    return redirect('sprint_list')