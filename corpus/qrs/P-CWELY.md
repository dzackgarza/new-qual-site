---
schema: qual/card@1
id: P-CWELY
kind: problem
title: "$V = \\theset{\\vector v \\in \\RR^3 \\suchthat \\inner{\\vector v}{\\thevector{3,4,5}} = \\vector 0}$ Subspace test: $V \\subset X$ is a linear subspace iff\u2026"
classification:
  areas:
  - prelim
  topics:
  - vector-spaces
  - linear-algebra
relations: []
review: draft
---
1. $V = \theset{\vector v \in \RR^3 \suchthat \inner{\vector v}{\thevector{3,4,5}} = \vector 0}$
   1. Subspace test: $V \subset X$ is a linear subspace iff $\theset{t\vector v_1 + \vector v_2 \suchthat t\in \RR, \vector v_i \in V} \subseteq V$.
   $$
   \inner{t\vector v_1 + \vector v_2}{\thevector{3,4,5}} = t\inner{\vector v_1}{\thevector{3,4,5}} + \inner{\vector v_2}{\thevector{3,4,5}} = t\vector 0 + \vector 0 = \vector 0.\qed
   $$
      1. Alternatively, just note that it is the kernel of the linear map $\inner{\wait}{\thevector{3,4,5}}: \RR^3 \to \RR^1$, and kernels are always sub-things.
   1. Yes, note $V$ defines a plane $P \cong \RR^2 \subset \RR^3$, so a projection onto $P^\perp = \thevector{3,4,5}$ will work:
   $$
   A = \left[ \begin{array}{ccc} 3 & 4 & 5 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right]
   $$
   Then $A\vector x = \thevector{3x + 4y + 5z, 0, 0}$ and if $\vector x \in V$ then $3x+4y+5z = 0$ by definition and thus $A\vector x = \vector 0$.
   1. Yes, first we look for a matrix that annihilates $\thevector{3,4,5}$ and has rank 2, since its rows will span the 2-dimensional subspace $V$. One that works is
   $$
    A = \left[ \begin{array}{ccc} 2 & 1 & -2 \\ 0 & -5 & 4 \\ 0 & 0 & 0\end{array}\right]
   $$
   So now we know that $\thevector{2,1,-2}, \thevector{0,-5,4} \in V$, and since $A$ is rank 2, they in fact span $V$. Thus we can take $A^T$, whose columns are these vectors. Then the columnspace of $A^T$ is $V$, and thus the linear map corresponding to $A^T$ has image $V$. $\qed$
   1. No, by rank nullity: $\abs{\im A} + \abs{\ker A} = \abs{\mathrm{domain} A}$, but $\abs{V} = 2$, so this would force the contradiction $2+2 = 3$.
   
