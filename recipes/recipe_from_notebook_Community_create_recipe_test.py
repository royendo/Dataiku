# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import json

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
f = open("/Users/rendo/Downloads/dss-job-diag-EVERYTHING-sched_build_2021-07-06T05-34-47.797/localconfig/projects/EVERYTHING/recipes/compute_covid_jpn_total_prepared.json",)
#print(f.read())
recipe_proto = json.load(f)
fr = open("/Users/rendo/Downloads/dss-job-diag-EVERYTHING-sched_build_2021-07-06T05-34-47.797/localconfig/projects/EVERYTHING/recipes/compute_covid_jpn_total_prepared.shaker",)
creation_setting = json.load(fr)
print(recipe_proto["inputs"]["main"]["items"][0]["ref"])
print(recipe_proto["outputs"]["main"]["items"][0]["ref"])
print(recipe_proto["type"])
input1 = recipe_proto["inputs"]["main"]["items"][0]["ref"]
output = recipe_proto["outputs"]["main"]["items"][0]["ref"]
type1 = recipe_proto["type"]
#print(recipe_proto)
#print(creation_setting)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
client = dataiku.api_client()
project = client.get_project("Everything")

print(project)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#createRecipe = project.create_recipe(recipe_proto, creation_setting)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
builder = project.new_recipe("sync")
builder = builder.with_input(input1)
builder = builder.with_new_output(output, "filesystem_managed", format_option_id="csv")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
recipe = builder.create()