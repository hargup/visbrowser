from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='visbrowser',
    version='0.2.2',
    author='Harsh Gupta',
    author_email='harsh@felvin.com',
    description='A visual browsing adapter for Playwright Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hargup/visbrowser',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)