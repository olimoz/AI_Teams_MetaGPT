## data_analysis.py
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

class DataAnalyzer:
    def __init__(self, data_path: str):
        self.data = pd.read_excel(data_path)
        self.summary = {}

    def preprocess_data(self):
        # Handle missing values
        imputer = SimpleImputer(strategy='mean')
        self.data = pd.DataFrame(imputer.fit_transform(self.data), columns=self.data.columns)

        # Convert non-numeric data to numeric
        self.data = self.data.apply(pd.to_numeric, errors='coerce')

        # Normalize the data
        scaler = StandardScaler()
        self.data = pd.DataFrame(scaler.fit_transform(self.data), columns=self.data.columns)

    def analyze_and_cluster_data(self, n_clusters: int = 3):
        self.preprocess_data()
        kmeans = KMeans(n_clusters=n_clusters)
        self.data['cluster'] = kmeans.fit_predict(self.data)

    def create_summary(self):
        self.summary = self.data.describe(include='all').to_dict()
