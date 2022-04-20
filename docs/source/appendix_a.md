# Appendix - Templates and Rubrics

## Appendix A. Content Management

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
cm_ |content_management|definition|essential|['weight':1]



## Appendix B. Requirements

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
req_ |requirements|definition|essential|['weight':1]

req_systems
req_data_owner
req_data_origin
req_data_production
req_date_acquired
req_date_deprecated
req_workshop_conducted
req_conceptual_model > high-level, real world customer data model concept(s)
req_logical_model > detailed connections between data fields and conceptual model(s)
req_canonical_model > same as mod_schema

#### Request for Engineering

Name|Type|Description
--|--|--
timestamp|Timestamp|Datetime for request. Each adjustment (row) to the short form for a data product and/or service within a specified project will have a unique timestamp.
requester|String|Name(s) of those initiating the short form requirements.
requester_info|String|Contact information for the requester.
customer|String|Name(s) of those receiving the deliverables of a data product and/or service.
customer_info|String|Contact information for the customer.
project|String|Name of the project from which the requirements originated.
deliverable|String|A list of products and services requested by the customer.
data_source|String|A list of raw data resources associated with requirements.
data_poc|String|Name(s) of those originating and/or curating the data sources.
data_poc_info|String|Contact information for the data point of contact.
schema|String|The schema and data dictionary for the raw data.
data_format|String|The format(s) in which the raw data is stored and/or delivered.
data_type|String|The raw data types and their requested transformations.
metadata|String|A list of key-value pairs for all raw data metadata.
endpoint|String|The requested product and/or service delivery specifications.
ux_ui|String|Optional field for user experience or user interface specifications.
security|String|Optional field for data security practices.



## Appendix C. Task Management

### Templates

#### Data Team Board Setup

The name of the board should be `Project Name - Data Team` where `Project Name` is the name of the project from which the business requirements originated. The list names and descriptions are as follows:

Name|Description
--|--
Backlog|The list of task and subtasks derived from the project's business requirements.
Sprint Backlog|The selected and prioritized list of tasks and subtasks scope for completion during a sprint.
In Progress|Assigned sprint tasks in the process of being completed for a sprint.
Sprint dd.mm.yy - x Weeks|Completed sprint tasks for a given sprint.

There are special cards included by default with this template:

Card|List|Description
--|--|--
Product Owner: Name|Backlog|The contact information and additional information for the product owner.
Scrum Master: Name|Backlog|The contact information and additional information for the project scrum master.
Product Goal|Backlog|The product goal statement used to scope the tasks in the backlog. Included a __*Definition of Done*__ for the product.
Sprint Goal|Sprint dd.mm.yy - x Weeks|The sprint goal statement used to scope the tasks in the sprint backlog.

To assist the product owner and scrum master, colored label should also be used to signal status in a sprint.

Label Color|Description
--|--
Green|On Track
Yellow|Testing
Orange|Quality Control
Red|Blocker
Black|Done



### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
tms_ |task_management|definition|essential|['weight':1]



## Appendix D. Version Control

### Templates

#### GitFlow

#### Process

Repository naming convention?
  project digraph + tool name
Readme template
  title
  description
  installation
  use limitations  
docs
  sphinx
wiki
issues
license
contributing
  GitFlow
  peer/mob coding

#### Repository Template

Goal is maximum reuse of well-documented code and methods.

from the top of the repository

* .gitignore
* README.md
  * Links/locations to CMS on information system(s)
* LICENSE.md
* CONTRIBUTING.md
* SECURITY.md
* data_ops
  * README.md
  * CONTRIBUTING.md
  * docs
    * requirements
      * README.md
    * task_management
      * README.md
    * methods_research
      * README.md
    * quality_assurance
      * README.md
    * images
      * README.md
  * data_management
    * storage
      README.md
      * pipelines
    * modeling
      README.md
    * analysis
      README.md
    * integration
      README.md

For each DMS section associated with code or tool methods, source folder content should maintain this baseline:

* models
  * model_a
    * README.md
    * source
    * tests


### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
vcs_ |version_control|definition|essential|['weight':1]



## Appendix E. Quality Assurance

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
qa_ |quality_assurance|definition|essential|['weight':1]



## Appendix F. Security

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
sec_ |security|definition|essential|['weight':1]



## Appendix G. Ethics

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
eth_ |ethics|definition|essential|['weight':1]



## Appendix H. Storage

### Templates

### Rubrics

* Benchmark
  * essential
  * non-essential
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
sto_data_manager|storage|manager that directs data storage practices and personnel|essential|['weight':1]
sto_deputy_data_manager|storage|data manager that assists the primary data manager (if exists)|optional|['weight':1]
sto_project_manager|storage|manager that runs a project for which a raw data asset is required|essential|['weight':1]
sto_legal_counsel|storage|counsel that advises on the legal limits for use of a raw data asset|optional|['weight':1]
sto_project_lead|storage|project manager that assists the primary project manager|optional|['weight':1]
sto_data_management_team|storage|team that supports the data manager and/or deputy data manager|essential|['weight':1]
sto_project_team|storage|team that supports the project manager and/or project lead|optional|['weight':1]
sto_data_engineer|storage|engineer that supports the data management team|essential|['weight':1]
sto_data_owner|storage|owner that produced the raw data asset|essential|['weight':1]
sto_data_steward|storage|steward that moves the raw data asset to the data manager|essential|['weight':1]
sto_tta|storage|security agent that is in charge of tracking loading of and access to raw data assets|essential|['weight':1]
sto_data_asset_name|storage|name of the stored raw data asset|essential|['weight':1]
sto_type|storage|type of raw data asset (e.g., reference, critical, project)|essential|['weight':1]
sto_requirements|storage|requirements reference for a raw data asset|essential|['weight':1]
sto_load_form|storage|form reference for the loading of a raw data asset|essential|['weight':1]
sto_access_form|storage|form reference for the access to a raw data asset|essential|['weight':1]
sto_task_management|storage|task management reference for data management team's raw data asset tasks|essential|['weight':1]
sto_version_control|storage|version control reference for data engineer(s) data loading methods and code|essential|['weight':1]
sto_data_mining|storage|data mining references for sourcing and methods of mined data|recommended if data mining conducted, else optional|['weight':1]
sto_pipelines|storage|pipeline references for models, tools and/or code for processing raw data into storage|essential|['weight':1]
sto_raw_data_location|storage|location reference(s) of raw data storage|essential|['weight':1]
sto_master_data_location|storage|location reference(s) of master data storage|essential|['weight':1]
sto_addendum|storage|form reference for the change in storage to a raw data asset|recommended if addendums generated, else optional|['weight':1]
sto_monitoring|storage|reference for the retention and deprication to all data assets|essential|['weight':1]



## Appendix I. Modeling

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
mod_data_manager|modeling|manager that directs data modeling practices and personnel|essential|['weight':1]
mod_deputy_data_manager|modeling|data manager that assists the primary data manager with modeling(if exists)|optional|['weight':1]
mod_data_management_team|modeling|team that supports the data manager and/or deputy data manager with modeling|essential|['weight':1]
mod_data_engineer|modeling|engineer(s) that support the data management team with modeling|essential|['weight':1]
mod_data_owner|modeling|data personnel that produced the modeled data asset(s)|essential|['weight':1]
mod_data_steward|modeling|steward that moves the raw data asset to and from data management team modeling|essential|['weight':1]
mod_task_management|modeling|task management reference for data management team's data modeling tasks|essential|['weight':1]
mod_version_control|modeling|version control reference for data engineer(s) data modeling methods and code|essential|['weight':1]
mod_scheme|modeling|scheme(s) for the final data model|essential|['weight':1]
mod_schema|modeling|schema(s) for the final data model including data types|essential|['weight':1]
mod_methods|modeling|methods derived from methodologies used in the modeling of the data asset|essential|['weight':1]
mod_description|modeling|description that outlines the overall model approach|essential|['weight':1]
mod_reviewers|modeling|reviewer(s) of the final model elements including scheme, schema, methods, and other essential features|essential|['weight':1]
mod_tags|modeling|tags for the model's associated categories|essential|['weight':1]
mod_entities|modeling|entities that are linked to the modeled data features|essential|['weight':1]
mod_dictionary|modeling|dictionary reference for the modeled data schema features|essential|['weight':1]
mod_transformation|modeling|tranformation details for the final data model|essential|['weight':1]
mod_normalization|modeling|normalization details for the final data model|essential|['weight':1]
mod_sampling|modeling|sampling method suggested for the data asset, used primarily in analytics and the data catalog|essential|['weight':1]
mod_synthetic|modeling|synthetic data reference used for a raw data asset|optional|['weight':1]
mod_entity_res|modeling|entity resolution reference used for a data asset model|optional|['weight':1]
mod_challenge|modeling|challenges that existed with the final model|essential|['weight':1]



## Appendix J. Analytics

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
ana_data_manager|analytics|manager that directs data analytics practices and personnel|essential|['weight':1]
ana_deputy_data_manager|analytics|data manager that assists the primary data manager with analytics(if exists)|optional|['weight':1]
ana_data_management_team|analytics|team that supports the data manager and/or deputy data manager with analytics|essential|['weight':1]
ana_data_engineer|analytics|engineer(s) that support the data management team with analytics|essential|['weight':1]
ana_data_owner|analytics|data personnel that retains the modeled data asset(s) for analytics|essential|['weight':1]
ana_data_steward|analytics|steward that moves the modeled data asset to and from data management team analytics|essential|['weight':1]
ana_task_management|analytics|task management reference for data management team's data analytics tasks|essential|['weight':1]
ana_version_control|analytics|version control reference for data engineer(s) data analytics methods and code|essential|['weight':1]
ana_accuracy|analytics|accuracy metrics of the modeled data asset(s)|essential|['weight':1]
ana_completeness|analytics|completeness metrics of the modeled data asset(s)|essential|['weight':1]
ana_consistency|analytics|consistency metrics of the modeled data asset(s)|essential|['weight':1]
ana_integrity|analytics|integrity metrics of the modeled data asset(s)|essential|['weight':1]
ana_reasonability|analytics|reasonability metrics of the modeled data asset(s)|essential|['weight':1]
ana_timeliness|analytics|timeliness metrics of the modeled data asset(s)|essential|['weight':1]
ana_uniqueness|analytics|uniqueness metrics of the modeled data asset(s)|essential|['weight':1]
ana_validity|analytics|validity metrics of the modeled data asset(s)|essential|['weight':1]
ana_data_size_model|analytics|size of the modeled data asset(s) when stored|essential|['weight':1]
ana_data_size_raw|analytics|size of the raw data asset(s) when stored|essential|['weight':1]
ana_data_shape_model|analytics|shape of the modeled data asset(s)|essential|['weight':1]
ana_data_shape_raw|analytics|shape of the modeled data asset(s)|essential|['weight':1]
ana_descriptive_statistics_model|analytics|statistical profile of the modeled data asset(s) features including nulls, value ranges, data types, and frequency distributions|essential|['weight':1]
ana_descriptive_statistics_raw|analytics|statistical profile of the raw data asset(s) features including nulls, value ranges, data types, and frequency distributions|essential|['weight':1]
ana_format|analytics|the format of the modeled data going through analytics processes|essential|['weight':1]



## Appendix K. Integration

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
int_data_manager|integration|manager that directs data integration practices and personnel|essential|['weight':1]
int_deputy_data_manager|integration|data manager that assists the primary data integration manager (if exists)|optional|['weight':1]
int_project_manager|integration|same as sto_project_manager|essential|['weight':1]
int_legal_counsel|integration|counsel that advises on the legal limits for integration of a modeled data asset|optional|['weight':1]
int_project_lead|integration|same as sto_project_lead|optional|['weight':1]
int_data_management_team|integration|team that supports the data integration manager and/or deputy data manager|essential|['weight':1]
int_project_team|integration|same as sto_project_team|optional|['weight':1]
int_data_engineer|integration|engineer that supports the data integration management team|essential|['weight':1]
int_data_owner|integration|owner that produced or controls the modeled data asset|essential|['weight':1]
int_data_steward|integration|steward that moves the modeled data integration to the data manager|essential|['weight':1]
int_tta|integration|security agent that is in charge of tracking loading of and access to modeled data assets and integrations|essential|['weight':1]
int_plan|integration|plan description for the integration endpoint deployment and delivery|essential|['weight':1]
int_assessment|integration|assessment of proposed final integration behaviors and outputs including format, quality, documentation, metadata lineage updates, data asset provenance, analytic metrics, and policy compliance|essential|['weight':1]
int_design|integration|description of resources and personnel tasked to implement the integration endpoint design|essential|['weight':1]
int_database|integration|database details for the integration endpoint solution|recommended if database used, else optional|['weight':1]
int_api|integration|api details for the integration endpoint solution|recommended if api used, else optional|['weight':1]
int_development|integration|developement details for the integration endpoint solution including testing and logging information|essential|['weight':1]
int_endpoint_implemented|integration|date and time the intgration endpoint was first accessed by the customer (this may be several datatimes, each needing an explanation)|essential|['weight':1]
int_endpoint_deprecated|integration|date and time the intgration endpoint ceased to be available to the customer (this may be several datatimes, each needing an explanation)|essential|['weight':1]
int_provenance|integration|description of how the data asset is used by the customer from the endpoint|essential|['weight':1]
int_monitoring|integration|description of monitoring details, metrics, and actions to be conducted for a deployed endpoint until end of lifecycle|essential|['weight':1]



## Appendix L. Metadata

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
met_metamodel|metadata|scheme description for the data asset's categorical metadata areas|essential|['weight':1]
met_tags|metadata|tags associated with the data asset metadata considerations including type, associated projects, security labels, and associated policy restrictions|essential|['weight':1]
met_editors|metadata|list of personnel contributing to the metadata for a data asset|essential|['weight':1]
met_strategy|metadata|strategy for use of a data asset via metadata element (e.g., knowledge discovery) including migrations|essential|['weight':1]
met_vcs|metadata|link to version control for metadata assets|essential|['weight':1]
met_schedule|metadata|schedule and practice details associated with metadata maintenance including review and enrichment|essential|['weight':1]



## Appendix M. Cataloging

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`

field_name|category|definition|benchmark|metrics
--|--|--|--|--
cat_data_manager|cataloging|manager that directs data cataloging practices and personnel|essential|['weight':1]
cat_deputy_data_manager|cataloging|data manager that assists the primary data manager (if exists)|optional|['weight':1]
cat_legal_counsel|cataloging|counsel that advises on the legal limits for use of a cataloged metadata or master data samples|optional|['weight':1]
cat_data_management_team|cataloging|team that supports the data manager and/or deputy data manager|essential|['weight':1]
cat_data_engineer|cataloging|engineer that supports the data management team|essential|['weight':1]
cat_data_owner|cataloging|owner that produced the master data sample|essential|['weight':1]
cat_data_steward|cataloging|steward that moves the master data sample to the data manager|essential|['weight':1]
cat_annotations|cataloging|annotations on a cataloged data record annotation special access or handling instructions for specific sections of the metadata within and outside of the catalog|essential|['weight':1]
cat_feedback|cataloging|feedback method(s) associated with a data sample for catalog users|essential|['weight':1]
cat_monitoring|cataloging|monitoring plan for the data catalog|essential|['weight':1]
