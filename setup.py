from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='ghfetch',
    version='0.1.1',
    author='Wooferz',
    author_email='contact@wooferz.dev',
    license='MIT',
    description='Fetches information of a specified github user.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/woooferz/ghfetch',
    py_modules=['ghfetch', 'app'],
    package_dir={'':"src"},
    packages=find_packages("src"),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        ghfetch=ghfetch:run
    '''
)
