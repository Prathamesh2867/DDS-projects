# 🐍 Python Mini-Projects Collection

This repository contains a set of Python command-line projects that demonstrate the use of core **data structures** and **file handling**.  
Each project is written in a simple style suitable for learning and academic submission.

---

## 🧮 Expression Calculator

### 📌 Overview
A command-line Expression Calculator that can evaluate **infix mathematical expressions**.  
It converts infix to postfix (RPN) using a stack and then evaluates the postfix expression.

### 🔑 Features
- 🔄 Infix → Postfix conversion.  
- 🧮 Postfix evaluation using a stack.  
- 🥇 Operator precedence handled (`*`, `/` before `+`, `-`).  
- 🧠 Parentheses supported.  
- ⚠️ Handles invalid inputs and errors.  

### 🛠️ Concepts & Data Structures
- **Stack (list)** → operators & operands.  
- **Infix → Postfix conversion**.  
- **Postfix evaluation** → compute result step by step.  

---

## 💰 Personal Finance Tracker

### 📌 Overview
A simple finance tracker that allows users to **record income and expenses**, set savings goals, and review transactions.  
It also supports saving and loading data from a file for persistence.

### 🔑 Features
- ➕ Add income or expense records.  
- 🔍 Search & filter (e.g., expenses over a certain amount).  
- 📊 Sort transactions.  
- 🎯 Savings goal tracking.  
- 💾 Save and load records from file.  
- 📉 ASCII bar chart for monthly spending.  

### 🛠️ Concepts & Data Structures
- **Array of dictionaries/objects** → stores transactions.  
- **Sorting & searching** → filter large expenses.  
- **File handling (CSV)** → persistent storage.  
- **ASCII visualization** → simple monthly chart.  

---

## 📇 Contact Book

### 📌 Overview
A Contact Management System built using a **linked list**.  
Contacts can be stored, searched, updated, and deleted, while maintaining alphabetical order.  
Data is also stored in a file so contacts persist across sessions.

### 🔑 Features
- 📥 Add new contacts (stored alphabetically).  
- 🔍 Search contacts by name.  
- ✏️ Update contact details.  
- ❌ Delete contacts.  
- 📑 Display all saved contacts.  
- 💾 File persistence (contacts are auto-saved and loaded).  

### 🛠️ Concepts & Data Structures
- **Linked List (self-referential nodes)** → stores contacts in memory.  
- **File handling (pickle)** → persistent storage.  
- **Sorted insertion** → keeps contacts alphabetically arranged.  
