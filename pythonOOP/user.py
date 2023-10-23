class User:
    def __init__(self, email, name, password, job_title):
        self.email = email
        self.Name = name
        self.password = password
        self.current_job = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job(self, new_job):
        self.current_job = new_job

    def get_user_info(self):
        print(f"User {self.Name} currently works as a {self.current_job}. you can contact him at {self.email}")



