"""Base part of the remediar CLI."""
from cement import Controller, ex
import os
import yaml
from ..helper.checking import get_check
import datetime

from ..constants import RUN_BANNER, VERSION_BANNER, HEADERS
from ..helper.output import add_row


class Base(Controller):
    """Base controller for the CLI."""

    class Meta:
        """Meta class for the CLI."""
        label = "base"

        # Text displayed at the top of --help output
        description = "Remediar is an issue and vulnerability tracker framework"

        # Text displayed at the bottom of --help output
        #epilog = "Usage: remediar run --foo bar"

        # Controller level arguments. ex: 'remediar --version'
        arguments = [
            # Add a version banner
            (["-v", "--version"], {"action": "version", "version": VERSION_BANNER})
        ]

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
        help="run tasks",
        arguments=[(["file"], {"help": "tasks file to process"})],
    )
    def run(self):
        """Run sub-command."""
        print(RUN_BANNER)
        if self.app.pargs.file is not None:
            tasks_file = self.app.pargs.file

        tasks_file_path = os.getcwd()

        with open(os.path.join(tasks_file_path, tasks_file), encoding='utf-8') as desc:
            tasks = desc.read()

        data = yaml.safe_load(tasks)

        self.app.print("{} - {} ({})".format(
            data.get('name'), data.get('description'), datetime.datetime.now().isoformat()
        ))

        rows = []

        for host in data['hosts']:
            #self.app.print((host['ip_address']))
            target = host['ip_address']

            # HTTP
            if host.get('http', None) is not None:
                http_config = host['http']
                port = http_config.get('port', 80)
                checks = http_config.get('checks')

                for check in checks:
                    result = get_check('http', check)(target)
                    add_row(rows, target, 'http', check, result)

            # SSH
            if host.get('ssh', None) is not None:
                ssh_config = host['ssh']
                port = ssh_config.get('port', 22)

                checks = ssh_config.get('checks')

                for check in checks:
                    result = get_check('ssh', check)(target, port)
                    add_row(rows, target, 'ssh', check, result)

            #    TCP
            if host.get('tcp', None) is not None:
                tcp_config = host['tcp']
                ports = tcp_config.get('ports')
                checks = tcp_config.get('checks')

                for check in checks:
                    for port in ports:
                        result = get_check('tcp', check)(target, port)
                        add_row(rows, target, 'tcp', check, result)

        self.app.render(rows, headers=HEADERS)
