from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This is required to save plot images inside function
plt.switch_backend("Agg")


data = pd.read_csv("data/data.csv")
# data.columns = ['Student id', ' Course id', ' Marks']

student_ids = data["Student id"].unique()
course_ids = data[" Course id"].unique()


app = Flask(__name__)


def save_plot(course_data, course_id):
    plt.figure()
    plt.hist(course_data[" Marks"], bins=np.arange(0, 120, 20))
    plt.yticks([0, 1, 2, 3])
    plt.title("Course ID: " + str(course_id))
    plt.savefig("static/images/course_id_graph.png")
    return "Success!"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        selected_option = request.form["selected_option"]
        selected_id = request.form["selected_id"]
        if selected_option == "student":
            student_id = int(selected_id)
            if student_id not in student_ids:
                return redirect("/")
            else:
                # creating a numpy array specific to this 'student id'
                student_data = np.array(data[data["Student id"] == student_id])
                n_student_data = len(student_data)

                return render_template(
                    "student.html",
                    student_id=student_id,
                    student_data=student_data,
                    n_student_data=n_student_data,
                )
        elif selected_option == "course":
            course_id = int(selected_id)
            if course_id not in course_ids:
                return redirect("/")
            else:
                # creating a numpy array specific to this 'course id'
                course_data = data[data[" Course id"] == course_id]

                # Saving the plot
                plt.figure()
                plt.hist(course_data[" Marks"], bins=np.arange(0, 120, 20))
                plt.yticks([0, 1, 2, 3])
                plt.title("Course ID: " + str(course_id))
                plt.savefig("static/images/course_id_graph.png")

                return render_template("course.html", course_id=course_id)
        else:
            return redirect("/")
    else:
        print("ERROR! Check the logs.")


if __name__ == "__main__":
    app.run(debug=True)
