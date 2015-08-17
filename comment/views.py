from datetime import datetime

from comment.models import Comment, CommentEvent
from account.models import CustomUser
from django.http import HttpResponse
import json


def add_comment(request):
    if request.is_ajax():
        comment = Comment(text=request.POST.get('comment-text', None), user_id=request.user.id,
                          time=datetime.now())
        comment.save()
        CommentEvent(comment_id=comment.id, event_id=request.POST.get('event', None)).save()

        results = []
        comment_json = {}
        comment_json['addedtime'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        comment_json['user'] = request.user.username
        results.append(comment_json)
        data = json.dumps(results)
        mimetype = 'application/json'

        return HttpResponse(data, mimetype)


def comments(event_id):
    comment_type_list = []
    for comment_id in CommentEvent.objects.filter(event_id=event_id):
        comment = Comment.objects.get(id=comment_id.comment_id)
        writer = CustomUser.objects.get(id=comment.user_id).username
        comment_type_list.append((comment, writer))

    return comment_type_list