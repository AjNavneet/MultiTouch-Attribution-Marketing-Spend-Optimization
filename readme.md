# Multi-Touch Attribution Model and Marketing Spend Optimization

## Business Objective
Marketing attribution is a vital aspect of understanding how various marketing channels contribute to overall success. This project delves into multi-channel attribution modeling, aiming to quantify the value of advertising campaigns and improve advertising ROI. The goal is to help stakeholders make informed decisions by isolating the impact of each touchpoint on conversions.

---

## Aim
This project aims to build various attribution models to determine the channels that lead to greater customer conversions.

---

## Data Description
The dataset is in CSV format and comprises 586,737 rows and 6 columns. The columns include:
- `Cookie`: Anonymous customer ID
- `Time`: Date and time of the visit
- `Interaction`: Categorical variable indicating the interaction type
- `Conversion`: Binary indicator (0 for not converted, 1 for converted)
- `Conversion value`: Value of the potential conversion event
- `Channel` (target variable): The marketing channel responsible for bringing the customer to the site

---

## Tech Stack
- Language: `Python`
- Libraries: `NumPy`, `Matplotlib`, `Seaborn`, `Itertools`, `Gekko`, `Pandas-Profiling`

---

## Approach
1. Import the required dependencies and libraries.
2. Import the dataset.
3. Exploratory Data Analysis (EDA):
   - Generate an EDA report using the Pandas Profiling Python module.
4. Building Single Touch Attribution Models:
   - Last Touch Attribution Model
   - First Touch Attribution Model
   - Last Non-Direct Touch Attribution Model
5. Building Multi-Touch Attribution Models:
   - Linear Attribution Model
   - Position-Based (U-Shaped) Attribution Model
   - Position Decay Attribution Model
6. Building Probabilistic Attribution Models:
   - Markov Attribution Model
   - Shapley Value Model
7. Results:
   - Tables: Average of all the models
   - Graphs: Model visualizations
8. Build a Budget Optimization Engine.

---

## Project Structure
- `input`: Contains the dataset in a CSV file named "attribution_data.csv."
- `src`: The core folder with modularized code.
   - `engine.py`: Main execution script.
   - `ML_Pipeline`: Modular Python functions for data processing.
- `output`: Stores model graphs.
- `lib`: Includes the original Jupyter notebook and reference materials.
- `ppt`: Presentation slides used for project explanation.

---

## Getting Started
1. Clone this repository.
2. Navigate to the `src` folder and run `engine.py` to execute the project.
3. Install required packages using `pip install -r requirements.txt`.

---

## Concepts Explored
1. Understanding the business problem.
2. Data import and library usage.
3. Basic Exploratory Data Analysis (EDA).
4. Building and evaluating Single Touch attribution models.
5. Building and evaluating Multi-Touch attribution models.
6. Building and evaluating Probabilistic attribution models.
7. Budget optimization engine development.

---


