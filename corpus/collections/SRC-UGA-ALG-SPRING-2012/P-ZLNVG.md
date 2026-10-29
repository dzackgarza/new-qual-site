---
schema: qual/card@1
id: P-ZLNVG
kind: problem
title: No simple group of order $70$, and three nonisomorphic groups of that order
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a group of order 70.

a. Show that $G$ is not simple.

b. Exhibit 3 nonisomorphic groups of order 70 and prove that they are not isomorphic.
:::

::: {.solution}

Let $D_{2n}$ denote the dihedral group of order $2n$.

::: pf

::: {.pf-step #s1-1}

Every group $G$ of order $70$ is nonsimple.


::: pf-proof

The number $n_5$ of Sylow $5$-subgroups divides $14$ and is congruent to $1$ modulo $5$. The divisors $1,2,7,14$ of $14$ leave only $1$ satisfying the congruence. Thus the Sylow $5$-subgroup is unique and normal. It has order $5$, so is proper and nontrivial.

:::

:::

::: {.pf-step #s1-2}

Three groups of order $70$ are
$$
\boxed{C_{70},\quad D_{70},\quad C_5\times D_{14}}.
$$


::: pf-proof

The cyclic group $C_{70}$ has order $70$. The dihedral group $D_{70}$ has order $2\cdot35=70$, and the direct product $C_5\times D_{14}$ has order $5\cdot14=70$.

:::

:::

::: {.pf-step #s1-3}

The three groups in step [](#s1-2){.pf-ref} are pairwise nonisomorphic.


::: pf-proof

The group $C_{70}$ is abelian, whereas both dihedral groups $D_{70}$ and $D_{14}$ are nonabelian, so the latter property holds for their indicated direct product as well. For odd $n\geq3$, the center of $D_{2n}$ is trivial: a central rotation $r^j$ must satisfy $r^{2j}=1$, giving $j\equiv0\pmod n$, and a reflection does not commute with $r$. Consequently $Z(D_{70})=1$, while $Z(C_5\times D_{14})=C_5\times Z(D_{14})\cong C_5$. Their centers have different orders, so they are not isomorphic.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} prove part (b).

:::

:::

:::
