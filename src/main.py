print("AI-Based Personalized Learning Path Generator")
print("---------------------------------------------")

name = input("Enter your name: ")
skill = input("Choose a skill (Python/Java/C/C++/SQL/JavaScript/Web Development): ")
level = input("Enter your level (Beginner/Intermediate): ")

print("\n--- Your Personalized Learning Path ---")
print("Student Name:", name)
print("Learning Goal:", skill)
print("Current Level:", level)

if skill.lower() == "python":
    roadmap = [
        "Learn Python basics",
        "Understand variables and data types",
        "Practice conditions and loops",
        "Build a Python mini project"
    ]

elif skill.lower() == "java":
    roadmap = [
        "Learn Java syntax",
        "Understand classes and objects",
        "Practice OOP concepts",
        "Build a Java mini project"
    ]

elif skill.lower() in ["c", "c programming"]:
    roadmap = [
        "Learn C syntax and data types",
        "Understand conditions and loops",
        "Learn arrays and functions",
        "Build a C mini project"
    ]

elif skill.lower() in ["c++", "cpp"]:
    roadmap = [
        "Learn C++ syntax",
        "Understand classes and objects",
        "Practice OOP concepts",
        "Build a C++ mini project"
    ]

elif skill.lower() == "sql":
    roadmap = [
        "Learn database basics",
        "Practice SELECT and WHERE",
        "Learn INSERT, UPDATE and DELETE",
        "Build a small database project"
    ]

elif skill.lower() in ["javascript", "js"]:
    roadmap = [
        "Learn JavaScript basics",
        "Understand variables and functions",
        "Practice DOM manipulation",
        "Build an interactive webpage"
    ]

elif skill.lower() == "web development":
    roadmap = [
        "Learn HTML",
        "Practice CSS",
        "Learn JavaScript basics",
        "Build a simple website"
    ]

else:
    roadmap = []

if level.lower() not in ["beginner", "intermediate"]:
    print("\nPlease enter Beginner or Intermediate as your level.")

elif roadmap:
    print("\nYour Learning Roadmap:")
    for step in roadmap:
        print("-", step)

else:
    print("\nSkill not available. Please choose one of the supported skills.")
