# Feature4Test
This tool that objective show the test traceability for feature in systems HCSs.

## First steps:

* Clone this repository: `git clone https://github.com/willianferrari/Feature4Test.git `
* Clone the Git repository of the target system in folder on your computer (as an example, SqLite Git repository: https://github.com/sqlite/sqlite.git)

## Required Software:

* [Doxygen](https://doxygen.nl/index.html)
* ![](https://img.shields.io/badge/python-3.6+-blue.svg)
    - [Pandas](https://pandas.pydata.org/) library
    - [Numpy](https://numpy.org/) library
* JDK 8
* [Gradle](http://gradle.org/ "Gradle") 4.4 as build system;
  - **For downgrade Java and Gradle can used [SDKMAN](https://sdkman.io/)**

## Setup to Run:

It will be necessary to update the parameters of the Exec.sh file:
* Parameters
  - **REPGIT**: URL GitHub System;
  - **SYSFOLDER**: system folder name;
  - **TESTFOLDER**: test folder name;
  - **NCOMMIT**: the Git commit hash to analyze;

* Type the following command in a command line:
  - ./Exec.sh