from flask import Flask, render_template, request
import pickle
import joblib


app = Flask(__name__)


# Load vectorizer
with open('C:\\Users\\hp\\PyCharmMiscProject\\git\\spam_sms_detection\\models\\tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = joblib.load(f)


# Load models
models = {
'lr': joblib.load(open('C:\\Users\\hp\\PyCharmMiscProject\\git\\spam_sms_detection\\models\\lr_spam_classifier.pkl', 'rb')),
'nb': joblib.load(open('C:\\Users\\hp\\PyCharmMiscProject\\git\\spam_sms_detection\\models\\nb_spam_classifier.pkl', 'rb')),
'svm': joblib.load(open('C:\\Users\\hp\\PyCharmMiscProject\\git\\spam_sms_detection\\models\\svm_spam_classifier.pkl', 'rb'))
}


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        message = request.form['message']
        selected_model = request.form['model']

        vectorized = vectorizer.transform([message])
        model = models[selected_model]

        result = model.predict(vectorized)[0]  # 🔴 IMPORTANT FIX

        prediction = 'Spam 🚫' if result == 1 else 'Not Spam ✅'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)