# Get the unparsed link
u = open(".unparsedLink.txt", 'r')
uplink = u.readlines()[0]
u.close()

# Parse youtube URL
utubeurl = "https://youtube.com"
addingToURL = False
for i in range(len(uplink)):

    if uplink[i:i+6] == "/watch":
        addingToURL = True

    if uplink[i] == '"':
        addingToURL = False

    utubeurl += uplink[i] * int(addingToURL)

# Write to .link.txt
newlink = open(".link.txt", "w+")
newlink.write(utubeurl)
newlink.close()
