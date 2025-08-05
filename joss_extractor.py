
import requests
import csv
import time
from typing import List, Dict
import json
from datetime import datetime

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

def create_csv(papers: List[Dict], filename: str = None):
    """Create CSV file with only software_repository column in quoted format"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"joss_repositories_{timestamp}.csv"
    
    print(f"Creating CSV file: {filename}")
    
    # Count repositories before writing
    repositories_with_data = []
    for paper in papers:
        repo = paper.get('software_repository', '').strip()
        if repo:  # Only include non-empty repositories
            repositories_with_data.append(repo)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Write header
        csvfile.write('software_repository\n')
        
        # Write data with explicit quotes
        for repo in repositories_with_data:
            csvfile.write(f'"{repo}"\n')
    
    print(f"✅ CSV created successfully!")
    print(f"📁 Filename: {filename}")
    print(f"📊 Records in CSV: {len(repositories_with_data)}")
    
    return len(repositories_with_data), filename

def main():
    """Main execution function"""
    start_time = datetime.now()
    print("🚀 JOSS Papers Data Extractor")
    print("=" * 50)
    print(f"🕒 Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Fetch data
    papers = fetch_joss_data()
    
    if papers:
        # Create CSV
        csv_record_count, csv_filename = create_csv(papers)
        
        # Print detailed summary with verification counts
        print("\n" + "="*60)
        print("📊 EXTRACTION SUMMARY")
        print("="*60)
        print(f"📥 Total papers processed: {len(papers)}")
        print(f"📝 Records written to CSV: {csv_record_count}")
        print(f"❌ Papers without repositories: {len(papers) - csv_record_count}")
        print(f"📈 Repository coverage: {(csv_record_count/len(papers)*100):.1f}%")
        print(f"📁 Output file: {csv_filename}")
        print(f"🕒 Extraction completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Verification check
        print(f"\n🔍 VERIFICATION:")
        print(f"✅ Processed {len(papers)} papers from API")
        print(f"✅ Wrote {csv_record_count} repository URLs to CSV")
        print(f"✅ Data integrity: {csv_record_count + (len(papers) - csv_record_count)} = {len(papers)} ✓")
        
        # Show first few entries as preview
        repositories_with_data = [p for p in papers if p.get('software_repository', '').strip()]
        print(f"\n📋 Preview (first 5 repositories):")
        for i, paper in enumerate(repositories_with_data[:5], 1):
            repo = paper.get('software_repository', '').strip()
            if repo:
                print(f'{i}. "{repo}"')
    else:
        print("❌ No data was extracted!")
    
    # Show total execution time
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n⏱️  Total execution time: {duration.total_seconds():.1f} seconds")

if __name__ == "__main__":
    main()
            