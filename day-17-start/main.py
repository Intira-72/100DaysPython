class User:
    def __init__(self, id, username):
    # initialise attributes
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    
    def follow(self, user):
        user.followers += 1
        self.following += 1


if __name__ == "__main__":
    # user1 = User()
    # user1.id = "001"
    # user1.username = "Angela"

    user1 = User("001", "Angela")
    user2 = User("002", "Jack")

    user1.follow(user2)

    print(f'Username: {user1.username}\nFollowers: {user1.followers}\nFollowing: {user1.following}')
    print(f'Username: {user2.username}\nFollowers: {user2.followers}\nFollowing: {user2.following}')