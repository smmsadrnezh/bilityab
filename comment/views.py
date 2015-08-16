from datetime import datetime

from django.http import HttpResponseRedirect

from comment.models import Comment, CommentEvent
from account.models import CustomUser


def add_comment(request):
    if request.method == 'POST':
        comment = Comment(text=request.POST.get('comment-text', None), user_id=request.POST.get(request.user.id, None),
                          time=datetime.now())
        comment.save()
        CommentEvent(comment_id=comment.id, event_id=request.POST.get('event', None))
        return HttpResponseRedirect()


def comments(event_id):
    comment_type_list = []
    for comment_id in CommentEvent.objects.filter(event_id=event_id):
        comment = Comment.objects.get(id=comment_id.comment_id)
        writer = CustomUser.objects.get(id=comment.user_id).username
        comment_type_list.append((comment, writer))

    return comment_type_list