from models import *

def get_data():
    eqs=Earthquake.query.all()
    process_eqs=[e.enable_print() for e in eqs]
    return process_eqs
