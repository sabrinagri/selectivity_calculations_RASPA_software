#!/bin/bash

l=('ch4_ethane_1_9' 'ch4_ethane_2_8' 'ch4_ethane_3_7' 'ch4_ethane_4_6' 'ch4_ethane_5_5' 'ch4_ethane_6_4' 'ch4_ethane_7_3' 'ch4_ethane_8_2' 'ch4_ethane_9_1')

for i in "${l[@]}"
do
        cp methane.def ethane.def force_field_mixing_rules.def sifsix-3-cu.cif pseudo_atoms.def ./selectivity/$i
cd ./selectivity/$i
sh ./qraspa.sh sifsix-3-cu_${i} para4
cd ../../

done
