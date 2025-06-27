Features
Displays the full student report card with marks across seven subjects.

Calculates basic statistics (mean, std, min, max, quartiles) for all numeric subjects.

Computes average marks per student.

Identifies the highest scorer (topper) in each subject.

Determines the overall topper based on average marks.

Calculates subject-wise average scores.

Lists students who scored below 75 in any subject.

Dataset
The data consists of 10 students with marks in the following subjects:

English

Math

Science

History

Computer

Hindi

Physical Education

How to Run
Make sure you have Python 3 installed.

Install the pandas library if you haven’t already:

bash
Copy
Edit
pip install pandas
Save the script file (e.g., student_report_card.py) and execute it:

bash
Copy
Edit
python student_report_card.py
The script will print the report and statistics directly to the console.

Code Explanation
The student marks are hardcoded into a dictionary and converted into a pandas DataFrame.

The script calculates averages per student, excluding the 'Name' column.

It finds the highest scorer in each subject by comparing marks.

The overall topper is identified by the highest average score.

Subject-wise averages are computed using pandas’ mean method.

Students scoring below 75 in any subject are filtered and displayed.

Sample Output
typescript
Copy
Edit
🔹 Student Report Card:

      Name  English  Math  Science  History  Computer  Hindi  Physical_Education
0    Aarav       88    95       85       75        92     78                  90
1    Meera       76    82       78       80        84     88                  85
...

🏆 Overall Topper: Vivaan with average 87.57

🔹 Students who scored below 75 in any subject:

      Name
4    Kabir
6   Ishaan
