---
schema: qual/card@1
id: P-NORI-GT-3-10
kind: problem
title: Quartic extensions containing a quadratic subfield have minimal polynomial $Q^2-cP^2$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.10 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the polynomial type of Problem 3.9, on which this problem depends, from p. 2 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Problem 3.9 concerns polynomials $f = Q^2 - cP^2$ where $c \in F$ and $P, Q \in F[X]$ with $Q$ monic of degree two and $\deg(P) < 2$, and shows that if such an $f$ is irreducible, then the field $F(\theta)$ obtained by adjoining a root $\theta$ of $f$ contains a quadratic extension of $F$.

Conversely, Let $E = F(\theta)$ be a edgree four extension of $F$ that contains a quadratic extension of $F$.
Prove that the (monic) minimal polynomial is of the type described in the previous problem.
Here we are assuming that $\operatorname{char} F$ is $\neq 2$.
:::
