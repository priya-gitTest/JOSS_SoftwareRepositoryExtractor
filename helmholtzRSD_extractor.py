import requests
from bs4 import BeautifulSoup
import datetime
import json

BASE_URL = "https://helmholtz.software/metadata/codemeta/"

def get_software_links(main_url):
    response = requests.get(main_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    # Find all <a> tags inside <header> tags
    for header in soup.find_all("header"):
        a = header.find("a", href=True)
        if a:
            href = a['href']
            full_url = main_url + href
            links.append(full_url)
    return links

def get_code_repository_from_page(url):
    response = requests.get(url)
    response.raise_for_status()
    # The pages contain JSON metadata inside <pre> or direct JSON?
    # Try to parse the whole text as JSON
    try:
        data = response.json()
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse from <pre> tag
        soup = BeautifulSoup(response.text, "html.parser")
        pre = soup.find("pre")
        if pre:
            try:
                data = json.loads(pre.get_text())
            except json.JSONDecodeError:
                return None
        else:
            return None

    # Extract codeRepository from the JSON data
    code_repo = data.get("codeRepository")
    return code_repo

def main():
    software_links = get_software_links(BASE_URL)
    print(f"Found {len(software_links)} software entries.")
    
    repositories = []
    no_repo_links = []
    for link in software_links:
        repo = get_code_repository_from_page(link)
        if repo:
            repositories.append(repo)
        else:
            print(f"Warning: No codeRepository found at {link}")
            no_repo_links.append(link)
    
    # Save to CSV
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Helmholtz_software_repositories_{timestamp}.csv"
    
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        csvfile.write('software_repository\n')
        for repo in repositories:
            csvfile.write(f'"{repo}"\n')
    
    # Save missing repos CSV
    missing_filename = f"Helmholtz_softwaremissing_Repositories_{timestamp}.csv"
    with open(missing_filename, 'w', encoding='utf-8', newline='') as csvfile:
        csvfile.write('software_page_url\n')
        for url in no_repo_links:
            csvfile.write(f'"{url}"\n')
    print(f"✅ CSV with missing codeRepository links created: {missing_filename}")

    print(f"\n✅ CSV created: {filename}")
    print(f"📊 Total repositories found: {len(repositories)}")

if __name__ == "__main__":
    main()
