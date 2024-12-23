# הוראות הפעלה - ספריית סרטים

## Backend - Django

1. **התקנת חבילות**:
```bash
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install Pillow
Better alternatively, install the required libraries from the requirements.txt file located in the back folder
```
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **הפעלת השרת**:
```bash
python manage.py runserver
```

השרת יעבוד על: `http://127.0.0.1:8000`

## Frontend - קבצי HTML

1. **הקבצים הנדרשים**:
   - `index.html`
   - `login.html`
   - `signup.html`

2. **הפעלה**:
   - פשוט פתח את `login.html או index.html` בדפדפן
   - הירשם או התחבר
   - המערכת תעביר אותך אוטומטית ל-`index.html`

## איך להשתמש?

1. **הפעל את שרת Django** (הוראות למעלה)
2. **פתח את `index.html` בדפדפן**
3. **הירשם או התחבר**
4. **תועבר לדף הראשי שם תוכל לראות ולהוסיף סרטים**

זהו! המערכת אמורה לעבוד 😊
