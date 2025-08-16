import csv
import requests
import time

# --- Configuration ---
# It's highly recommended to use a GitHub Personal Access Token to avoid rate limiting.
# Unauthenticated requests are limited to 60 requests per hour.
# Create a token here: https://github.com/settings/tokens
# The token does not need any special permissions for this script.
GITHUB_TOKEN = "" # Paste your token here
CSV_FILE_PATH = "joss_repositories_20250806_080130.csv"
OUTPUT_CSV_FILE = "joss_repositories_20250806_080130_licenses.csv"
# -------------------

def get_repo_license(github_url):
    """
    Fetches the license information for a given GitHub repository URL.

    Args:
        github_url (str): The full URL of the GitHub repository.

    Returns:
        str: The name of the license, or a message indicating it's not found or an error occurred.
    """
    try:
        # Split the URL to get the owner and repository name
        parts = github_url.strip().split('/')
        if len(parts) < 5 or parts[2].lower() != 'github.com':
            return "Invalid GitHub URL"
            
        owner = parts[3]
        repo = parts[4]

        # Construct the API URL
        api_url = f"https://api.github.com/repos/{owner}/{repo}"

        # Set up headers for the API request
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"

        # Make the API request
        response = requests.get(api_url, headers=headers)
        
        # Check for rate limiting
        if response.status_code == 403 and 'rate limit exceeded' in response.text.lower():
            print("Rate limit exceeded. Waiting for 1 minute before retrying...")
            time.sleep(60)
            response = requests.get(api_url, headers=headers) # Retry once

        # Raise an exception for other bad status codes (404, 500, etc.)
        response.raise_for_status()

        repo_data = response.json()

        # Check if the license information is present
        if repo_data.get("license") and repo_data["license"].get("name"):
            return repo_data["license"]["name"]
        else:
            return "License not specified"

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            return "Repository not found"
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except IndexError:
        return "Could not parse owner/repo from URL"
    except Exception as err:
        return f"An unexpected error occurred: {err}"

def main():
    """
    Main function to read the CSV, process each repository, and write results to a new CSV.
    """
    print(f"Reading repositories from '{CSV_FILE_PATH}'...")
    try:
        with open(CSV_FILE_PATH, mode='r', newline='', encoding='utf-8') as infile, \
             open(OUTPUT_CSV_FILE, mode='w', newline='', encoding='utf-8') as outfile:
            
            # Set up CSV writer and write the header
            writer = csv.writer(outfile)
            writer.writerow(["Repository URL", "License"])

            # Assuming the CSV has one column with the URLs and may or may not have a header
            # Sniffing the dialect helps handle different CSV formats
            dialect = csv.Sniffer().sniff(infile.read(1024))
            infile.seek(0)
            # Check if there is a header
            has_header = csv.Sniffer().has_header(infile.read(1024))
            infile.seek(0)
            
            reader = csv.reader(infile, dialect)

            if has_header:
                next(reader) # Skip header row

            for row in reader:
                if row: # Ensure the row is not empty
                    repo_url = row[0]
                    print(f"Processing: {repo_url}")
                    license_name = get_repo_license(repo_url)
                    print(f"-> License: {license_name}")
                    
                    # Write the result to the output file
                    writer.writerow([repo_url, license_name])
        
        print(f"\nProcessing complete. Results have been saved to '{OUTPUT_CSV_FILE}'.")

    except FileNotFoundError:
        print(f"Error: The file '{CSV_FILE_PATH}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
