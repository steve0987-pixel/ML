from setuptools import find_packages, setup

HYPER_E_DOT = '-e .'

def get_requirements(file_path: str) -> list[str]:
    """Read requirements from a file and remove '-e .' if present."""
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]
        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    return requirements

setup(
    name='ml',
    version='0.0.1',
    author='Steve',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
