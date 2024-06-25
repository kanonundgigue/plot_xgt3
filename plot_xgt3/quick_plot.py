# quick_plot.py
from .data_loader import Gtool3DataLoader
from .plotter import ContourPlotter

def error_handling_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            print(f"Error: The specified date (year={kwargs.get('year')}, month={kwargs.get('month')}, day={kwargs.get('day')}) does not exist in the dataset. Please check the data file and the date parameters.")
    return wrapper

@error_handling_decorator
def quick_plot(filename, levels, title="", colorbar_orientation='horizontal', figsize=(10, 5.5), figure_name="tmp.png", save_fig=False, central_longitude=180, cmap='viridis', year=None, month=None, day=None):
    """
    Load data from a file and plot a colored contour map with specified projection.
    
    Args:
        filename (str): Path to the data file.
        levels (list): Contour levels.
        title (str): Plot title.
        colorbar_orientation (str): Orientation of the color bar ('horizontal' or 'vertical').
        figsize (tuple): Figure size (width, height).
        figure_name (str): Name of the file to save the figure.
        save_fig (bool): Whether to save the figure to a file.
        central_longitude (int): Central longitude for the map projection.
        cmap (str): Colormap for the plot.
        year (int): Year for slicing the data.
        month (int): Month for slicing the data.
        day (int): Day for slicing the data.
    """
    # データの読み込み
    loader = Gtool3DataLoader()
    data = loader.load_data(filename)

    # データの選択
    if year and month:
        if day:
            time_str = f'{year}-{month:02d}-{day:02d}'
        else:
            time_str = f'{year}-{month:02d}'
        data = data.sel(time=time_str)
    data = data.squeeze()

    # プロット
    plotter = ContourPlotter()
    plotter.plot_data(data, levels, cmap, title, colorbar_orientation, figsize, figure_name, save_fig, central_longitude)
