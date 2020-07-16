#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Scannertool:
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
        result = Scanner.scan(self.target, self.port_range, '-sV' + nmap_flags)

        # - Formatting output - #
        self.write_output(Scanner, result)

        # - Special flags - #
        get_flags = Flags(self.parameters, self.target)
        get_flags.execute_flag(Scanner)

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
            ports = Scanner[self.target].all_tcp()
            table_chain = ""
            #print(ports)
            for port in ports:
                port_service = Scanner[self.target]['tcp'][port]['name']
                port_state = Scanner[self.target]['tcp'][port]['state']
                port_state = sep_nmap_states(port_state)

                # - Each line in output table - #
                add_string = f"{port:<9}{port_state}\t {port_service}\n\t    {white}"
                table_chain += add_string

            print(table.format(self.target, white + table_chain))


class Flags(Scannertool):
    def __init__(self, parameters, target):
        self.parameters = parameters
        self.target = target

    @staticmethod
    def get_nmap_flags(parameters):
        special_keywords = {'!port_info', '!raw'}
        for i in special_keywords:
            if i in parameters:
                arguments = " ".join(parameters).strip(i)
                return arguments

        arguments = " ".join(parameters)
        return arguments


    def execute_flag(self, Scanner):
        def switch(flag):
            method_name = flag.strip('!')
            method = getattr(self, method_name)
            return method(Scanner)

        sp_flags = {'!port_info'}
        for flag in sp_flags:
            if flag in self.parameters:
                switch(flag)


    def port_info(self, Scanner):
        from config.colors import bold, green

        ports = Scanner[self.target].all_tcp()
        table = """\
        {}[{}]
        JAR_SOFTWARE = {}
        SERVER_INFO  = {}\n
        \
        """

        for port in ports:
            port_service = Scanner[self.target]['tcp'][port]['name']
            if port_service == 'minecraft':
                server_jar = Scanner[self.target]['tcp'][port]['version']
                server_inf = Scanner[self.target]['tcp'][port]['extrainfo']

                print(table.format(green + bold, port, server_jar, server_inf))
