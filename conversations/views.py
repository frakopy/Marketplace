from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm


@login_required(login_url="login")
def create_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    condition = Q(members__in=[request.user]) & Q(item=item)
    conversation = Conversation.objects.filter(condition).first()

    if conversation:
        conv_pk = conversation.pk
        return redirect(reverse("conversation:detail", kwargs={"conversation_pk": conv_pk}))

    form = ConversationMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Create a new conversation object
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            # Create a new conversation message object
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.sender = request.user
            conversation_message.save()

            url = reverse("item_detail", kwargs={"pk": item_pk}) + "?message_sent"

            return redirect(url)

    return render(request, "conversation/create_conversation.html", {"form": form})


@login_required(login_url="login")
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])
    return render(request, "conversation/inbox.html", {"conversations": conversations})


@login_required(login_url="login")
def detail(request, conversation_pk):
    # Get the conversation for the current user, filtering by members to prevent other users from accessing
    # the conversation. If the path is known, someone could potentially add a random primary key (pk) at
    # the end of the URL.
    conversation = Conversation.objects.filter(members__in=[request.user]).get(pk=conversation_pk)
    messages = conversation.messages.all()

    form = ConversationMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # Create a new conversation message object
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.sender = request.user
            conversation_message.save()

            # To update the attribute modified_at in the Conversation model
            conversation.save()

    return render(
        request,
        "conversation/detail.html",
        {"conversation": conversation, "messages": messages, "form": form},
    )
