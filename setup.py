from distutils.core import setup

setup(
    name='Mortality_Analysis',
    version='0.1.0',
    description='Data analysis',
    author='Lokesh Dondapati',
    author='Sai Krishna Dadi',
    author='Thulasi ram',
    author_email='ldondapa@mail.yu.edu',
    author_email='sdadi@mail.yu.edu',
    author_email='tveerama@mail.yu.edu',
    license='MIT',
    url='https://github.com/LokeshDondapati/Mortality_Analysis',
    packages=['mortality_analysis'],
    install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'seaborn>=0.11.0',
        'scikit-learn>=1.3.2',
        'scipy>=1.11.4',
        'requests>=2.31.0'


    ],
)
