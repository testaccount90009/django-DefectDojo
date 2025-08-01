---
title: "Codechecker Report native"
toc_hide: true
---
Import Codechecker static analyzer report in JSON format: https://codechecker.readthedocs.io/en/latest/
Report format described here: https://codechecker.readthedocs.io/en/latest/analyzer/user_guide/#parse

One could make Codechecker JSON report using command like this: 
```shell
CodeChecker parse /path/to/codechecker/analyzer/output/directory -e json -o /path/to/output/file.json
```

Before this step you should build your project with Codechecker build process interception, 
```shell
odeChecker log -b "make -j8" -o ./my.project.codechecker.log
```

then analyze it
```shell
CodeChecker analyze ./codechecker.log -o /path/to/codechecker/analyzer/output/directory
```

### Sample Scan Data
Sample Codechecker Report native scans can be found [here](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans/codechecker).

### Default Deduplication Hashcode Fields
By default, DefectDojo identifies duplicate Findings using these [hashcode fields](https://docs.defectdojo.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
