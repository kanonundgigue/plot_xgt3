# plotter.py
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

class Plotter(ABC):
    @abstractmethod
    def plot_data(self, data, levels, cmap, title, colorbar_orientation, figsize, figure_name, save_fig, central_longitude):
        pass
    
class ContourPlotter(Plotter):
    def plot_data(self, data, levels, cmap, title, colorbar_orientation, figsize, figure_name, save_fig, central_longitude):
        plt.figure(figsize=figsize)
        ax = plt.axes(projection = ccrs.PlateCarree(central_longitude))
        contourf = data.plot.contourf(ax=ax, transform=ccrs.PlateCarree(), levels=levels, cmap=cmap, add_colorbar=True, cbar_kwargs={'orientation': colorbar_orientation})
        ax.coastlines()
        plt.title(title)
        
        if save_fig:
            plt.savefig(figure_name)
        plt.show()
        plt.close()