import input_skills
def skills(skill_from_company,pdf_text):
    """This function is going to give the count and the number of skills that are matching with
        the list that is provided by the company and the skills in the resume."""
    skills_possed = []
    num =0
    for skill in skill_from_company:
    # num +=1
        for skills in pdf_text:
            if skill == skills:
                skills_possed.append(skill)
                num +=1

    return [num,skills_possed]
