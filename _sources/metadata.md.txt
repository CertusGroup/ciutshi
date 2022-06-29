# Metadata

The most important data asset artifact in the data management process is metadata. Loss of lineage and provenance associated with data assets is not only a failing for many data governance systems, but a costly oversight which may greatly reduce the value and impact of data for an institution. As a result, measures must be taken to carefully curate and improve the legacy of data utilization through consistent and rigorous implementation of metadata practices. When these practices are applied across multiple systems, it can improve the visibility of patterns in business activity while expanding the analytic opportunities of data assets.

ciuTshi suggests a persistent, simplified augmentation of metadata for the entire lifecycle of a data asset, tailored to you specific project needs and strategic business model(s). Data operations often involve complex models of data management in rapidly changing and dynamic governance environments. This complexity demands a critical focus on metadata practices from requirements to deprecation of the data asset. Through curation and enrichment of metadata artifacts along the way, the institution can rapidly mobilize data inventories toward knowledge discovery and exploratory data analysis. As a result, insights can be garnered and project vectors can be visible far quicker for leadership, customers, and stakeholders. With the added complexity of parity across multiple information systems and data architectures, metadata is at the core of effective data management and institutional data governance success.

This document will outline the essentials for metadata practices, directing data engineers to content management systems on specific information systems for detailed data architecture implementations. ciuTshi's data management system draws from DAMA[1](metadata/references) and other resources. For additional context on this documents sections, refer to the references section.

## Challenge

Data management lifecycles require rapid access to insightful details for a variety of data assets. A shift from heuristic documentation models to broader automation efforts requires and enhanced metadata paradigm: artifacts from each phase of data operations for a data asset cataloged for longitudinal data operations metrics in support of institutional knowledge discovery. This massive effort requires data engineers to capitalize on efficiencies within each phase of data management, responding to numerous requirements, each with varying complexity and tight deadlines. In order to accelerate the data management team's service model, cataloging of templated metadata profiles for a data asset will result in accelerated customer engagements for problem redefinition while shortening the timeline for future requests of existing data assets.

## Goals

* Aggregate essential metadata elements for cataloging resulting in organizational understanding of data asset utility and potential impact
* Apply tagging practices to data asset metadata to ensure categorical sorting of assets
* Provide baseline statistics for a data asset resulting in rapid insight generation for customers
* Maintain data lineage and provenance resulting in longitudinal study potential for strategic insight generation

## Processes

Metadata is an inseperable part of the data asset: it containd all essential information for how the raw data evolved into the final integration deliverable. ciuTshi recommends a metadata strategy to establish a baseline for metadata elements that can be migrated upward through information systems for enrichment. Metadata requirements will entail capturing of key data points at each phase of data operations, culminating in a baseline metamodel for each data asset. The metamodel should observe security and policy restrictions through the use of tags, noting everything from usage to transfer restrictions. This metadata must be maintained within each information system, looking at quality and relevance via the data catalog's analytic reports and queries.

> Note: There are many types of metadata such as business, technical, and operational. Data engineers must constantly be examining the use of metadata types across the data catalog, making migrations if necessary. ISO 11179 is an excellent reference for metadata registries.

### Lifecycle Management

#### Metadata Strategy

This metadata strategy is primarily focused on data asset enrichment as a result of observations gathered during data operations' workflows. Each time raw data is modeled, metadata for the asset should be updated. The metadata updates will generally be accumulated throughout the workflow and then updated in the catalog. These can be partial updates depending on the metadata elements and data team workflows. All metadata should be version controlled or backed up for essential analysis on the effects of workflow changes on the outputs. The data catalog will act as the main integration point for metadata access, using group policy for access as dictated by the data catalog software or system architecture. Dormant data assets that are not reference data sets must be assessed at the end of their utilization timeline (e.g., the deadline associated with the requirements that brought the asset into the institution's data systems). As with all aspects of data management, data governance, and data operations, security factors will comply with information systems and data architecture policies.

#### MetaModel

The metamodel must cover these categorical areas:

* _Stored Data_ covers the metadata elements associated with mining, pipelines, and storage including originating documentation and source information such as data version.
* _Logical Technical Data_ covers the metadata elements associated with modeling, schema, and methods.
  * _Operational Data_ is a subset that covers processing specific elements
* _Business Data_ covers the metadata elements associated with data dictionaries, provenance, lineage, and baseline analytics.
* _Physical Technical Data_ covers the metadata elements associated with integrations and physical endpoints for data delivery.
  * _Operational Data_ is a subset that covers the monitoring specific elements

> Note: this is subject to change depending on the information systems, data architectures, and their associated data capabilities profile. Reference the CMS documentation on those systems for specific guidance.

#### Metadata Maintenance

Data assets are largely acquired and stored in association with projects. As a result, initial maintenance of metadata will begin post-integration until the end of the delivery timeline dictated in the requirements for the data asset. This changes if the data asset is updated in raw storage, necessitating management workflow runs and metadata updates. This metadata management posture entails accountability, standards, and improvement benchmarks implemented by the data management team to ensure resources are allocated and deprecated while maintaining these metadata artifacts in the data catalog (in compliance with security, policy, and customer stipulations). Retention of metadata is critical for institutional leadership as querying and analysis of historical holdings in association with organization goals permit knowledge discovery for project insights, business development leads, and customer engagements.

(metadata/references)=

## References

Number|Reference
--|--
1|Henderson. D., Earley, S., Sebastian-Coleman, L., Sykora, E., Smith, E. (Eds.). (2017). *DAMA-DMBOK: Data management body of knowledge (2nd Ed.).* Basking Ridge, NJ: Technics Publications.