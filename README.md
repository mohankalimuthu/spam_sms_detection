## 👨‍💻 Author
**Mohan K**  
- 📧 Email: mohankalimuthu2004@gmail.com  
- 🔗 LinkedIn: https://www.linkedin.com/in/mohan-kalimuthu/
- 💻 GitHub: https://github.com/mohankalimuthu

# 📱 Spam SMS Detection

## 📌 Abstract
Unwanted spam messages are one of the most common issues faced by mobile users.  
This project implements a **machine learning–based SMS spam classifier** to automatically detect and classify SMS messages as **spam** or **ham (not spam)**.  
It leverages natural language processing (NLP) techniques for text preprocessing, feature extraction, and classification.

---

## 🎯 Project Target
- Build an ML model to accurately classify SMS messages into spam/ham.  
- Reduce false positives (legit messages marked as spam).  
- Provide a reproducible pipeline that can be extended for real-world deployment.

---

## 📊 Metrics Required
The following metrics were used to evaluate model performance:
- **Accuracy** → Overall correctness of predictions.  
- **Precision** → Fraction of predicted spam messages that were actually spam.  
- **Recall** → Fraction of actual spam messages correctly identified.  
- **F1-score** → Balance between precision and recall.  
- **Confusion Matrix** → To visualize classification results.

---

## 🤖 Predict Spam SMS Detection
The project follows these key steps:
1. **Data preprocessing** – cleaning text, removing stopwords, stemming/lemmatization.  
2. **Feature engineering** – converting text to numerical features using Bag-of-Words / TF-IDF.  
3. **Model training** – applying ML algorithms to classify messages.  
4. **Prediction** – new SMS messages are classified into spam or ham.  

---

## 🧩 Models Used
- Logistic Regression  
- Naive Bayes (Multinomial)  
- Support Vector Machine (SVM)  

*Logistic Regression -  0.9632286995515695*
*Naive Bayes -  0.9632286995515695*
*Support Vector Machine - 0.9775784753363229*

---

## 📂 Define File Path
- `data/` → contains dataset (`spam.csv`).  
- `code/` → contains Jupyter Notebook (`spam sms detection.ipynb`).  
- `models/` → trained model pickle file (`model.pkl`).  
                  - Naive Bayes model (`nb_spam_classifier.pkl`)
                  - Logistic Regression (`lr_spam_classifier.pkl`)
                  - Support Vector Machine (`svm_spam_classifier.pkl`)
---

## ✨ Features
- Dataset: SMS messages labeled as spam or ham.  
- Preprocessing: lowercasing, removing punctuation, tokenization, stopword removal.  
- Feature extraction: Bag-of-Words / TF-IDF vectorization.  
- Model saving and loading with **Pickle** for reuse.  

---

## ✅ Conclusion
- SMS spam detection using ML is feasible and achieves high accuracy.  
- Among tested models, **SVM** performed best with **97% accuracy**.  
- Future work:  
  - Use deep learning (RNN/LSTM) for better feature representation.  
  - Deploy as a web/mobile app for real-time spam detection.

---

