# Todo App (Flask + React)

A simple **Todo List** application built using **Flask** (Backend) and **React** (Frontend). This app allows users to add, delete, and toggle todos.

## 🚀 Features
- Add new todos ✅
- Delete todos ❌
- Mark todos as completed ✔️
- Simple and clean UI 🎨

---

## 📸 Screenshots
### Home Page
![Home Page](/list.png)


---

## 🛠 Tech Stack
- **Frontend:** React (Vite) + Bootstrap
- **Backend:** Flask
- **Package Manager:** npm / pip

---

## 🏗 Project Structure
```
    📦 dp-todo-as
    ┣ 📂 server  # Flask API
    ┃ ┣ 📜 app.py  # Main Flask application
    ┃ ┣ 📜 requirements.txt  # Backend dependencies
    ┣ 📂 client  # React App
    ┃ ┣ 📂 src
    ┃ ┃ ┣ 📜 App.jsx  # Main component
    ┃ ┃ ┣ 📂 components
    ┃ ┃ ┃ ┣ 📜 TodoList.jsx  # List component
    ┃ ┃ ┃ ┣ 📜 TodoItem.jsx  # Single Todo Item component
    ┃ ┣ 📜 package.json  # Frontend dependencies
    ┣ 📜 README.md  # Project Documentation

```
---

## 🔧 Installation & Setup

### 1️⃣ Backend (Flask API)
#### Prerequisites
- Python 3.x installed

#### Steps:
```bash
# Navigate to backend directory
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```
**API will run at:** `http://127.0.0.1:5000`

---

### 2️⃣ Frontend (React App)
#### Prerequisites
- Node.js & npm installed

#### Steps:
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```
**React app will run at:** `http://localhost:5173`

---

## 🔄 How to Use
1. Open `http://localhost:5173` in your browser.
2. Add a new **Todo** by entering a title and pressing `Add`.
3. Click on a **Todo** to toggle completion.
4. Click the **Delete**  to delete a Todo.

---

## 🐞 Troubleshooting
- **CORS Errors?** Make sure Flask-CORS is enabled in `app.py`:
```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

- **Port Already in Use?** Stop any process using the port with:
```bash
lsof -i :5000  # Find process using port 5000
kill -9 <PID>   # Replace <PID> with actual process ID
```

- **Frontend Not Loading?** Try restarting the React server:
```bash
npm run dev
```

---

## 💡 Author
👨‍💻 **[Jagamohan Panda]** - Feel free to reach out!

