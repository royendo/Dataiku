# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import pprint as pp
client = dataiku.api_client()
project = client.get_project("EVERYTHING")
scenario = project.get_scenario("New")
scenario.run_and_wait(params=None, no_fail=False)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
last_runs = scenario.get_last_finished_run()
scenarioStep = last_runs.get_details()['scenarioRun']['scenario']['params']['steps']
nestedScenarios = []
for steps in scenarioStep:
    pp.pprint(steps)
    ScenarioID = steps['id'].split(".",1)[1]
    nestedScenarios.append(ScenarioID)
print(nestedScenarios)
for scenarios in nestedScenarios:
    nestedScenario = project.get_scenario(scenarios)
    nested_last_run = nestedScenario.get_last_finished_run().get_details()
    result = nested_last_run['scenarioRun']['result']['outcome']
    if result == "FAILED":
        print("The scenario "+ scenarios +" Failed.")