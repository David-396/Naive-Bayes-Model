# Naive Bayes Classifier Server

מערכת מבוססת FastAPI המאפשרת סיווג (Classification) של רשומות באמצעות מודל נאיב-בייס. המערכת מורכבת משני שרתים:  
- **Classifier Server** – אחראי לקבל בקשות לסיווג.
- **Server Side** – אחראי להכין את הדאטה, לאמן מודל, לבדוק אותו ולהחזיר אותו ל-Classifier במידת הצורך.

---

## 🚀 מבנה כללי
Naive_Bayes/
│
├── classifier_server/ # שרת קבלת הבקשות לסיווג
│ ├── classifier.py
│ ├── classifier_route.py # הנתיב /classify-record
│ ├── requirements.txt
│ └── Dockerfile
│
├── server_side/ # שרת אימון המודל
│ ├── data/
│ ├── data_handling/ # טעינה, ניקוי
│ │ ├── data_cleaning.py
│ │ └── data_loader.py
│ ├── model/ # מודל נאיב בייס והטסטים עליו
│ │ ├── naive_bayes_model.py
│ │ └── test_accuracy.py
│ ├── server_statics/
│ ├── run_server.py
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── test_server.py
└── start.sh


---

## 🧠 איך זה עובד

### שלב 1: בקשת סיווג
הלקוח שולח בקשת `POST` לניתוב: record-classify/   
עם גוף (JSON) המכיל רשימת ערכים לסיווג.

### שלב 2: בדיקת קיום מודל
- אם כבר קיים מודל מאומן – הסרבר משתמש בו ומחזיר את הסיווג (הערך עם ההסתברות הגבוהה ביותר).
- אם לא קיים מודל – הסרבר מבצע **בקשת GET** לשרת החיצוני.

### שלב 3: אימון מודל (בשרת החיצוני)
- השרת השני (Server Side) טוען את הדאטה (`data_loader.py`)
- מנקה אותו (`data_cleaning.py`)
- מאמן עליו מודל נאיב-בייס (`naive_bayes_model.py`)
- בודק את ביצועי המודל (`test_accuracy.py`)
- מחזיר את המודל כ-**dictionary** עם הסתברויות לכל ערך אפשרי

### שלב 4: חזרה לסיווג
- ה-Classifier מקבל את המודל, מסווג את הרשומה שנשלחה, ומחזיר את הסיווג המתאים.

---

## 🧪 בדיקות

- הקובץ `test_server.py` מאפשר לבצע בדיקות של סיווג.
- הקוד כולל בדיקות דיוק למודל המאומן.

---

## 🐳 Docker

לכל אחד מהשרתים יש `Dockerfile` וניתן להריץ אותם בקונטיינרים נפרדים. להרצה מהירה:

```bash
./start.sh


📬 דוגמה לבקשת POST

POST /classify-record
Content-Type: application/json

{
  "record": [1.2, 3.4, 5.6, 7.8, 0.9]
}





