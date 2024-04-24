import requests
import os
import csv


def download_and_rename_files(url, filename):
    try:
        response = requests.get(url)

        filename = f"{filename}.jpg"
        # Save the file
        with open(filename, "wb") as file:
            file.write(response.content)
            
        print(f"Downloaded and saved {filename}")
    except Exception as e:
            print(f"Error downloading {url}: {str(e)}")


def main():
    # Fetch the list of URLs

    with open('output.csv','r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[2] != '':
                download_and_rename_files(row[2], row[1])


if __name__ == "__main__":
    main()