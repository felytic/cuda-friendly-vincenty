try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='cuda-friendly-vincenty',
    version='0.1',
    description='Function for geographical distances calculation '
    'that can run on GPU using CUDA.',
    long_description=open('README.rst').read(),
    author='Serhii Hulko',
    author_email='felytic@gmail.com',
    url='https://github.com/felytic/cuda-friendly-vincenty',
    packages=['cuda-friendly-vincenty'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
