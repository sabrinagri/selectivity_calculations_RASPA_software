#!/bin/bash

l=('molecule1_molecule2_1_9' 'molecule1_molecule2_2_8' 'molecule1_molecule2_3_7' 'molecule1_molecule2_4_6' 'molecule1_molecule2_5_5' 'molecule1_molecule2_6_4' 'molecule1_molecule2_7_3' 'molecule1_molecule2_8_2' 'molecule1_molecule2_9_1')

for i in "${l[@]}"
do
        cp molecule1.def molecule1.def force_field_mixing_rules.def MOF.cif pseudo_atoms.def ./selectivity/$i
cd ./selectivity/$i
sh ./qraspa.sh MOF_${i} para4
cd ../../

done
