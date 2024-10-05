#Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. For example, if the input 
# is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
#"Itinerary 1: Alice - From New York to London
#Itinerary 2: Bob - From Tokyo to San Francisco"




def format_itineraries(itineraries):
    return "\n".join(
        f"Itinerary {i + 1}: {name} - From {origin} to {destination}"
        for i, (name, origin, destination) in enumerate(itineraries)
    )

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
result = format_itineraries(itineraries)
print(result)
