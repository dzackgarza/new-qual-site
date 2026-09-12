---
schema: qual/card@1
id: E-AMD-V3WFKTM6
kind: problem
title: $\maxspec(R)\subseteq\spec(R)$, with strict containment possible
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that $\maxspec(R) \subseteq \spec(R)$, and give an example where the containment is strict.
:::


::: {.solution}
<1>1. Every maximal ideal of $R$ is prime.
::: {.proof}
Let $\mathfrak m$ be a maximal ideal. Then $R/\mathfrak m$ is a field, hence an integral domain. Therefore $\mathfrak m$ is prime.
:::

<1>2. Hence $\maxspec(R)\subseteq\spec(R)$.
::: {.proof}
By definition, $\maxspec(R)$ is the set of maximal ideals and $\spec(R)$ is the set of prime ideals. The inclusion follows from <1>1.
:::

<1>3. The inclusion can be strict.
::: {.proof}
Take $R=\ZZ$. Since $\ZZ$ is an integral domain, $(0)$ is a prime ideal. It is not maximal because
\[
(0)\subsetneq (2)\subsetneq\ZZ.
\]
Thus
\[
(0)\in\spec(\ZZ)\setminus\maxspec(\ZZ),
\]
so $\maxspec(\ZZ)\subsetneq\spec(\ZZ)$.
:::

<1>4. Strictness is not automatic for every ring.
::: {.proof}
If $R=k$ is a field, then $(0)$ is its only proper ideal, and it is both prime and maximal. Hence
\[
\maxspec(k)=\spec(k)=\{(0)\}.
\]
:::
:::
