---
schema: qual/card@1
id: P-AGH534MULTLOCRING
kind: problem
title: The Hilbert-Samuel polynomial and the multiplicity of a local ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Surfaces
relations: []
review: draft
---

::: problem
Let $A$ be a noetherian local ring with maximal ideal $\mfm$. For any $l>0$, let $\psi(l)=\operatorname{length}\left(A / \mfm^l\right)$. We call $\psi$ the **Hilbert-Samuel function of $A$**.

a. Show that there is a polynomial $P_A(z) \in \QQ[z]$ such that $P_A(l)=\psi(l)$ for all $l \gg 0$. This is the Hilbert-Samuel polynomial of $A$.

  Hint: Consider the graded ring $\mathrm{gr}_{\mfm} A=\bigoplus_{d \geqslant 0} \mfm^d / \mfm^{d+1}$, and apply $(\mathrm{I}, 7.5)$.

  See Nagata $[7, \text{Ch} III, \S 23]$ or Zariski-Samuel $[1, \text{vol} 2 , \text{Ch} VIII, \S 10]$.

b. Show that $\operatorname{deg} P_A=\operatorname{dim} A$.

c. Let $n=\operatorname{dim} A$. Then we define the multiplicity of $A$, denoted $\mu(A)$, to be $(n !)\cdot$ (leading coefficient of $P_A$). If $P$ is a point on a noetherian scheme $X$, we define the multiplicity of $P$ on $X$, $\mu_P(X)$, to be $\mu\left(\mathcal{O}_{P, X}\right)$.

d. Show that for a point $P$ on a curve $C$ on a surface $X$, this definition of $\mu_P(C)$ coincides with the one in the text just before (3.5.2).

e. If $Y$ is a variety of degree $d$ in $\PP^n$, show that the vertex of the cone over $Y$ is a point of multiplicity $d$.
:::
