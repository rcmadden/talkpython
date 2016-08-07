def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------------------------')
    print('              JOURNAL APP')
    print('-----------------------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_data = []

    while cmd != 'X':
        cmd = input('([L]ist entries, [A]dd an entry, E[x]it:')
        cmd = cmd.upper().strip()

        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entry(journal_data)
        elif cmd != 'X':
            print("Sorry, we don't understand '{}".format(cmd))

    print('Done, goodbye.')


def list_entries(data):
    print("Your journal entries")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))


def add_entry(data):
    text = input('Type you entry, <enter> to exit: ')
    data.append(text)


main()
