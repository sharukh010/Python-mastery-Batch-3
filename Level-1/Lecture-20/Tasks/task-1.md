# **Python Project: Restaurant Menu and Billing System**

### **Problem Statement**

Develop a **Restaurant Menu and Billing System** using basic Python concepts. Do not use classes or objects.

### **1. Create the Restaurant Menu**

- Create a list named `menu` to store all food items.
- Each food item should contain:
  - `id`: Integer
  - `name`: String
  - `price`: Float
- Add at least 6 different food items to the menu.
- Every food item must have a unique ID.

### **2. Display the Menu**

When the application starts, display all available food items in the following format:

```
Welcome to ABC Restaurant!

Available Menu:

1. Pani Puri - Rs. 10
2. Biriyani - Rs. 120
3. Chocolate Cake - Rs. 30
4. Pizza - Rs. 150
5. Burger - Rs. 80
6. Sandwich - Rs. 50
```

### **3. Take Customer Orders**

- Ask the customer to enter the IDs of the items they want to order.
- Allow multiple item IDs separated by commas.
- Convert the entered IDs into a suitable collection.
- Use a **set** to eliminate duplicate item IDs.
- Each item should be considered only once, even if the customer enters its ID multiple times.

**Sample Input:**

```
Enter the item IDs: 1,2,3,1,2
```

The application should consider only IDs `1, 2, 3`.

### **4. Generate the Bill**

Display all the selected food items in the following format:

```
Your Order:

1. Pani Puri - Rs. 10
2. Biriyani - Rs. 120
3. Chocolate Cake - Rs. 30
```

Calculate and display:

- **Total:** Sum of all selected item prices.
- **Discount:** Discount amount based on the discount rule.
- **Final Amount:** Total amount after deducting the discount.

### **5. Apply Discount**

Implement the following discount rule:

- If the customer orders more than 3 unique items, provide a 10% discount.
- Otherwise, no discount should be applied.

### **6. Expected Output**

**Example 1:**

```
Enter the item IDs: 1,2,3

Your Order:

1. Pani Puri - Rs. 10
2. Biriyani - Rs. 120
3. Chocolate Cake - Rs. 30

Total: Rs. 160
Discount: Rs. 0
Final Amount: Rs. 160
```

**Example 2:**

```
Enter the item IDs: 1,2,3,4,1

Your Order:

1. Pani Puri - Rs. 10
2. Biriyani - Rs. 120
3. Chocolate Cake - Rs. 30
4. Pizza - Rs. 150

Total: Rs. 310
Discount: Rs. 31
Final Amount: Rs. 279
```

### **7. Additional Conditions**

1. If the customer enters an invalid item ID, display an appropriate error message.
2. Duplicate item IDs must not be considered.
3. If the customer enters an empty order, display an appropriate message.
4. Display the bill only for validly selected items.

### **8. Additional Tasks**
1. Add a logic to take quantity of the order. 
if there are duplicate orders ask the user if he wants duplicate order 
```text
ex: 
Do you want to add Duplicate orders? Yes 
Dont not use sets to remove the duplicated 
```


### **Concepts to Practice**

- Lists and nested lists
- Sets
- Loops (`for` and `while`)
- Conditional statements (`if`, `elif`, `else`)
- String methods (`split`, `strip`)
- Type conversion
- Arithmetic operations
