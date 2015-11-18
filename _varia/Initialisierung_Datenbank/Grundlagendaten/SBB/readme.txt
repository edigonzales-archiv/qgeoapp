
CREATE SCHEMA sbb
  AUTHORIZATION ebsoadmin;
GRANT ALL ON SCHEMA sbb TO ebsoadmin;
GRANT USAGE ON SCHEMA sbb TO ebsopublic;

ogr2ogr gleisnetz.shp Solothurn_Lebern.dxf -where 'ogr_geometry = "LINESTRING"' -where "LAYER='BS-Gleisnetz-Bestehend'"
shp2pgsql -s 21781 -I gleisnetz.shp sbb.gleisnetz | psql -d pnfebso

(funktioniert als user: stefan)


ALTER TABLE sbb.gleisnetz OWNER TO ebsoadmin;
GRANT ALL ON TABLE sbb.gleisnetz TO ebsoadmin;
GRANT SELECT ON TABLE sbb.gleisnetz TO ebsopublic;

