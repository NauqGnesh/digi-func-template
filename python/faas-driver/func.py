from parliament import Context
import digi

reconciler_running = False

def start_reconciler(): 
    """
    An idempotent function to start the digi reconciler.  
    """
    global reconciler_running 
    if not reconciler_running:
        digi.run()
        reconciler_running = True

def main(context: Context):
    if 'request' in context.keys():
        start_reconciler()
        return 'Reconciler running', 200
        
    else:
        print("Empty request", flush=True)
        return "{}", 200

