---
title: "Sysdig Vulnerability Reports"
toc_hide: true
---
Import CSV report files from Sysdig or a Sysdig UI JSON Report
Parser will accept Pipeline, Registry and Runtime reports created from the UI
More information available at [sysdig reporting docs page](https://docs.sysdig.com/en/docs/sysdig-secure/vulnerabilities/reporting)

### Sample Scan Data
Sample Sysdig Vulnerability Reports scans can be found [here](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans/sysdig_reports).

### Default Deduplication Hashcode Fields
By default, DefectDojo identifies duplicate Findings using these [hashcode fields](https://docs.defectdojo.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
