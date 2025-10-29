from datetime import datetime

class DataProcessor:
    """Base class for all data processing operations."""
    
    def process(self, data):
        """Process the data and return the result."""
        raise NotImplementedError


class DateParser(DataProcessor):
    """Extract and parse dates from text entries."""
    
    def __init__(self, date_format="%Y-%m-%d"):
        """
        Initialize the parser.
        
        Args:
            date_format: String format for parsing dates (default: "%Y-%m-%d")
        """
        # TODO: Store the date_format
        pass
    
    def process(self, entries):
        """
        Parse dates from text entries.
        
        Args:
            entries: List of strings, each potentially containing a date
            
        Returns:
            List of dictionaries with 'date' (datetime) and 'text' (str) keys
        """
        # TODO: Implement this method
        # Hint: Try to parse the beginning of each line as a date
        # If successful, split on ": " to separate date from text
        # Skip entries that don't have valid dates
        pass


class WeekdayFilter(DataProcessor):
    """Filter entries to keep only specific days of the week."""
    
    def __init__(self, allowed_days):
        """
        Initialize the filter.
        
        Args:
            allowed_days: List of day names to keep (e.g., ['Monday', 'Friday'])
        """
        # TODO: Store allowed_days
        pass
    
    def process(self, entries):
        """
        Filter entries by day of week.
        
        Args:
            entries: List of dictionaries with 'date' and 'text' keys
            
        Returns:
            List of entries where the date falls on an allowed day
        """
        # TODO: Implement this method
        # Hint: Use date.strftime("%A") to get the day name
        pass


class DateFormatter(DataProcessor):
    """Format dates into readable strings."""
    
    def __init__(self, output_format="%B %d, %Y"):
        """
        Initialize the formatter.
        
        Args:
            output_format: String format for output dates (default: "%B %d, %Y")
        """
        # TODO: Store output_format
        pass
    
    def process(self, entries):
        """
        Format entries as strings with formatted dates.
        
        Args:
            entries: List of dictionaries with 'date' and 'text' keys
            
        Returns:
            List of formatted strings
        """
        # TODO: Implement this method
        # Hint: Format should be "formatted_date: text"
        pass


class ProcessingPipeline:
    """Chain multiple processors together."""
    
    def __init__(self, processors):
        self.processors = processors
    
    def process(self, data):
        """Run data through all processors in sequence."""
        result = data
        for processor in self.processors:
            result = processor.process(result)
        return result
    pass