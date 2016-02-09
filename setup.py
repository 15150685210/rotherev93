from setuptools import setup, find_packages

setup(
    name='rotherev93',

    description='Simulations based on Roth Erev \'93',

    long_description=open('README.md').read(),

    version=open('VERSION').read().strip(),

    author='Matt Gambogi',

    author_email='gambogi@csh.rit.edu',

    packages=find_packages(),

    include_package_data=True,

    install_requires= open('requirements.txt').readlines()
)
