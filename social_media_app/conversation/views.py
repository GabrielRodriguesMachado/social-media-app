from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ConversationMessageForm
from .models import Conversation


@login_required
def conversation_list(request):
    user = request.user
    conversations = user.conversations.all()

    return render(
        request,
        "conversation/conversation_list.html",
        {"conversations": conversations},
    )


@login_required
def show_conversation(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    messages = conversation.messages.all()

    context = {
        'conversation': conversation,
        'messages': messages,
    }

    return render(request, 'conversation/conversation_detail.html', context)


@login_required
def new_conversation(request, pk):
    user = request.user
    recipient = get_object_or_404(User, pk=pk)

    conversation = Conversation.objects.filter(members=user).filter(
        members=recipient
    )

    if conversation.exists():
        return redirect("conversation_detail", pk=conversation.first().pk)
    else:
        create_conversation = Conversation.objects.create()
        create_conversation.members.add(user, recipient)
        create_conversation.save()

        return redirect("conversation_detail", pk=create_conversation.pk)


@login_required
def send_message(request, conversation_pk):
    conversation = get_object_or_404(Conversation, pk=conversation_pk)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            return redirect("conversation_detail", pk=conversation.pk)
