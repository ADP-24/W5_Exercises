def get_department_name(dept_code):
    if dept_code == 1:
        return "Marketing"
    elif dept_code == 5:
        return "Human Resources"
    elif dept_code == 10:
        return "Accounting"
    elif dept_code == 12:
        return "Legal"
    elif dept_code == 18:
        return "IT"
    elif dept_code == 20:
        return "Customer Relations"
    else:
        return "Unknown Department"
    
test_code = [1, 5, 10, 12, 18, 20, 7]

for code in test_code:
    dept_name = get_department_name(code)
    print(f"Department code {code}: {dept_name}")