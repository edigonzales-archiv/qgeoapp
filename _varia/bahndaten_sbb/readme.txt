- einfache tabelle 
- mit shp2pgsl einlesen
- umwandlung des dxf mit ogr2ogr:
     ogr2ogr SBB_Linien_2.shp Solothurn_Lebern.dxf -where 'ogr_geometry = "LINESTRING"' -where "LAYER='BS-Gleisnetz-Bestehend'"
- mit tablemanager in shape unnötige attribute löschen



CREATE SCHEMA sbb
  AUTHORIZATION ebsoadmin;
GRANT ALL ON SCHEMA sbb TO ebsoadmin;
GRANT USAGE ON SCHEMA sbb TO ebsopublic;


shp2pgsql -s 21781 -I gleisnetz.shp sbb.gleisnetz | psql -d pnfebso

(funktioniert als stefan)


ALTER TABLE sbb.gleisnetz OWNER TO ebsoadmin;
GRANT ALL ON TABLE sbb.gleisnetz TO ebsoadmin;
GRANT SELECT ON TABLE sbb.gleisnetz TO ebsopublic;

