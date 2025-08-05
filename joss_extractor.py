
import requests
import csv
import time
from typing import List, Dict
import json

def fetch_joss_data() -> List[Dict]:
    """Fetch all JOSS papers data from the API"""
    base_url = "https://joss.theoj.org/papers/published.json"
    all_papers = []
    page = 1
    total_records = 3111  # Based on your information
    total_pages = (total_records + 19) // 20  # Ceiling division
    
    print(f"Starting extraction of {total_records} papers across {total_pages} pages...")
    
    while True:
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}?page={page}"
        
        print(f"Fetching page {page}/{total_pages}...")
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if not data:  # Empty response means we've reached the end
                break
                
            all_papers.extend(data)
            print(f"  → Retrieved {len(data)} papers (Total: {len(all_papers)})")
            
            # Small delay to be respectful to the server
            time.sleep(0.1)
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            if page > total_pages:
                break
            page += 1
            continue
    
    return all_papers

def create_csv(papers: List[Dict], filename: str = "joss_papers.csv"):
    """Create CSV file with title and software_repository columns"""
    print(f"Creating CSV file: {filename}")
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(['title', 'software_repository'])
        
        # Write data
        for paper in papers:
            title = paper.get('title', '').strip()
            repo = paper.get('software_repository', '').strip()
            writer.writerow([title, repo])
    
    print(f"CSV created successfully with {len(papers)} papers!")

def main():
    """Main execution function"""
    print("JOSS Papers Data Extractor")
    print("=" * 50)
    
    # Fetch data
    papers = fetch_joss_data()
    
    if papers:
        # Create CSV
        create_csv(papers)
        
        # Print summary
        print("\nSummary:")
        print(f"Total papers extracted: {len(papers)}")
        print(f"Papers with repositories: {sum(1 for p in papers if p.get('software_repository'))}")
        print(f"CSV file saved as: joss_papers.csv")
        
        # Show first few entries as preview
        print("\nPreview (first 3 entries):")
        for i, paper in enumerate(papers[:3], 1):
            print(f"{i}. {paper.get('title', 'N/A')}")
            print(f"   Repository: {paper.get('software_repository', 'N/A')}")
            print()
    else:
        print("No data was extracted!")

if __name__ == "__main__":
    main()
            
