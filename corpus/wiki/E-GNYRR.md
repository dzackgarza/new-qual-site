---
schema: qual/card@1
id: E-GNYRR
kind: exercise
title: "Prove Cayley-Hamilton in the following way."
classification:
  areas:
  - algebra
  topics:
  - minimal-and-characteristic-polynomials
  - eigenvalues-and-eigenvectors
  - linear-algebra
relations: []
review: draft
solved: false
---
:::{.exercise title="?"}
Prove Cayley-Hamilton in the following way.
Let $V = \spanof\ts{\vector v_1, \cdots, \vector v_n}$ and define the $i$th flag as $\Fil_i V \da \spanof\ts{\vector v_1, \cdots, \vector v_i}$ for all $1\leq i \leq n$, and set $\Fil_0 V \da \ts{0}$.
Show that if if $A$ is upper triangular, then $A(\Fil_i V) \subseteq \Fil_i V$.
Now supposing $\vector v_i$ are eigenvectors for $\lambda_i$, show that
\[
(A-\lambda_n I) \Fil_n V &\subseteq \Fil_{n-1} V \\
(A-\lambda_{n-1} I) (A-\lambda_n I ) \Fil_n V &\subseteq \Fil_{n-2} V \\
&\vdots \\
\prod_i (A-\lambda_{n-i} I) \Fil_n V &\subseteq \Fil_0 V = \ts{0}
.\]
Conclude that $\chi_A(A) = 0$.
:::
