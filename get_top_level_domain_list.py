import sys

topLevelDomainList = ['.es', '.com', '.net', '.org', '.co', '.biz', '.io', '.at', '.us', '.me', '.co.uk', '.eu', '.info', '.xyz', '.ca', '.be', '.am', '.tv', '.la', '.life', '.ch', '.ms', '.in', '.club', '.bar', '.tech', '.site', '.online', '.store', '.space', '.website', '.fun', '.host', '.press', '.digital', '.today', '.farm']

for i in topLevelDomainList: 
    print ("http://" + sys.argv[1] + str(i))
