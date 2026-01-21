def read_file(file_path):
    file_data = []
    with open(file_path, "r") as f:
        for line in f:
            file_data.append(line.rstrip("\n"))
    
    return file_data


def extract_csv(file_data):
    if len(file_data) == 0:
        raise ValueError("File is empty!")
    headers = file_data[0].split(",")
    csv_map = { header: [] for header in headers }
    for line in file_data[1:]:
        records = line.split(",")
        for i in range(len(headers)):
            csv_map[headers[i]].append(records[i])
    print(csv_map)
    return csv_map



if __name__ == "__main__":
    file_path = "/Users/kunalgupta/Documents/coding/files/dummy.csv"
    file_data = read_file(file_path=file_path)
    for line in file_data:
        print(line)
    try:
        csv_data = extract_csv(file_data)
    except ValueError as e:
        print("Some error occured!", e)
    finally:
        print("Data extracted successfully!")