from setuptools import setup, find_packages

setup(
    name='easy_db',
    version='0.1.0',
    author='Shubham Akshit',
    author_email='akshitshubhammas@gmail.com',
    description='A simple database management package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shubhamakshit/easy_db',
    packages=find_packages(),
    install_requires=[
        'pymongo',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
