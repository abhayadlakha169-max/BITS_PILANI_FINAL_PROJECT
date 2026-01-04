from sklearn.model_selection import train_test_split
import pandas as pd
from config.paths_config import *

data = pd.read_csv("artifacts/raw/Hotel Reservations.csv")
train_data , test_data = train_test_split(data , test_size=0.2 , random_state=42)

train_data.to_csv(TRAIN_FILE_PATH)
test_data.to_csv(TEST_FILE_PATH)