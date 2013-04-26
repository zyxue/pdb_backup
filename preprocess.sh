#!/bin/bash

# this script process the pdb file created by pymol roughly and create the
# corresponding gro, top, itp (posres) file

for i in *.pdb; do
    pf=$(string_slice.sh ${i} 0 -4)
    printf "14\n1\n3\n3\n" | pdb2gmx -f ${pf}.pdb -o ${pf}.gro -p ${pf}.top -i ${pf}.itp -ignh -ter
done