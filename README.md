# Project README

## Overview
This project displays 2 implementations of a three-layered neural network to identify handwritten digits, trained using the MNIST dataset. The 2 implementations of the neural network include:
1. Low-Level/Algorithmic Implementation
2.Sophisticated/Library-based Implemetation

## Project Structure
The codebase is organized into two main sections: low-level implementations and sophisticated abstractions.

### Low-Level Implementations
- This implementation uses Numpy and pure linear algebra to implement custom forward and backward propagation and stochastic gradient descent functions for self-training, and Matplotlib to visualize the error rate per epoch during the training phase

### Sophisticated Implementations
- This implementation uses modern tools/libraries, namely OpenCV and Tensorflow, to implement a high-level neural network model

## Project Setup
### Dependencies
To run this project, ensure you have the following dependencies installed:

- Python 3.8 or higher
- Streamlit 1.0.0 or higher
- Pandas 1.2.0 or higher
- NumPy 1.19.0 or higher
- Matplotlib 3.3.0 or higher
- Seaborn 0.11.0 or higher
- Scikit-learn 0.24.0 or higher

```bash
pip install streamlit pandas numpy matplotlib scikit-learn
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd Digit-Identifying-Neural-Network
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
To run the application, use the following command in your terminal:
```bash
cd "Sophisticated NN"
streamlit run user_interface.py
```
This will start a local server, and you can access the application in your web browser at `http://localhost:8501`.

### Instructions on Using the Interface
- Once the application is running, you will see the main interface where you can upload your data files.
- Follow the prompts to select the type of analysis you wish to perform.
- Utilize the various features available in the sidebar to customize your analysis and visualizations.

## Interface
*Images and screenshots will be added here to illustrate the user interface and its functionalities.*
