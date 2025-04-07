
# 🧠 Quora-Like Django Web App

A simple Django-based web application inspired by [Quora](https://www.quora.com/) that allows users to register, ask questions, answer them, and like answers from others.

## 🚀 Features

- 🔐 User Registration & Login
- ❓ Post New Questions
- 👁️ View All Questions
- ✍️ Answer Existing Questions
- ❤️ Like Answers
- 🚪 Logout

## 🛠️ Tech Stack

- **Framework:** Django (Python)
- **Frontend:** Django Templates (HTML, CSS)
- **Database:** SQLite (default)
- **Other Tools:** Django Authentication, Django Forms

## 📂 Folder Structure

```
quora_clone/
├── apps/         # Project settings
├── core/         # Main Django app
│   ├── migrations/
│   ├── templates/
|   |   |__ errors
|   |   |     |__ page_404.html
|   |   |     |__ page_500.html
│   │   ├── home.html
│   │   ├── post_question.html
│   │   |── question_detail.html
│   │   |__ question_list.html
│   │   
│   │   
│   ├── static/          
|   |__ templates/
|        |   |__ registration/
|        |          |__ login.html
|        |          |__ register.html
|        |__ base.html
|        |__ footer.html
|        |__ header.html
|        |__ script.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## ✅ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/quora-clone.git
cd quora-clone
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist, generate one using:
```bash
pip freeze > requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Open in Browser

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Functional Overview

| Function              | Description                                  |
|-----------------------|----------------------------------------------|
| Register/Login        | Create account and login                     |
| Post Question         | Users can submit questions                   |
| View Questions        | List of all posted questions                 |
| Answer Questions      | Users can answer any question                |
| Like Answers          | Like other users’ answers                    |
| Logout                | Secure session logout                        |

---

## 🔮 Future Enhancements

- 🧑‍💼 User Profile Pages
- 🏷️ Tags/Categories for Questions
- 🔍 Search Functionality
- 🔄 Pagination
- 📱 Responsive Design with Bootstrap/Tailwind
- 📊 Answer Sorting by Likes

---

## 📃 License

This project is licensed under the MIT License - feel free to use and modify it as needed.

---

## 🤝 Contribution

Have suggestions or improvements? Feel free to fork the repo and submit a PR!

---

Made with ❤️ using Django.
