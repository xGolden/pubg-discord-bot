class Player:
    
    """Represents a player present in the Discord server"""
    
    def __init__(self, DISCORDID, DISCORDNAME, PUBGNAME):
        self.id = DISCORDID
        self.name = DISCORDNAME
        self.pname = PUBGNAME
        self.isPlaying = False
    
    def get_DISCORDID(self):
        return self.id
    
    def get_DISCORDNAME(self):
        return self.name
    
    def get_PUBGNAME(self):
        return self.pname
    
    def get_stats_link(self):
        return "https://pubg.op.gg/user/" + self.pname + "?server=pc-na"
    
    def get_sh_link(self):
        return "https://pubg.sh/" + self.pname + "/pc-na"
    
    def get_stats_filename(self):
        return self.pname + ".json"
    
    def get_matches_filename(self):
        return self.pname + "_matches.json"