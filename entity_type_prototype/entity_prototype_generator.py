import argparse
from distutils.dir_util import copy_tree
import os, fnmatch, glob
import subprocess
import json


def findReplaceInFile(directory, find, replace, filePattern):
    for filepath in glob.iglob('{0}/**/*.*'.format(directory), recursive=True):
    	with open(filepath) as file:
        	s = file.read()
    	s = s.replace(find, replace)
    	with open(filepath, "w") as file:
        	file.write(s)

def findReplaceFileName(directory, find, replace):
    for subdir, dirs, files in os.walk(directory):
    	for f in files:
        	fileName = subdir+"/"+f
        	os.rename(fileName, fileName.replace(find, replace))

#generic json file opener helper
def openJSONFile(filename):
	with open(filename, 'r') as myfile:
		content = json.loads(myfile.read())

	return content

def createEntityAppFromProtoApp(entityTypeDisplayName, entityTypeId):
	fromDirectory = "./DA-ITSI-CP-entity_type"
	toDirectory = "./build/DA-ITSI-CP-{0}".format(entityTypeId)
	copy_tree(fromDirectory, toDirectory)

	findReplaceInFile(toDirectory, "ENTITY-TYPE-ID", entityTypeId, "*")
	findReplaceInFile(toDirectory, "ENTITY-TYPE-DISPLAY", entityTypeDisplayName, "*")
	findReplaceFileName(toDirectory, "ENTITY-TYPE-ID", entityTypeId)

	return "DA-ITSI-CP-{0}".format(entityTypeId)

def tarEntityApp(parentFolder, zipFolder, entityTypeId):
	tar = "DA-ITSI-CP-{0}.spl".format(entityTypeId)

	subprocess.call("cd {0} && zip -r {1} {2}".format(parentFolder, tar, zipFolder), shell=True)

	return parentFolder+"/"+tar

def createEntityTypeInTargetSplunkInstance(args):
	proto = openJSONFile("./entity_type_prototype.json")
	proto = json.dumps(proto).replace("ENTITY-TYPE-ID", args.entityTypeId).replace("ENTITY-TYPE-DISPLAY", args.entityTypeDisplayName)
	
	curlCommand = "curl -k -u {0}:{1} '{2}:8089/servicesNS/nobody/SA-ITOA/itoa_interface/entity_type' --header 'Content-Type: application/json' -X POST -d '{3}'".format(args.splunkUsername, args.splunkPassword, args.splunkServerURL, proto)

	subprocess.call(curlCommand, shell=True)

def main(args):
	folder = createEntityAppFromProtoApp(args.entityTypeDisplayName, args.entityTypeId)
	tar = tarEntityApp("./build", folder, args.entityTypeId)
	createEntityTypeInTargetSplunkInstance(args)


	instructions="""




***************************************************************************
*** Successfully generated the entity type. Please perform the following
***************************************************************************
    1. Manually install the DA-ITSI-CP add-on that was generated for this entity type located here: {2}
    2. After step 1, follow the entity type build-out instructions here: /en-US/app/{0}/{1}
	""".format(folder, args.entityTypeId+"_overview", tar)

	print (instructions)

# Start of script
parser = argparse.ArgumentParser()
parser.add_argument("entityTypeDisplayName", help="The user friendly display name of the entity type in singular form. (I.E. Web Server. Not Web Servers)")
parser.add_argument("entityTypeId", help="The identifier name for the entity. Typically matches entity name in all lower case and spaces switched to underscores. (I.E. web_server)")
parser.add_argument("splunkServerURL", help="The Splunk instance on which to build the new entity type. (I.E. https://localhost)")
parser.add_argument("splunkUsername", help="The Splunk username credentials with access to run adminstrative functions using REST API")
parser.add_argument("splunkPassword", help="The Splunk password credentials with access to run adminstrative functions using REST API")

main(parser.parse_args())