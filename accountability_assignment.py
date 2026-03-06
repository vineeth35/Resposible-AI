# Program to demonstrate assigning roles and responsibilities in an AI project
def assign_rai_responsibilities(team_members):
    roles = {
        "Data Scientist": "Model development and bias detection",
        "Project Manager": "Ensuring compliance with ethical standards",
        "AI Ethicist": "Reviewing ethical implications and fairness",
        "Legal Counsel": "Regulatory compliance and risk management"
    }
    assignment = {}
    for role, member in zip(roles.keys(), team_members):
        assignment[member] = (role, roles[role])
    return assignment

team = ["Alice", "Bob", "Charlie", "Diana"]
responsibilities = assign_rai_responsibilities(team)

print("RAI Responsibility Matrix:")
for name, info in responsibilities.items():
    print(f"{name}: Role - {info[0]}, Responsibility - {info[1]}")
