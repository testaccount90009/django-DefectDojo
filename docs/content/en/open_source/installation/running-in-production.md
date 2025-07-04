---
title: "Running in Production (Open Source)"
description: "For use in Production environments, performance tweaks and backups are recommended."
draft: false
weight: 4
---

## Production Use (with Docker compose)

The docker-compose.yml file in this repository is fully functional to evaluate DefectDojo in your local environment.

Although Docker Compose is one of the supported installation methods to deploy a containerized DefectDojo in a production environment, the docker-compose.yml file is not intended for production use without first customizing it to your particular situation.

See [Running with Docker Compose](https://github.com/DefectDojo/django-DefectDojo/blob/master/readme-docs/DOCKER.md) for more information how to run DefectDojo with Docker Compose.

### System Requirements

It is recommended to use a dedicated database server and not the preconfigured PostgreSQL database. This will improve the performance of DefectDojo significantly.

#### Instance Size

With a separate database, the minimum recommendations to run DefectDojo are:

-   2 vCPUs
-   8 GB of RAM
-   10 GB of disk space (remember, your database is not here \-- so
     what you have for your O/S should do). You could allocate
    a different disk than your OS\'s for potential performance
    improvements.

### Security
Verify the `nginx` configuration and other run-time aspects such as security headers to comply with your compliance requirements.
Change the AES256 encryption key `&91a*agLqesc*0DJ+2*bAbsUZfR*4nLw` in `docker-compose.yml` to something unique for your instance.
This encryption key is used to encrypt API keys and other credentials stored in Defect Dojo to connect to external tools such as SonarQube. A key can be generated in various ways for example using a password manager or `openssl`:

```
     openssl rand -base64 32
```
```
      DD_CREDENTIAL_AES_256_KEY: "${DD_CREDENTIAL_AES_256_KEY:-<PUT THE GENERATED KEY HERE>o}"
```

## File Backup

In both cases (dedicated DB or containerized), if you are self-hosting, it is recommended that you implement and create periodic backups of your data.

### Media files

Media files for uploaded files, including threat models and risk acceptance, are stored in a docker volume. This volume needs to be backed up regularly.

## Performance Adjustments

### uWSGI

By default (except in `ptvsd` mode for debug purposes), uWSGI will
handle 4 concurrent connections.

Based on your resource settings, you can tweak:

-   `DD_UWSGI_NUM_OF_PROCESSES` for the number of spawned processes.
    (default 2)
-   `DD_UWSGI_NUM_OF_THREADS` for the number of threads in these
    processes. (default 2)

For example, you may have 4 processes with 6 threads each, yielding 24
concurrent connections.

### Celery worker

By default, a single mono-process celery worker is spawned. When storing a large amount of findings or running large imports it might be helpful to adjust these parameters to prevent resource starvation.

The following variables can be changed to increase worker performance, while keeping a single celery container.

-   `DD_CELERY_WORKER_POOL_TYPE` will let you switch to `prefork`.
    (default `solo`)

When you enable `prefork`, the variables below have
to be used. see the
Dockerfile.django-* for in-file references.

-   `DD_CELERY_WORKER_AUTOSCALE_MIN` defaults to 2.
-   `DD_CELERY_WORKER_AUTOSCALE_MAX` defaults to 8.
-   `DD_CELERY_WORKER_CONCURRENCY` defaults to 8.
-   `DD_CELERY_WORKER_PREFETCH_MULTIPLIER` defaults to 128.

You can execute the following command to see the configuration:

`docker compose exec celerybeat bash -c "celery -A dojo inspect stats"`
and see what is in effect.

### Asynchronous Import: Deprecated
This feature has been removed in 2.47.0