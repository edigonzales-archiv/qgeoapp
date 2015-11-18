# Makefile for a PyQGIS plugin 
UI_FILES = complexchecks/Ui_createdifferencelayer.py

default: compile
	
compile: $(UI_FILES)  

%.py : %.ui
	pyuic4 -o $@ $<
