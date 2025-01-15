# CodAlpha AI Internship Projects

This repository contains three projects completed during my internship at CodAlpha AI. Each project demonstrates different aspects of artificial intelligence and machine learning applications, showcasing the diversity of skills applied during the internship.

---

## Projects Overview

## FAQs Chatbot with Streamlit UI
A simple, interactive FAQ chatbot built with Python that uses natural language processing to find and return the most relevant answers from a FAQ database. The chatbot features a user-friendly web interface built with Streamlit.

### Features
- Natural Language Processing (NLP) based question matching.
- Interactive web interface.
- Confidence score for answers.
- Chat history with matched questions.
- Pattern matching and response generation.

#### Technologies Used
- **Python**
- **Natural Language Processing Libraries**
- **Machine Learning Frameworks**

---

### 2. Language Translation (Google API Integration)
A translation service that leverages Google's powerful translation APIs to provide accurate multi-language translation capabilities.

#### Key Features
- Support for multiple languages.
- Real-time translation.
- API integration with Google Translate.
- Efficient handling of translation requests.

#### Technologies Used
- **Python**
- **Python Google Translation Library**

---

### 3. Object Detection and Tracking
A computer vision system capable of detecting and tracking objects in real-time through video feeds or images.

#### Key Features
- Real-time object detection.
- Object tracking across video frames.
- Multiple object class recognition.
- Bounding box visualization.

#### Technologies Used
- **Python**
- **OpenCV**
- **Deep Learning Frameworks**
- **Computer Vision Libraries**

---

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/Phavour-EBEN/CodAlpha.git
cd CodAlpha
```

### Install Required Dependencies
- **cd into the respective directories and install the requirements**
```bash
pip install -r requirements.txt
```

---

## Project Structure
```
CodAlpha/
├── FAQ_ChatBot/
|   ├── app.py              # Streamlit web interface
|   ├── faq_chatbot.py      # Core chatbot functionality
|   ├── requirements.txt    # Project dependencies
|   └── product_faq_dataset # The dataset
├── Language_Trans_Tool/
│   ├── 
├── object_detection/
│   ├── 
│   └── requirements.txt
└── README.md
```

---

## Running the Projects

### FAQs Chatbot
```bash
cd FAQ_ChatBot
In the terminal run
streamlit run app.py
```

### Language Translation
```bash
cd Language_Trans_Tool
In the terminal run
streamlit run bidirectional.py
```

### Object Detection and Tracking
```bash
cd Object Detection
cd yolo
cd Scripts
activate
cd yolo
cd yolov7-python
python .\detection.py --weights .\yolov7-tiny.onnx --source "PATH TO IMAGE/VIDEO"
```

---

## Future Improvements
- **FAQ_ChatBot:** Implement machine learning for improved response accuracy.
- **Language_Trans_Tool:** Add support for more languages and offline translation.
- **Object Detection:** Implement real-time tracking optimization.

---

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

---

## Acknowledgments
- **CodAlpha AI** for providing the internship opportunity.
- **Open Source Communities** for the tools and libraries used.

---

## Contact
For any queries regarding these projects, please contact **ME** at **ainooebenezer05@gmail.com**.

---
