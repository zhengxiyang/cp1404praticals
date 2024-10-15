FILENAME = "subject_data.txt"

def main():
    data = get_data()
    print_results(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students, followed by scores."""
    input_file = open(FILENAME)
    data = []

    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        scores = [int(score) for score in parts[3:]]  # Convert score strings to integers
        parts[3:] = scores
        data.append(parts)

    input_file.close()
    return data


def print_results(data):
    print("Subject | Maximum | Minimum | Average")
    print("-" * 40)

    for subject_data in data:
        subject_name, lecturer, num_students, *scores = subject_data
        max_score = max(scores)
        min_score = min(scores)
        avg_score = sum(scores) / len(scores)

        print(f"{subject_name:8} | {max_score:7} | {min_score:7} | {avg_score:7.2f}")


if __name__ == "__main__":
    main()
