import re

def generate_email(line,company):
    # Regular expression to match the name and company
    pattern = r'^([\w\s]+)\s*-\s*([\w\s]+)$'
    match = re.match(pattern, line.strip())
    
    thing = line.split(" ")
    name = thing[1:3:]
    # if match:
    #     name, company = match.groups()
        
    #     # Split the name into first and last name
    #     name_parts = name.split()
    #     if len(name_parts) >= 2:
    #         first_name, last_name = name_parts[0], name_parts[-1]
        
    
    #     # Remove spaces from company name
    #     company = company.replace(" ", "")
        
        # Generate email
    print(name)
    if len(name)>=2:
        first_name, last_name = name[0], name[1]
        email = f"{first_name}.{last_name}@{company}.com"
        
        print(email)
        return email
    
    return line  # Return the original line if it doesn't match the pattern

# Read the input file
input_file = 'google_results.txt'
output_file = 'emails.txt'


with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:

    company = ""
    for line in infile:
        if line.startswith("Search term:"):
                    #Search term: Atlas Venture  linkedin
            
            stripper = line.split(":")[1]
            #stripper = line[0].strip().split(" ") #[:-1:] #.join("")
            # print(line)
            # print("search term")
            # print(stripper)
            stripper = "".join( stripper.split(" ") ).strip()
            stripper = stripper[:len(stripper)-8:]
            #print("stripped" , stripper)
            #company = line.split(":", 1)[1].strip().split()[0]
        else:
            email = generate_email(line,stripper)
            outfile.write(email + '\n')
print(f"Processed file saved as {output_file}")