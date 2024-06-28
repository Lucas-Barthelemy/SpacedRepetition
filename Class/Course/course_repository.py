import datetime
import sqlite3

from course import Course

class CourseRepository:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

        # Create the courses table if it doesn't exist
        self.c.execute(
            '''
                CREATE TABLE IF NOT EXISTS courses
                (id INTEGER PRIMARY KEY, title TEXT, description TEXT, start_date TEXT)
            '''
        )

    def add_course(self, title, description, start_date):
        start_date_str = start_date.isoformat()
        self.c.execute(
            "INSERT INTO courses VALUES (?, ?, ?)",
            (title, description, start_date_str)
        )
        self.conn.commit()

    def delete_course(self, course_id):
        self.c.execute(
            "DELETE FROM courses WHERE id = ?",
            (course_id,)
        )
        self.conn.commit()

    def modify_course(self, course_id, title, description, start_date):
        start_date_str = start_date.isoformat()
        self.c.execute(
            "UPDATE courses SET title = ?, description = ?, start_date = ? WHERE id = ?",
            (title, description, start_date_str, course_id))
        self.conn.commit()

    def get_course(self, course_id):
        self.c.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        row = self.c.fetchone()
        
        start_date = datetime.datetime.fromisoformat(row['start_date'])
        course = Course(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            start_date=start_date
        )

        return course

    def get_courses(self):
        self.c.execute("SELECT * FROM courses")
        rows = self.c.fetchall()
        
        courses = []
        for row in rows:
            start_date = datetime.datetime.fromisoformat(row['start_date'])
            course = Course(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                start_date=start_date
            )
            courses.append(course)

        return courses
    

    def close(self):
        self.conn.close()