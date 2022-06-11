#!/bin/bash

#PATH System
PATHSYS="/Users/willianmendonca/Documents/database/sqlite/"
#PATH Tests
PATHTEST="/Users/willianmendonca/Documents/database/sqlite/test"
#Name of Test Folder
TESTFOLDER="test"
#Commit Sha
NCOMMIT="6fdac751277981a8fa4db8eda339b9c140140bd7"
# #PATH System
# PATHSYS="<PATH SYSTEMS>"
# #PATH Tests
# PATHTEST="<PATH TEST FOLDER>"
# #Name of Test Folder
# TESTFOLDER="<NAME TEST FOLDER>"
# #Commit Sha
# NCOMMIT="<COMMIT SHA HASH>"

#PATH
PATHSCRIPT=$PWD
#PATH XML Files
PATHXML="${PATHSYS}xml"

# Exec Feature Location
# cd MineFeaturesLines
# gradle run -Pmyargs=$PATHSYS,"${PATHSCRIPT}/result-featurelocation",$NCOMMIT

#Exec Doxygen
# cd $PATHSCRIPT
# cp -a Doxygen/Doxyfile $PATHSYS
# cd $PATHSYS
# doxygen Doxyfile

#Exec ParserXML
cd "${PATHSCRIPT}/TraceTest"
python3 traceTest.py $PATHTEST $PATHXML $TESTFOLDER

# Exec Merge Feature X Tests
cd "${PATHSCRIPT}/Test4Feature"
python3 mergeFeature4Test.py "${PATHSCRIPT}/TraceTest/result/ref.csv" "${PATHSCRIPT}/result-featurelocation/${NCOMMIT}/FilesFeature/feature.csv"
