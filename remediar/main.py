"""Main file Remediar."""
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal

from .controllers.base import Base
from .core.exc import RemediarError

# Configuration defaults
# CONFIG = init_defaults('remediar')
# CONFIG['remediar']['foo'] = 'bar'


class Remediar(App):
    """Remediar primary application."""

    class Meta:
        label = "remediar"

        # Configuration defaults
        # config_defaults = CONFIG

        # Call sys.exit() on close
        exit_on_close = True

        # Load additional framework extensions
        extensions = ["yaml", "colorlog", "print", "tabulate"]

        # Configuration handler
        config_handler = "yaml"

        # Configuration file suffix
        config_file_suffix = ".yml"

        # Set the log handler
        log_handler = "colorlog"

        # Set the output handler
        output_handler = "tabulate"

        # Register handlers
        handlers = [Base]


class RemediarTest(TestApp, Remediar):
    """A sub-class of Remediar that is better suited for testing."""

    class Meta:
        label = "remediar"


def main():
    """."""
    with Remediar() as app:
        try:
            app.run()

        except AssertionError as e:
            print("AssertionError > %s" % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except RemediarError as e:
            print("RemediarError > %s" % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print("\n%s" % e)
            app.exit_code = 0


if __name__ == "__main__":
    main()
