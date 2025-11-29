## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Ollama (for AI model)
- 8GB+ RAM (for running Llama 3.1 8B model)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/g-adi/sbi-form-filling-pipeline.git
cd "Form filling pipeline 1"
```

#### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

#### 3. Install Ollama

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from [ollama.com](https://ollama.com)

#### 4. Start Ollama Service

```bash
ollama serve
```

Keep this terminal running in the background.

#### 5. Pull Llama 3.1 8B Model

In a new terminal:

```bash
ollama pull llama3.1:8b-instruct-q8_0
```

⏳ This downloads ~8.5GB and takes 5-10 minutes depending on your internet speed.

#### 6. Start the Web Application

```bash
python3 app.py
```

#### 7. Open in Browser

Visit: **http://localhost:5001**

---

## 📖 Usage

### Step 1: Enter Your Details

Paste your information in ANY format. The AI will understand it!

**Example 1 - Structured:**
```
Name: Priya Singh
Father: Rajesh Singh
Mother: Sunita Singh
DOB: 25/03/1995
Gender: Female
Status: Married

Address: B-204 Green Valley Apartments, Malviya Nagar
Near Metro Station, New Delhi 110017
Phone: 9876543210
Email: priya.singh@gmail.com

Office: Tech Solutions Pvt Ltd, A-15 Cyber City
Sector 18, Gurgaon, Haryana 122015
Office Phone: 0124-4567890

Bank: Connaught Place Delhi, Code: 12345
PAN: ABCDE1234F
Nationality: Indian
```

**Example 2 - Messy/Conversational:**
```
My name is Anmol Deepak Verma, and my father is Late Mr. Devendra Pratap Verma while my mother’s name is Kavita Lata Verma. I think my date of birth is 07/02/1988 (or maybe it was written as 7th Feb ’88 in my old school TC, not sure).
Right now I’m living at Flat No. 12C, Sunrise Residency, Near Greenfield Arcade, Sector 52, somewhere around Noida Extension, with the landmark usually noted as Opp. Metro Plaza Gate-2, Uttar Pradesh – 201304. Our old landline 011-55678890 barely works, so I use my mobile 9811122233 more often. Also, sometimes my emails bounce between anmol.v88@gmail.com
 and deepak.anmol@outlook.in
 depending on which account I signed in last.

My office address is Trident Nexa Technologies Pvt. Ltd., inside Block-D Infinity Corporate Towers, Cyber Heights Road, with the landmark Behind Stellar Business Hub, located in Gurugram, Haryana – 122016. Office telephone is 0124-7799001, and the fax line 0124-7799002 (nobody in the office even remembers we have a fax machine).

This whole form was supposed to go to the Karol Bagh Branch, New Delhi, with Code No. 99821, filled on 29/11/2025. They also asked for a CIF number, so I scribbled 89898911223 there. My PAN is XYPDV5566Q, nationality Indian, gender marked as Male (though the last bank representative mistakenly ticked “Female” once), marital status Single, customer type Regular, but for correspondence I always prefer Address C (office), not the residential one since courier people never find my flat.

I’ve also attached a passport photo named photo_random.jpg and a signature scan called sign_sample.png—both are somewhere in my downloads folder. One more thing: the building guard usually writes my name as “Anmol Verman” on parcels, so some deliveries get delayed; mentioning this just in case.
```

### Step 2: Upload Images (Optional)

- Click **📸 Photograph** box → Upload passport-size photo
- Click **✍️ Signature** box → Upload signature image
- Supported: JPG, PNG, GIF, BMP (max 5MB each)

### Step 3: Generate Form

1. Click **"✨ Fill Form"** button
2. Wait 5-10 seconds for AI processing
3. Review extracted data
4. Click **"📥 Download Filled PDF"**


## 🎯 Supported Form Fields

### Personal Details (6 fields)
- Full name, father's name, mother's name
- Date of birth, gender, marital status

### Residential Address (11 fields)
- 3 address lines, landmark
- City, state, pincode
- Phone, mobile, 2 email addresses

### Office Address (9 fields)
- 3 address lines, landmark
- City, state, pincode
- Office phone, fax number

### Bank Details (6 fields)
- Branch name, code
- Date, CIF number
- PAN, nationality

### Selections (2 fields)
- Customer type (Public/Staff)
- Correspondence address (Residential/Office)

### Images (2 fields)
- Photograph (optional)
- Signature (optional)
