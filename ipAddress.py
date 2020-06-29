class IpAddress:
    #blocks = []

    def __init__(self, stringRepresentation = None):
        self.blocks = []
        if (stringRepresentation is None):
            for i in range(4):
                self.blocks.append(0)
            return
        strings = stringRepresentation.split('.')
        if len(strings) != 4:
            raise Exception('-- Failed to read "%s". It\'s not an IPv4 address or there were invalid number of blocks for IPv4 address. --' % (stringRepresentation))
        for i in range(4):
            try:
                block = int(strings[i])
            except Exception as error:
                raise Exception('-- Failed to read "%s". Invalid "%s" block for IPv4 address. --' % (strings[i], stringRepresentation))
            if (block < 0 or block > 255):
                raise Exception('-- Failed to read "%s". Invalid "%d" block for IPv4 address. --' % (stringRepresentation, block))
            self.blocks.append(block)

    def description(self):
        return ('%d.%d.%d.%d' % (self.blocks[0], self.blocks[1], self.blocks[2], self.blocks[3]))

    def descriptionByte(self):
        return ('%s.%s.%s.%s' % (bin(self.blocks[0])[2:], bin(self.blocks[1])[2:], bin(self.blocks[2])[2:], bin(self.blocks[3])[2:]))
