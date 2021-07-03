from pathlib import Path


from setuptools import setup, find_packages


def load_module_dict(filename: str) -> dict:
    import importlib.util as ilu
    filename = Path(__file__).parent / filename
    spec = ilu.spec_from_file_location('', filename)
    module = ilu.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__dict__


name = "rcd_str"
constants = load_module_dict(f'{name}/_constants.py')

readme = (Path(__file__).parent / 'README.md').read_text(encoding="utf-8")
readme = "# " + readme.partition("\n#")[-1]

setup(
    name=name,
    version=constants['__version__'],

    author="Artëm IG",
    author_email="ortemeo@gmail.com",
    url='https://github.com/rtmigo/rcd_str_py',

    packages=find_packages(exclude=['tests']), #include=['rcd_wikipedia/*']),

    install_requires=[""],
    description="Reusable code handling strings",

    long_description=readme,
    long_description_content_type='text/markdown',

    license="MIT",

    keywords="string unicode".split(),

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
     ],
)
