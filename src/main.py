print("==============================================")
print("AI-Based Personalized Learning Path Generator")
print("==============================================")

skill_aliases = {
"python": "python",
"python programming": "python",
"python language": "python",
"java": "java",
"java programming": "java",
"java language": "java",
"c": "c",
"c programming": "c",
"c++": "c++",
"cpp": "c++",
"c++ programming": "c++",
"sql": "sql",
"sql programming": "sql",
"javascript": "javascript",
"js": "javascript",
"javascript programming": "javascript",
"web development": "web development",
"web designing": "web development"
}

level_aliases = {
"basic": "beginner",
"beginner": "beginner",
"easy": "beginner",
"medium": "intermediate",
"intermediate": "intermediate",
"moderate": "intermediate",
"advanced": "advanced",
"expert": "advanced"
}

roadmaps = {
"python": {
"beginner": [
"Learn Python syntax and variables",
"Understand data types and operators",
"Practice conditions and loops",
"Build a simple Python program"
],
"intermediate": [
"Learn functions and modules",
"Practice lists, dictionaries and sets",
"Learn file handling and exceptions",
"Build a Python application"
],
"advanced": [
"Learn decorators and generators",
"Practice advanced object-oriented programming",
"Explore asynchronous programming",
"Build an advanced Python application"
]
},
"java": {
"beginner": [
"Learn Java syntax and variables",
"Understand data types and operators",
"Practice conditions and loops",
"Build a simple Java program"
],
"intermediate": [
"Learn object-oriented programming",
"Practice collections and exception handling",
"Understand file handling",
"Build a Java application"
],
"advanced": [
"Learn design patterns",
"Explore multithreading",
"Understand JVM fundamentals",
"Build a scalable Java application"
]
},
"c": {
"beginner": [
"Learn C syntax and data types",
"Practice conditions and loops",
"Understand arrays and functions",
"Build a simple C program"
],
"intermediate": [
"Learn pointers and structures",
"Practice dynamic memory allocation",
"Understand file handling",
"Build a C application"
],
"advanced": [
"Explore function pointers",
"Practice memory management",
"Learn modular programming",
"Build an advanced C project"
]
},
"c++": {
"beginner": [
"Learn C++ syntax and variables",
"Practice conditions and loops",
"Understand functions and arrays",
"Build a simple C++ program"
],
"intermediate": [
"Learn classes and objects",
"Practice inheritance and polymorphism",
"Understand STL containers",
"Build a C++ application"
],
"advanced": [
"Explore templates",
"Practice advanced STL algorithms",
"Learn smart pointers",
"Build an advanced C++ project"
]
},
"sql": {
"beginner": [
"Understand databases and tables",
"Learn SELECT and WHERE",
"Practice INSERT, UPDATE and DELETE",
"Create a simple database"
],
"intermediate": [
"Practice JOIN operations",
"Learn GROUP BY and aggregate functions",
"Understand subqueries",
"Build a database project"
],
"advanced": [
"Learn indexes and query optimization",
"Practice common table expressions",
"Understand transactions",
"Optimize a database project"
]
},
"javascript": {
"beginner": [
"Learn JavaScript syntax and variables",
"Understand data types and operators",
"Practice conditions and loops",
"Build an interactive webpage"
],
"intermediate": [
"Learn arrays and objects",
"Practice DOM manipulation",
"Understand promises and async/await",
"Build a JavaScript application"
],
"advanced": [
"Explore closures and scope",
"Practice asynchronous programming",
"Learn modules and application architecture",
"Build an advanced JavaScript application"
]
},
"web development": {
"beginner": [
"Learn HTML structure",
"Practice CSS styling",
"Learn JavaScript basics",
"Build a simple website"
],
"intermediate": [
"Create responsive webpages",
"Learn advanced JavaScript",
"Understand APIs and HTTP",
"Build a multi-page website"
],
"advanced": [
"Learn frontend architecture",
"Understand web security basics",
"Practice API integration",
"Build a complete web application"
]
}
}

def get_input(message):
  return input(message).strip()

def choose_skill():
  while True:
    print("\nSupported Skills:")
    print("Python, Java, C, C++, SQL, JavaScript, Web Development")

    entered_skill = get_input(
        "\nEnter your skill (or type exit to quit): "
    ).lower()

    if entered_skill == "exit":
        return None

    skill = skill_aliases.get(entered_skill)

    if skill in roadmaps:
        return skill

    print("\nSorry, '{}' is not currently supported.".format(
        entered_skill if entered_skill else "(empty input)"
    ))

    print("Please choose a skill from the list.")

    retry = get_input("Would you like to try again? (yes/no): ").lower()

    if retry in ["no", "n"]:
        return None

    while retry not in ["yes", "y", "no", "n"]:
        print("Please enter yes or no.")
        retry = get_input("Would you like to try again? (yes/no): ").lower()

    if retry in ["no", "n"]:
        return None

def choose_level():
  while True:
    print("\nAvailable Levels: Beginner, Intermediate, Advanced")

    entered_level = get_input(
        "Enter your level (or type exit to quit): "
    ).lower()

    if entered_level == "exit":
        return None

    level = level_aliases.get(entered_level)

    if level is not None:
        return level

    print("\nInvalid level. Please try again.")
    print("You can enter Basic, Beginner, Medium, Intermediate, Advanced or Expert.")

def main():
  print("\nWelcome! Let's create your learning path.")

name = get_input("Enter your name: ")

if not name:
  name = "Student"

while True:
    skill = choose_skill()

    if skill is None:
        break

    level = choose_level()

    if level is None:
        break

    print("\n==============================================")
    print("YOUR PERSONALIZED LEARNING PATH")
    print("==============================================")
    print("Student Name :", name)
    print("Learning Goal:", skill.title())
    print("Current Level:", level.title())

    print("\nRecommended Roadmap:")

    for number, step in enumerate(roadmaps[skill][level], start=1):
        print("{}. {}".format(number, step))

    print("\nRoadmap generated successfully!")

    again = get_input(
        "\nWould you like another roadmap? (yes/no): "
    ).lower()

    while again not in ["yes", "y", "no", "n"]:
        print("Please enter yes or no.")
        again = get_input(
            "Would you like another roadmap? (yes/no): "
        ).lower()

    if again in ["no", "n"]:
        break

print("\nThank you for using the Learning Path Generator!")
print("Keep learning and keep building!")

if name == "main":
    main()

