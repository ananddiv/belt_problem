import os
from dotenv import load_dotenv
load_dotenv()
import gurobipy as gp
from gurobipy import GRB


# Explicitly pull from os.environ to guarantee WLS takes absolute priority
wls_params = {
    "WLSACCESSID": os.getenv("WLS_WLSACCESSID"),
    "WLSSECRET": os.getenv("WLS_WLSSECRET"),
    "LICENSEID": int(os.getenv("WLS_LICENSEID", 0)), 
}

# Block local files by forcing an empty environment with direct parameters
with gp.Env(empty=True) as env:
    for param, value in wls_params.items():
        env.setParam(param, value)
    env.start()
    
    # Pass your secure env to the model
    with gp.Model("ForcedWLSModel", env=env) as model:
        #decision variables
        x=model.addVar(vtype=GRB.CONTINUOUS, name="x")
        y=model.addVar(vtype=GRB.CONTINUOUS, name="y")
        #objective function
        model.setObjective(3*x + 4*y, GRB.MAXIMIZE)
        #constraints
        model.addConstr(x + y <= 800, "c0")
        model.addConstr(2*x + y <= 1000, "c1")
        model.addConstr(x <= 400, "c2")
        model.addConstr(y <= 700, "c3")
        model.addConstr(x >= 0, "c4")
        model.addConstr(y >= 0, "c5")

        #optimize the model
        model.optimize()
        #display the results
        if model.status == GRB.OPTIMAL:
            print(f"Optimal value: {model.objVal}")
            print(f"x: {x.x}")
            print(f"y: {y.x}")
        else:
            print("No optimal solution found.") 
        print(model.display())
