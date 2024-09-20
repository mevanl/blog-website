from flask import Flask, render_template
from blogs.blogs_blueprint import blogs_blueprint


website = Flask(__name__)
website.register_blueprint(blogs_blueprint)


@website.route("/")
def home():
  return render_template("home.html")

@website.route("/about")
def about():
  return render_template("about.html")



if __name__ == "__main__":
  website.run()