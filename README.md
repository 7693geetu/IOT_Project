# Smart Light Control System (IoT Simulation with Flask)

## 🔧 Project Overview

This project simulates a smart home light control system using Flask. It allows users to control a virtual light (ON/OFF) through a web dashboard and REST API. This project is a basic example of how IoT devices like smart lights can be controlled and monitored remotely.

---

## 🚀 Features

- 🟢 Turn ON/OFF the light via REST API
- 🌐 Web Dashboard to control and view light status
- 🧠 Simple simulation of home automation using Python and Flask

---

## 📁 Project Structure

```
iot_flask_smart_light_control/
├── app.py                  # Main Flask application
└── templates/
    └── index.html          # HTML dashboard
```

---

## 📡 API Endpoints

### POST `/control`
Turn the light ON or OFF.

#### Request Body:
```json
{ "action": "ON" }
```

### GET `/status`
Check current light status.

---

## ⚙️ How to Run

1. Install Flask:
    ```bash
    pip install flask
    ```

2. Run the application:
    ```bash
    python app.py
    ```

3. Visit:
    ```
    http://localhost:5000/
    ```

---

## 📌 Use Case

This project is ideal for:
- Learning basics of smart home automation
- Demonstrating RESTful control for IoT devices
- Frontend-backend integration using Flask

---

## 👩‍💻 Author

**Geetanjali Dake**  
B.Tech in Artificial Intelligence and Data Science  
[Portfolio](https://7693geetu.github.io/dakegeetanjali.github.io/)

---
