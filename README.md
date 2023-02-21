# Introduction

This repository is a simple todo app built with Python3 and MySQL. This application allows you to add, edit, delete, and view to-do tasks. The tasks are stored in a MySQL database and can be accessed by multiple users.

## Installation

- Clone the repository.
- Install the required dependencies using the following command: `pip3 install -r requirements.txt`.
- Create a MySQL database.
- Open the `app/settings.py` file and modify the following variables with your MySQL database credentials: `PORT,HOST,PASSWORD,USER,NAME`.

## Starting local server

- Open the console and navigate to the project directory.
- Run the following command to start the application: `python3 manage.py runserver`.

## Migrations

- Run the following command to setup migrations: `python3 manage.py migrate`.

## Superuser

For creating superuser, first reach the same directory as that of `manage.py` and run the following command: `python3 manage.py createsuperuser`.

## Screenshots

![create-task](pictures/create-task.png)
![edit-task](pictures/edit-task.png)
![dashboard](pictures/dashboard.png)
![home](pictures/home.png)
![login](pictures/login.png)
![register](./pictures/register.png)
