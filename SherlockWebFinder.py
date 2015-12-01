#!/usr/bin/python
# -*- coding: utf-8 -*-

import Queue
import threading
import os
import urllib2

def banner():
    print """
   _____  __                 __              __
  / ___/ / /_   ___   _____ / /____   _____ / /__
  \__ \ / __ \ / _ \ / ___// // __ \ / ___// //_/
 ___/ // / / //  __// /   / // /_/ // /__ / ,<
/____//_/ /_/ \___//_/   /_/ \____/ \___//_/|_|

            WEB IDENTIFIER TOOL
            CODED BY - D0ctor
            www.nanoshots.com.br
    """
    main()
#FUNCÇÕES QUE TRATAM OS FRAMEWORKS

def codeigniter(thread):
    global web_paths
    directory = 'frameworks/CodeIgniter/'
    os.chdir(directory)

    web_paths = Queue.Queue()

    for r,d,f in os.walk("."):
        for files in f:
            remote_path = "%s/%s" % (r, files)
            if remote_path.startswith("."):
                remote_path = remote_path[1:]

            if os.path.splitext(files)[1] not in filters:
                web_paths.put(remote_path)

    threads(directory, thread)



def joomla(thread):
    global web_paths
    directory = 'frameworks/Joomla/'
    os.chdir(directory)

    web_paths = Queue.Queue()

    for r,d,f in os.walk("."):
        for files in f:
            remote_path = "%s/%s" % (r, files)
            if remote_path.startswith("."):
                remote_path = remote_path[1:]

            if os.path.splitext(files)[1] not in filters:
                web_paths.put(remote_path)

    threads(directory, thread)


def drupal(thread):
    global web_paths
    directory = 'frameworks/Drupal/'
    os.chdir(directory)

    web_paths = Queue.Queue()

    for r,d,f in os.walk("."):
        for files in f:
            remote_path = "%s/%s" % (r, files)
            if remote_path.startswith("."):
                remote_path = remote_path[1:]

            if os.path.splitext(files)[1] not in filters:
                web_paths.put(remote_path)

    threads(directory, thread)


def moodle(thread):
    global web_paths
    directory = 'frameworks/Moodle/'
    os.chdir(directory)

    web_paths = Queue.Queue()

    for r,d,f in os.walk("."):
        for files in f:
            remote_path = "%s/%s" % (r, files)
            if remote_path.startswith("."):
                remote_path = remote_path[1:]

            if os.path.splitext(files)[1] not in filters:
                web_paths.put(remote_path)

    threads(directory, thread)


def magento(thread):
    global web_paths
    directory = 'frameworks/Magento/'
    os.chdir(directory)

    web_paths = Queue.Queue()

    for r,d,f in os.walk("."):
        for files in f:
            remote_path = "%s/%s" % (r, files)
            if remote_path.startswith("."):
                remote_path = remote_path[1:]

            if os.path.splitext(files)[1] not in filters:
                web_paths.put(remote_path)

    threads(directory, thread)

def wordpress(thread):
    global web_paths
    directory = 'frameworks/Wordpress/'
    os.chdir(directory)

    web_paths = Queue.Queue()

    for r,d,f in os.walk("."):
        for files in f:
            remote_path = "%s/%s" % (r, files)
            if remote_path.startswith("."):
                remote_path = remote_path[1:]

            if os.path.splitext(files)[1] not in filters:
                web_paths.put(remote_path)

    threads(directory, thread)


def general(thread):
    global web_paths
    #Constrói a Wordlist
    directory = 'frameworks/General/all-dirs.txt'
    fd = open(directory, "rb")
    raw_words = fd.readlines()
    web_paths = Queue.Queue()

    for word in raw_words:
        word.rstrip('\n')
        web_paths.put(word)

    threads(directory, thread)


def subdomain_finder(thread):
    global web_paths
    #Constrói a Wordlist
    directory = 'frameworks/General/subdomains.txt'
    fd = open(directory, "rb")
    raw_words = fd.readlines()
    web_paths = Queue.Queue()

    for word in raw_words:
        word.rstrip('\n')
        web_paths.put(word)

    subdomain_thread(thread)



def subdomain_thread(thread):
    for i in range(thread):
        print "Spawning Thread: %d" % i
        t = threading.Thread(target=subdomain_construct)
        t.start()




def subdomain_construct():
    while not web_paths.empty():
        word = web_paths.get()
        word = word.replace('\n','')
        url = 'http://%s.%s' % (word, target)
        request = urllib2.Request(url)

        try:
            response = urllib2.urlopen(request)
            content = response.read()

            print "[%d] => %s" % (response.code, url)
            response.close()

        except urllib2.HTTPError as error:
            print "[%d] => %s" % (error.code, url)
            pass


#FUNÇÕES DO SISTEMA
#Função responsável pelas Threads
def threads(directory, thread):

    for i in range(thread):
        print "Spawning Thread: %d" % i
        t = threading.Thread(target=test_remote)
        t.start()



#Função de Construção e Teste das URLS
def test_remote():

    while not web_paths.empty():
        path = web_paths.get()
        url = "%s%s" % (target,path)
        request = urllib2.Request(url)

        try:
            response = urllib2.urlopen(request)
            content = response.read()

            print "[%d] => %s" % (response.code, url)
            response.close()

        except urllib2.HTTPError as error:
            print "[%d] => %s" % (error.code, url)
            pass


#Função Main do Painel
def main ():
    global filters
    global target

    print "1 - CodeIgniter Analysis - v3.0.3"
    print "2 - Joomla Analysis - v3.4.5"
    print "3 - Drupal Analysis - v8.0.0"
    print "4 - Moodle Analysis - v3.0"
    print "5 - Magento Analysis"
    print "6 - Wordpress Analysis - v4.3.1"
    print "7 - General Analysis - General or Custom Sites"
    print "8 - Subdomain Finder"
    print "9 - Admin Page Finder"
    print "0 - Exit"
    print ""
    option = raw_input("Inform a Option: ")
    target = raw_input("Inform a Target URL: ")
    thread = raw_input("Inform a Number of Threads: ")
    filters = ['.jpg', '.gif', '.png', '.css']
    option = int(option)
    thread = int(thread)

    if option == 1:
        codeigniter(thread)

    elif option == 2:
        joomla(thread)

    elif option == 3:
        drupal(thread)

    elif option == 4:
        moodle(thread)

    elif option == 5:
        magento(thread)

    elif option == 6:
        wordpress(thread)

    elif option == 7:
        general(thread)

    elif option == 8:
        subdomain_finder(thread)

    elif option == 9:
        admin_finder(thread)

    elif option == 0:
        exit()


banner()

