from setuptools import setup, find_packages

setup(
    name='ustat_var',
    version='0.3.0',
    description='Unbiased estimators for variance of teacher effects',
    package_dir={'': 'src'},    
    packages=find_packages(where='src'),  
    install_requires=[
        'numpy',
        'scipy',
    ],
    python_requires='>=3.7',
)
