class StudentProfile:
    def __init__(self):
        self.name = "Not provided"
        self.age = "Not provided"
        self.favorite = "Not provided"
        self.hobbies = ["To be updated"]

    def display_profile(self):
        print("===== STUDENT PROFILE =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Favorite:", self.favorite)
        print("Hobbies:", ", ".join(self.hobbies))