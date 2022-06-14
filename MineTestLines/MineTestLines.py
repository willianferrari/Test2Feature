import pandas as pd
import os
import xml.etree.ElementTree as ET
import sys

def readFiles(dirct,testsfile):
    listFile = []
    listFileAux = []
    for diretorio, subpastas, arquivos in os.walk(dirct):
        
        normalized_path = os.path.normpath(diretorio)
        path_components = normalized_path.split(os.sep)
        aux = path_components[path_components.index(testsfile):len(path_components)]
        path = os.path.join(*aux)

        for arquivo in arquivos:
            file = os.path.join(arquivo)
            if file.endswith('.c'):
                if file in listFile:
                    file = path + '/' + file
                    file = file.split('/')
                    file = file[-2]+'/'+file[-1]
                    listFile.append(file)

                else:
                    listFile.append(file)

                file = file.replace('_','__')
                file = file.replace('.c','_8c.xml')
                file = file.replace('/','_2')
                listFileAux.append(file)

    return listFileAux

def renameFile(file):
    file = file.replace('__','_')
    file = file.replace('_8c.xml','.c')
    file = file.replace('_8c','.c')
    file = file.replace('_8h','.h')
    file = file.replace('_8txt','.txt')
    file = file.replace('_2','/')
    return file

def xmlparserReferences(listFile,dirc):

    df = pd.DataFrame(columns=['TestFile', 'TestCase', 'TargetFile', 'TargetFunction', 'LineFrom', 'LineTo'])
    for path_file in listFile:
        file = renameFile(path_file);
        path_file = dirc + "/" + path_file
        if os.path.isfile(path_file):
            with open(path_file) as XMLFile:
                textoArquivo = XMLFile.read()
                root = ET.fromstring(textoArquivo)
   
            for main in root.findall('compounddef'):
                for sectiondef in main.findall('sectiondef'):               
                    for memberdef in sectiondef.findall('memberdef'):
                        name = memberdef.find('name')

                        for referencedby in memberdef.findall('references'):
                            if(memberdef.get('kind') == 'function'):    
                                file_name = referencedby.get('compoundref')
                                if(file_name != None):
                                    startline =  referencedby.get('startline')
                                    endline =  referencedby.get('endline')
                                    
                                    file_name = renameFile(file_name)
                                    df = pd.concat([df, pd.DataFrame.from_records([{'TestFile' : file, 'TestCase' : name.text, 'TargetFile' : file_name, 'TargetFunction' :  referencedby.text, 'LineFrom': startline, 'LineTo':endline}])])

        else:
            print("File not find: " + path_file)

    return df

def main():
    
    listFile = readFiles(sys.argv[1],sys.argv[3])

    dfRef = xmlparserReferences(listFile,sys.argv[2])

    dfRef.to_csv('result/MineTestLines.csv')

main()