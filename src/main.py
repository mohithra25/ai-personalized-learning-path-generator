print("AI-Based Personalized Learning Path Generator")
print("---------------------------------------------")

name = input("Enter your name: ")
skill = input("What skill do you want to learn? ")
level = input("What is your current level (Beginner/Intermediate)? ")

print("\n--- Your Personalized Learning Path ---")
print("Student Name:", name)
print("Learning Goal:", skill)
print("Current Level:", level)

if level.lower() == "beginner":
    print("\nYour Learning Roadmap:")
    print("1. Learn the basics of", skill)
    print("2. Practice simple programs")
    print("3. Solve beginner-level problems")
    print("4. Build a small project")

elif level.lower() == "intermediate":
    print("\nYour Learning Roadmap:")
    print("1. Revise the fundamentals of", skill)
    print("2. Learn advanced concepts")
    print("3. Solve coding challenges")
    print("4. Build a real-world project")

else:
    print("\nPlease enter Beginner or Intermediate as your level.")
