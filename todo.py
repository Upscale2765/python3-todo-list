import json
import uuid
import sys

todo_file = open('todo.json', 'r')
data = json.load(todo_file)
todo_file.close()

def write_json():
  todo_file = open('todo.json', 'w')
  json.dump(data, todo_file);
  todo_file.close();
  print('Saved!')

def add_new():
  print('Adding a new task...')
  id = str(uuid.uuid4())
  data[id] = {
    'Task': input('Task: '),
    'Description': input('Description: '),
    'Deadline': input('Deadline: '),
    'Status': input('Status: ')
  };

  write_json()

def edit():
  print('Editing an existing task...')
  id = input('UUID: ')
  data_change = False
  key = {1: 'Task', 2: 'Description', 3: 'Deadline', 4: 'Status'}

  while True:
    print('What would you like to edit?')
    print('Task (1)')
    print('Description (2)')
    print('Deadline (3)')
    print('Status (4)')
    print('Save and quit(5)')

    choice = input('Select: ')

    try:
      choice = int(choice)
      if choice == 5:
        write_json()
        break

      if choice <= 5 and choice >= 1:
        data[id][key[choice]] = input(key[choice] + ': ')
        print('Done!')
      else:
        print('Invalid Integer.')

    except:
      print('Invalid Input.')

    print("") # Blank separator line

def delete():
  print('Deleting a task...')

  while True:
    id = input('UUID: ')

    if id in data:
      del data[id]
      print('Task deleted!')
      write_json()
      break
    else:
      print('Invalid UUID.')

def list():
  for i in data:
    print("UUID: " + i)

    for j in data[i]:
      print(j + ": " + data[i][j])

    print("") # Blank separator line

def usage():
  print('Usage: ')
  print('  -a        Add a new task')
  print('  -e        Edit an existing task')
  print('  -d        Delete an existing task')
  print('  -l        List all tasks')

valid_args = {
 '-a': add_new,
 '-e': edit,
 '-d': delete,
 '-l': list
}

if len(sys.argv) == 1:
  usage()
else:
  if sys.argv[1] in valid_args:
    valid_args[sys.argv[1]]()
  else:
    print('Invalid argument: ' + sys.argv[1])
