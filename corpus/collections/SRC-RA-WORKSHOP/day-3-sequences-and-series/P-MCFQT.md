---
schema: qual/card@1
id: P-MCFQT
kind: problem
title: $\sqrt{n}(\sqrt{n+1}-\sqrt{n})\to\frac12$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $a_n =\sqrt{n}\left(\sqrt{n+1}-\sqrt{n}\right)$.
Prove that $\lim_{n\to\infty}a_n=1/2$.
:::
::: {.solution}

::: pf

::: pf-step

$a_n = \sqrt{n}(\sqrt{n+1} - \sqrt{n}) = \sqrt{n}\cdot\frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{\sqrt{n}}{\sqrt{n+1} + \sqrt{n}}$.

::: pf-proof

rationalize: $\sqrt{n+1} - \sqrt{n} = \frac{(n+1)-n}{\sqrt{n+1}+\sqrt{n}}$.

:::

:::

::: {.pf-step #s2}

$a_n = \dfrac{1}{\frac{\sqrt{n+1}}{\sqrt{n}} + 1} = \dfrac{1}{\sqrt{1 + 1/n} + 1}$.

::: pf-proof

divide numerator and denominator by $\sqrt{n}$.

:::

:::

::: {.pf-step #s3}

$\sqrt{1 + 1/n} \to 1$ as $n \to \infty$.

::: pf-proof

continuity of the square root and $1 + 1/n \to 1$ (or the standard squeeze $1 \le \sqrt{1+1/n} \le 1 + 1/(2n)$-style bound).

:::

:::

::: pf-qed

: $a_n \to \dfrac{1}{1 + 1} = \dfrac{1}{2}$.

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, by the quotient law for limits.

:::

:::

:::
