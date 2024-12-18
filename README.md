# Todo List

## Project Description

This is a simple web application for task management. Users can create tasks, mark them as completed, edit or delete
them. There is also an option to add tags to each task, which helps to better organize and filter tasks.

## Features

- **Add tasks**: Users can create a new task with a description, deadline, and tags.
- **Edit tasks**: Users can modify the description, deadline, and tags of a task.
- **Delete tasks**: Users can remove tasks that are no longer needed.
- **User interface**: Tasks are displayed in a table with options to mark them as done or undo that action.
- **Tags**: Tasks can be linked to multiple tags, helping users to categorize and filter tasks.

## Technologies

- **Programming Language:** Python 3.12.2
- **Framework:** Django 5.1
- **Database:** SQLite (The default database for storing tasks and tags.)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Additional Libraries:** Django Crispy Forms and Crispy Bootstrap5 for enhanced form styling

## Installation

### Prerequisites

- Python 3.12.2
- Git

### Steps to Install

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Ananiev-Vitalii/todo-list.git
    cd todo_list
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    ```

    - **For Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **For macOS/Linux:**

      ```bash
      source venv/bin/activate
      ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application**

   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

## Usage

1. **Create a new account or sign in to an existing one.**
2. **Go to the home page to view your task list.**
3. **Add, edit, and delete tasks and tags as needed.**
4. **Use tags to filter and organize tasks.**

## Contact

- **Developer:** Vitalii Ananiev
- **Email:** ananievvitalii10@gmail.com
- **GitHub:** [Ananiev-Vitalii](https://github.com/Ananiev-Vitalii/todo-list)