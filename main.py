from ipAddress import IpAddress
from ipAnalyzer import IpAnalyzer

file = open('ipAddresses.txt', 'r')
ipAddresses = []
print('\nReading IPv4 addresses from text file...')
for line in file:
    if (line is not None and line not in ('', '\n')):
        try:
            ipAddresses.append(IpAddress(str.replace(line, '\n', '')))
        except Exception as error:
            print(error)
print('\nFollowing IPv4 addresses were read:')
for ipAddress in ipAddresses:
    print("- %s (%s)" % (ipAddress.description(), ipAddress.descriptionByte()))

if (len(ipAddresses) > 0):
    analyzer = IpAnalyzer(ipAddresses)
    print('\nSubnet is: ' + analyzer.getSubnet().description())
else:
    print('-- no correct IPv4 addresses --')

