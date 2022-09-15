# K-theory
Algorithms employed in my thesis and the paper "C*-algebras of higher-rank graphs..."
These were not designed for the public eye! They are therefore messy and poorly commented.
To get some more detail about what they are used for, read my thesis: "New models of higher-rank graphs..."

3D_dominoes.py takes lists of tiles (themselves lists of length 4) and configures them into 3D-dominoes.
It outputs the list of cubes, as well as the relevant short exact sequence of Evans as MAGMA-readable code.

3D_homology.py takes tiles and 3D-dominoes (constructed from 3D_dominoes.py) and outputs the boundary matrices used in computation of cellular homology.

Files output_"".txt are some examples of the output of 3D_dominoes.py.
[4,3,3] lists the maps used in Evans' sequence, when the group is a product of free groups of orders 4,3,3.
q_[a,b,c] lists the maps when the group is formed from the Rungtanapirom--Stix--Vdovina algorithm with prime power q and labels a,b,c.

Files bdry_matrices_"".txt are some examples of the output of 3D_homology.py.
201xF2 is the result of the domino group 2.01xF2, where 2.01 is from Kimberley--Robertson and F2 is the free group of rank 2.
axbxc is the result of the product of three free groups of ranks a,b,c.
q_[a,b,c] is the result of 3D_dominoes.py with prime power q and labels a,b,c, obtained from the Rungtanapirom--Stix--Vdovina algorithm.
