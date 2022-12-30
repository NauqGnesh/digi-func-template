from parliament import Context
import digi

def main(context: Context):
    if 'request' in context.keys():
        digi.run()
        return 'Done reconciliation', 200
    else:
        print("Empty request", flush=True)
        return "{}", 200

