# MACE Model Repository

This Repository uses `pip install mace-models` to make the models available.

To use the models, please install

```sh
pip install mace-models
pip install git+https://github.com/ACEsuit/mace.git
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15HjYX24L2g0yJw68J8wyviU2L75z-CIH)

```python
import mace_models
from ase.build import molecule

model = mace_models.load("MACE-MP-0", remote="https://github.com/PythonFZ/mace-models")

water = molecule("H2O")
water.calc = model.get_calculator(dtype="float64")

print(water.get_potential_energy())
>>> -14.159366
```

# Models

- `MACE-MP-0` https://arxiv.org/abs/2401.00096
