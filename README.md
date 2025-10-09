# Investment Decision Simulator Platform
# Project Overview
The Investment Decision Simulator Platform is a Python-based tool designed to help users simulate and analyze investment strategies. It allows users to make investment decisions, evaluate outcomes, and understand the effects of different financial strategies in a controlled, interactive environment. The platform combines data analysis, simulation models, and a user-friendly interface to support learning and experimentation in investment decision-making.

# Key Features
Interactive Simulation: Users can simulate different investment scenarios and visualize outcomes.

Data-Driven Analysis: Supports importing datasets for real-world investment evaluation.

Decision Scoring: Evaluates investment decisions based on risk, return, and portfolio metrics.

Extensible Architecture: Easily add new models, investment strategies, or visualization tools.

Cross-Platform Compatibility: Runs on Windows, macOS, and Linux.

# Project Structure
Investment-Decision-Simulator-Platform/

backend/

 simulation.py
 
 decision_engine.py
 
 utils.py
frontend/

 index.html
 
 styles.css
 
 app.js
data/

 sample_investments.csv
notebooks/

 analysis.ipynb
requirements.txt

README.md

LICENSE

# Installation
Clone the repository

git clone https://github.com/Cynthia71904/Investment-Decision-Simulator-Platform.git cd Investment-Decision-Simulator-Platform

Create a virtual environment

python -m venv venv source venv/bin/activate # macOS/Linux venv\Scripts\activate # Windows

Install dependencies

pip install -r requirements.txt

# Usage
·Open the following webpage to experience：http://localhost:8502

·Or try the following:

Run the simulation backend

python backend/simulation.py

Launch the frontend

Open frontend/index.html in a browser to interact with the simulator.

Optional: Run analysis notebook

jupyter notebook notebooks/analysis.ipynb

# Example
Load a sample dataset:

from backend.simulation import Simulator sim = Simulator("data/sample_investments.csv") sim.run_strategy("balanced_portfolio") sim.visualize_results()

# License
This project is licensed under the MIT License. See the LICENSE file for details.
