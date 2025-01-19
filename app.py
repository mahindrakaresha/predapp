

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('D:/proj/trained_model1.sav', 'rb'))

def predict(input_data):
    # Convert input data to a numpy array and reshape for prediction
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_array)
    
    # Return the prediction result
    if prediction[0] == 'R':
        return '🪨 The object is a Rock'
    else:
        return '⛏️ The object is a Mine'

def main():
    # Page title and description
    st.markdown("""
    <div style="background-color: #f4f4f4; padding: 10px; border-radius: 8px; text-align: center;">
        <h1 style="color: #2b5b84;">🔍 Rock vs Mine Prediction</h1>
        <p style="font-size: 16px; color: #4b4b4b;">
            Welcome to the Rock vs Mine Predictor!<br>
            This app uses a machine learning model to predict whether an object is a rock or a mine based on 60 features.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Input container
    st.markdown("""
    <div style="margin: 20px 0; padding: 10px; border: 1px solid #ddd; border-radius: 8px; background-color: #fdfdfd;">
        <h4 style="color: #444;">Enter your data below 👇</h4>
    </div>
    """, unsafe_allow_html=True)

    # Input field for user data
    user_input = st.text_input(
        'Enter 60 comma-separated numeric values:',
        placeholder='e.g., 0.02, 0.37, 0.42, 0.20, ...',
    )

    # Add a button with a modern style
    button_style = """
    <style>
    .stButton button {
        background-color: #2b5b84;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #1a3c5c;
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Trigger prediction on button click
    if st.button('🚀 Predict Now'):
        if user_input:
            try:
                # Convert the input string into a list of float values
                input_values = [float(x.strip()) for x in user_input.split(',')]

                # Validate input size
                if len(input_values) == 60:
                    # Call the prediction function
                    result = predict(input_values)

                    # Show success result with style
                    st.markdown(f"""
                    <div style="background-color: #dff9db; padding: 10px; border-radius: 8px; text-align: center; color: #1e5128;">
                        <h3>{result}</h3>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error('Please enter exactly 60 values.')
            except ValueError:
                st.error('Invalid input. Please enter numeric values separated by commas.')

if __name__ == '__main__':
    main()
