#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Scannertoolv2:
    def __init__(self, target, port_range, parameters):
        self.target = target
        self.port_range = port_range
        self.parameters = parameters

    def port_lookup(self):
        import nmap
        from config.functions import cprint

        cprint(f"[~] portscanner >> scanning '{self.target}'\n", 'yellow', True)

        # - Scanning target - #
        Scanner = nmap.PortScanner()
        nmap_flags = Flags.get_nmap_flags(self.parameters)
        result = Scanner.scan(self.target, self.port_range, nmap_flags)

        # - Formatting output - #
        self.write_output(Scanner, result)

    def write_output(self, Scanner, result):
        from config.colors import white
        from config.functions import sep_nmap_states

        if '!raw' in self.parameters:
            print(f'{white}{Scanner.csv()}\n')

        else:
            table = """\
            >> RESULTS FROM {}
            [PORT]  [STATE]     [SERVICE]
            -----    -----       -------
            {}
            \
            """
            ports = Scanner.all_tcp()
            for port in ports:
                port_service = Scanner[self.target]['tcp'][port]['name']
                port_state = Scanner[self.target]['tcp'][port]['state']
                port_state = sep_nmap_states(port_state)


class Flags(Scannertoolv2):
    def __init__(self, parameters):
        super().__init__(parameters)

    @staticmethod
    def get_nmap_flags(parameters):
        special_keywords = ['!port_info', '!raw']
        for i in special_keywords:
            if i in parameters:
                arguments = " ".join(parameters).strip(i)
                return arguments

        arguments = " ".join(parameters)
        return arguments
