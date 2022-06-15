from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db = "email_validation"
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_email(data):
        is_valid = True
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def display_all(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        print("************", emails)
        return emails