from flask import Blueprint, render_template

blogs_blueprint = Blueprint("blogs", __name__, template_folder="templates",url_prefix="/blogs")


@blogs_blueprint.route("/")
def index():
  return "My blogs"

@blogs_blueprint.route("/<int:date>")
def post(date: int):
  return f"blog post {date}"