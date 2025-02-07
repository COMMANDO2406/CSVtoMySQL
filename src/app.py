from flask import Flask, render_template, request, flash, redirect, url_for
import subprocess
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your_secret_key"
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        database_name = request.form["database"]
        table_name = request.form["table"]
        column_names = request.form["columns"]

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected", "danger")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)  # Save uploaded file

        try:
            result = subprocess.run(
                ["python", "csv_to_mysql.py", database_name, table_name, column_names, file_path],  
                text=True,
                capture_output=True
            )

            flash(result.stdout, "success")
            if result.stderr:
                flash(result.stderr, "danger")

        except Exception as e:
            flash(f"Error: {e}", "danger")

        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
