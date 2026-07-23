---
schema: qual/card@1
id: P-KOTV2
kind: problem
title: "1. It will exactly be the row space of"
classification:
  areas: []
  topics: []
relations: []
review: draft
---
1. It will exactly be the row space of 
$$
A = \left(\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
3 & 4 & 6 & 7 \\
5 & 6 & 8 & 9
\end{array}\right),
$$ 
where we could note that $R_3 = 2R_1 + R_2$ but $R_1 \neq \lambda R_2$ and so the first two rows span the correct subspace. We can also easily compute the RREF, which has the same rowspace, $$\tilde A = \left(\begin{array}{rrrr}
1 & 0 & -2 & -3 \\
0 & 1 & 3 & 4 \\
0 & 0 & 0 & 0
\end{array}\right)$$
from which we find that $\vector v_1 = \thevector{1,0,-2,-3}$ and $\vector v_2 = \thevector{0,1,3,4}$ also do the job. $\qed$

