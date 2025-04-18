def calculate_salary(experience, role):
    '''Calculate salary based on experience and role'''
    base_salary={
        "Intern":30000,
        "Juinor":50000,
        "Mid-Level":80000,
        "Senior":120000,
        "Manager":150000
        }

    if role not in base_salary:
        raise ValueError("Invalide job role")
        
    return base_salary[role]+(experience*2000)  #Increment    
    