---
schema: qual/card@1
id: P-5UUNM
kind: problem
title: "Show that $Z(G) \\leq G$ is always characteristic."
classification:
  areas:
  - algebra
  topics:
  - centralizers-and-normalizers
  - automorphisms
  - subgroups
relations: []
review: draft
---
:::{.exercise title="?"}
Show that $Z(G) \leq G$ is always characteristic.
:::

:::{.solution}
Let $\psi\in \Aut(G)$.
For one containment, we can show $\psi(g) = h = h\psi(g)$ for all $\psi(g) \in \psi(G)$ and $h\in G$.
This is a computation:
\[
\psi(g) h 
&= \psi(g) (\psi \psi\inv)(h) \\
&= \psi( g ) \psi( \psi \inv (h)) \\
&= \psi( \psi\inv(h) g) \\
&= (\psi\psi\inv)(h) \psi(g) \\
&= h\psi(g)
.\]
This yields $\psi(Z(G)) \subseteq Z(G)$.
Applying the same argument to $\psi\inv$ yields $\psi\inv(Z(G)) \subseteq Z(G)$.
Since $\psi$ is a bijection, $\psi\psi\inv(A) = A$ for all $A\leq G$, 
so $Z(G) \subseteq \psi(Z(G))$.

:::
