"""Utility functions used by the data quality framework."""
import inspect
import logging
import pyodbc
import re
import sqlite3
import sys
import ntpath


def config_logger():
    """Load logging configuration."""
    logging.basicConfig(
        # filename='data_quality.log',
        stream=sys.stdout,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_file_name(path):
    """Extract file name from absolute path."""
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def get_database_connection(data_source):
    """
    Get connection string and credentials for the corresponding data source,
    connects to it using an ODBC connection and return a connection object.
    """
    connection_string = data_source.connectionString

    # Add login to connection string if it is not empty
    if data_source.login:
        connection_string = connection_string + 'uid={};'.format(data_source.login)

    # Add password to connection string if it is not empty
    if data_source.password:
        connection_string = connection_string + 'pwd={};'.format(data_source.password)

    # Hive
    if data_source.dataSourceTypeId == 1:
        connection = pyodbc.connect(connection_string)
        connection.setencoding(encoding='utf-8')

    # Impala
    if data_source.dataSourceTypeId == 2:
        connection = pyodbc.connect(connection_string)
        connection.setencoding(encoding='utf-8')

    # Microsoft SQL Server
    if data_source.dataSourceTypeId == 3:
        connection = pyodbc.connect(connection_string)
        pass

    # MySQL
    if data_source.dataSourceTypeId == 4:
        connection = pyodbc.connect(connection_string)
        pass

    # PostgreSQL
    if data_source.dataSourceTypeId == 5:
        connection = pyodbc.connect(connection_string)
        pass

    # SQLite
    if data_source.dataSourceTypeId == 6:
        connection = sqlite3.connect(connection_string)

    # Teradata
    if data_source.dataSourceTypeId == 7:
        connection = pyodbc.connect(connection_string)
        connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        connection.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-8')
        connection.setencoding(encoding='utf-8')
    return connection
