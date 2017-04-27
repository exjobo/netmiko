
from __future__ import unicode_literals

import re
import time

from netmiko.juniper.juniper_ssh import JuniperBase


class JuniperTelnet(JuniperBase):
    def telnet_login(self, pri_prompt_terminator='#', alt_prompt_terminator='>',
                     username_pattern=r"ogin", pwd_pattern=r"assword",
                     delay_factor=1, max_loops=60):
        """Telnet login. Can be username/password or just password."""
        super(JuniperTelnet, self).telnet_login(
            pri_prompt_terminator=pri_prompt_terminator,
            alt_prompt_terminator=alt_prompt_terminator,
            username_pattern=username_pattern,
            pwd_pattern=pwd_pattern,
            delay_factor=delay_factor,
            max_loops=max_loops)
