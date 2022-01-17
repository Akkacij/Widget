from blocks.mainblocks.block150x70 import Block150x70


class BlockGraph(Block150x70):
    def __init__(self, win, name="BlockGraph"):
        super().__init__(win=win, name=name)
        self.version = "Akkacij 1.0 12.01.2022"