---
schema: qual/card@1
id: PR-DEGP1
kind: proposition
title: Properties of the degree
slogan: 'The degree is multiplicative, constant on homotopy classes, and reversed by a reflection.'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
---

::: {.proposition}
Let $n\geq1$ and let $f,g\colon S^n\to S^n$ be continuous.

- $\deg\id_{S^n}=1$, and $\deg f=0$ if $f$ is not surjective, in particular if $f$ is constant.
- If $f\homotopic g$ then $\deg f=\deg g$; conversely maps of equal degree are homotopic [@Hat02, Corollary 4.25].
- $\deg(f\circ g)=\deg f\cdot\deg g$, so $\deg f=\pm1$ if $f$ is a homotopy equivalence.
- A reflection $R_i$ of $S^n\subseteq\RR^{n+1}$ changing the sign of one coordinate has $\deg R_i=-1$, so the antipodal map $x\mapsto -x=R_1\circ\cdots\circ R_{n+1}$ has degree $(-1)^{n+1}$.
- If $f$ has no fixed point then $\deg f=(-1)^{n+1}$.

[@Hat02, §2.2]
:::
