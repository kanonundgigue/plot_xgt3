from setuptools import setup, find_packages

setup(
    name='plot_xgt3',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.23.0',
        'matplotlib',
        'cartopy',
        'xgtool3 @ git+https://github.com/k1bb/xgtool3.git'
    ],
    author='Kanon Kino',
    author_email='kanon@hydra.t.u-tokyo.ac.jp',
    description='A package to plot gtool data',
    url='https://github.com/kanonundgigue/plot_xgt3'  
)