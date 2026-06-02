def common_skills(set1, set2):
    if not set1 or not set2:
        print("Invalid skill sets")
        return

    print("Common Skills:", set1 & set2)

skills1 = {"Python", "SQL", "Java"}
skills2 = {"Python", "C++", "SQL"}

common_skills(skills1, skills2)
