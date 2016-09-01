"""
This is the main logic for the journal application
"""
import os
import io

def load(name):
    """
    This method creates and loads a new journal
    :param name: This is the base name of the journal
    :return: A new journal structure populated with reloaded data
    """
    filename = get_path(name)
    data = []

    if(os.path.exists(filename)):
        with open(filename) as fin:
            for entry in fin.readlines():
                print("Load: " +entry.rstrip())
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    filename = get_path(name)
    print('saving to: {0}'.format(filename))

    #fout = open(filename, 'w')
    with open(filename, 'w') as fout:

        for entry in journal_data:
            fout.write(entry + '\n')
    
    #fout.close()

def add_entry(journal_data):
    body = input("Entry: ")
    journal_data.append(body)

def get_path(name):
    filename = os.path.abspath(os.path.join('.', 'aJournal', name + '.ajl'))
    return filename