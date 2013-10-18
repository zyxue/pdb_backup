
# epz1_c: epz1 coil
# for aa in 'B': cmd._alt(string.lower(aa))
# for aa in 'GVPGVGVPGVGVPGVGVPGVGVPGVGVPGVGVPGVAAAAAKAAKYGVGTPAAAAAKAAAKAAQFGVPGVGVPGVGVPGVGVPGVGVPGVGVPGVGVPGVAAAAAKAAKYGVGTPAAAAAKAAAKAAQFGVPGVGVPGVGVPGVGVPGVGVPGVGVPGVGVPGV': cmd._alt(string.lower(aa))
# editor.attach_amino_acid('pk1', 'nhh')
# save /home/zyxue/labwork/pdb_backup/epz1.pdb,((ace))

from pymol import cmd, editor

def build_XL(ssid=0):
    """
    Build the cross-linking (XL) domain
    
    :Parameters:
    - `ssid`: secondary structure id

    0: coil (default)
    1: alpha-helix
    2: antiparallel beta-sheet
    3: parallel beta-sheet
    """
    cmd.set('secondary_structure', ssid)
    XL1 = 'AAAAAKAAKY'
    linker = 'GVGTP'
    XL2 = 'AAAAAKAAAKAAQF'
    for aa in XL1:
        cmd._alt(aa.lower())
    # because of Pro in the linker, it has to be coil
    cmd.set('secondary_structure', 0)
    for aa in linker:
        cmd._alt(aa.lower())
    cmd.set('secondary_structure', ssid)
    for aa in XL2:
        cmd._alt(aa.lower())
    
def build_HP(ssid=0):
    cmd.set('secondary_structure', ssid)
    HP = 'GVPGVGVPGVGVPGVGVPGVGVPGVGVPGVGVPGV'
    for aa in HP:
        cmd._alt(aa.lower())

def build_epz1_h():
    """Build epz1_h (epz1 with XL domains in alpha-helix)"""

    cmd._alt('B'.lower()) # N-terminal actyl group
    build_HP(0)
    build_XL(1)
    build_HP(0)
    build_XL(1)
    build_HP(0)

    editor.attach_amino_acid('pk1', 'nhh')
    cmd.save('/home/zyxue/labwork/pdb_backup/lele/epz1_h.pdb')
