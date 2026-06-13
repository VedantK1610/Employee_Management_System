from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import time


app = Flask(__name__)

for i in range(20):
    try:
        db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
    except:
        time.sleep(5)

@app.route("/")
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()

    return render_template("index.html", employees=employees)

@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO employees(name,email,department) VALUES(%s,%s,%s)",
            (name,email,department)
        )

        db.commit()
        cursor.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit_employee(id):

    cursor = db.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]

        cursor.execute(
            """
            UPDATE employees
            SET name=%s,email=%s,department=%s
            WHERE id=%s
            """,
            (name,email,department,id)
        )

        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM employees WHERE id=%s",(id,))
    employee = cursor.fetchone()

    return render_template("edit.html",employee=employee)


@app.route("/delete/<int:id>")
def delete_employee(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)