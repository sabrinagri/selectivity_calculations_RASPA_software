#script to calculate selectivity in different molar fraction at RASPA software
#Sabrina Grigoletto - UFMG - Brazil

import os

# Molar fractions list to each component
molar_frac_1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
molar_frac_2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Main dir to all the molar fractions dirs
diretório_principal = "selectivity"
if not os.path.exists(diretório_principal):
    os.mkdir(diretório_principal)

# Create each dir and simulation.input for each molar fraction separated.
for i in range(len(molar_frac_1)):
    for j in range(len(molar_frac_2)):
        sum_molar_frac = molar_frac_1[i] + molar_frac_2[j]
        if sum_molar_frac == 1:
            dir_name = f"ch4_ethane_{i+1}_{j+1}" #coloca o nome do diretório com nomes das moléculas e o index das frações de cada uma na lista (o +1 é para evitar que comece em 0)
            caminho_diretório = os.path.join(diretório_principal, dir_name) #caminho do novo diretório a ser criado
            os.makedirs(caminho_diretório, exist_ok=True) #comando para criar o novo diretório das frações molares, desde que eles não existam ainda
            caminho_arquivo = os.path.join(caminho_diretório, "simulation.input") # de forma semelhante como foi feito, cria o caminho, mas agora para o arquivo
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.write("SimulationType                   MonteCarlo\n")
                arquivo.write("NumberOfCycles                   1000000\n")
                arquivo.write("NumberOfInitializationCycles     50000\n")
                arquivo.write("PrintEvery                       1000\n")
                arquivo.write("\n")
                arquivo.write("Forcefield                       GenericMOFs\n")
                arquivo.write("CutOffVDW                        12.0\n")
                arquivo.write("\n")
                arquivo.write("ChargeMethod                     Ewald\n")
                arquivo.write("CutOff                           12.0\n")
                arquivo.write("EwaldPrecision                   1e-6\n")
                arquivo.write("\n")
                arquivo.write("Framework                        0\n")
                arquivo.write("FrameworkName                    MOF\n") #insert mof cif file name
                arquivo.write("UnitCells                        1 1 1\n")
                arquivo.write("HeliumVoidFraction               0.XX\n") #insert calculated he void fraction
                arquivo.write("ExternalTemperature              XXX\n") #set simulation temperature
                arquivo.write("ExternalPressure                 XXXX\n") #set simulation pressur
                arquivo.write("\n")
                arquivo.write("UseChargesFromCIFFile            yes\n")
                arquivo.write("\n")
                arquivo.write(f"Component 0 MoleculeName         molecule 1\n") #set component 0 
                arquivo.write("             MoleculeDefinition   TraPPE\n")
                arquivo.write(f"             MolFraction         {molar_frac_1[i]}\n")
                arquivo.write("             TranslationProbability 0.5\n")
                arquivo.write("             IdentityChangeProbability 1.0\n")
                arquivo.write("               NumerOfIdentityChanges  2\n")
                arquivo.write("               IdentityChangesList     0 1\n")
                arquivo.write("             IdealGasRosenbluthWeight  1.0\n")
                arquivo.write("             TranslationProbability    0.5\n")
                arquivo.write("             RotationProbability       0.0\n")
                arquivo.write("             ReinsertionProbability    0.5\n")
                arquivo.write("             SwapProbability           1.0\n")
                arquivo.write("             CreateNumberOfMolecules   0\n")
                arquivo.write("\n")
                arquivo.write(f"Component 1 MoleculeName         molecule 2\n") #set component 1
                arquivo.write("             MoleculeDefinition   TraPPE\n")
                arquivo.write(f"             MolFraction         {molar_frac_2[j]}\n")
                arquivo.write("             TranslationProbability 1.0\n")
                arquivo.write("             IdentityChangeProbability 1.0\n")
                arquivo.write("               NumberOfIdentityChanges 2\n")
                arquivo.write("               IdentityChangesList     0 1\n")
                arquivo.write("             IdealGasRosenbluthWeight  1.0\n")
                arquivo.write("             TranslationProbability    0.5\n")
                arquivo.write("             RotationProbability       0.0\n")
                arquivo.write("             ReinsertionProbability    0.5\n")
                arquivo.write("             SwapProbability           1.0\n")
                arquivo.write("             CreateNumberOfMolecules   0\n")
