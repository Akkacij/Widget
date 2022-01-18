from panel.mainpanel.panel150x70 import Panel150x70


class PanelGraph(Panel150x70):
    def __init__(self, win, name="BlockGraph"):
        super().__init__(win=win, name=name)
        self.pn_version = "Akkacij 1.0 12.01.2022"
