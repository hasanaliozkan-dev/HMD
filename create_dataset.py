import pandas as pd
import numpy as np
import random


np.random.seed(42)
random.seed(42)


def random_gender():
    return random.choice(["Male", "Female", None] if random.random() < 0.1 else ["Male","Female"])

def random_education():
    
    return random.choice(["High School", "Bachelor's", "Master's", "PhD", None] if random.random() < 0.1 else ["High School", "Bachelor's", "Master's", "PhD"])

def random_income():
    
    return random.choice([random.randint(20000, 120000), None] if random.random() < 0.1 else [random.randint(20000, 120000)])

def random_age():
    
    return random.choice([random.randint(18, 65), None] if random.random() < 0.1 else [random.randint(18, 65)])

def random_satisfaction():
    
    return random.choice([random.randint(1, 10), None] if random.random() < 0.1 else [random.randint(1, 10)])

def random_purchase():
    
    return random.choice(["Yes", "No", None] if random.random() < 0.1 else ["Yes", "No"])

# Generate the dataset
data = {
    "ID": range(1, 101),
    "Age": [random_age() for _ in range(100)],
    "Gender": [random_gender() for _ in range(100)],
    "Education Level": [random_education() for _ in range(100)],
    "Income": [random_income() for _ in range(100)],
    "Satisfaction Rating": [random_satisfaction() for _ in range(100)],
    "Purchased Product": [random_purchase() for _ in range(100)],
}

df = pd.DataFrame(data)


csv_path = "synthetic_missing_data.csv"
df.to_csv(csv_path, index=False)


