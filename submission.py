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
        self.date_format = date_format
    
    def process(self, entries):
        """
        Parse dates from text entries.
        
        Args:
            entries: List of strings, each potentially containing a date
            
        Returns:
            List of dictionaries with 'date' (datetime) and 'text' (str) keys
        """
        results = []
        
        for line in entries:
            try:
                date_str, text = line.split(": ", 1)
                parsed_date = datetime.strptime(date_str, self.date_format)
                results.append({'date': parsed_date, 'text': text})
            except Exception:
                continue
        
        return results

# Test 1: DateParser basic functionality
parser = DateParser(date_format="%Y-%m-%d")
entries = ["2024-10-15: Event 1", "2024-10-16: Event 2"]
result = parser.process(entries)
print(f"Parsed {len(result)} entries")  # Should be 2

class WeekdayFilter(DataProcessor):
    """Filter entries to keep only specific days of the week."""
    
    def __init__(self, allowed_days):
        self.allowed_days = allowed_days
    
    def process(self, entries):
        results = []
        for entry in entries:
            day_name = entry['date'].strftime("%A")
            if day_name in self.allowed_days:
                results.append(entry)
        return results
# Test 2: DateParser with invalid entries
parser = DateParser(date_format="%Y-%m-%d")
entries = ["2024-10-15: Valid", "Not a date", "2024-10-16: Also valid"]
result = parser.process(entries)
print(f"Parsed {len(result)} entries")  # Should be 2 (skips invalid)



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