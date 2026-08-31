---
schema: qual/card@1
id: P-QC76S
kind: problem
title: Free modules over an integral domain are torsion-free; $\QQ$ is torsion-free
  but not free as a $\ZZ$-module
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Integral Domains
relations: []
review: draft
---

::: problem
Let $E$ be a free module over $R$ an integral domain.
Then $E$ has a basis $\theset{\vector e_i} \subseteq F$, so if $x \neq 0 \in E$, we have
$$
x = \sum_i r_i \vector e_i
$$

where each $r_i \in R$.
Moreover, since $x\neq 0$, at least one $r_i \neq 0$, so let $r_j$ denote one of the nonzero coefficients.

Now suppose $x$ is a torsion element, so $mx = 0$ for some $m\neq 0 \in E$.
We can then write
$$
mx = m\sum_i r_i \vector e_i = \sum_i mr_i \vector e_i = 0
$$

But by linear independence, this forces $mr_i = 0$ for all $i$.
In particular, $mr_j = 0$ where $r_j \neq 0$.
But this exhibits either $m$ or $r_j$ as a zero divisor, and since the only zero divisor in an integral domain is zero, we must have $m=0$ or $r_j = 0$, a contradiction.

So $x$ can not be a torsion element.
But since $x \in E$ was arbitrary, $E$ must be torsion-free.

For an example of a torsion-free module over an integral domain that is *not* free, consider $\QQ$ as a $\ZZ\dash$module.
Then $\QQ$ is torsion-free: if $n \cdot q = 0$ for some $n \in \ZZ$ and $q \in \QQ$, then either $n = 0$ or $q = 0$ (since $\QQ$ is a field, hence an integral domain, and $n \cdot q = 0$ in $\QQ$ with $n \neq 0$ forces $q = 0$), so no nonzero element of $\QQ$ is annihilated by a nonzero integer.

But $\QQ$ is not free as $\ZZ\dash$module.
Supposing that $\mathcal B =\theset{\vector b_1, \vector b_2, \cdots} \subset \QQ$ was a $\ZZ\dash$basis, consider $\vector b_1 = \frac {p_1} {q_1}$ and $\vector b_2 = \frac {p_2} {q_2}$.
Then $\vector b_1, \vector b_2$ can not be linearly independent over $\ZZ$, which follows from the fact that
$$
q_1 p_2 \vector b_1 + q_2 p_1 \vector b_2 = p_2 p_1 - p_1 p_2 = 0, 
$$

while $q_1 p_2, ~q_2 p_1 \neq 0 \in \ZZ$.
$\qed$
:::
