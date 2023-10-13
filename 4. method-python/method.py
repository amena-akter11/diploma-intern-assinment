def my_name_is():
    print("My name is Amena Akter")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"

course_and_learn = [ 
    {
        "course": "Python & web",
        "backend": "Python and it's framework",
        "frontend": "Html, CSS, Bootstrap",
    },
    {
        "course": "Java Spring Boot",
        "backend": "Java",
       "frontend": "Html, CSS, Bootstrap",
    },
    {
        "course": "C# & ASP.NET Core",
        "backend": "C#",
        "frontend": "Entity Framework, Razor",
    },
    {
        "course": "MERN Development",
        "backend": "Node",
        "frontend": "React, HTML, CSS",
    },
    {
        "course": "PHP & Laravel",
        "backend": "PHP",
        "frontend": "Blade, Eloquent",
    },
]

for item in course_and_learn:
    course_name = item["course"]
    backend = item["backend"]
    frontend = item["frontend"]

    
    my_name_is()
    i_have_enrolled_course(course_name)
    result = i_have_learning(backend, frontend)
    print(result)
    print()
    print()