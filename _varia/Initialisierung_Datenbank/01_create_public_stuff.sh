#!/bin/bash

# DB-Role/Group für Grundlagedaten. 
GROUP="pnfpublic";

DB_NAME="pnf_varia"
PG_VERSION="8.4"

echo "Create pnfvaria database"
#sudo -u postgres createdb $DB_NAME
sudo -u postgres createlang plpgsql $DB_NAME


echo "Load postgis"
sudo -u postgres psql -d $DB_NAME -f /usr/share/postgresql/$PG_VERSION/contrib/postgis-1.5/postgis.sql
sudo -u postgres psql -d $DB_NAME -f /usr/share/postgresql/$PG_VERSION/contrib/postgis-1.5/spatial_ref_sys.sql

echo "Create pnfpublic group"
#sudo -u postgres psql -d $DB_NAME -c "CREATE GROUP $GROUP;"

echo "Grant..."
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON geometry_columns TO $GROUP;"
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON spatial_ref_sys TO $GROUP;"
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON geography_columns TO $GROUP;"


