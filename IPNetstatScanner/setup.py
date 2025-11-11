from setuptools import setup, find_packages

setup(
    name='IPNetstatScanner',
    version='1.0.0',
    author='Alberto aka Trewsaazz, Lidia aka LidiaGL',
    author_email='trewsaz99@gmail.com, lidiagutierrezlopez@gmail.com',
    description='Tool to scan and analyze network connections using IP and netstat data, to find malicious connections.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/trewsaazz/IPNetstatScanner',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.9',
    install_requires=[
        'psutil>=5.9.5',
        'requests>=2.31.0',
        'python-dotenv>=1.0.0',
        'geoip2>=4.9.0',
    ],
    entry_points={
        'console_scripts': [
            'ipnetstatscanner=ip_threat_scanner.main:cli_main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
    ],
)
