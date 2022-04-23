from App.models import User, Friend
from App.database import db

def create_friend (userID, friendUID):
    user= User.query.get(friendUID)
    newFriend= Friend(userID=userID, friendUID=friendUID)
    db.session.add(newFriend)
    db.session.commit()

def get_all_friends_json (userID):
    friends= Friend.query.filter_by(userID=userID)
    if not friends:
        return []
    friends = [f.toDict() for f in friends]
    return friends

def get_all_friends (userID):
    return Friend.query.filter_by(userID=userID)

def delete_friend (friendID):
    friend= Friend.query.get(friendID)
    if not friend:
        return(f'No friend with ID {friendID} exists')
    db.session.delete(friend)
    db.session.commit()
    return (f"Friend with ID {friendID} deleted!")

def delete_all_friends(userID):
    count=0
    friends=Friend.query.filter_by(userID=userID)
    if not friends:
        return ('0')
    for f in friends:
        db.session.delete(f)
        count=count+1
    db.session.commit()
    return(f'{count} friend(s) deleted!')
