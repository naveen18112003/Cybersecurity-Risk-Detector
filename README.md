

---

## 📘 Project Guide — *Cybersecurity Risk Detector using ML & Streamlit*

---

### 🛡️ Project Title:

**Cybersecurity Risk Detector**

---

### 📌 Problem Statement:

In today's digital world, systems are often exposed to various cybersecurity threats. Regular users or organizations may not always have the expertise or tools to assess their system’s security posture in real-time.

This project solves that problem by using **machine learning** to predict the **cyber risk level** of a system based on a few basic input parameters.

---

### 🎯 Objective:

To develop a machine learning-based web application that:

* Accepts key system information from users
* Predicts whether the system is at **Low**, **Medium**, or **High** cybersecurity risk
* Is easy to use by anyone via a simple web interface

---

### 🧠 Novelty of the Project:

| Aspect                        | Innovation                                                                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 🧾 **Custom Dataset**         | Dataset was synthetically generated to mimic real-world system vulnerabilities and incidents, allowing full control over features and labels. |
| 🔄 **Multi-Model Comparison** | 10+ ML algorithms were tested, evaluated, and compared to choose the best-performing model.                                                   |
| 🌐 **Streamlit Integration**  | Real-time web interface created using Streamlit, enabling users to interactively test risk levels without needing any technical setup.        |
| 📦 **Reusable Model**         | Best model was saved using `joblib` and integrated into the app for lightweight and fast predictions.                                         |
| 🎓 **Educational Tool**       | Project also acts as a learning resource for beginners in ML + cybersecurity domains.                                                         |

---

### 🛠️ Technologies Used:

* **Programming Language:** Python
* **ML Libraries:** scikit-learn
* **Data Processing:** pandas, numpy
* **Visualization:** matplotlib
* **Web App Framework:** Streamlit
* **Model Saving:** joblib
* **Version Control:** Git & GitHub

---

### 🔧 Implementation Steps:

#### 1. Dataset Creation:

* A synthetic dataset was generated and saved as `veri.csv` using Python code (`veri.ipynb`).
* Features included: vulnerabilities, uptime, incidents, patch frequency, and open ports.

#### 2. Model Training:

* Trained 10 different ML models: Decision Tree, Random Forest, Logistic Regression, etc.
* Selected the **best-performing model** based on accuracy and precision.
* Saved final model as `eniyi.joblib`.

#### 3. Web App Development:

* Built a user interface using **Streamlit** where users can input system data.
* Integrated the trained model into the app to predict real-time cyber risk.

#### 4. Testing & Demonstration:

* The app was tested with different inputs.
* A working demo video is linked in `link.text`.

---

### 📊 Sample Inputs:

| Parameter          | Example |
| ------------------ | ------- |
| Vulnerabilities    | 10      |
| Uptime (days)      | 120     |
| Security Incidents | 3       |
| Patch Frequency    | Weekly  |
| Open Ports         | 12      |

**Prediction Output:** 🔴 **High Risk**

---

### 📁 Project Structure:

```
cyber-risk-detector/
├── veri.csv                  # Generated dataset
├── veri.ipynb                # Data generation & training notebook
├── eniyi.joblib              # Trained ML model
├── app.py                    # Streamlit web app
├── README.md                 # Project description
└── link.text                 # Demo video link
```

---

### 🚀 How to Run Locally:

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/cyber-risk-detector
   cd cyber-risk-detector
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

---

### 🎓 Ideal For:

* B.Tech/BE Machine Learning projects
* Cybersecurity awareness tools
* Educational demos for risk modeling
* Personal portfolio project

---

## How to Collect Cybersecurity Risk Parameters on WindowsNumber of Vulnerabilities Definition: Known flaws or bugs in your system/software that attackers can exploit Tools/Methods:

Use Nessus (https://www.tenable.com/products/nessus) to scan and report system vulnerabilities.

Use Microsoft Defender: Go to Windows Security → Virus & threat protection → Protection history

System Uptime (in days)
Definition: The number of days your system has been running continuously.
Commands:

Command Prompt: systeminfo | find "System Boot Time"

PowerShell: (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime

Number of Security Incidents
Definition: Events like failed logins, malware detection, unauthorized access.
Steps:

Open Event Viewer: Press Win + R → type: eventvwr.msc

Navigate to Windows Logs → Security

Check for:

4625: Failed login attempts

4688: Suspicious process creation

4720: New user account created

Also check: Windows Security → Virus & Threat Protection → Protection history

Patch Update Frequency
Definition: How frequently system updates are applied (Daily/Weekly/Monthly).
Steps:

Go to Settings → Update & Security → View update history

Based on pattern:

Daily: Every 1–2 days

Weekly: Once a week

Monthly: Once or twice a month

Number of Open Ports
Definition: Network ports that are open and accepting connections.
Commands:

Command Prompt: netstat -an | find "LISTEN"

PowerShell: Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"} | Measure-Object

Ideal For:

Final year ML/Cybersecurity projects

Resume and portfolio projects

Practical demonstration in colleges or workshops

Awareness tool for non-tech users

Let me know if you'd like to add:

Your name and college

Demo screenshots

Submission date

I can generate that version too!






