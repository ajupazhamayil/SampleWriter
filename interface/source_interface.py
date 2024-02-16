class SourceInterface:
    """
    Interface for all sources.
    """

    def process(self) -> int:
        """
        Process the sample source.

        Returns:
            status code.
        """
        pass
