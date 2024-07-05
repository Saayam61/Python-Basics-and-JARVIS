# The match-case statement is conceptually similar to the switch statement in languages like C or C#,
# but it has significant differences and added capabilities.

# The match-case statement in Python supports complex pattern matching, including matching against data 
# structures like lists, tuples, and dictionaries.
# It allows for binding variables and matching specific parts of a structure.

# no need for 'break'

# match-case can differentiate between types, allowing different cases for different types of data.

# match-case allows adding conditions to patterns using the if keyword.

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(197)) # Output: Unknown status

# advanced eg:
def handle_message(message):
    match message:
        # dictionary
        case {"type": "greeting", "content": content}:
            return f"Greeting received: {content}"
        # list with string and variable + checks condition
        case ["error", code, description] if code == 404:
            return f"Error 404: {description}"
        # *details is using the unpacking operator to collect any additional elements (after severity) 
        # into a tuple named details.
        # For example, if the message is ("alert", "high", "disk space low", "warning"), then 
        # details would be ("disk space low", "warning").
        
        # '*' can be used to unpack iterables (like lists, tuples, strings) into individual elements
        case ("alert", severity, *details):
            return f"Alert with severity {severity}: {details}"
            # _(wildcard) is default case
        case _:
            return "Unknown message type"

# Examples
print(handle_message({"type": "greeting", "content": "Hello"}))  # Greeting received: Hello
print(handle_message(["error", 404, "Page not found"]))  # Error 404: Page not found
print(handle_message(("alert", "high", "disk space low")))  # Alert with severity high: ('disk space low',)
print(handle_message("some other message"))  # Unknown message type
