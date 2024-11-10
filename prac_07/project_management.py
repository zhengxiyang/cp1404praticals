import datetime
from project import Project

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")

def main():
    """Project Management Program."""
    filename = "projects.txt"
    projects = load_projects(filename)

    menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (A)dd new project\n- (Q)uit"
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "a":
            name = input("Name: ")
            start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(new_project)
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").lower()

    save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")

if __name__ == "__main__":
    main()
