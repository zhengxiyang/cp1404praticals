from project import Project

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return projects

def display_projects(projects):
    for project in projects:
        print(project)

def main():
    projects = load_projects('projects.txt')

    print("Projects:")
    display_projects(projects)


main()
