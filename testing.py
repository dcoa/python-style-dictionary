import subprocess


# Define the Style Dictionary command to execute
style_dictionary_command = 'node build.js'


# Execute the Style Dictionary command using subprocess
subprocess.run(style_dictionary_command, shell=True, check=True)


# import os
# from node_edge import NodeEngine

# package = {
#     "dependencies": {
#         "axios": "^1.2.0",
#         "style-dictionary": "^3.8.0"
#     },
# }

# with NodeEngine(package) as ne:
#     style = ne.import_from('style-dictionary').extend({
# 	"source": [
# 		os.getcwd() + "/tokens/**/*.json"
# 	],
# 	"platforms": {
# 		"css": {
# 			"prefix": "pgn",
# 			"transformGroup": "css",
# 			"buildPath": os.getcwd() + "/build/bragi/",
# 			"files": [
# 				{
# 					"destination": "_variables.css",
# 					"format": "css/variables",
# 					"options": {
# 						"outputReferences": True
# 					}clear

# 				}
# 			]
# 		}
# 	}
# })
    # style.buildAllPlatforms()

# from javascript import require


# style = require('style-dictionary').extend('/home/dcoa/Documents/eduNext/distro/style-dictionary/config.json')
# style.buildAllPlatforms()
