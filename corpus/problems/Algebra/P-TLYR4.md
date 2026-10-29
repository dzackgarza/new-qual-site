---
schema: qual/card@1
id: P-TLYR4
kind: problem
title: Finite-dimensional division algebras over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Semisimplicity
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Classify all finite-dimensional (associative) division algebras over the field of real numbers $\RR$ (Frobenius' Theorem).
:::

::: {.solution}
Let $D$ be a finite-dimensional associative division algebra over $\RR$ with center $Z$.

::: pf

::: {.pf-step #center}
$Z\cong\RR$ or $Z\cong\CC$.

::: pf-proof
$Z$ is a commutative division algebra, hence a field, and it is a finite extension of $\RR$.
:::

:::

::: {.pf-step #complex-center}
If $Z\cong\CC$, then $D=\CC$.

::: pf-proof
For $x\in D$, the subalgebra $\CC[x]$ is commutative, finite-dimensional, and has no zero divisors, so it is a finite field extension of $\CC$.
Since $\CC$ is algebraically closed, $\CC[x]=\CC$, so $x\in\CC$.
:::

:::

::: {.pf-step #real-center}
If $Z\cong\RR$, then $D\cong\RR$ or $D\cong\HH$.

::: pf-proof
Then $D$ is a central division algebra over $\RR$, so it defines a class in $\operatorname{Br}(\RR)\cong\ZZ/2\ZZ$, whose two classes are those of $\RR$ and of the Hamilton quaternions $\HH$.
Each Brauer class contains exactly one division algebra up to isomorphism, so $D\cong\RR$ or $D\cong\HH$.
:::

:::

::: pf-step
Every finite-dimensional associative division algebra over $\RR$ is isomorphic to exactly one of $\boxed{\RR,\ \CC,\ \HH}$.

::: pf-proof
Steps [](#center){.pf-ref}, [](#complex-center){.pf-ref} and [](#real-center){.pf-ref} show that $D$ is one of these.
They are pairwise non-isomorphic, since their real dimensions are $1$, $2$ and $4$.
:::

:::

:::

:::
