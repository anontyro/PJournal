import io
import Journal

def run_event_loop():
    cmd = ""
    print("Welcome to your awesome journal")
    journal_name = input('Load:')
    journal_data = Journal.load(journal_name)

    while(cmd != 'x'):
        cmd = input('[L]ist entries, [A]dd an entry, E[X]it: ')
        if(cmd.lower().strip() =='l'):
            list_entries(journal_data)
        elif(cmd.lower().strip() =='a'):
            Journal.add_entry(journal_data)
        elif(cmd.lower().strip() == 'x'):
            print('goodbye')
            Journal.save( journal_name, journal_data )
            exit()
            
        else:
            print('Error enter a valid input')


def list_entries(data):
    for i,entry in enumerate (reversed(data)):
        print('[{0}] {1}'.format((i+1), entry))


def main():
    run_event_loop()



#if you execute the file the name of that file is called main from the __name__
#This is great to prevent imported files from executing
if(__name__ == '__main__'):
    main()