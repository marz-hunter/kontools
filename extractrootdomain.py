# This script will read in a file with a list of subdomains and extract the root domain for each subdomain.

# Read in the file
with open('file.txt') as f:
    subdomains = f.readlines()

# Create a list to store the root domains
root_domains = []

# Iterate through the list of subdomains
for subdomain in subdomains:
    # Strip the whitespace
    subdomain = subdomain.strip()
    # Split the subdomain into parts
    parts = subdomain.split('.')
    # The root domain is the last two parts
    root_domain = parts[-2] + '.' + parts[-1]
    # Append the root domain to the list
    root_domains.append(root_domain)

# Print the list of root domains
print(root_domains)
