---
schema: qual/card@1
id: P-HCAX14
kind: problem
title: Poles and residues of the cosecant function
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
relations: []
review: draft
---

::: problem
Find all poles and residues of $1/\sin z$.
:::

::: solution
The zeros of $\sin z$ are exactly the points $z=n\pi$, $n\in\mathbb Z$. Since
\[
(\sin z)'\big|_{z=n\pi}=\cos(n\pi)=(-1)^n\ne0,
\]
each zero is simple. Therefore $1/\sin z$ has a simple pole at each $n\pi$ and no other poles.

For a quotient $1/g(z)$ at a simple zero $a$ of $g$, the residue is $1/g'(a)$. Hence
\[
\operatorname{Res}_{z=n\pi}\frac1{\sin z}
=\frac1{\cos(n\pi)}
=(-1)^n.
\]
Thus the poles are precisely $n\pi$ for $n\in\mathbb Z$, and the residue at $n\pi$ is $(-1)^n$.
:::
