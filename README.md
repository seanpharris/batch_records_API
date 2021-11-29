# Batch Jobs API - Coding Exercise 01


## About
As an simplified representative of applications built at ORNL's OLCF Software Services this program will simulate batch records from from work done on a supercomputer. Using the Django framework, the data is retrieved from an Sqlite3 database and output to a single RESTful API endpoint representing individual batch jobs by batch number, submitted date/time, and number of nodes used.

## Built with
* Django REST Framework 0.1.0
* Django 1.8.19
* Python 3.8.7

## Getting started
Dowload the zip file, un-zip it, and have a Python IDE of choice.

## Installation
Open your IDE and load the project file.

We will now run a few commands in the terminal:

- `python -m venv env`
- `pip install django`
- `pip install djangorestframework`



## Usage

Now that our virtual environment is set up,
run the following command in the terminal:

`python manage.py runserver`

In the terminal an API endpoint will be supplied.

To end the program at anypoint within the IDE, hit Ctrl + C.**

## Data types to query
- batch_number - Integer
- submitted_by - ISP 8601 datetime
- nodes_used - integer

## Keywords for querying
- filter[submitted_after]= 
- filter[submitted_before]=
- filter[min_nodes]=
- filter[max_nodes]=
- filter[batch_number]=

While the API is running, in the search bar of the browser, use a URI that starts with the API endpoint given and then
add the resource "/batch_jobs/" or click it on the Django REST framework page in the browser

You may use any combination of filters desired. Use "&" to separate your filters.

Example: /batch_jobs/filter[submitted_after]=2018-02-28T15:00:00+00:00&filter[submitted_before]=2018-03-01T15:00:00+00:00&filter[min_nodes]=2&filter[max_nodes]=20

# Contact

* Sean Pharris - pharris.sean@gmail.com
* LinkedIn - https://www.linkedin.com/in/sean-pharris-32656a201/

End
