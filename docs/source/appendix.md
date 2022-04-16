# Appendix

## Appendix A. Data Strategy

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
ds_ |strategy|definition|essential|['weight':1]

### Form

### Report



## Appendix B. Content Management

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



## Appendix C. Requirements

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



## Appendix D. Task Management

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
tms_ |task_management|definition|essential|['weight':1]



## Appendix E. Version Control

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
vcs_ |version_control|definition|essential|['weight':1]



## Appendix F. Quality Assurance

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



## Appendix G. Security

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



## Appendix H. Ethics

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



## Appendix I. Storage

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
sto_data_manager|storage|manager that directs data practices and personnel|essential|['weight':1]
sto_deputy_data_manager|storage|data manager that assists the primary data manager (if exists)|optional|['weight':1]
sto_project_manager|storage|manager that runs a project for which a raw data asset is required|essential|['weight':1]
sto_legal_counsel|storage|counsel that advises on the legal limits for use of a raw data asset|optional|['weight':1]
sto_project_lead|storage|project manager that assists the primary project manager|optional|['weight':1]
sto_data_management_team|storage|team that supports the data manager and/or deputy data manager|essential|['weight':1]
sto_project_team|storage|team that supports the project manager and/or project lead||['weight':1]
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



## Appendix J. Modeling

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





## Appendix K. Analytics

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
ana_ |analytics|definition|essential|['weight':1]



## Appendix L. Integration

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
int_ |integration|definition|essential|['weight':1]



## Appendix M. Metadata

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`



## Appendix N. Cataloging

### Templates

### Rubrics

* Benchmark
  * essential
  * optional
  * recommended > reason
* Metrics
  * Weight by default is set to `1`





