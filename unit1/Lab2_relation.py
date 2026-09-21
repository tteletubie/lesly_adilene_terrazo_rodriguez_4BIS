class User:
    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self._password = password
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"The user {self.username} created a post.")

    def show_posts(self):
        print(f"\nPosts by {self.username}:")
        for post in self.posts:
            post.print_post()


class Post:
    def __init__(self, description, user, likes=0):
        self.description = description
        self.likes = likes
        self.user = user

    def increment_likes(self):
        self.likes += 1

    def print_post(self):
        print(f"[{self.likes} likes] {self.user.username}: {self.description}")


class Comments:
    def __init__(self, comment, user, post, likes=0):
        self.comment = comment
        self.likes = likes
        self.user = user
        self.post = post

    def show_comment(self):
        print(f"{self.user.username} commented: '{self.comment}' ({self.likes} likes)")


class Message:
    def __init__(self, text, sender, receiver):
        self.text = text
        self.sender = sender
        self.receiver = receiver

    def send(self):
        print(
            f"Message from {self.sender.username} to {self.receiver.username}: {self.text}"
        )


# Instances
user_lesly = User("Lesly", "Terrazo", "lesly_terrazor", "1234")
user_carlos = User("Carlos", "Perez", "carlos_p", "abcd")

post_lesly = Post("ex test", user_lesly, likes=3)
post_lesly1 = Post("ex test", user_lesly, likes=3)
post_lesly2 = Post("ex test", user_lesly, likes=3)
user_lesly.add_post(post_lesly)
user_lesly.add_post(post_lesly1)
user_lesly.add_post(post_lesly2)

comment = Comments("comment", user_carlos, post_lesly, likes=1)
comment.show_comment()

message = Message("msg", user_carlos, user_lesly)
message.send()

user_lesly.show_posts()
