from setuptools import setup, find_packages

install_requires = ['click==8.1.3', 'requests==2.31.0', 'tabulate==0.8.9', 
                    'nba-api==1.3.1', 'pandas==2.0.3', 'prettytable==3.9.0',
                    'lxml==4.9.3', 'html5lib==1.1', 'bs4==0.0.1', 'scipy==1.10.1']

setup(
    name='nba-stats-dragon',
    description='NBA CLI Tool to display Head to Head Stats.',
    packages=find_packages(),
    author='Rakeen Rouf (rmr327)',
    entry_points="""
    [console_scripts]
    nbastats=mylib.nba_stats:run_stats
    """,
    install_requires=install_requires,
    version='0.1.0',
    url='https://github.com/nogibjj/nba-cli-tool',
)
