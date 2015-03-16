import logging
import osandio.fileUtils
import os
from osandio._7ZipController import _7ZipController

class BBOSConfig:
    #Gameday
    gamedayURL = 'http://gd2.mlb.com/components/game/'
    gamedayDaysBackToLoad = 2
    dbUser = 'bbos'
    dbPass = 'bbos'
    dbHost = 'localhost'
    dbPort = 3306
    dbName = 'gameday'
    mySQLLocation = '/usr/local/mysql/bin/mysql'
    numberOfThreads = 6
    
    #logging
    logLocation = 'logs'
    logScreenPrintingLogLevel = logging.INFO  
    
    #file compression
    pathTo7Zip = ".." + os.sep + "tools" + os.sep + "7-Zip" + os.sep + "7za.exe"
    unzipController = _7ZipController(os.path.abspath(pathTo7Zip))
    
    #retrosheet
    retrosheetURL = "http://www.retrosheet.org/game.htm"
    pathToChadwick = ".." + os.sep + "tools" + os.sep + "retrosheet" + os.sep
    
    sqlAlchemyEngine = 'mysql+pymysql'
    sqlAlchemyHost = 'localhost'
    sqlAlchemyDatabase = 'retrosheet'
    sqlAlchemySchema = ''
    sqlAlchemyUser = 'bbos'
    sqlAlchemyPassword = 'bbos'

#executed on loading of config file
osandio.fileUtils.mkdir(BBOSConfig.logLocation)    
