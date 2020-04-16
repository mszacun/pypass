import subprocess
import re


class PasswordStoreEntry:
    PASS_ADDITIONAL_ENTRY_REGEXP = re.compile('(\w+): (.*)')

    def __init__(self, path):
        self.parsed_content = {}

        self._parse_entry(path)

    def _read_password_store_entry(self, path):
        return subprocess.check_output(['pass', path]).decode().splitlines()

    def _parse_entry(self, path):
        content = self._read_password_store_entry(path)

        self.parsed_content['password'] = content[0]
        for line in content[1:]:
            match = self.PASS_ADDITIONAL_ENTRY_REGEXP.match(line)
            if match:
                self.parsed_content[match.group(1)] = match.group(2)

    def __getitem__(self, key):
        return self.parsed_content[key]
