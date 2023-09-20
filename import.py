import json
 
# Read the input JSON file
with open('repos.json', 'r') as f:
   data = f.read()
 
# Remove leading and trailing '[' and ']' characters if they exist
data = data.strip('[').strip(']')
 
# Split the input data into individual JSON objects using ","
entries = data.split(',')
 
# Process and print the output for each entry
for entry in entries:
   try:
       entry_data = json.loads('{' + entry + '}')
       repo_name = list(entry_data.keys())[0].split('/')[-1]
       team_name = entry_data[list(entry_data.keys())[0]]['team']
 
       output = f"- name: {repo_name}\nBranch: main\n- ProductTeam: {team_name}\n"
 
       # Print or save the output as needed
       print(output)
   except json.JSONDecodeError:
     
       pass