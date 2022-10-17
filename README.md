# Test2Feature
This tool that objective show the test traceability for feature in systems HCSs.

## First steps:

* Clone this repository: `git clone https://github.com/willianferrari/Test2Feature.git `

## Required Software:

* [Doxygen](https://doxygen.nl/index.html)
* ![](https://img.shields.io/badge/python-3.6+-blue.svg)
    - [Pandas](https://pandas.pydata.org/) library
    - [Numpy](https://numpy.org/) library
* JDK 8
* [Gradle](http://gradle.org/ "Gradle") 4.4 as build system;
  - **For downgrade Java and Gradle can used [SDKMAN](https://sdkman.io/)**

## Setup to Run:

It will be necessary to update the parameters of the ConfigFile.sh file:
* Parameters
  - **REPGIT**: URL GitHub System;
  - **SYSFOLDER**: system folder name;
  - **TESTFOLDER**: test folder name;
  - **NCOMMIT**: the Git commit hash to analyze;

* Type the following command in a command line:
  - ./ConfigFile.sh
 
 ## The original paper was published at:

* Willian D. F. Mendonça, Silvia R. Vergilio, Gabriela K. Michelon, Alexander Egyed, and Wesley K. G. Assunção. 2022. Test2Feature: feature-based test traceability tool for highly configurable software. In Proceedings of the 26th ACM International Systems and Software Product Line Conference - Volume B (SPLC '22). Association for Computing Machinery, New York, NY, USA, 62–65. https://doi.org/10.1145/3503229.3547031
