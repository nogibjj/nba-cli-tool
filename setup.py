from setuptools import setup, find_packages

# read the requirements.txt file and use it to install dependencies
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='nba-stats',
    description='NBA CLI Tool to display Head to Head Stats.',
    packages=find_packages(),
    author='Rakeen Rouf (rmr327)',
    entry_points="""
    [console_scripts]
    nbastats=mylib.nba_stats:run_stats
    """,
    install_requires=install_requires,
    version='0.0.1',
    url='https://github.com/nogibjj/nba-cli-tool',
)
