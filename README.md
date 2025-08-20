# 🚀 JOSS + Helmholtz(RSD) Software Repository Extractor 

<div align="center">

![JOSS](https://img.shields.io/badge/JOSS-Journal%20of%20Open%20Source%20Software-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSIjRkZGRkZGIi8+Cjwvc3ZnPgo=)
![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub Codespaces](https://img.shields.io/badge/GitHub-Codespaces%20Ready-green?style=for-the-badge&logo=github&logoColor=white)
![AI Generated](https://img.shields.io/badge/AI%20Generated-Claude-purple?style=for-the-badge&logo=anthropic&logoColor=white)

**An intelligent Python tool to extract and catalog software repositories from JOSS published papers**

[🎯 Features](#-features) • [🚀 Quick Start](#-quick-start) • [📊 Output](#-output) • [🛠️ Usage](#️-usage) • [📈 Statistics](#-statistics)

</div>

---

## 🎯 Features

<table>
<tr>
<td>

### ⚡ **Fast & Efficient**
- Scans all 3,100+ published papers in minutes (2 mins approx)
- Rate-limited API calls to respect server
- Progress tracking with real-time updates

</td>
<td>

### 🎯 **Smart Extraction**
- Filters out papers without repositories
- Handles edge cases and malformed URLs
- Comprehensive error handling

</td>
</tr>
<tr>
<td>

### 📊 **Detailed Analytics**
- Processing vs output record counts
- Repository coverage statistics
- Data integrity verification

</td>
<td>

### 📁 **Professional Output**
- Timestamped CSV files
- Quoted URL format
- UTF-8 encoding support

</td>
</tr>
</table>

## 🚀 Quick Start

### 🐙 **GitHub Codespaces** *(Recommended)*

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/priya-gitTest/JOSS_SoftwareRepositoryExtractor)

```bash
# 1. Open in Codespaces (click badge above)
# 2. Install dependencies
pip install requests
```
# 3. Run the JOSS extractor
```bash
python joss_extractor.py
```
# 4. Run the Helmholtz(RSD) extractor
```bash
python helmholtzRSD_extractor.py
```

### 💻 **Local Installation**

```bash
# Clone the repository
git clone https://github.com/priya-gitTest/JOSS_SoftwareRepositoryExtractor.git
cd JOSS_SoftwareRepositoryExtractor

# Install dependencies
pip install requests

# Run the script
python joss_extractor.py
python helmholtzRSD_extractor.py
```

## 📊 Output

The script generates a timestamped CSV file with software repositories:

```csv
software_repository
"https://github.com/example/awesome-tool"
"https://gitlab.com/research/data-analyzer"
"https://codeberg.org/dev/ml-framework"
```

### 📁 **File Naming Convention**
```
joss_repositories_YYYYMMDD_HHMMSS.csv
Helmholtz_software_repositories_YYYYMMDD_HHMMSS.csv
```

**Example:** `joss_repositories_20250805_143022.csv`

## 🛠️ Usage

### **Basic Usage**
```python
python joss_extractor.py
python helmholtzRSD_extractor.py
```

### **Expected Output**
```
🚀 JOSS Papers Data Extractor
==================================================
🕒 Started at: 2025-08-05 14:30:15

Fetching page 1/156...
  → Retrieved 20 papers (Total: 20)
Fetching page 2/156...
  → Retrieved 20 papers (Total: 40)
...

============================================================
📊 EXTRACTION SUMMARY
============================================================
📥 Total papers processed: 3,111
📝 Records written to CSV: 3,089
❌ Papers without repositories: 22
📈 Repository coverage: 99.3%
📁 Output file: joss_repositories_20250805_143022.csv
🕒 Extraction completed at: 2025-08-05 14:32:18

🔍 VERIFICATION:
✅ Processed 3,111 papers from API
✅ Wrote 3,089 repository URLs to CSV
✅ Data integrity: 3,089 + 22 = 3,111 ✓

⏱️ Total execution time: 123.4 seconds
```

## 📈 Statistics

<div align="center">

| Metric | Typical Value |
|--------|---------------|
| **Total Papers** | ~3,100+ |
| **Repository Coverage** | ~99% |
| **Execution Time** | 2-5 minutes |
| **Output Size** | ~200KB |
| **API Pages** | ~156 pages |

</div>

## 🔧 Technical Details

### **Requirements**
- Python 3.6+
- `requests` library
- Internet connection

### **API Details**
- **Base URL:** `https://joss.theoj.org/papers/published.json`
- **Pagination:** 20 records per page
- **Total Pages:** ~156 pages
- **Rate Limiting:** 100ms delay between requests

### **Data Processing**
1. **Fetch** all pages from JOSS API
2. **Filter** papers with valid repository URLs
3. **Format** URLs with explicit quotes
4. **Export** to timestamped CSV file
5. **Verify** data integrity

## 🤝 Contributing

This project was generated with the assistance of **Claude AI**. Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

6. [TODO : Fix  Licence extraction logic for non GITHUB repo's]

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **[JOSS](https://joss.theoj.org/)** - For providing the excellent API
- **[Claude AI](https://claude.ai/)** - For assisting in code generation
- **[GitHub Codespaces](https://github.com/features/codespaces)** - For seamless development environment

---

<div align="center">

**Made with ❤️ and AI assistance**

[![GitHub stars](https://img.shields.io/github/stars/priya-gitTest/JOSS_SoftwareRepositoryExtractor?style=social)](https://github.com/priya-gitTest/JOSS_SoftwareRepositoryExtractor)
[![GitHub forks](https://img.shields.io/github/forks/priya-gitTest/JOSS_SoftwareRepositoryExtractor?style=social)](https://github.com/priya-gitTest/JOSS_SoftwareRepositoryExtractor)

</div>
