from user import User
from post import Post
app_user_one = User("dd@dd.com", "David Alkobi", "pwd", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("top@secret.com", "James Bond", "Top secret pwd", "Secret Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.Name)
new_post.get_post_info()
