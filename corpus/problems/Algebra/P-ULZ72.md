---
schema: qual/card@1
id: P-ULZ72
kind: problem
title: Elements $g$ for which $\chi(g)$ is real for every character $\chi$
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Conjugacy
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and $g\in G$. Suppose $\chi(g)\in\RR$ for every complex irreducible character $\chi$ of $G$. What can be said about $g$?
:::

::: {.solution}
One has
\[
\chi(g^{-1})=\overline{\chi(g)}
\]
for every complex character $\chi$. Indeed, a finite-group representation may be chosen unitary, so the eigenvalues of $\rho(g)$ lie on the unit circle and the trace of $\rho(g^{-1})$ is the complex conjugate of the trace of $\rho(g)$.

By hypothesis $\chi(g)$ is real for every irreducible character, hence
\[
\chi(g^{-1})=\chi(g)
\]
for every irreducible $\chi$.

Irreducible characters form a basis of the space of complex class functions on $G$. Therefore two elements on which all irreducible characters take the same values must lie in the same conjugacy class. Hence
\[
g^{-1}\sim g.
\]

Conversely, if $g$ is conjugate to $g^{-1}$, then every character satisfies
\[
\chi(g)=\chi(g^{-1})=\overline{\chi(g)},
\]
so $\chi(g)$ is real.

Thus
\[
\boxed{\chi(g)\in\RR\text{ for every irreducible }\chi
\iff g\text{ is conjugate to }g^{-1}.}
\]
:::
