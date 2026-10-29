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

::: {.problem}
Let $f(x) \in \QQ[x]$ be a polynomial and $K$ be a splitting field of $f$ over $\QQ$.
Assume that $[K:\QQ] = 1225$ and show that $f(x)$ is solvable by radicals.
:::

::: {.solution}

Let $G=\operatorname{Gal}(K/\QQ)$.

::: pf

::: pf-step

The group $G$ has a normal abelian subgroup $P$ of order $49$.


::: pf-proof

The splitting field is Galois in characteristic zero, so $|G|=1225=5^2\cdot7^2$. Sylow's theorems give $n_7\mid25$ and $n_7\equiv1\pmod7$. Among the divisors $1,5,25$ of $25$, only $1$ is congruent to $1$ modulo $7$. Hence the Sylow $7$-subgroup $P$ is unique and normal. Its order is $7^2$, so it is abelian.

:::

:::

::: {.pf-step #s1-2}

The group $G$ is solvable.


::: pf-proof

The quotient $G/P$ has order $25=5^2$ and is abelian. Hence the commutator subgroup $G'=[G,G]$ is contained in $P$. Because $P$ is abelian, $G''=[G',G']=1$. Thus the derived series terminates and $G$ is solvable.

:::

:::

::: {.pf-step #s1-3}

The polynomial $f$ is solvable by radicals.


::: pf-proof

The Galois criterion for solvability by radicals in characteristic zero states that a polynomial is solvable by radicals precisely when the Galois group of its splitting field is solvable. This applies by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} establishes the assertion.

:::

:::

:::
