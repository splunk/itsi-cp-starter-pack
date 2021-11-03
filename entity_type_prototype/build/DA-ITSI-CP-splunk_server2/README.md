# ITSI Content Starter Pack - New/Custom Entity Type Generator 

## Overview
Entity types are a powerful concept in ITSI and IT Essentials - Work, but their configuration is not necessarily obvious and much of the configuration is "boilerplate" that you shouldn't have to be worried about. As such, this content pack seeks to facilitate creating new entity types easily, and with boilerplate code using best practice configurations that you can simply update to meet the specific needs of your entity type.

Review the rest of the README to understand how to create a new entity type with "prototype / boilerplate" code that you can update for your specific entity type.


## High Level Steps
To get a new entity type created, follow the below high level steps:
1. Run a python3 command to generate the new entity type in a target Splunk instance
2. Manually install the corresponding DA-ITSI-CP-* app into your Splunk instance which houses the Core Splunk knowledge objects used by your entity type
3. Proceed on with the configuration of the entity type in your target Splunk instance


### Step 1 - Run the python command
1. Ensure python3 is installed in your environment
2. From a shell within the ./entity_type_prototype folder execute the following command
3. python3 ./entity_prototype_generator.py "YOUR ENTITY TYPE DISPLAY NAME" "YOUR ENTITY TYPE ID" https://theURIOfYourSplunkInstance admin adminpassword

### Step 2 - Manually install the newly generated DA-ITSI-CP-* App
1. Review the output from the python command above... it should indicate success and the name of the new DA-ITSI-CP app
2. The app (DA-ITSI-CP-entity_id.spl) should be located in the ./entity_type_prototype/build folder
3. Manually install it into the Splunk environment (Ususally within the manage app screen)

### Step 3 - Configure the remainder of the entity type config
1. Review the output from the python command above... it should indicate a relateive URL to navigate to in your Splunk instance
2. Navigate to the relative URL of the overview dashboard for your newly created entity type and follow the instructions for entity type build out


Example shell commands and output to build a new entity type
