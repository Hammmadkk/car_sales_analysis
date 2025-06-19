# 🚗 Car Sales Data Analysis

Welcome to the **Car Sales Data Analysis** project!  
This project uses Python, Pandas, and Matplotlib to perform a complete visual analysis of car sales across various regions and models. The goal is to uncover sales patterns, pricing insights, and regional performance trends — all with clean, insightful visualizations.

---

## 📦 Dataset Overview

The dataset includes daily car sales records with the following columns:

- `Date` — Sales date  
- `Region` — Sales region (North, South, East, West)  
- `Car Model` — Type of car sold (SUV, Sedan, Truck, etc.)  
- `Units Sold` — Number of cars sold on that day  
- `Unit Price` — Price per car  
- `Total Sales` — Revenue generated (Units Sold × Unit Price)

---

## 📈 Visualizations & Analysis

The project uses multiple plot types to explore the dataset:

### ✅ Line Plot
- Visualizes **daily units sold** over time
- Helps detect trends and volume fluctuations

### ✅ Scatter Plot
- Shows relationship between **Units Sold and Total Sales**
- Reveals how high-value cars affect revenue despite low volume

### ✅ Bar Chart
- Compares **total sales across regions**
- Identifies strongest and weakest performing markets

### ✅ Histogram
- Displays the **distribution of car unit prices**
- Shows dominance of mid-range pricing, with some luxury outliers

### ✅ Pie Chart
- Illustrates **market share by car model**
- Highlights the most popular vehicle types

### ✅ Subplots & Customized Dual Axis Plot
- Combines **Units Sold** and **Revenue** for better comparison
- Offers insights into the effectiveness of pricing strategies

---

## 📊 Insights Summary

- **SUVs and Sedans** are top-selling models.
- **West** is the best-performing region by revenue.
- Luxury models contribute **high revenue even with low unit sales**.
- Most vehicles fall in the **mid-range price category**.
- Regional performance shows opportunity for **growth in North and South**.

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas
- Matplotlib
- Jupyter Notebook (VS Code or browser)

---

## 🧰 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/car-sales-analysis.git
   cd car-sales-analysis

Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (on Windows)
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Launch the Jupyter Notebook:

bash
Copy
Edit
jupyter notebook
Or open directly in VS Code and run all cells.

📁 Folder Structure
bash
Copy
Edit
car-sales-analysis/
│
├── data/
│   └── car_sales_data.csv          # Dataset file
│
├── car_sales_analysis.ipynb        # Jupyter notebook (main analysis)
├── graph_observations.md           # Auto-generated insights
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
🤝 Contributions
Feel free to fork the project, raise issues, or suggest improvements!
Let’s make data more insightful, one chart at a time 🚀



Made with ❤️ by Hammad Hayat Khan
📧 hammadhayat16@gmail.com | 💼https://www.linkedin.com/in/hammad-hayat-khan/| 🌐 https://github.com/Hammmadkk
