---
title: "ScoutSuite"
toc_hide: true
---
Multi-Cloud security auditing tool. It uses APIs exposed by cloud
providers. Scan results are located at
`scan-reports/scoutsuite-results/scoutsuite\_\*.json` files.
Multiple scans will create multiple files if they are runing agains
different Cloud projects. See <https://github.com/nccgroup/ScoutSuite>

### Sample Scan Data
Sample ScoutSuite scans can be found [here](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans/scout_suite).

### Default Deduplication Hashcode Fields
By default, DefectDojo identifies duplicate Findings using these [hashcode fields](https://docs.defectdojo.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- file path
- vuln id from tool
