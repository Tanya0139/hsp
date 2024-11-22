# **Hospital Management System** 🏥  

## **Overview**  
The **Hospital Management System (HMS)** is a Python-based application integrated with a **MySQL database**, designed to simplify and optimize the management of hospital operations. It allows for the seamless handling of patient, doctor, and worker records while automating appointment bookings and other hospital workflows.  

This project is aimed at reducing manual paperwork, ensuring data security, and improving the efficiency of managing hospital data.

---

## **Features**  

1. **Patient Management**:  
   - Add patient details, including name, age, problems, and phone number.  
   - View all patient records.  
   - Search for specific patient information.  

2. **Doctor Management**:  
   - Add doctor details, such as name, age, department, and phone number.  
   - View all doctor records.  
   - Search for a specific doctor by name.  

3. **Worker Management**:  
   - Add worker details, including name, age, work type, and phone number.  
   - View all worker records.  
   - Search for specific worker information.  

4. **Appointment Management**:  
   - Book appointments between patients and doctors, specifying date and time.  

5. **Data Security & Ease of Use**:  
   - Login authentication for secure access.  
   - Maintains accurate and well-structured records for easy retrieval.  

---

## **Objectives**  

- **Computerization**: Automate hospital operations by replacing manual record-keeping with digital processes.  
- **Error-Free Operations**: Reduce errors and redundancy in maintaining records.  
- **Quick Retrieval**: Allow for instant access to patient and doctor records.  
- **Efficient Inventory Management**: Maintain records of available medicines and reduce stock automatically during use.  
- **Improved Accessibility**: Simplify appointment scheduling and consultation processes.

---

## **Advantages**  

- Minimal maintenance costs.  
- Handles large volumes of data efficiently.  
- Ensures secure data storage with backups.  
- Scalable for future enhancements and integrations.  

---

## **System Requirements**  

### **Hardware**  
- **Processor**: Intel  
- **RAM**: Minimum 512 MB  
- **Storage**: 80 GB or more  
- **Other**: Keyboard, Mouse, Printer, Monitor (14-17 inch)  

### **Software**  
- **Operating System**: Windows  
- **Programming Language**: Python  
- **Database**: MySQL  

---

## **Setup & Installation**  

### Prerequisites:  
1. Install Python and MySQL on your system.  
2. Install the `mysql-connector-python` library:  
   ```bash
   pip install mysql-connector-python
   ```

### Steps:  
1. Open **MySQL** and create a database named `project`:  
   ```sql
   CREATE DATABASE project;
   ```
2. Clone or download the project files.  
3. Run the script `table.py` to create necessary tables in the database:  
   ```bash
   python table.py
   ```
4. Run the main application `menu.py`:  
   ```bash
   python menu.py
   ```
5. Login with the username and password:  
   - Username: `vasu`  
   - Password: `vasu6072`  

---

## **How It Works**  

1. **Login**: Secure authentication ensures that only authorized users can access the system.  
2. **Menu Options**: Once logged in, users can:  
   - Register new patients, doctors, and workers.  
   - View all records or search for specific records.  
   - Book appointments between doctors and patients.  
3. **Database Integration**: All entered data is stored in the **MySQL database**, ensuring data persistence and easy retrieval.  
4. **User Interaction**: The application uses a menu-driven interface, making it intuitive and user-friendly.  

---

## **Source Code**  

### **table.py**  
Handles the creation of tables for patient, doctor, and worker records in the MySQL database, which is h1.py here.

### **menu.py**  
Implements the menu-driven application, allowing the user to perform CRUD operations, book appointments, and view records, which is h2.py here.  

---

## **Flowchart**  

<img width="350" height="300" alt="Screenshot 2024-11-22 at 5 56 47 PM" src="https://github.com/user-attachments/assets/ff4b1a62-18e4-422b-9391-8b24a7342dce">
<img width="350" height="300" alt="Screenshot 2024-11-22 at 5 56 55 PM" src="https://github.com/user-attachments/assets/380b840f-1b63-4ee5-89dc-19c66e298af8">
<img width="350" height="300" alt="Screenshot 2024-11-22 at 5 57 01 PM" src="https://github.com/user-attachments/assets/00c9be46-87ed-4fb8-9d36-29ecce54226f">


---

## **Screenshots**  

<img width="500" height="500" alt="Screenshot 2024-11-22 at 5 59 10 PM" src="https://github.com/user-attachments/assets/b5abe0e1-0136-486f-a8d1-9b6777aa4f7a">
<img width="500" height="500" alt="Screenshot 2024-11-22 at 5 59 51 PM" src="https://github.com/user-attachments/assets/1d8c21fb-97a7-487d-ad84-447d38334a3a">
<img width="500" height="500" alt="Screenshot 2024-11-22 at 6 00 01 PM" src="https://github.com/user-attachments/assets/a508cfaf-2128-4764-ae40-106b3d6461b1">
<img width="500" height="500" alt="Screenshot 2024-11-22 at 5 59 25 PM" src="https://github.com/user-attachments/assets/0400e994-0b05-4441-88dc-373947fbfd6f">
<img width="500" height="500" alt="Screenshot 2024-11-22 at 6 00 13 PM" src="https://github.com/user-attachments/assets/28a76360-d6d9-48ce-b2b4-53a4d6c6151d">

---

## **Conclusion**  

The **Hospital Management System** makes hospital record management and operations easier, faster, and more efficient. By storing data electronically, this system ensures data security, quick access, and reduced dependency on paper records. It streamlines workflows for doctors, patients, and administrative staff, ultimately enhancing the overall healthcare experience.  

---

## **Bibliography**  

- *Sumita Arora's Computer Science with Python*  
- *Hospital Management System Report by Praveen M Jigajinni*  
- References: [W3Resource](https://www.w3resource.com), [Wikipedia](https://en.wikipedia.org)  

--- 
