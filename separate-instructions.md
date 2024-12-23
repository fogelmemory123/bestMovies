# הוראות הפעלה - פרויקט ספריית סרטים

## Backend (Django)

1. **התקנת חבילות**:
```bash
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install Pillow
```

2. **הגדרת בסיס הנתונים**:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **הרצת השרת**:
```bash
python manage.py runserver
```

השרת יפעל בכתובת: `http://127.0.0.1:8000`

נקודות קצה זמינות:
- `http://127.0.0.1:8000/api/users/signup/` - הרשמה
- `http://127.0.0.1:8000/api/users/login/` - התחברות
- `http://127.0.0.1:8000/api/movies/` - ניהול סרטים

## Frontend (HTML/JS)

1. **הכנת הקבצים**:
   - הכן תיקייה חדשה (למשל `frontend`)
   - העתק לתוכה את הקבצים:
     - `index.html`
     - `login.html`
     - `signup.html`

2. **הפעלת הדפים**:
   - אפשרות 1: פתח את הקבצים ישירות בדפדפן
   - אפשרות 2 (מומלצת): השתמש בשרת פיתוח פשוט:
     ```bash
     # אם יש לך Python מותקן:
     python -m http.server 5500
     
     # או אם יש לך Node.js מותקן:
     npx serve
     ```

3. **גישה לממשק**:
   - פתח בדפדפן את `http://localhost:5500` (או הפורט שהוגדר)
   - התחל ב-`login.html` להתחברות
   - או `signup.html` להרשמה
   
## הערות חשובות

1. **הפעל קודם את ה-Backend**:
   - חשוב להפעיל את שרת ה-Django לפני השימוש בממשק המשתמש
   - ודא שהשרת רץ על פורט 8000

2. **Cross-Origin (CORS)**:
   - ה-Backend כבר מוגדר לאפשר בקשות מה-Frontend
   - אין צורך בהגדרות נוספות

3. **סדר הפעולות המומלץ**:
   1. הפעל את שרת ה-Django
   2. הפעל את שרת ה-Frontend
   3. פתח את הדפדפן בכתובת של ה-Frontend
   4. התחל בהרשמה/התחברות

במקרה של בעיות:
- ודא ששני השרתים (Backend & Frontend) רצים במקביל
- בדוק שהכתובות והפורטים תואמים למה שמוגדר בקוד
- נסה להשתמש בדפדפן אחר אם יש בעיות CORS