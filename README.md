# Digit Identifying Neural Network

## Overview
This project displays 2 implementations of a three-layered neural network to identify handwritten digits, trained using the MNIST dataset. The 2 implementations of the neural network include:
1. Low-Level/Algorithmic Implementation
2. Sophisticated/Library-based Implemetation

## Project Structure
The codebase is organized into two main sections: low-level implementations and sophisticated abstractions.

### Low-Level Implementation
- This implementation uses Numpy and pure linear algebra to implement custom forward and backward propagation and stochastic gradient descent functions for self-training, and Matplotlib to visualize the error rate per epoch during the training phase

### Sophisticated Implementation
- This implementation uses modern tools/libraries, namely OpenCV and Tensorflow, to implement a high-level neural network model. There is a demo set up with this implementation as well that can be run locally using Streamlit

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
   git clone https://github.com/rmaskey1/Digit-Identifying-Neural-Network.git
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
![image](https://github.com/user-attachments/assets/1928f813-1755-4f3b-99ea-cbf709f9b205)
![image](https://github.com/user-attachments/assets/6e770809-743c-4ec2-85d7-892380717bd8)


## Current Challenge
As of now, there is an issue with retrieving data from the user interface. The neural network is designed to accurate process 28x28 pixel digit images. When taking the handdrawn digit from the user input, the program scales it down to 28x28 pixels. However, this image transformation creates inaccuracies in the pixel data, resulting in inaccurate predictions from the AI model. When testing the model with true 28x28 pixel digit images, the model works almost perfectly. Below, you can see the accuracy and loss of each training epoch:

![image](https://github.com/user-attachments/assets/c188b5d0-fba7-4aa8-9efa-382e915a1164)

To further test the neural network, you can run and modify the ```sophisticated_nn_test.py``` file:
```bash
python sophisticated_nn_test.py
```
