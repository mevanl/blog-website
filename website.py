from flask import Flask, render_template
import os


website = Flask(__name__)


@website.route("/")
def index():
  return render_template("index.html")

@website.route("/about")
def about():
  return render_template("about.html")

# if no year is selected
@website.route("/blog")
def blog():
  return render_template("blog.html")

# when a certain year is selected
@website.route("/blog/<int:year>")
def blog(year):

  return render_template("blog.html")

# when a certain year is selected
@website.route("/blog/<int:year>/<string:post_title>")
def blog(year, post_title):

  return render_template("blog.html")

# NOT DONE, NEED TO GET ALL HTML FILES IN THE YEAR DIRECTORY 
def load_years_posts(year=None):
  posts = []
  base_path = 'blog_posts/'

  for directory in os.listdir(base_path):
    # (if year) meaning not None, and directory is correct year
    if year and directory != str(year):
      continue
    
    # Once they match...
    full_path = os.path.join(base_path, directory)

    # Get the html files
    if os.path.isdir(full_path):
      for file in os.listdir(full_path):
        if file.endswith('.html'):
          # We will now get the content of the html file
          file_path = os.path.join(full_path, file)
          # read contents
          with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            posts.append((file, content))
  
  return posts


if __name__ == "__main__":
  website.run(debug=True)