def handle_get_weather_error(e):
    """Function to handle exceptions and print error messages."""
    if isinstance(e, r.exceptions.ConnectionError):
        print("Error: Failed to connect to the weather API. Check your network connection.")
    elif isinstance(e, r.exceptions.Timeout):
        print("Error: The request to the weather API timed out.")
    elif isinstance(e, r.exceptions.HTTPError):
        print(f"HTTP error occurred: {e}")
    elif isinstance(e, ValueError):
        print("Error: Received an invalid response (possibly not JSON).")
    else:
        print(f"An unexpected error occurred: {e}")