ADMIN="agisoadmin"
ADMINPWD="agisoadmin"
USER="agisouser"
USERPWD="agisouser"
DB_NAME="pnf_agiso"

GROUP="pnfpublic";
PG_VERSION="8.4"

# Auskommentieren falls man z.B. nur DB neu anlegen will.
echo "Create database user"
sudo -u postgres psql -d postgres -c "CREATE ROLE $ADMIN CREATEDB LOGIN PASSWORD '$ADMINPWD';"
sudo -u postgres psql -d postgres -c "CREATE ROLE $USER LOGIN PASSWORD '$USERPWD';"

echo "Create database: $DB_NAME"
sudo -u postgres createdb --owner $ADMIN $DB_NAME
sudo -u postgres createlang plpgsql $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "ALTER SCHEMA public OWNER TO $ADMIN;"

echo "Load postgis"
sudo -u postgres psql -d $DB_NAME -f /usr/share/postgresql/$PG_VERSION/contrib/postgis-1.5/postgis.sql
sudo -u postgres psql -d $DB_NAME -f /usr/share/postgresql/$PG_VERSION/contrib/postgis-1.5/spatial_ref_sys.sql

echo "Grant tables to..."
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL ON SCHEMA public TO $ADMIN;"
sudo -u postgres psql -d $DB_NAME -c "ALTER TABLE geometry_columns OWNER TO $ADMIN;"
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL ON geometry_columns TO $ADMIN;"
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL ON spatial_ref_sys TO $ADMIN;"
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL ON geography_columns TO $ADMIN;"

sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON geometry_columns TO $USER;"
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON spatial_ref_sys TO $USER;"
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON geography_columns TO $USER;"

sudo -u postgres psql -d $DB_NAME -c "GRANT $GROUP TO $ADMIN;"
sudo -u postgres psql -d $DB_NAME -c "GRANT $GROUP TO $USER;"
