#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_info = {} #Store source and destination as KVP
    route = [] #function should output an array of strings with the entire route of your trip.

    #Loop through each individual ticket in tickets
    for ticket in tickets:
        #Store source as key and destination as value
        ticket_info[ticket.source] = ticket.destination
    
    #the ticket for your first flight has a destination with a source of NONE
    starting_location = "NONE"

    #Need to loop through each ticket, index will act as a pointer
    index = 0

    while index < length:
        #Get will give us just the value, since that's the only thing we need,
        starting_location = ticket_info.get(starting_location)
        #can append to our list
        route.append(starting_location)
        #keep going until we reach the length
        index +=1

    return route
