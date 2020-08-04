"""Python
ELI5: What is callback?

Jimmy sells products to users. He gets requests from clients for different items. 
Jimmy does not know how to make the different items, but he knows a lot of factories that produce the different items that the clients want. 
Jimmy also has a friend Bob, who rides around in his van delivering the products to the clients.

Client Tom calls Jimmy and orders a chair for his home.
Jimmy then calls Okay-A Furniture:tm: who will produce the chair. In code the procedure could look like this:
"""
def OkayAFactory_Produce(furniture):
    item = produce(furniture)
    return item

"""
But there is an issue with this piece of code. 
This function returns item to the caller (Jimmy). 
However, if this item is sent back to Jimmy, then Jimmy has to send it to Bob and then Bob would have to send it to the client. 
That’s a lot of effort! What if we could instead tell Okay-A Furniture Factory what to do with the furniture after it is done? Fortunately, we can! 
This is what is called a callback, which is a function that is passed to a function/method/etc. 
which is then called at the end of the piece of code.
"""
def OkayAFactory_Produce(furniture, deliverFunction):
    item = produce(furniture)
    deliverFunction(item)   # replace the return with the callback!

# Here is what Bob’s deliver function might look like:
def Bob_deliverFurniture(item):
    address = item.address
    Bod_TravelTo(address)

"""
And then Jimmy would call the factory like this:
-- tell the factory to produce "chair" and pass it to Bob when it's done!
Now after the factory is done producing the chair, it will call back to Bob, because this is what Jimmy told them to do!
"""
OkayAFactory_Produce("chair", Bob_deliverFurniture)