import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME= "IPYNBrenderer"
AUTH_USER_NAME= "gouri1694"
SRC_REPO="IPYNBrenderer"
AUTH_EMAIL="igouri8@gmail.com"

setuptools.setup(
    name=SRC_REPO.capitalize,
    version=__version__,
    author=AUTH_USER_NAME,
    author_email=AUTH_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTH_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTH_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)