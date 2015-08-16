from comment.models import Comment,CommentEvent
from account.models import CustomUser

def comments(event_id):
    print(Comment.objects.get(id=2).text)
    comment_type_list = []
    for comment_id in CommentEvent.objects.filter(event_id=event_id):
        comment = Comment.objects.get(id=comment_id.comment_id)
        writer = CustomUser.objects.get(id=comment.user_id).username
        comment_type_list.append((comment, writer))

    return comment_type_list