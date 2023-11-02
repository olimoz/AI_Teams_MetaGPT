## main.py
from data_analysis import DataAnalyzer
from plotting import Plotter
from file_operations import FileOperator

def main():
    data_path = 'input.xlsx'
    output_data_path = 'output.xlsx'
    treemap_path = 'treemap.jpg'

    # Initialize the DataAnalyzer, Plotter, and FileOperator classes
    data_analyzer = DataAnalyzer(data_path)

    # Analyze and cluster data
    data_analyzer.analyze_and_cluster_data()

    # Create summary
    data_analyzer.create_summary()

    # Initialize the Plotter and FileOperator classes with the updated data
    plotter = Plotter(data_analyzer.data)
    file_operator = FileOperator(data_analyzer.data)

    # Create treemap
    plotter.create_treemap()

    # Print treemap
    plotter.print_treemap(treemap_path)

    # Save data to Excel
    file_operator.save_data_to_excel(output_data_path)

if __name__ == "__main__":
    main()
