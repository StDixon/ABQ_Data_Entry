==========================
ABQ Data Entry Application
==========================


Description
===========

This program provides a data entry form for ABQ Agrilabs laboratory data.

Features
--------

* Provides a validated entry form to ensure correct data
* Stores data to ABQ-format CSV files
* Auo-fills form fields where possible

Authors
=======

Alan D More, 2018
Steve Dixon, 2018

Requirements
============

* Python 3
* Tkinter

Usage
=====

To start the application, run::

python3 ABQ_Data_entry/abq_data_entry.py

General Notes
=============

The CSV file will be saved to your current directory in the format "abq_data_record_CURREN-DATE.csv",
where CURRENT-DATE is today's date in ISO format

This pogram only appends to the CSV file. You should have a spreadsheet program installed in
case you need to edit or check the file. 

