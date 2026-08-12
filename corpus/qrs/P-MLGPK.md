---
schema: qual/card@1
id: P-MLGPK
kind: problem
title: "Let $R$ be a simple rng (a nonzero ring which is not assume to\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $R$ be a simple rng (a nonzero ring which is not assume to have a 1, whose only two-sided ideals are $(0)$ and $R$) satisfying the following two conditions:

i. $R$ has no zero divisors, and
ii. If $x\in R$ with $x\neq 0$ then $2x\neq 0$, where $2x\definedas x+x$.

Prove the following:

a.
For each $x\in R$ there is one and only one element $y\in R$ such that $x = 2y$.

b.
Suppose $x,y\in R$ such that $x\neq 0$ and $2(xy) = x$, then $yz = zy$ for all $z\in R$.

> You can get partial credit for (b) by showing it in the case $R$ has a 1.


:::{.remark}
A general opinion is that this is not a great qual problem! 
Possibly worth skipping.
:::


:::{.concept}
\envlist

- $R$ has no left zero divisors iff $R$ has the left cancellation property: $xa=xb \implies a=b$.
- $R$ has no right zero divisors iff $R$ has the right cancellation property: $ax=bx \implies a=b$.
:::

:::{.solution}
Note: solutions borrowed from folks on Math twitter!

:::{.proof title="part 1"}
\envlist

- Existence: the claim is that $2R \da \ts{2y \st y\in R}$ is a nontrivial two-sided ideal of $R$, forcing $2R = R$ by simpleness.
  - That $2R \neq 0$ follows from condition (1):
  Provided $y\neq 0$, we have $2y\neq 0$, and so if $R\neq 0$ then there exists some nonzero $a\in R$, in which case $2a\neq 0$ and $2a\in 2R$.
  - That $2R$ is a right ideal: clear, since $(2y)\cdot r = 2(yr)\in 2R$.
  - That $2R$ is a left ideal: use that multiplication is distributive:
  \[
  r\cdot 2y \da r(y+y) = ry + ry \da 2(ry) \in 2R
  .\]
- So $2R = R$ by simpleness.
- Uniqueness: 
  - Use the contrapositive of condition (1), so that $2x = 0 \implies x=0$.
  - Suppose toward a contradiction that $x=2y_1 = 2y_2$, then
  \[
  0 = x-x = 2y_1 - 2y_2 = 2(y_1 - y_2) \implies y_1 - y_2 = 0 \implies y_1 = y_2
  .\]
:::

:::{.proof title="part 2"}
\envlist

- First we'll show $z=2(yz)$:
\[
xy + xy &= x \\
\implies xy + xy - x &= 0 \\
\implies xyz + xyz - xz &= 0 \\
\implies x(yz + yz - z) &= 0 \\
\implies yz + yz - z &= 0 && \text{since } x\neq 0 \text{ and no zero divisors }\\
\implies 2(yz) &= z 
.\]

- Now we'll show $z=2(zy)$:
\[
yz + yz &= z \\
\implies zyz + zyz &= zz \\
\implies zyz + zyz - zz &= 0 \\
\implies (zy + zy - z)z &= 0\\
\implies z=0 \text{ or } zy+zy-z &= 0 && \text{ no zero divisors } 
.\]

- Then if $z=0$, we have $yz = 0 = zy$ and we're done.
- Otherwise, $2(zy) = z$, and thus
\[
2(zy) = z = 2(yz) \implies 2(zy - yz) = 0 \implies zy-yz = 0
,\]
so $zy=yz$.
:::

:::{.proof title="of 2, if $R$ is unital"}
\envlist

- If $1\in R$, 
\[
2xy &= x \\
\implies 2xy-x &= 0 \\
\implies x(2y-1) &= 0 \\
\implies 2y-1 &= 0 && x\neq 0 \text{ and no zero divisors}\\
\implies 2y &= 1
.\]
- Now use
\[
1\cdot z &= z\cdot 1 \\
\implies (2y)z &= z(2y) \\
\implies (y+y)z &= z(y+y) \\
\implies yz+yz &= zy+zy \\
\implies 2(yz) &= 2(zy) \\
\implies 2(yz-zy) &= 0 \\
\implies yz-zy &= 0 \\
,\]
using condition (2).
:::

:::
