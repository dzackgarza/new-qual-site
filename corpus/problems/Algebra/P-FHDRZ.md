---
schema: qual/card@1
id: P-FHDRZ
kind: problem
title: The smallest extension of $\FF_q$ splitting every polynomial of degree at most $4$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let $f\in\FF_q[x]$ have degree at most $4$.
Find the smallest extension $\FF_{q^N}$ that is guaranteed to split every such polynomial completely.
:::

::: {.solution}

::: pf

::: {.pf-step #divides}
An irreducible polynomial over $\FF_q$ of degree $d$ splits over $\FF_{q^N}$ if and only if $d\mid N$.

::: pf-proof
A root $\alpha$ generates $\FF_q(\alpha)\cong\FF_{q^d}$, and $\FF_{q^d}\subseteq\FF_{q^N}$ if and only if $d\mid N$.
Since $\FF_{q^d}/\FF_q$ is normal, the polynomial splits over $\FF_{q^N}$ as soon as one root lies in it.
:::

:::

::: {.pf-step #suff}
Every polynomial of degree at most $4$ over $\FF_q$ splits over $\FF_{q^N}$ if and only if $1,2,3,4\mid N$.

::: pf-proof
The irreducible factors of such a polynomial have degrees in $\{1,2,3,4\}$, so divisibility by $1,2,3,4$ suffices by step [](#divides){.pf-ref}.
Conversely, irreducible polynomials of every degree exist over $\FF_q$, in particular of degrees $3$ and $4$, so step [](#divides){.pf-ref} forces $3\mid N$ and $4\mid N$.
:::

:::

::: pf-step
The smallest such extension is $\boxed{\FF_{q^{12}}}$.

::: pf-proof
By step [](#suff){.pf-ref}, the admissible $N$ are the multiples of $\lcm(1,2,3,4)=12$.
:::

:::

:::

:::
