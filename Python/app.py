from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

DB_FILE = "csci375team3.db"

def create_database():
    # Connect to the database
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create the users table
    c.execute(
        '''CREATE TABLE IF NOT EXISTS Courses (
            courseID TEXT PRIMARY KEY,
            courseName TEXT NOT NULL,
            description TEXT,
            recommendedHours REAL,
            courseDifficulty REAL,
            sections TEXT,
            recommendedYear INTEGER,
            term TEXT
        )'''
    )

    # Insert data into the users table
    c.execute(
        '''INSERT INTO Courses (courseName, description) VALUES
            ("test1", "user1@example.com"),
            ("test2", "user2@example.com"),
            ("test3", "user3@example.com")'''
    )

    # Save changes and close the connection
    conn.commit()
    conn.close()

create_database()

def perform_search(query):
    # Connect to the database
    conn = sqlite3.connect('database')
    c = conn.cursor()

    # Execute the search query
    c.execute("SELECT * FROM users WHERE username LIKE ?", (query,))
    results = c.fetchall()

    # Close the connection
    conn.close()

    return results

@app.route('/')
def search_page():
    return render_template('test.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = perform_search(query)
    return render_template('test2.html', query=query, results=results)

if __name__ == '__main__':
    app.run()