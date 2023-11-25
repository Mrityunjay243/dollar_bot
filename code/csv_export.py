import csv

def export_to_csv(user_id, expenses):
    
    filename = f"expenses_{user_id}.csv"

    # Define the CSV header
    header = ["Date", "Category", "Amount", "Description"]

    # Write data to CSV file
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        # Write the header
        writer.writeheader()

        # Write expense data
        for expense in expenses:
            writer.writerow(expense)

    return filename
