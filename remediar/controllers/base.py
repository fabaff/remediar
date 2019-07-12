"""Base part of the Remediar CLI."""
import datetime
import os

from cement import Controller, ex
import yaml

from ..constants import HEADERS, RUN_BANNER, VERSION_BANNER
from ..helper.checking import get_check
from ..helper.output import add_row


class Base(Controller):
    """Base controller for the CLI."""

    class Meta:
        """Meta class for the CLI."""

        label = "base"

        # Text displayed at the top of --help output
        description = "Remediar is an issue and vulnerability tracker framework"

        # Text displayed at the bottom of --help output
        # epilog = "Usage: remediar run --foo bar"

        # Controller level arguments. ex: 'remediar --version'
        arguments = [
            # Add a version banner
            (["-v", "--version"], {"action": "version", "version": VERSION_BANNER})
        ]

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(help="run tasks", arguments=[(["file"], {"help": "tasks file to process"})])
    def run(self):
        """Run sub-command."""
        print(RUN_BANNER)
        if self.app.pargs.file is not None:
            tasks_file = self.app.pargs.file

        tasks_file_path = os.getcwd()

        with open(os.path.join(tasks_file_path, tasks_file), encoding="utf-8") as desc:
            tasks = desc.read()

        data = yaml.safe_load(tasks)

        self.app.print(
            "{} - {} ({})".format(
                data.get("name"),
                data.get("description"),
                datetime.datetime.now().isoformat(),
            )
        )

        rows = []

        for host in data["hosts"]:
            target = host["ip_address"]

            groups = list(host.keys())
            groups.remove("ip_address")
            groups.remove("name")

            for group in groups:
                group_config = host[group]
                ports = group_config.get("ports")
                port = group_config.get("port")
                checks = group_config.get("checks")

                for check in checks:
                    # self.app.print(
                    #     "Running '{}' of {} on {} ...".format(
                    #         check, group, target
                    #     )
                    # )
                    result = get_check(group, check)(target, port=port, ports=ports)
                    add_row(rows, target, group, check, result)

        self.app.render(rows, headers=HEADERS)
