# Makefile for a PyQGIS plugin 
UI_FILES = basic/help/Ui_about.py basic/settings/Ui_options.py basic/file/Ui_importdata.py basic/file/Ui_deleteproject.py modules/qnplso/settings/Ui_setdatabase.py

RESOURCE_FILES = resources.py



default: compile
	
compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<

