# 📧 Email Header Analyzer 

> A powerful Python tool to analyze email headers for phishing, spoofing, and cyber threat detection.  
> Built to assist **INSA** (Information Network Security Agency of Ethiopia) in securing government email domains.
---
## 🌟 Key Features

- **Deep Email Header Parsing**  
  Extracts *From*, *To*, *Subject*, *Date*, *Return-Path*, *Message-ID*, and complete `Received` chains.
- **SPF, DKIM & DMARC Validation**  
  Validates sender authorization and message integrity using industry standards.
- **IP & Domain Enrichment**  
  Leverages WHOIS, RDAP, ASN, and GeoIP data to profile sender infrastructure.
- **Risk Scoring & Anomaly Detection**  
  Assigns a risk score (0–100) with human-readable reasons based on suspicious patterns.
- **Detailed Forensic Reports**  
  JSON/HTML output for analysts; optionally encrypted for secure handling.
- **User-Friendly Web Interface**  
  Flask-based UI to upload raw headers or `.eml` files and instantly get analysis.
- **Easy MTA Integration**  
  Supports integration with Postfix/Sendmail via `pymilter` for real-time blocking.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 Project Structure
email-header-analyzer/
│
├── app.py              # Flask web application
├── analyzer.py         # Core analysis logic (SPF/DKIM/DMARC, enrichment, scoring)
├── parser.py           # Email header parsing and IP extraction
├── requirements.txt    # Project dependencies
├── README.md           # This documentation
└── samples/            # Sample email headers for testing

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔎 Sample JSON Output

{
  "score": 85,
  "reasons": [
    "SPF fail",
    "DKIM fail",
    "Domain age < 30 days",
    "Geolocation mismatch (US vs Ethiopia)"
  ],
  "spf": {"result": "fail"},
  "dkim": {"dkim_pass": false},
  "dmarc": {"policy": "reject", "result": "fail"},
  "ip_info": {"country": "United States", "asn": "AS16509"},
  "whois": {"creation_date": "2025-07-12"}
}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙ Advanced Features & Future Work

Aggregation & analysis of DMARC reports
Integration with threat intelligence feeds for proactive blocking
Automated IP/domain blacklisting and incident ticketing
Role-based access and audit logging for analyst workflows
Encrypted report storage with secure key management






