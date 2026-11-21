---
schema: qual/card@1
id: P-HGRO18
kind: problem
title: A normal subgroup of order $11$ in a group of order $99$
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Checked n_11 = 1 by listing the divisors of 9 (1, 3, 9) and their residues modulo 11, and checked that the uniqueness argument is not vacuous: Sylow's theorem supplies at least one Sylow 11-subgroup, and 11^2 does not divide 99. The normality step is now the conjugation argument rather than the bare word "hence normal". No retained solution set covers the question (the provenance is the oral-question extraction, which has no worked answers), and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $G$ be a group of order $99$.
Must $G$ have a normal subgroup of order $11$?
Justify your answer.
:::

::: {.solution}
Yes. No retained solution set covers this oral question: the collection's provenance is the Harvard group-theory oral-question extraction, which holds the question and no worked answer. The argument is the card's own and is Sylow's theorem applied twice.

Write $n_p$ for the number of Sylow $p$-subgroups of $G$.

::: pf

::: {.pf-step #order}
$\cardinality{G}=99=3^2\cdot11$.

::: pf-proof
$3^2\cdot11=9\cdot11=99$.
:::

:::

::: {.pf-step #sylow}
$n_{11}\ge1$, $n_{11}\equiv1\pmod{11}$ and $n_{11}\divides9$.

::: pf-proof
$11$ is prime and $11$ divides $\cardinality{G}$ while $11^2$ does not, so a Sylow $11$-subgroup of $G$ exists and has order $11$; $n_{11}$ is by definition the number of them, so $n_{11}\ge1$. Sylow's theorem gives $n_{11}\equiv1\pmod{11}$ and that $n_{11}$ is the index of the normalizer of a Sylow $11$-subgroup, hence divides $\cardinality{G}/11=9$ by step [](#order){.pf-ref}.
:::

:::

::: {.pf-step #divisors}
The positive divisors of $9$ are $1,3,9$, and only $1$ is congruent to $1$ modulo $11$.

::: pf-proof
$9=3^2$, so its positive divisors are $3^0,3^1,3^2$, that is $1,3,9$. Now $1=0\cdot11+1$, while $3=0\cdot11+3$ and $9=0\cdot11+9$ have remainders $3$ and $9$, neither equal to $1$.
:::

:::

::: {.pf-step #unique}
$G$ has exactly one Sylow $11$-subgroup.

::: pf-proof
$n_{11}$ is a positive divisor of $9$ congruent to $1$ modulo $11$ by step [](#sylow){.pf-ref}, and step [](#divisors){.pf-ref} leaves $n_{11}=1$ as the only possibility.
:::

:::

::: {.pf-step #normal}
The unique Sylow $11$-subgroup $P$ of $G$ is normal in $G$ and has order $11$.

::: pf-proof
For $g\in G$ the set $gPg^{-1}$ is a subgroup of order $\cardinality{P}=11$, hence a Sylow $11$-subgroup; by step [](#unique){.pf-ref} it equals $P$. So $gPg^{-1}=P$ for every $g$, which is normality of $P$. Its order is $11$ because it is a Sylow $11$-subgroup and $11^2$ does not divide $99$.
:::

:::

::: {.pf-step}
The answer is yes: $G$ has a normal subgroup of order $11$.

::: pf-proof
Step [](#normal){.pf-ref} exhibits one, the unique Sylow $11$-subgroup.
:::

:::

:::
:::
