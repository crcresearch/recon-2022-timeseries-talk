FROM postgres:14

ENV POSTGIS_MAJOR 3

RUN apt-get update \
      && apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
      && apt-get install -y --no-install-recommends \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts \
      && rm -rf /var/lib/apt/lists/* 

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./compose/production/postgres/postgis/initdb-postgis.sh /docker-entrypoint-initdb.d/14_postgis.sh
COPY ./compose/production/postgres/postgis/update-postgis.sh /usr/local/bin

COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
