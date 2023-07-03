from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    connection = sqlite3.connect("db/posts.db")
    posts = []
    cursor = connection.cursor()
    cursor.execute("select * from posts")
    return render_template(
        "index.html",
        posts=posts,
    )
