print("AI-Based Personalized Learning Path Generator")
print("---------------------------------------------")

name = input("Enter your name: ")

print("\nSupported Skills:")
print("Python, Java, C, C++, SQL, JavaScript, Web Development")

skill = input("\nChoose a skill: ").strip().lower()
level = input("Enter your level (Beginner/Intermediate): ").strip().lower()

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
"Understand file handling and exceptions",
"Build a Python application"
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
"Practice object-oriented programming",
"Learn collections and exception handling",
"Understand file handling",
"Build a Java application"
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
]
},
"javascript": {
"beginner": [
"Learn JavaScript syntax and variables",
"Understand data types and operators",
"Practice conditions, loops and functions",
"Build an interactive webpage"
],
"intermediate": [
"Learn array methods and objects",
"Practice DOM manipulation",
"Understand promises and async/await",
"Build a JavaScript application"
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
"Create responsive web pages",
"Learn advanced JavaScript",
"Understand APIs and HTTP basics",
"Build a multi-page website"
]
}
}

print("\n--- Your Personalized Learning Path ---")
print("Student Name:", name)
print("Learning Goal:", skill.title())
print("Current Level:", level.title())

if skill not in roadmaps:
   print("\nSkill not available. Please choose a supported skill.")
elif level not in ["beginner", "intermediate"]:
   print("\nInvalid level. Please enter Beginner or Intermediate.")
else:
   print("\nYour Learning Roadmap:")
for step in roadmaps[skill][level]:
   print("-", step)

print("\nThank you for using the Learning Path Generator!")
