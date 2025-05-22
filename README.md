The Bakery Management System is a Python-oriented system designed to streamline and facilitate daily operations in a small family-owned bakery.
The system is capable of catering to the following roles, manager, cashier, baker(s), and customer, providing appropriate functionalities to each role. 
The system efficaciously coordinates the operations for each distinct role, ensuring the bakery business is running seamlessly. 
In developing the Bakery Management System, several assumptions were made to handle aspects that are not explicitly defined. 
Based on industry standards and logical inferences, the following assumptions were established: 

(I) Manager as System Administrator  
- Manager’s account is predefined during system setup, coming with a default username (manager_05) and password (Mng_UCDF2309). 
- No user, including the manager have access to modify the manager’s account. 
- The manager has full control over user accounts, including cashier, baker, and customer. 

(II) User Accounts 
- Employee user accounts are unmodifiable, by employees, only the manager can create, modify, and delete employee user accounts. 
- Customers user accounts are modifiable by customers; customers have full access to update their account details.
  
(III) Order Management 
- Customers can create virtual carts to order products and proceed to check out to confirm orders. 
- Customers can view order details and status with a real-time order tracking system.
- Only manager can update order completion status.
- Customers have the privilege to leave feedback and ratings for only products that they had ordered.
- The Bakery Management System only accepts payment methods such as COD, TNG, and online banking for online transactions.
- The Bakery Management System provides pick-up and delivery services.
- Cashiers may generate digital receipts for customers and the manager may update the order as completed.

(IV) Financial Management 
- Financial management tasks are done on a monthly basis.
- Monthly net profits are estimated based on monthly projected income and total expenses of the month before.
- Only sales tax, income tax, and payroll tax are included. 
- Income taxes are calculated with tax liabilities excluded.⁠
- Tax record for a specific month needs to be manually updated if it is recorded before tax rates were altered. 
- Basic salary for all employees is fixed and cannot be adjusted. 

(V) Inventory Management  
- The manager is responsible for both raw ingredients and product management while bakers are only responsible for product management. 
- Product Management: Both the manager and bakers have permission to add, modify, or remove products. 
- Ingredient Management: Only category and threshold quantity of raw ingredients can be modified. The bought quantity, price, and supplier of existing ingredients can only be modified after restocking. 

(VI) Equipment Management 
- The manager and bakers are responsible for equipment management, monitoring the condition of equipment on a monthly basis.
- Bakers records the condition of each equipment monthly and may make an equipment malfunction report to the manager if there is malfunction of equipment. 
- The manager will get notified if there is an equipment malfunction reported by the bakers and resolve it. 

These assumptions form the foundation of the overall system architecture, ensuring all operations runs smoothly. 
