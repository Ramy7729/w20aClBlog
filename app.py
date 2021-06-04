#Collaborated with Liz for this assignment.

# Import modules to use them.
import dbcreds
import mariadb
import traceback

# This allows the user to create a blog post.
def create_blog_post(blog_post, cursor, conn):
    # Testing for errors.
    try:
        # Executes the INSERT statement.
        cursor.execute(f"INSERT INTO blog_post (username, content) VALUES ('{username}', '{blog_post}')")
        # This saves any changes that were made to the database.
        conn.commit()
    # Handling the error when data can't be saved.
    except:
        print("Blog post not saved to the database")
        traceback.print_exc()

# This allows the user to get all the blog posts that were made.
def get_blog_posts(cursor):
    # Executes the SELECT statement.
    cursor.execute("SELECT id, username, content FROM blog_post")
    # Fetches all data based on the specified query statment.
    return cursor.fetchall()

# Takes in user input to get their username.
username = input("Please enter your username: ")
# Testing for errors
try:
    # Establishing a connection which takes in key arguments based on the dbcreds file.
    conn = mariadb.connect(database=dbcreds.database, host=dbcreds.host, port=dbcreds.port, user=dbcreds.user, password=dbcreds.password)
    # This cursor object allows the execution of SQL commands.
    cursor = conn.cursor()
# Handling the error when a connection can't be made.
except:
    print("Connection error")
    traceback.print_exc()

while True:
    # Prints options for the user to select from.
    print("1) Write a new post")
    print("2) See all other posts")
    print("3) Quit")

    # Takes in user input to get the option they selected.
    selection = input("Please select an option: ")
    # Conditionals that are based on user input.
    # If the user selects 1 a function is called to create a blog post.
    if (selection == "1"):
        blog_post = input("Enter your blog post: ")
        create_blog_post(blog_post, cursor, conn)
    # Else if a user selects 2, their post id, name, and content are printed.
    elif (selection == "2"):
        try:
            # Function to get all blog posts which is assigned as posts.
            posts = get_blog_posts(cursor)
            # For loop to iterate through each post and print specified user information.
            for post in posts:
                print(f"=======================")
                print(f"Post ID: {post[0]}")
                print(f"Written by: {post[1]}")
                print(f"Content: {post[2]}")
            print(f"=======================")
        # Handling an error if the blog post isn't displayed.
        except:
            print("Could not get blog post")
            traceback.print_exc()
    # This closes the cursor and allows the user to quit the program.
    elif (selection == "3"):
        conn.close()
        # Breaks the loop.
        break
    else:
        print("Invalid input, please select from 1, 2, or 3.")

