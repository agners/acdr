import ConfigParser

class AcdrConf(ConfigParser.RawConfigParser):
    """Asterisk CDR configuration file.
    """

    def __init__(self, filenames):
        ConfigParser.RawConfigParser.__init__(self)
        if filenames:
            self.read(filenames)

    def __getitem__(self, name):
        return self.has_section(name) and self.items(name) or []

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self.__class__.__dict__:
            return self.__class__.__dict__[name]
        else:
            return self.__getitem__(name)
