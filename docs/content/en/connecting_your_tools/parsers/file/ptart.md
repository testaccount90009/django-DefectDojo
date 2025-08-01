---
title: "PTART Reports"
toc_hide: true
---

### What is PTART?
PTART is a Pentest and Security Auditing Reporting Tool developed by the Michelin CERT (https://github.com/certmichelin/PTART)

### Importing Reports
Reports can be exported to JSON format from the PTART web UI, and imported into DefectDojo by using the "PTART Report" importer.

### Sample Scan Data
Sample scan data for testing purposes can be found [here](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans/ptart).

### Default Deduplication Hashcode Fields
By default, DefectDojo identifies duplicate Findings using these [hashcode fields](https://docs.defectdojo.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
