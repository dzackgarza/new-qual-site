---
schema: qual/card@1
id: P-QJE7B
kind: problem
title: "Let $\\vector w_i$ be the proposed new basis elements -- then $\\theset{\\vector w_i}$ will be a\u2026"
classification:
  areas:
  - prelim
  topics:
  - vector-spaces
  - bases
relations: []
review: draft
---
1. Let $\vector w_i$ be the proposed new basis elements -- then $\theset{\vector w_i}$ will be a basis if it is linearly independent and spans $\RR^3$. Since there are already three vectors in this set, we only need to check that they are linearly independent.
  By definition, we have
  $$
  \theset{\vector e_i} \text{ is linearly independent} \iff \sum c_i \vector e_i = \vector 0 \implies \forall i, ~ c_i = 0.
  $$

    Furthermore, since $\theset{\vector v_i}$ is known to be a basis, we have
  $$
  \sum c_i \vector v_i = \vector 0 \implies \forall i, ~ c_i = 0.
  $$

    So suppose $\sum c_i \vector w_i = \vector 0$, we want to show that $c_i = 0$ for each $i$. (This will mean that $\theset{\vector w_i}$ is linearly independent.) 

    We can expand this in terms of $\vector v_i$ as follows:
  $$
  c_1 \vector w_1 + c_2 \vector w_2 + c_3 \vector w_3  = \vector 0\\ 
  \implies c_1 (\vector v_1 + \vector v_2)  + c_2(\vector v_1 + \vector v_2 + \vector v_3) + c_3(-\vector v_2 + 2\vector v_3)  = \vector 0\\
  \implies c_1 \vector v_1 + (c_1+c_2+c_3) \vector v_1 + (-c_2 + 2c_3) \vector v_3  = \vector 0
  $$

    And using the fact that $\vector v_i$ is linearly independent, each coefficient of $\vector v_i$ here must be zero, and we arrive at the following system of equations:
  $$
  \begin{array}{lll}
  c_1 &&       &&       &=& 0 \\
  c_1 &+& c_2  &+& c_3  &=& 0 \\
      && -c_2 &+& 2c_3 &=& 0 \\
  \end{array}
  $$

    which can be rewritten as the matrix equation
  $$
  A\vector c 
  = \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} \right]
  \left[\begin{array}{l}c_1 \\ c_2 \\ c_3 \end{array}\right] 
  = \vector 0
  $$

    and thus $\vector w_i$ will be linearly independent precisely if $A\vector c = \vector 0$ has only the trivial solution $\vector c = \vector 0$, which is precisely when $A$ has full rank, which happens iff $\det A \neq 0$. A quick calculation shows that $\det A = 3 \neq 0$, and so we are done. $\qed$

