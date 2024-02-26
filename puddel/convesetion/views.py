from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item

from .forms import ConvesetionMessageForm
from .models import Convesetion

# Create your views here.
@login_required
def new_convesetion(request, item_pk):
    item=get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    convesetion=Convesetion.objects.filter(item=item).filter(members__in=[request.user.id])

    if convesetion:
        return redirect('convesetion:detail', pk=convesetion.first().id)

    if request.method == 'POST':
        form = ConvesetionMessageForm(request.POST)

        if form.is_valid():
            convesetion=Convesetion.objects.create(item=item)
            convesetion.members.add(request.user)
            convesetion.members.add(item.created_by)
            convesetion.save()

            convesetion_message=form.save(commit=False)
            convesetion_message.convesetion=convesetion
            convesetion_message.created_by=request.user
            convesetion_message.save()

            return redirect('item:detail', pk=item_pk)
        
    else:
            form=ConvesetionMessageForm()

    return render (request, 'convesetion/new.html',{
            'form':form
        })

@login_required
def inbox(request):
    convesetions = Convesetion.objects.filter(members__in=[request.user.id])

    return render(request, 'convesetion/inbox.html', {'convesetions': convesetions})

@login_required
def detail(request, pk):
      convesetion = Convesetion.objects.filter(members__in=[request.user.id]).get(pk=pk)

      if request.method == 'POST':
           form=ConvesetionMessageForm(request.POST)
           if form.is_valid():
                convesetion_message=form.save(commit=False)
                convesetion_message.convesetion=convesetion
                convesetion_message.created_by=request.user
                convesetion_message.save()

                convesetion.save()

                return redirect('convesetion:detail', pk=pk)
      else:
            form=ConvesetionMessageForm()
           
      return render(request, 'convesetion/detail.html',{
           'convesetion':convesetion,
           'form':form

      })
