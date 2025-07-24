# 🔐 Web Cache Deception Scanner (WCD-Scan)

A fast Python tool to detect **Web Cache Deception** vulnerabilities on web apps by appending fake static extensions (like `.css`, `.jpg`, etc.) to sensitive endpoints.

## 🚀 Features

- Scans multiple sensitive endpoints
- Appends various payload extensions (`.css`, `.jpg`, `;style.css`, etc.)
- Checks:
  - HTTP status codes
  - Response size
  - `Cache-Control` header
  - Signs of personal info leaks (`name`, `email`, `wallet`, etc.)
- Multithreaded for fast scanning

---

## ⚙️ Setup

### 📦 Requirements

- Python 3.x
- Install dependencies:
  ```bash
  pip install requests

### 🔧 Usage

```bash
pip install requests
python wcd_scanner.py https://www.target.com

