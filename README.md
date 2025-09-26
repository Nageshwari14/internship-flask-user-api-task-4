# internship-flask-user-api-task-4
A simple Flask REST API for user management with CRUD operations (Create, Read, Update, Delete). Users are stored in an in-memory list. Tested with Postman and curl. 
# Flask User CRUD API

## Overview
This project is a simple **REST API** built using **Python and Flask** to manage user data.  
It covers all **CRUD operations**: Create, Read, Update, and Delete users.  
The users are stored in an **in-memory list** (dictionary-based storage), following the task requirements.

**Task Objective:**  
- Learn **API development fundamentals**.  
- Create endpoints using Flask.  
- Store and manage user data in memory.  
- Test API functionality using `curl` or Postman.

---

## Tools Used
- Python 3.13  
- Flask  
- Postman / curl (for testing)  
- VS Code (for development)  

---

## Endpoints

| Method | URL                  | Description                               | Request Body Example                  |
|--------|---------------------|-------------------------------------------|-------------------------------------|
| GET    | `/users`             | Get all users                             | N/A                                 |
| GET    | `/users/<id>`        | Get single user by ID                      | N/A                                 |
| POST   | `/users`             | Create a new user                          | `{ "name": "Charlie", "email": "charlie@example.com" }` |
| PUT    | `/users/<id>`        | Update an existing user                     | `{ "name": "Bobby" }`               |
| DELETE | `/users/<id>`        | Delete a user                               | N/A                                 |

---

## How to Run

1. **Clone the repo**:
```bash
git clone <your-repo-link>
cd <your-repo-folder>
