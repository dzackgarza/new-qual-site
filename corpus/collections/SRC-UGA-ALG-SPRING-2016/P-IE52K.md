---
schema: qual/card@1
id: P-IE52K
kind: problem
title: Sylow theorems, and groups of order 1225
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a. State the three Sylow theorems.

b. Prove that any group of order 1225 is abelian.

c. Write down exactly one representative in each isomorphism class of abelian groups of order 1225.
:::

::: pf

::: pf-step

The three Sylow theorems are existence, conjugacy and containment, and enumeration.


::: pf-proof

For a finite group $G$ and prime $p$, write $|G|=p^am$ with $p\nmid m$. (i) There is a subgroup of order $p^a$. (ii) Every $p$-subgroup is contained in one of these Sylow $p$-subgroups, and any two Sylow $p$-subgroups are conjugate. (iii) Their number $n_p$ divides $m$ and satisfies $n_p\equiv1\pmod p$.

:::

:::

::: pf-step

Every group $G$ of order $1225$ is abelian.


::: pf-proof

Since $1225=5^2 7^2$, the Sylow theorems give $n_7\mid25$ and $n_7\equiv1\pmod7$. Of the divisors $1,5,25$, only $1$ satisfies the congruence. Similarly, $n_5\mid49$ and $n_5\equiv1\pmod5$, and of $1,7,49$ only $1$ qualifies. Hence the Sylow subgroups $P_5,P_7$ are normal. Their intersection is trivial, and their orders multiply to $|G|$, so $G=P_5P_7$. For $x\in P_5$ and $y\in P_7$, normality gives $[x,y]\in P_5\cap P_7=\{1\}$, making the product direct: $G\cong P_5\times P_7$. Both factors have prime-square order and are therefore abelian (their centers are nontrivial and the quotient by the center, when nontrivial, is cyclic). Thus $G$ is abelian.

:::

:::

::: pf-step

The complete list of isomorphism classes of groups of order $1225$ is
\[
\boxed{\begin{gathered}
C_{25}\times C_{49},\qquad C_{25}\times C_7\times C_7,\\
C_5\times C_5\times C_{49},\qquad
C_5\times C_5\times C_7\times C_7.
\end{gathered}}
\]


::: pf-proof

By step <1>2 every such group is abelian. The classification of finite abelian groups gives precisely two possibilities for its Sylow $5$-subgroup, $C_{25}$ or $C_5^2$, and precisely two for its Sylow $7$-subgroup, $C_{49}$ or $C_7^2$. Their independent products give the four displayed types, which are pairwise nonisomorphic because their primary components are nonisomorphic.

:::

:::

::: pf-qed

Steps <1>1, <1>2, and <1>3 answer parts (a), (b), and (c).

:::

:::
