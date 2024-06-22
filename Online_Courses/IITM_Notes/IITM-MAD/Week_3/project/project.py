# Imports

import sys
from jinja2 import Template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data/data.csv")
# data.columns = ['Student id', ' Course id', ' Marks']

student_ids = data["Student id"].unique()
course_ids = data[" Course id"].unique()


if sys.argv[1] == "s":
    student_id = int(sys.argv[2])

    if student_id not in student_ids:
        print("Error: Wrong Student ID!")

    else:
        # creating a numpy array specific to this 'student id'
        student_data = np.array(data[data["Student id"] == student_id])
        n_student_data = len(student_data)

        # Read the student_template.html file into a variable
        student_template_file = open("jinja2/student_template.html")
        student_template_read = student_template_file.read()
        student_template_file.close()

        # Render this using jinja2
        student_template = Template(student_template_read)
        student_content = student_template.render(
            student_id=student_id,
            student_data=student_data,
            n_student_data=n_student_data,
        )

        # Save the rendered html document
        student_output_file = open("output/student_output.html", "w")
        student_output_file.write(student_content)
        student_output_file.close()

elif sys.argv[1] == "c":
    course_id = int(sys.argv[2])

    if course_id not in course_ids:
        print("Error: Wrong Course ID!")

    else:
        # creating a numpy array specific to this 'course id'
        course_data = data[data[" Course id"] == course_id]

        plt.figure()
        plt.hist(course_data[" Marks"], bins=np.arange(0, 120, 20))
        plt.yticks([0, 1, 2, 3])
        plt.title("Course ID: " + str(course_id))
        plt.savefig("images/course_id_graph.png")

        # Read the course_template.html file into a variable
        course_template_file = open("jinja2/course_template.html")
        course_template_read = course_template_file.read()
        course_template_file.close()

        # Render this using jinja2
        course_template = Template(course_template_read)
        course_content = course_template.render(course_id=course_id)

        # Save the rendered html document
        course_output_file = open("output/course_output.html", "w")
        course_output_file.write(course_content)
        course_output_file.close()

else:
    print("Error: Wrong Course ID!")
