
# 🧪 Python Calculator App Testing Checklist

## ✅ Main Menu Navigation
- [ ] App runs and displays the main menu properly
- [ ] All menu options lead to their correct modules (e.g., arithmetic, algebra, etc.)
- [ ] "Exit" option works and cleanly exits the program

## ➗ Basic Arithmetic Module
Test each operation:
- [ ] Addition (e.g., 5 + 7 = 12)
- [ ] Subtraction (e.g., 10 - 4 = 6)
- [ ] Multiplication (e.g., 6 * 3 = 18)
- [ ] Division (e.g., 8 / 2 = 4)
- [ ] Handles division by zero

## 🧮 Algebra Module

### Linear Equations
- [ ] Solves simple linear equations (e.g., `2x = 10` → `x = 5`)

### Simultaneous Equations
- [ ] Accepts and solves systems of 2 equations

### Change of Subject (Transposition)
- [ ] Accepts symbolic input and solves for desired variable

### Quadratic Equations
- [ ] Calculates roots correctly (real and complex)
- [ ] Displays discriminant
- [ ] Shows proper output format (e.g., `x = 2 | x = 5`)
- [ ] Graph displays and zooms correctly

### Cubic Equations
- [ ] Accepts coefficients and shows real roots (if applicable)
- [ ] Graph responds to different coefficients (no static graph)

## 📊 Graphing
- [ ] Quadratic graph shows correctly
- [ ] Cubic graph changes shape when coefficients are different
- [ ] Graphs are readable and scaled properly
- [ ] Only one plot window opens

## 💻 Code Structure
- [ ] Files are properly modularized (`main.py`, `menus/`, `algebra/`, `basic/`, etc.)
- [ ] No circular imports
- [ ] Error handling works across modules
- [ ] Code is clean, comments included where necessary
