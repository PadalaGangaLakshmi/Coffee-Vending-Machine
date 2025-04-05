# ☕ Coffee Vending Machine (Python + PostgreSQL)

This is a **command-line coffee vending machine** simulator built using Python and PostgreSQL. It allows users to:
- Choose coffee types (espresso, filtercoffee, cappuccino)
- Insert currency to pay
- Track resources (water, milk, coffee)
- Store & view transaction history from PostgreSQL

---

## 🛠 Features

- Menu & pricing fetched from PostgreSQL
- Resources like water, milk, coffee are tracked
- Money input (1, 2, 5, 10, 20 rupee notes)
- Transaction records stored in a `Transactions` table
- View last 10 transactions
- Restock functionality
- Admin commands: `report`, `history`, `restock`, `off`

---

## 📦 Technologies Used

- Python 3
- PostgreSQL
- psycopg2 (Python DB adapter)

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```
### 2. Setup PostgreSQL

```
Create a database 
```

### 3. Run the Coffee Machine

```
python machine.py
```

---
## 📁Folder Structure
```
📁 Folder Structure
coffee-vending-machine/
├── machine.py         # Main Python file              
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Output



![Screenshot 2025-04-05 213824](https://github.com/user-attachments/assets/992a8308-fad5-4816-b520-1f4e0075a6c9)





