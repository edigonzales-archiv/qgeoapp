#!/bin/bash

DB_NAME="pnf_varia"
GROUP="pnfpublic"
DATA_PATH="Grundlagendaten"

echo "Create SBB schema"
sudo -u postgres psql -d $DB_NAME -c "CREATE SCHEMA sbb AUTHORIZATION postgres;"
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL ON SCHEMA sbb TO postgres;"
sudo -u postgres psql -d $DB_NAME -c "GRANT USAGE ON SCHEMA sbb TO $GROUP;"

echo "Import SBB data"
sudo -u postgres shp2pgsql -s 21781 -I $DATA_PATH/SBB/gleisnetz.shp sbb.gleisnetz | sudo -u postgres psql -d $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON TABLE sbb.gleisnetz TO $GROUP;"


echo "Create SOGIS schema"
sudo -u postgres psql -d $DB_NAME -c "CREATE SCHEMA sogis AUTHORIZATION postgres;"
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL ON SCHEMA sogis TO postgres;"
sudo -u postgres psql -d $DB_NAME -c "GRANT USAGE ON SCHEMA sogis TO $GROUP;"

echo "Import SOGIS data"
sudo -u postgres shp2pgsql -s 21781 -I -W latin1 $DATA_PATH/SOGIS/AfU/Abbaustellen/abbaustellen_afu.shp sogis.abbaustellen_afu | sudo -u postgres psql -d $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON TABLE sogis.abbaustellen_afu TO $GROUP;"

sudo -u postgres shp2pgsql -s 21781 -I -W latin1 $DATA_PATH/SOGIS/AfU/Reservoir/reservoir_afu.shp sogis.reservoir_afu | sudo -u postgres psql -d $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON TABLE sogis.reservoir_afu TO $GROUP;"

sudo -u postgres shp2pgsql -s 21781 -I -W latin1 $DATA_PATH/SOGIS/AfU/Flachmoor/flachmoor_afu.shp sogis.flachmoor_afu | sudo -u postgres psql -d $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON TABLE sogis.flachmoor_afu TO $GROUP;"

sudo -u postgres shp2pgsql -s 21781 -I -W latin1 $DATA_PATH/SOGIS/ARP/Freileitungen/freileitungen_arp.shp sogis.freileitungen_arp | sudo -u postgres psql -d $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON TABLE sogis.freileitungen_arp TO $GROUP;"

sudo -u postgres shp2pgsql -s 21781 -I -W latin1 $DATA_PATH/SOGIS/AWJF/Waldplan/wap_bst.shp sogis.waldplan_awjf | sudo -u postgres psql -d $DB_NAME
sudo -u postgres psql -d $DB_NAME -c "GRANT SELECT ON TABLE sogis.waldplan_awjf TO $GROUP;"
