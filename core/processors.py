from conversations.models import ConversationMessage


def get_messages(request):
    if request.user.is_authenticated:
        conversations = request.user.conversations.all()
        user = request.user
        filtered_messages = ConversationMessage.objects.filter(
            read=False, conversation__in=conversations
        ).exclude(sender=user)

        return {
            "num_messages": len(filtered_messages),
            "filtered_messages": filtered_messages,
        }

    return {"num_messages": 0, "filtered_messages": []}
