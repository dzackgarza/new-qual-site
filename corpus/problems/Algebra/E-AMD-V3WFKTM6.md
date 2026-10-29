---
schema: qual/card@1
id: E-AMD-V3WFKTM6
kind: problem
title: $\mspec(R)\subseteq\Spec(R)$, with strict containment possible
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Ideals
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
Let $R$ be a commutative ring with identity. Show that every maximal ideal of $R$ is prime, that is, $\mspec(R) \subseteq \Spec(R)$, and give an example of a prime ideal that is not maximal, so that the containment is strict.
:::


::: {.solution}

::: pf

::: {.pf-step #maximal-implies-prime}
Every maximal ideal of $R$ is prime.

::: pf-proof
Let $\mathfrak m$ be a maximal ideal. Then $R/\mathfrak m$ is a field, hence an integral domain. Therefore $\mathfrak m$ is prime.
:::

:::

::: pf-step
Hence $\mspec(R)\subseteq\Spec(R)$.

::: pf-proof
By definition, $\mspec(R)$ is the set of maximal ideals and $\Spec(R)$ is the set of prime ideals. The inclusion follows from step [](#maximal-implies-prime){.pf-ref}.
:::

:::

::: pf-step
The inclusion can be strict.

::: pf-proof
Take $R=\ZZ$. Since $\ZZ$ is an integral domain, $(0)$ is a prime ideal. It is not maximal because
$$
(0)\subsetneq (2)\subsetneq\ZZ.
$$
Thus
$$
(0)\in\Spec(\ZZ)\setminus\mspec(\ZZ),
$$
so $\mspec(\ZZ)\subsetneq\Spec(\ZZ)$.
:::

:::

:::

:::

::: {.remark}
Strictness is not automatic for every ring. If $R=k$ is a field, then $(0)$ is its only proper ideal, and it is both prime and maximal. Hence
$$
\mspec(k)=\Spec(k)=\{(0)\}.
$$
:::

::: {.remark title="Elementwise proof"}
Let $\mm$ be maximal, and suppose $ab\in \mm$ and $b\notin \mm$. Then $\mm \subsetneq \mm + (b)$, so $\mm + (b) = R$. Write $1 = m + rb$ with $m\in\mm$ and $r\in R$. Then $a = am + r(ab)\in\mm$, so $\mm$ is prime.
:::
