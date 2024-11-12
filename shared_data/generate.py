import csv
import random

def generate_large_csv(filename, num_rows, num_cols):
    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for _ in range(num_rows):
                row = [random.randint(1, 1000) for _ in range(num_cols)]
                csv_writer.writerow(row)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    # Example usage:
    generate_large_csv('large_data.csv', 10000, 10)  # 1 million rows, 10 columns

