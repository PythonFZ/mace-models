from mace_models import LoadModel
import zntrack

with zntrack.Project() as project:
    LoadModel(model_path="data/2023-12-03-mace-mp.model", name="MACE-MP-0")

project.run()