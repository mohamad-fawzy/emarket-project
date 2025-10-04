# 🛍️ E-Market Project

A full-featured E-commerce RESTful API built with **Django REST Framework (DRF)**.  
This project provides endpoints for managing products, users, authentication.

---

## 🚀 Features

- 🧾 User registration and login (JWT Authentication)
- 🛒 Product listing, details, and categories
- 🧍 User profile management
- 🔐 Secure token-based authentication
- 📦 Admin panel for product and order management

---

## 🧰 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default), can be switched to PostgreSQL  
- **Authentication:** Simple JWT  
- **Testing:** Postman  

---

## 📄 API Documentation

You can explore and test the API using Postman:

- 🌐 **Live Documentation:** [View API Docs on Postman](https://your-postman-docs-link-here)
- 📥 **Download Collection (JSON):** [EMarket_API_Collection.json](EMarket_API_Collection.json)

*(Replace the links above with your actual Postman documentation and JSON file paths.)*

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mohamad-fawzy/emarket-project.git
cd emarket-project
```

---

### 2️⃣ Create a virtual environment

```bash
# On Linux / macOS
python3 -m venv venv

# On Windows
python -m venv venv
```

---

### 3️⃣ Activate the virtual environment

```bash
# On Linux / macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

💡 When activated, your terminal prompt should show `(venv)` at the beginning.

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Apply migrations

```bash
python manage.py migrate
```

---

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

---

### 7️⃣ Access the API

Open your browser or Postman and navigate to:

👉 [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)


---

## 🧑‍💻 Author

**Mohamad Fawzy**

- 📧 linkedin: [Mohamed Fawzy Alborolusy](https://www.linkedin.com/in/mohamedweb-developer/)
- 💻 GitHub: [https://github.com/mohamad-fawzy](https://github.com/mohamad-fawzy)

---

## 🪪 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/mohamad-fawzy/emarket-project/issues).

---

## ⭐ Show your support

Give a ⭐️ if you like this project!

---