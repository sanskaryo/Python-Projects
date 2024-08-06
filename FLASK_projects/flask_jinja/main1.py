from flask import Flask, render_template
import random
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return f" enter  guess/your_name in top url"
    
    
@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_responses = requests.get(gender_url)
    gender_data = gender_responses.json()
    gender = gender_data["gender"]
    
    age_url = f"https://api.agify.io/?name={name}"
    age_response =  requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html",name=name, gender=gender , age = age)
    
    
if __name__ == '__main__':
    app.run(debug=True)