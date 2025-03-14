from setuptools import setup, find_namespace_packages, find_packages

setup(
  name = 'jaxrk',
  packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  version = '0.1.1',
  license='MIT',
  python_requires="<=3.10",
  description = 'JaxRK is a library for working with (vectors of) RKHS elements and RKHS operators using JAX for automatic differentiation.',   # Give a short description about your library
  author = 'Ingmar Schuster',
  author_email = 'ingmar.schuster@zalando.de',
  url = 'https://github.com/zalandoresearch/jaxrk',
  download_url = 'https://github.com/zalandoresearch/jaxrk/v_01.tar.gz',
  keywords = ['Jax', 'RKHS', 'kernel'], 
  install_requires=['jax==0.3.1', 'numpy==1.26.4', 'jaxlib==0.3.0', 'scipy<=1.12.0,>= 1.6.0', 'matplotlib', 'flax==0.3.0', 'pathlib2'],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)