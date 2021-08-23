# The IT Service Intelligence Content Starter Pack

## Overview
This content pack was created to provide both example code and production ready code that can be used to fast track understanding of core ITSI concepts. Read on to see what's present in the content pack and how it can be used

## Installation
1. Install the .spl Splunk App contained in this git repo into your ITSI search head to deliver the necessary core Splunk knowledge objects
2. Using ITSI's backup/restore functionality create a restore for the .zip file contained in this git repo to deliver the necessary ITSI knowledge objects

## Content and Uses Cases in this Content Pack

### Automatic Entity Discovery Searches
It's an ITSI best practice to create entities automatically from searches. The best practice has already been implemented for many common entity types supported out of the box with ITSI and IT Essentials - Work. However you will often find it necessary to add your own custom entities or enhance the alias and info fields of existing entities. The content pack contains several searches to help you get started creating your own entities from search. See the documentation for more information on [how to import entities from search](https://docs.splunk.com/Documentation/ITSI/latest/Entity/ImportSearch) 
1. **IT Service Intelligence - ITSI Starter Pack Entity Discovery Template - Entity Discovery Search** - This search is intended to act as a template for all your entity discovery searches. It should be cloned and updated for the entities you wish to discover and import
2. **IT Service Intelligence - ITSI Starter Pack Example Entity - Entity Discovery Search** - This search was provided as a specific example of what a template clone might look like. It can be run as-is to import 5 sample entities into the environment that contain alias, info, and entity type information

### Automated Service Tree Build
Similar to how entities can be created from search, so to can ITSI services and service treed. This is an advanced ITSI concept that you may find is right for you when you are trying to dynamically manage a tree from structure within your data or trying to mirror a service model stored in another system. The content pack contains several searches to help you get started creating your own services and service trees from search. See the documentation for more information on [how to create services from search](https://https://docs.splunk.com/Documentation/ITSI/latest/SI/ImportSearch) 
1. **IT Service Intelligence - ITSI Starter Pack Service Tree Creation Template - Service Tree Search** - This search is intended to act as a template for all your automatic service and service tree creation searches. It should be cloned and updated for the services you wish to discover and import
2. **IT Service Intelligence - ITSI Starter Pack Example Automatic Tree - Service Tree Search** - This search was provided as a specific example of what a template clone might look like. It can be run as-is to import 4 new services in a simple service tree hierarchy into the environment. Before you run this search, you must first create the example entities as is outlined in the *Automatic Entity Discovery Searches* section of the documentation
