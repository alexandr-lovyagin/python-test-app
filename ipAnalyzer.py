from ipAddress import IpAddress

class IpAnalyzer:

    def __init__(self, addresses):
        self.ipAddresses = addresses

    def getSubnet(self):
        result = IpAddress()
        for i in range(4):
            blocks = [ipAddress.blocks[i] for ipAddress in self.ipAddresses]
            blocksSet = set(blocks)
            if (len(blocksSet) == 1):
                result.blocks[i] = blocks.pop()
                continue # all blocks at this position are equal, moving along...
            else:
                result.blocks[i] = self.__extractBlock(blocksSet)
                break
            
        return result

    def __extractBlock(self, blocks):
        for i in range(1, 8):
            subBlocks = [block & (255 - (2 ** i - 1)) for block in blocks] # using masks for each block (11111111, then 11111110 and so on) until reaching equality, after that apply this mask to get subnet block
            subBlocksSet = set(subBlocks)
            if (len(subBlocksSet) == 1):
                return subBlocks[0]
        return 0