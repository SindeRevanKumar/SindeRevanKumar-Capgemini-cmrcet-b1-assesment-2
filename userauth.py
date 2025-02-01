from abc import ABC, abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass
    @abstractmethod
    def logout(self):
        pass

class GoogleAuthentication(UserAuthentication):
    def login(self, username, password):
        print(f"Logging in with Google account: {username}")
        if username == "user@google.com" and password == "googlepass123":
            print("Google authentication successful.")
        else:
            print("Google authentication failed.")
    def logout(self):
        print("Logged out from Google.")

class FacebookAuthentication(UserAuthentication):
    def login(self, username, password):
        print(f"Logging in with Facebook account: {username}")
        if username == "user@facebook.com" and password == "facebookpass123":
            print("Facebook authentication successful.")
        else:
            print("Facebook authentication failed.")
    def logout(self):
        print("Logged out from Facebook.")

def authenticate_user(auth_service):
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    auth_service.login(username, password)
    auth_service.logout()

google_auth = GoogleAuthentication()
facebook_auth = FacebookAuthentication()

print("Google Authentication:\n")
authenticate_user(google_auth)
print("Facebook Authentication:\n")
authenticate_user(facebook_auth)