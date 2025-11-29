# 🌐 Web Frontend Guide

## Overview

The **Intelligent SBI Form Filler** now has a beautiful web interface! Fill forms directly from your browser with a user-friendly UI.

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Start Ollama (if not already running)

```bash
ollama serve
```

### 3. Pull the AI Model (one-time setup)

```bash
ollama pull llama3.1:8b-instruct-q8_0
```

### 4. Start the Web Server

```bash
python3 app.py
```

### 5. Open in Browser

Visit: **http://localhost:5001**

---

## ✨ Features

### 🎨 Beautiful UI
- Modern gradient design
- Responsive layout (works on mobile too!)
- Real-time health status indicator
- Smooth animations and transitions

### 📝 Smart Input
- **Accepts any format** - structured, messy, or conversational
- **Quick examples** - Load pre-made examples with one click
- **Large text area** - Plenty of space for your data
- **Helpful hints** - Tips on what to enter

### 🤖 AI Processing
- **Live status updates** - See what's happening
- **Progress indicator** - Animated spinner during processing
- **Error handling** - Clear error messages with solutions
- **Auto-validation** - Checks Ollama connection

### 📊 Data Display
- **Organized cards** - Extracted data shown in neat sections
- **Color-coded fields** - Easy to scan and verify
- **Complete information** - All 40+ fields displayed

### 📥 Easy Download
- **One-click download** - Get your filled PDF instantly
- **Unique filenames** - Timestamped to avoid overwriting
- **Fast delivery** - Direct download from server

---

## 📋 How to Use

### Step 1: Enter Your Data

Paste your information in ANY format. Examples:

**Structured:**
```
Name: Priya Singh
Father: Rajesh Singh
DOB: 25/03/1995
Gender: Female
Address: B-204 Green Valley, Delhi 110017
Mobile: 9876543210
Email: priya@gmail.com
...
```

**Messy:**
```
hi my name is amit kumar born 15/08/1990
dad ramesh mom sunita, married male
live at flat 301 noida 201301
phone 9876543210 email amit@email.com
...
```

**Conversational:**
```
I'm Rahul Sharma, want to open account
Born 20 June 1992, male, married
Stay in Mumbai at 25 Sea View Apartments
Call me on 9988776655
...
```

### Step 2: Click "Fill Form"

The AI will:
- Analyze your text
- Extract all relevant information
- Validate and format data
- Fill the PDF form
- Show you what was extracted

**Processing time:** 5-10 seconds

### Step 3: Review Extracted Data

The UI shows all extracted information organized by category:
- 👤 Personal Details
- 🏠 Residential Address
- 🏢 Office Address
- 🏦 Bank & Identity

### Step 4: Download PDF

Click the **"Download Filled PDF"** button to get your form!

---

## 🎯 Quick Examples

The interface includes **3 built-in examples**:

### 1. Structured Format
Pre-formatted with clear labels (Name:, DOB:, etc.)

### 2. Messy Format
Unstructured text with casual language

### 3. Minimal Info
Bare minimum required fields

**Click any example button to load it instantly!**

---

## 🔧 Technical Details

### Architecture

```
┌─────────────────────────────────────────┐
│         Browser (index.html)            │
│  - Input form                           │
│  - Display results                      │
│  - Download button                      │
└──────────────┬──────────────────────────┘
               │ AJAX Request
               ▼
┌─────────────────────────────────────────┐
│         Flask Server (app.py)           │
│                                         │
│  /                 → Render HTML        │
│  /api/fill-form    → Process input      │
│  /download/<file>  → Serve PDF          │
│  /api/health       → Check status       │
└──────────────┬──────────────────────────┘
               │ Function Calls
               ▼
┌─────────────────────────────────────────┐
│   Backend Processing                    │
│  - call_ollama_llm()                    │
│  - clean_extracted_data()               │
│  - PDFFormFiller()                      │
└─────────────────────────────────────────┘
```

### API Endpoints

#### `GET /`
- Returns the main HTML page
- Response: HTML

#### `POST /api/fill-form`
- Accepts: `{ "input_text": "..." }`
- Returns: `{ "success": true, "extracted_data": {...}, "download_url": "..." }`
- Processing: LLM → Cleaning → PDF filling

#### `GET /download/<filename>`
- Downloads the generated PDF
- Returns: PDF file

#### `GET /api/health`
- Checks system status
- Returns: `{ "status": "running", "ollama": "connected", "model_llama3_1": true }`

### File Structure

```
Form filling pipeline 1/
├── app.py                      # Flask web server
├── templates/
│   └── index.html             # Frontend HTML/CSS/JS
├── outputs/                    # Generated PDFs (auto-created)
├── intelligent_form_filler.py  # Backend logic
└── step4_fill_form.py         # PDF filling
```

---

## 🎨 UI Components

### Health Status Indicator
- **🟢 AI Ready ✓** - All systems operational
- **🔴 Model Missing** - Need to pull model
- **🔴 Ollama Offline** - Ollama not running
- **🔴 Server Error** - Connection issue

### Input Section
- Large textarea (300px height)
- Placeholder with example
- Character count display
- Hint box with tips

### Example Buttons
- Structured Format
- Messy Format
- Minimal Info
- Clear button

### Fill Button
- Gradient background
- Disabled during processing
- Shows "⏳ Processing..." when active
- Hover effects

### Status Section
- **Loading state**: Spinner + message
- **Success state**: Green background + data cards
- **Error state**: Red background + troubleshooting tips

### Data Cards
- Color-coded by category
- Left border accent
- Field labels in bold
- Responsive grid layout

### Download Button
- Green gradient
- Large and prominent
- Hover animation
- Direct download on click

---

## 🛠️ Customization

### Change Port

Edit `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)
#                              ^^^^
#                          Change this
```

### Modify Styling

Edit `templates/index.html` - All CSS is inline in `<style>` tag

**Colors:**
- Primary: `#667eea` (purple-blue)
- Secondary: `#764ba2` (purple)
- Success: `#28a745` (green)
- Error: `#dc3545` (red)
- Warning: `#ffc107` (yellow)

**Fonts:**
- Body: `-apple-system, BlinkMacSystemFont, 'Segoe UI'`
- Code: `'Courier New', monospace`

### Add Custom Examples

Edit `templates/index.html` in the `loadExample()` function:

```javascript
function loadExample(type) {
    const textarea = document.getElementById('inputData');
    
    if (type === 'your_custom') {
        textarea.value = `Your custom example text here...`;
    }
}
```

Then add button:
```html
<button class="example-button" onclick="loadExample('your_custom')">
    Your Custom Example
</button>
```

---

## 🚨 Troubleshooting

### Issue: "Ollama Offline" in health indicator

**Solution:**
```bash
# Start Ollama server
ollama serve
```

### Issue: "Model Missing" in health status

**Solution:**
```bash
# Pull the model
ollama pull llama3.1:8b-instruct-q8_0
```

### Issue: Page won't load

**Solutions:**
1. Check if Flask is running: Look for "Running on http://127.0.0.1:5001"
2. Try different port: Edit `app.py` and change port number
3. Check firewall: Allow port 5001

### Issue: "Error calling Ollama" when filling form

**Solutions:**
1. Verify Ollama is running: `ollama list`
2. Check model is installed: Look for `llama3.1:8b-instruct-q8_0`
3. Restart Ollama: `killall ollama && ollama serve`

### Issue: Processing takes too long

**Causes & Solutions:**
- **First run**: Model loading takes 10-20 seconds (normal)
- **Large input**: Keep input under 1000 characters
- **System resources**: Close other heavy applications
- **Model size**: Consider using smaller model (7B instead of 8B)

### Issue: PDF download fails

**Solutions:**
1. Check `outputs/` folder exists
2. Verify PDF was generated (check console logs)
3. Try refreshing the page
4. Check disk space

### Issue: Extracted data is incorrect

**Solutions:**
1. **Be more explicit**: Use clear labels (Name:, DOB:, etc.)
2. **Check format**: Dates should be DD/MM/YYYY
3. **Review input**: Ensure all info is present
4. **Try examples**: Load a built-in example to test

---

## 📊 Performance Metrics

### Response Times

| Operation | Time | Notes |
|-----------|------|-------|
| Page load | <1s | HTML + CSS |
| Health check | <500ms | Ollama ping |
| LLM processing | 3-8s | First request slower |
| PDF generation | <1s | After LLM |
| Download | <500ms | Instant |

### Resource Usage

| Resource | Usage | Peak |
|----------|-------|------|
| RAM | 8-10 GB | During LLM inference |
| CPU | 50-80% | During processing |
| Network | Minimal | Local only |
| Disk | ~50 KB | Per PDF |

### Capacity

- **Concurrent users**: 1-2 (single-threaded)
- **Requests/minute**: 5-10
- **Max input size**: 16 MB
- **Typical input**: 500-1000 chars

---

## 🔐 Security Notes

### For Development Use

⚠️ This is a **development server** - do NOT use in production!

**Security considerations:**
- No authentication
- No input sanitization (LLM handles)
- No rate limiting
- Debug mode enabled
- Runs on all interfaces (0.0.0.0)

### For Production

If deploying publicly, add:
- User authentication
- Input validation
- Rate limiting
- HTTPS/SSL
- Error logging
- Session management
- CORS configuration
- Production WSGI server (gunicorn/uwsgi)

---

## 🚀 Deployment

### Option 1: Local Network

Already configured! Access from other devices:
```
http://<your-local-ip>:5001
```

Find your IP: `ifconfig` (Mac/Linux) or `ipconfig` (Windows)

### Option 2: Ngrok (Public URL)

```bash
# Install ngrok
brew install ngrok  # Mac

# Expose local server
ngrok http 5001

# Share the generated URL
```

### Option 3: Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN ollama pull llama3.1:8b-instruct-q8_0
EXPOSE 5001
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t sbi-form-filler .
docker run -p 5001:5001 sbi-form-filler
```

### Option 4: Cloud (AWS/GCP/Azure)

Deploy Flask app on:
- AWS Elastic Beanstalk
- Google App Engine
- Azure App Service
- DigitalOcean App Platform

**Note:** Ensure sufficient RAM (8GB+) for Ollama!

---

## 📱 Mobile Support

The UI is fully responsive and works on:
- ✅ iPhone / iPad
- ✅ Android phones / tablets
- ✅ Desktop browsers
- ✅ Laptop screens

**Features:**
- Touch-friendly buttons
- Scrollable text area
- Readable text size
- Optimized layout for small screens

---

## 🎯 Use Cases

### 1. Bank Branch Office
- Officer uses interface on computer
- Customer provides details verbally
- Officer types notes in any format
- Form filled instantly
- PDF printed for signature

### 2. Self-Service Kiosk
- Customer uses touch screen
- Types their own details
- Reviews extracted data
- Downloads or prints PDF
- Takes form to counter

### 3. Remote Form Filling
- Customer fills from home
- Uploads documents separately
- Downloads filled form
- Visits branch for submission

### 4. Mobile Bank Van
- Officer uses tablet/phone
- Collects info on the go
- Generates forms offline (if Ollama local)
- Submits later

---

## 💡 Tips & Tricks

### For Best Results

1. **Use clear keywords**: "Father:", "DOB:", "Address:", etc.
2. **Include all sections**: Personal, residential, office (if applicable)
3. **Check preview**: Review extracted data before downloading
4. **Test examples**: Try built-in examples first
5. **Keep it concise**: Avoid overly long addresses

### For Faster Processing

1. **Keep Ollama running**: Don't stop/start frequently
2. **Reuse server**: Keep Flask server running
3. **Pre-load model**: First request is slower
4. **Limit input length**: Under 1000 characters ideal
5. **Close heavy apps**: Free up RAM/CPU

### For Troubleshooting

1. **Check health indicator**: Top-right corner shows status
2. **Read error messages**: Errors include troubleshooting steps
3. **Check console**: Flask shows detailed logs
4. **Try examples**: Verify system with known-good data
5. **Restart services**: When in doubt, restart Ollama + Flask

---

## 🎉 Success!

Your web interface is now running at **http://localhost:5001**

**Enjoy filling forms with AI!** 🤖✨

---

## 📞 Support

### Documentation
- `INTELLIGENT_FILLER_GUIDE.md` - CLI version guide
- `AI_INTEGRATION_SUMMARY.md` - Technical details
- `README.md` - Project overview

### Logs
- Flask logs: Terminal where you ran `python3 app.py`
- Ollama logs: Terminal where Ollama is running
- PDF outputs: `outputs/` directory

### Common Commands

```bash
# Check if Ollama is running
ollama list

# Start Ollama
ollama serve

# Restart Flask
# Press Ctrl+C in terminal, then
python3 app.py

# Check port usage
lsof -i :5001

# Kill process on port
kill -9 $(lsof -t -i:5001)
```

---

**Made with ❤️ using Flask + Ollama + Llama 3.1 8B**
