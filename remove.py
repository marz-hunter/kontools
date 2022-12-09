#open the file
with open('httpx2', 'r') as f:
  #read the file contents
  contents = f.read()
  #replace "http://" and "https://" with ""
  contents = contents.replace("http://", "")
  contents = contents.replace("https://", "")

#open the file for writing
with open('httpx2', 'w') as f:
  #write the new contents
  f.write(contents)
