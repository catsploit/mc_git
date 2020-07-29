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
        from config.colors import yellow, bold, normal

        print("{0}{1}[~] {0}Scanning {1}{2}{0} . . .\n".format(yellow, bold, self.target))

        # - Scanning target - #
        Scanner = nmap.PortScanner()
        nmap_flags = Flags.get_nmap_flags(self.parameters)
        try:
            result = Scanner.scan(self.target, self.port_range, f'-sV {nmap_flags}')
        except Exception as e:
            return(cprint(f"[!] portscanner >> Something went wrong: '{e}'\n", 'red', True))

        # - Formatting output - #
        self.write_output(Scanner, result)

        # - Special flags - #
        get_flags = Flags(self.parameters, self.target)
        get_flags.execute_flag(Scanner)

    def write_output(self, Scanner, result):
        from config.colors import white, blue, bold, normal
        from config.functions import sep_nmap_states, cprint

        if '!raw' in self.parameters:
            print(f'{white}{Scanner.csv()}\n')

        else:
            table = """\
>> SCAN RESULTS FROM {} <<
{}
\
"""
            try:
                ports = Scanner[self.target].all_tcp()
            except KeyError:
                return(cprint("[!] portscanner >> Please specify a port range\n", 'yellow'))

            table_chain = ""
            #print(ports)
            for port in ports:
                port_service = Scanner[self.target]['tcp'][port]['name']
                port_state = Scanner[self.target]['tcp'][port]['state']
                port_state = sep_nmap_states(port_state)

                # - Each line in output table - #
                add_string = "{0}{1}[-]{2} Discovered {3}{2} port on {4}, running {5}\n".format(blue, bold, normal, port_state, port, port_service)
                table_chain += add_string

            print(white + table.format(self.target, table_chain))


class Flags(Scannertool):
    def __init__(self, parameters, target):
        self.parameters = parameters
        self.target = target

    @staticmethod
    def get_nmap_flags(parameters):
        arguments = list(parameters)
        special_keywords = {'!port_info', '!raw'}
        for i in special_keywords:
            if i in parameters:
                arguments.pop(arguments.index(i))

        arguments = " ".join(arguments)
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
        from config.colors import bold, green, blue, normal

        ports = Scanner[self.target].all_tcp()
        table = """\
{0}{1}[+] {5}{2} Port deep scan:
{6}{1}[-] {5}JAR file: {3}
{6}{1}[-] {5}SERVER_INFO: {4}\n
        \
        """

        for port in ports:
            port_service = Scanner[self.target]['tcp'][port]['name']
            if port_service == 'minecraft':
                server_jar = Scanner[self.target]['tcp'][port]['version']
                server_inf = Scanner[self.target]['tcp'][port]['extrainfo'].replace(',', f'\n{blue}{bold}[-]{normal}')
                print(table.format(green, bold, port, server_jar, server_inf, normal, blue))
