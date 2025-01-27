# Multi-Touch Attribution Model and Marketing Budget Optimization

## Business Objective
Marketing attribution is essential for understanding the contribution of various marketing channels to overall success. This project focuses on multi-channel attribution modeling to quantify the value of advertising campaigns and enhance advertising ROI. The primary goal is to empower stakeholders to make data-driven decisions by isolating the impact of each touchpoint on conversions.

---

## Aim
This project aims to develop and compare various attribution models to identify the marketing channels that drive higher customer conversions and optimize budget allocation for maximum efficiency.

---

## Data Description
The dataset used in this project is in CSV format, comprising 586,737 rows and 6 columns. The columns include:
- **`Cookie`**: Anonymized customer ID.
- **`Time`**: Date and time of the customer visit.
- **`Interaction`**: Type of interaction (categorical variable).
- **`Conversion`**: Binary indicator (0 for not converted, 1 for converted).
- **`Conversion Value`**: Monetary value of the conversion event.
- **`Channel`**: The marketing channel responsible for directing the customer to the site (target variable).

---

## Tech Stack
- **Programming Language**: Python
- **Libraries**:
  - `NumPy` for numerical computations
  - `Pandas` for data manipulation
  - `Matplotlib` and `Seaborn` for data visualization
  - `Itertools` for iteration utilities
  - `Gekko` for mathematical optimization
  - `Pandas-Profiling` for generating automated EDA reports

---

## Approach

1. **Import Dependencies**:
   - Load all required libraries and modules for the analysis.

2. **Data Import**:
   - Read the dataset into a Pandas DataFrame.

3. **Exploratory Data Analysis (EDA)**:
   - Generate a comprehensive EDA report using `Pandas-Profiling`.
   - Perform data cleaning and visualization to understand key trends and patterns.

4. **Build Single Touch Attribution Models**:
   - **Last Touch Attribution Model**: Assign credit to the last channel before conversion.
   - **First Touch Attribution Model**: Assign credit to the first channel in the customer journey.
   - **Last Non-Direct Touch Attribution Model**: Assign credit to the last channel before conversion, excluding direct visits.

5. **Build Multi-Touch Attribution Models**:
   - **Linear Attribution Model**: Distribute credit evenly across all touchpoints.
   - **Position-Based (U-Shaped) Attribution Model**: Assign 40% credit to the first and last touchpoints, and 20% to the intermediate points.
   - **Position Decay Attribution Model**: Assign decreasing credit to touchpoints as they get further from the conversion event.

6. **Build Probabilistic Attribution Models**:
   - **Markov Attribution Model**: Use transition probabilities to evaluate channel contributions.
   - **Shapley Value Model**: Apply cooperative game theory to determine the marginal contribution of each channel.

7. **Results**:
   - Consolidate results from all models into tables for comparison.
   - Generate and save visualizations to illustrate model outputs.

8. **Budget Optimization Engine**:
   - Use optimization algorithms (e.g., GEKKO) to allocate marketing budgets efficiently across channels based on model results.

---

## Project Structure

```plaintext
.
├── input/                                # Contains input dataset (e.g., attribution_data.csv).
├── src/                                  # Source code folder with modularized scripts.
│   ├── engine.py                         # Main script to execute the pipeline.
│   ├── ML_Pipeline/                      # Folder containing modular Python functions.
│       ├── data_processing.py            # Data preprocessing utilities.
│       ├── attribution_models.py         # Attribution modeling functions.
│       ├── optimization.py               # Budget optimization functions.
├── output/                               # Stores output visualizations and reports.
├── lib/                                  # Includes the original Jupyter notebook and reference materials.
├── ppt/                                  # Presentation slides for project explanation.
├── requirements.txt                      # File containing project dependencies.
└── README.md                             # Project documentation.
```

---

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies**:

   Use the following command to install all required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Project**:

   Navigate to the `src` folder and execute the `engine.py` script:

   ```bash
   python src/engine.py
   ```

4. **Explore the Outputs**:

   - Check the `output/` folder for model graphs and reports.
   - Review detailed EDA insights and model results.

---

## Results

- **Attribution Insights**:
  - Quantified the contribution of marketing channels to conversions.
- **Budget Optimization**:
  - Reallocated budget for improved ROI.
- **Visualizations**:
  - Clear and actionable graphs to support decision-making.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature"
   ```

4. Push your branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For any questions or suggestions, please reach out to:

- **Name**: Abhinav Navneet
- **Email**: mailme.AbhinavN@gmail.com
- **GitHub**: https://github.com/AjNavneet

---

## Acknowledgments

Special thanks to:

- The Python open-source community for excellent tools and libraries.
- [GEKKO](https://www.apmonitor.com/gekko) for providing optimization capabilities.

