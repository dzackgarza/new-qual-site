---
schema: qual/card@1
id: E-0SFDE
kind: problem
title: The line as a countable union of sets with empty interior
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

The Baire category theorem implies that $\RR$ cannot be written as a countable union of closed subsets having empty interiors.
Show this fails if the sets are not required to be closed.
:::

::: {.solution}

::: pf

::: pf-step

Construction of the partition:
    1. Let $\QQ$ be the set of rational numbers in $\RR$. Since $\QQ$ is countably infinite, choose an enumeration $\QQ = \{q_1, q_2, q_3, \dots\}$.
    2. Let $A_0 = \RR \setminus \QQ$ be the set of all irrational numbers.
    3. For each $n \in \ZZ_+$, let $A_n = \{q_n\}$.
    4. Then $\bigcup_{n=0}^\infty A_n = (\RR \setminus \QQ) \cup \bigcup_{n=1}^\infty \{q_n\} = (\RR \setminus \QQ) \cup \QQ = \RR$.

:::

::: pf-step

Each singleton $A_n = \{q_n\}$ has empty interior for $n \ge 1$:
    *Proof:* Every non-empty open subset of $\RR$ contains an open interval $(a, b)$ with $a < b$, which contains uncountably many points. Since $A_n$ contains exactly one point, $A_n$ contains no open interval. Thus $\operatorname{Int}(A_n) = \emptyset$.

:::

::: pf-step

The set of irrationals $A_0 = \RR \setminus \QQ$ has empty interior:
    *Proof:* If $\operatorname{Int}(\RR \setminus \QQ) \neq \emptyset$, it would contain a non-empty open interval $(a, b)$ with $a < b$. By the density of $\QQ$ in $\RR$, there exists a rational number $q \in (a, b) \subset \RR \setminus \QQ$, which contradicts $q \in \QQ$. Thus $\operatorname{Int}(A_0) = \emptyset$.

:::

::: pf-step

$A_0$ is not closed in $\RR$:
    *Proof:* By the density of the irrationals in $\RR$, the closure of $A_0 = \RR \setminus \QQ$ is $\overline{\RR \setminus \QQ} = \RR \neq A_0$.

:::

:::

    By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\RR = \bigcup_{n=0}^\infty A_n$ is a countable union of subsets with empty interior, and by step [](#s4){.pf-ref} the set $A_0$ is not closed.
:::
