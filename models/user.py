class User:
    def __init__(self, user_id: str, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(user_id={
            self.user_id}, username={
            self.username}, email={
            self.email})"

    def __str__(self):
        return f"User ID: {
            self.user_id}, Username: {
            self.username}, Email: {
            self.email}"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get("user_id"),
            username=data.get("username"),
            email=data.get("email")
        )

    def update_email(self, new_email: str):
        if "@" in new_email and "." in new_email:
            self.email = new_email
        else:
            raise ValueError("Invalid email format")

    def update_username(self, new_username: str):
        if new_username and len(new_username) > 0:
            self.username = new_username
        else:
            raise ValueError("Username cannot be empty")
