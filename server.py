from flask import Flask,render_template,request
import random
import datetime
import requests
app=Flask(__name__)
data=[
  {
    "id": 1,
    "title": "The Life of Cactus",
    "subtitle": "Who knew that cacti lived such interesting lives.",
    "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify."
  },
  {
    "id": 2,
    "title": "Top 15 Things to do When You are Bored",
    "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
    "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today."
  },
  {
    "id": 3,
    "title": "Introduction to Intermittent Fasting",
    "subtitle": "Learn about the newest health craze.",
    "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
  }
]
@app.route("/")
def home():
    num=random.randint(0,100)
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    y = date.strftime("%Y")
    return render_template("index.html",n=num,year=y)

@app.route("/name/<name>")
def apidata(name):
    response=requests.get(url=f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    data=response.json()
    name=data["name"].title()
    gender=data["gender"].title()
    return render_template("api_dynamic_data.html",name=name,gender=gender)

@app.route("/blog")
def get_blogs():
    all_posts=data
    return render_template("blog.html",posts=all_posts)
@app.route("/contact-form")
def open_form():
    return render_template("contact-form.html")
@app.route("/login",methods=["POST"])
def receive_data():
    username=request.form["username"]
    password=request.form["password"]
    return f"<h1>Username:{username} Password:{password}</h1>"

if __name__=="__main__":
    app.run(debug=True)


