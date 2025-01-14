from pydispatch import dispatcher

USER_REGISTERED = 'user-registered'
USER_LOGGED_IN = 'user-logged-in'

class User:
  def __init__(self,username) -> None:
    self.username = username
    
  def register(self):
    print(f'{self.username} has been registered')
    dispatcher.send(signal=USER_REGISTERED, sender=self)
    
  def login(self):
    print(f'{self.username} has been logged in')
    dispatcher.send(signal=USER_LOGGED_IN, sender=self)
    
class NotificationService:
  def __init__(self) -> None:
    dispatcher.connect(self.user_registered, signal=USER_REGISTERED, sender=dispatcher.Any)
    dispatcher.connect(self.user_logged_in, signal=USER_LOGGED_IN, sender=dispatcher.Any)
    
  def user_registered(self, sender):
    print(f'Notification service: {sender.username} has been registered')
    
  def user_logged_in(self, sender):
    print(f'Notification service: {sender.username} has been logged in')
    
if __name__ == '__main__':
  notification_service = NotificationService()
  
  user1 = User('Alice')
  user1.register()
  user1.login()
  
  user2 = User('Bob')
  user2.register()
  user2.login()