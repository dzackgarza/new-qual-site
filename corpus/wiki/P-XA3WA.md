---
schema: qual/card@1
id: P-XA3WA
kind: problem
title: "Zeros of a polynomial in the closed unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

:::{.problem title="?"}
Find the number of roots on $\abs{z} \leq 1$ of
\[
f(z)=z^{6}+4 z^{2} e^{z+1}-3
.\]
:::

:::{.solution}

- Small: $m(z) = z^6-3$
- Big: $M(z) = 4z^2 e^{z+1}$, which has two such zeros

Now estimate $m$ from above:
\[
\abs{m(z)} = \abs{z^6 - 3} \leq \abs{z}^6 + 3 = 4
.\]
and $M$ from below:
\[
\abs{M(z)} = \abs{4z^2 e^{z+1}} 
= 4e\abs{z}^4 e^{\Re(z)} 
= 4e e^{\Re(z)} 
\geq 4e e^{-1} = 4
,\]
which unfortunately isn't quite enough.
But equality occurs iff $\Re(z) = -1$ on $S^1$, so $z=-1$, in which case $\abs{m(-1)} = \abs{1-3} = 2$, so the inequality is in fact strict.
So $2 = Z_M = Z_f$.
:::

