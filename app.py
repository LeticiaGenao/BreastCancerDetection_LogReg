from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model (ensure 'model.pkl' is in the correct path)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve data from form
        input_features = [
            float(request.form['clump_thickness']),
            float(request.form['uniformity_of_cell_size']),
            float(request.form['uniformity_of_cell_shape']),
            float(request.form['marginal_adhesion']),
            float(request.form['single_epithelial_cell_size']),
            float(request.form['bare_nuclei']),
            float(request.form['bland_chromatin']),
            float(request.form['normal_nucleoli']),
            float(request.form['mitoses'])
        ]
        features = np.array(input_features).reshape(1, -1)
        prediction = model.predict(features)[0]

        # Convert numeric prediction back to label
        prediction = 'Malignant' if prediction == 1 else 'Benign'

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)