CREATE TABLE $$DBSCHEMA.t_maengel_fehler
(
	ogc_fid SERIAL PRIMARY KEY,
        gruppe VARCHAR,
	fehler_txt VARCHAR
)
WITH (OIDS=FALSE);
GRANT SELECT ON $$DBSCHEMA.t_maengel_fehler TO $$USER;

INSERT INTO $$DBSCHEMA.t_maengel_fehler (fehler_txt) VALUES('löschen');
INSERT INTO $$DBSCHEMA.t_maengel_fehler (fehler_txt) VALUES('Lagedifferenz');
INSERT INTO $$DBSCHEMA.t_maengel_fehler (fehler_txt) VALUES('fehlt');
INSERT INTO $$DBSCHEMA.t_maengel_fehler (fehler_txt) VALUES('umattribuieren');
INSERT INTO $$DBSCHEMA.t_maengel_fehler (fehler_txt) VALUES('Darstellung nicht nach Richtlinie');
INSERT INTO $$DBSCHEMA.t_maengel_fehler (fehler_txt) VALUES('weitere');


CREATE TABLE $$DBSCHEMA.t_maengel_art
(
	ogc_fid SERIAL PRIMARY KEY,
	gruppe VARCHAR,
	art_txt VARCHAR
)
WITH (OIDS=FALSE);
GRANT SELECT ON $$DBSCHEMA.t_maengel_art TO $$USER;


INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','BB.Strasse_Weg');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','BB.Trottoir');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','BB.Verkehrsinsel');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','BB.uebrige_befestigte');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','BB.uebrige_humusierte');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','EO.Laermschutzwand');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','EO.Tunnel_Unterfuehrung_Galerie');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','EO.Bruecke_Passerelle');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','EO.Pfeiler');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','EO.schmaler_Weg');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','EO.Fahrspur');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Strasse','andere Fehlergruppe');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bahn','BB.Bahn');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bahn','EO.Laermschutzwand');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bahn','EO.Bahnsteig');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bahn','EO.Bahngeleise');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bahn','EO.Bahngeleise_ueberdeckt');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','BB.Gewaesser.stehendes');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','BB.Gewaesser.fliessendes');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','BB.Schilfguertel');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','EO.eingedoltes_oeffentliches_Gewaesser');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','EO.Bruecke_Passerelle');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','EO.Schwelle');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','EO.Rinnsal');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Gewaesser','EO.Quelle');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB.Gebaeude');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB.Wasserbecken');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB.Lagerplatz');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB.Gebaeudeerschliessung');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB.Parkplatz');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB.Gartenanlage');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','BB/EO.Objektname');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.Mauer');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.unterirdisches_Gebaeude');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.uebriger_Gebaeudeteil');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.wichtige_Treppe');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.Reservoir');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.Unterstand');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.Silo_Turm_Gasometer');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bebautes Gebiet','EO.weitere');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bestockte Flaeche','BB.geschlossener_Wald');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bestockte Flaeche','BB.Hecke');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bestockte Flaeche','BB.Parkanlage_bestockt');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bestockte Flaeche','BB.uebrige_bestockte');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Bestockte Flaeche','EO.schmale_bestockte_Flaeche');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Landwirtschaft','BB.Acker_Wiese');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Landwirtschaft','BB.Weide');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Landwirtschaft','BB.Reben');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Landwirtschaft','BB.Obstkultur');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Landwirtschaft','BB.uebrige_Intensivkultur');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Flugplatz');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Sportanlage_befestigt');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.uebrige_befestigte');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Boeschungsbauwerk');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Parkanlage_humusiert');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Sportanlage_humusiert');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Friedhof');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Hoch_Flachmoor');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.uebrige_humusierte');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Fels');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Geroell_Sand');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Steinbruch');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Kiesgrube');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.Deponie');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.uebriger_Abbau');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','BB.uebrige_vegetationslose');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Brunnen');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Hochkamin');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Denkmal');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Mast_Antenne');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Mast_Leitung');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Aussichtsturm');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Uferverbauung');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Lawinenverbauung');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.massiver_Sockel');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Ruine_archaeologisches_Objekt');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Landungssteg');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.einzelner_Fels');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Hochspannungsfreileitung');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Druckleitung');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Luftseilbahn');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Gondelbahn_Sesselbahn');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Materialseilbahn');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Skilift');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Faehre');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Grotte_Hoehleneingang');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Achse');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.wichtiger_Einzelbaum');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Seltene Objekte','EO.Bildstock_Kruzifix');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Perimeterrand','BB.Differenzen am Perimeterrand');
INSERT INTO $$DBSCHEMA.t_maengel_art (gruppe, art_txt) VALUES('Perimeterrand','EO.Differenzen am Perimeterrand');


