---
schema: qual/card@1
id: P-FPWNW
kind: problem
title: Groups of order $p^2$ are abelian; the Sylow theorems; groups of order $4225=5^2
  13^2$ are abelian, with their isomorphism classes
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
a. Show that every group of order $p^2$ with $p$ prime is abelian.

b. State the 3 Sylow theorems.

c. Show that any group of order $4225 = 5^2 13^2$ is abelian.

d. Write down one representative from each isomorphism class of abelian groups of order 4225.
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #center-nontrivial}
Let $G$ have order $p^2$. Then $Z(G) \neq 1$ (a $p$-group has nontrivial center).

::: pf-proof
class equation.
:::

:::

::: {.pf-step #quotient-order}
$G/Z(G)$ has order $1$ or $p$ (since $|Z(G)|$ is $p$ or $p^2$).

::: pf-proof
Step [](#center-nontrivial){.pf-ref} and Lagrange.
:::

:::

::: {.pf-step #cyclic-quotient-abelian}
If $|G/Z(G)| = p$, then $G/Z(G)$ is cyclic, which forces $G$ abelian (a group with cyclic center quotient is abelian).

::: pf-proof
standard fact.
:::

:::

::: {.pf-step #trivial-quotient-abelian}
If $|G/Z(G)| = 1$, then $G = Z(G)$ is abelian.

::: pf-proof
Step [](#quotient-order){.pf-ref}.
:::

:::

::: {.pf-step #part-a-conclusion}
Hence $G$ is abelian.

::: pf-proof
Step [](#cyclic-quotient-abelian){.pf-ref} and step [](#trivial-quotient-abelian){.pf-ref}.
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #part-b-sylow-statement}
**Sylow 1:** For each prime $p$ dividing $|G|$, there is a Sylow $p$-subgroup.
**Sylow 2:** All Sylow $p$-subgroups are conjugate, and the number $n_p$ satisfies $n_p \equiv 1 \pmod p$ and $n_p \mid |G|$.
**Sylow 3:** $n_p \equiv 1 \pmod p$ and $n_p$ divides $|G|/p^a$ (where $p^a$ is the largest power of $p$ dividing $|G|$).

::: pf-proof
statement of the Sylow theorems.
:::

:::

:::

**(c).**

::: pf

::: pf-step
Let $G$ have order $4225 = 5^2 \cdot 13^2$. By Sylow, $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 13^2 = 169$, so $n_5 \in \{1, 169\}$.

::: pf-proof
Sylow's theorem.
:::

:::

::: {.pf-step #n13-equals-one}
$n_{13} \equiv 1 \pmod{13}$ and $n_{13} \mid 25$, so $n_{13} = 1$.

::: pf-proof
Sylow's theorem (the divisors of $25$ are $1, 5, 25$, and only $1 \equiv 1 \pmod{13}$).
:::

:::

::: {.pf-step #unique-sylow-13}
Hence $G$ has a unique normal Sylow $13$-subgroup $P \cong \ZZ/13^2$ or $\ZZ/13 \times \ZZ/13$.

::: pf-proof
Step [](#n13-equals-one){.pf-ref}.
:::

:::

::: {.pf-step #n5-equals-one}
The normal subgroup $P$ acts by conjugation on the Sylow $5$-subgroups, so $n_5$ divides $|P| = 169$ and $n_5 \equiv 1 \pmod 5$; the only such divisor is $n_5 = 1$.

::: pf-proof
Step [](#unique-sylow-13){.pf-ref} and Sylow (the orbit sizes divide $169$, and $n_5 \equiv 1 \pmod 5$ forces $n_5 = 1$).
:::

:::

::: {.pf-step #unique-sylow-5-and-13}
Hence $G$ has a unique normal Sylow $5$-subgroup $Q$ and a unique normal Sylow $13$-subgroup $P$, so $G = P \times Q$.

::: pf-proof
Step [](#unique-sylow-13){.pf-ref} and step [](#n5-equals-one){.pf-ref}.
:::

:::

::: {.pf-step #part-c-conclusion}
$P$ and $Q$ are abelian (groups of order $p^2$ are abelian by (a)), so $G = P \times Q$ is abelian.

::: pf-proof
Step [](#unique-sylow-5-and-13){.pf-ref} and (a).
:::

:::

:::

**(d).**

::: pf

::: {.pf-step #abelian-groups-as-products}
The abelian groups of order $4225 = 5^2 \cdot 13^2$ are the products of abelian groups of order $5^2$ and $13^2$.

::: pf-proof
fundamental theorem of finite abelian groups.
:::

:::

::: {.pf-step #abelian-groups-of-prime-square-order}
The abelian groups of order $5^2$ are $\ZZ/25$ and $\ZZ/5 \times \ZZ/5$; the abelian groups of order $13^2$ are $\ZZ/169$ and $\ZZ/13 \times \ZZ/13$.

::: pf-proof
fundamental theorem.
:::

:::

::: {.pf-step #part-d-isomorphism-classes}
Hence the four isomorphism classes are:
$$\ZZ/25 \times \ZZ/169,\ \ZZ/25 \times \ZZ/13 \times \ZZ/13,\ \ZZ/5 \times \ZZ/5 \times \ZZ/169,\ \ZZ/5 \times \ZZ/5 \times \ZZ/13 \times \ZZ/13.$$

::: pf-proof
Step [](#abelian-groups-as-products){.pf-ref} and step [](#abelian-groups-of-prime-square-order){.pf-ref}.
:::

:::

::: pf-qed
Step [](#part-a-conclusion){.pf-ref} (a), step [](#part-b-sylow-statement){.pf-ref} (b), step [](#part-c-conclusion){.pf-ref} (c), step [](#part-d-isomorphism-classes){.pf-ref} (d).
:::

:::

:::
