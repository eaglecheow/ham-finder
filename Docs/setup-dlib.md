# How to Setup Dlib Python Package

## Tools Required

1. [Python](https://www.python.org/)

2. [CMake](https://cmake.org/download/)

3. Windows SDK (Required while installing for Windows)

4. C++ Compiler (MSVC is used for this document)

> For this case, both Windows SDK and MSVC can be obtained through [Visual Studio Installer](https://visualstudio.microsoft.com/).

> For the time this document is written, some of the packages that will be used only supports Python 3.7. Therefore it is recommended to check the version of Python you're using.

## How to Install

1. Make sure all the tools mentioned in [this](#tools-required) section is installed correctly.

2. Navigate to your project folder.

3. Install `pipenv` to enable Python virtual environment.

    ```batch
    pip install pipenv
    ```

4. By using `pipenv`, install the `dlib` Python package.

    ```batch
    pipenv install dlib
    ```

    This command initiates a virtual environment in the project folder (if haven't already), and install the `dlib` package to the virtual environment. This process might take a while and takes quite an amount of resource as C++ compilation will be done in the background.

5. Once installed, `dlib` should be ready to be imported and consumed in the project.
