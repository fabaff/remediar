"""Helper for remediar.."""


class Check:
    """An abstract class for Remediar checks."""

    @property
    def name(self) -> str:
        """Return the name of the check."""
        return None

    @property
    def check_group(self) -> str:
        """Return the check group of the check."""
        return None

    @property
    def check_type(self) -> str:
        """Return the check type of the check."""
        return None

    @property
    def result(self) -> str:
        """Return the state of the entity."""
        return None

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return None
