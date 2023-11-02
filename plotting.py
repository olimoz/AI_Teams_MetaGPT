## plotting.py
import plotly.graph_objects as go
import pandas as pd
import kaleido

class Plotter:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.treemap = None

    def create_treemap(self):
        self.treemap = go.Figure(data=go.Treemap(
            labels=self.data.index,
            parents=self.data['cluster'],
            values=self.data['value']
        ))

    def print_treemap(self, file_path: str = 'treemap.jpg'):
        if self.treemap is None:
            raise ValueError("Treemap has not been created. Please call create_treemap() method first.")
        self.treemap.write_image(file_path, engine="kaleido")
