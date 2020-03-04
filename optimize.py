pk = Psikit()
pk.read_from_smiles("c1ccccc1")
print("Optimized SCF Energy: ", pk.optimize())
# Optimizer: Optimization complete!
# Optimized SCF Energy:  -230.71352354223438
