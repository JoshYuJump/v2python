def echo(value=None):
    print "Execution starts when 'next()' is called for the first time."
    try:
        while True:
            yield value
    finally:
        print "Don't forget to clean up when 'close()' is called."


g = echo(1)
print g.next()
print g.next()
print g.next()  
print g.next()        
g.throw(TypeError, "spam")
