---
schema: qual/card@1
id: P-TQNU2
kind: problem
title: A polynomial over $\QQ$ whose splitting field has degree $1225$ is solvable
  by radicals
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Galois Theory
  - Sylow Theory
relations: []
review: draft
---

::: problem
Let $f(x) \in \QQ[x]$ be a polynomial and $K$ be a splitting field of $f$ over $\QQ$.
Assume that $[K:\QQ] = 1225$ and show that $f(x)$ is solvable by radicals.
:::

::: solution
Because $K$ is the splitting field over a field of characteristic $0$, the
extension $K/\QQ$ is finite Galois. Put
\[
G=\operatorname{Gal}(K/\QQ).
\]
Then
\[
|G|=[K:\QQ]=1225=5^2\cdot7^2.
\]

Let $n_7$ be the number of Sylow $7$-subgroups of $G$. Sylow's theorems give
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid25.
\]
The divisors of $25$ are $1,5,25$, and only $1$ is congruent to $1$ modulo
$7$. Hence $n_7=1$. Thus the Sylow $7$-subgroup $P$ is normal in $G$ and has
order $49$.

Every group of order $p^2$ is abelian, so $P$ is abelian. The quotient
$G/P$ has order
\[
|G/P|=25,
\]
and is therefore abelian as well. Consequently the commutator subgroup
$G'=[G,G]$ is contained in $P$. Since $P$ is abelian,
\[
G''=[G',G']=1.
\]
Thus $G$ is solvable.

By the Galois criterion for solvability by radicals, a polynomial over a field
of characteristic $0$ is solvable by radicals if and only if the Galois group
of its splitting field is solvable. Therefore
\[
\boxed{f(x)\text{ is solvable by radicals}.}
\]
:::
