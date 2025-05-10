from flask import Flask, render_template
from flask import send_from_directory
from flask import request, flash, redirect, url_for




app = Flask(__name__)
app.secret_key = "heheho" 


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    project_list = [
        {
            "title": "Job Application Tracker",
            "description": "A web app to track job applications using Flask and Bootstrap. Extracts job details using a Chrome extension.",
            "tech": ["Flask", "Bootstrap", "JavaScript", "Python"],
            "github": "https://github.com/TonyStark-47/Job-Application-Tracker"
        },
        {
            "title": "Grammar Scoring Engine",
            "description": "Built for a Kaggle competition to score spoken English using ML techniques.",
            "tech": ["Python", "NLP", "scikit-learn"],
            "github": "https://www.kaggle.com/competitions/shl-intern-hiring-assessment/leaderboard"
        },
        {
            "title": "Blog Site",
            "description": "Built a blog site using Flask, allowing users to create, edit, and delete posts. Implemented authentication and authorization using Flask-login for user access control.",
            "tech": ["Flask", "Flask-login", "HTML", "CSS", "SQLite"],
            "github": "https://github.com/TonyStark-47/My_Blog_Site"
        }

    ]
    return render_template("projects.html", projects=project_list)


@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/resume/download")
def download_resume():
    return send_from_directory("resume", "Tony_Resume.pdf", as_attachment=True)

@app.route("/resume/view")
def view_resume():
    return send_from_directory("resume", "Tony_Resume.pdf")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        print(f"[Contact] Name: {name}, Email: {email}, Message: {message}")
        
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route("/blog")
def blog():
    posts = [
        {"title": "How I Built My Portfolio", "date": "2025-05-10", "content": "A walkthrough of my Flask + Bootstrap site."},
        {"title": "650+ LeetCode Problems", "date": "2025-03-20", "content": "Tips on consistency and solving patterns."}
    ]
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
