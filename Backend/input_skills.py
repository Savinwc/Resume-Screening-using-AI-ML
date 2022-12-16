# for company input
def get_soft_skills_data():
    """This function takes the input of the sof skills that the company requires"""
    
    n = int(input("Enter the number of soft skills that you want: "))

    print("Please enter the soft skills: ")
    soft_skills = []
    for i in range(0,n):
        s = input()
        soft_skills.append(s)

    # print("the soft skills entered are: ")
    # print(soft_skills)
    return soft_skills


def get_tech_skills_data():
    """This function takes the input of the technical skills that the company requires"""

    n = int(input("Enter the number of technical skills that you want:"))
    
    print("Enter the technical skills that are required:")
    tech_skills = []
    for i in range(0,n):
        s = input()
        tech_skills.append(s)

    return tech_skills

# print("hi")