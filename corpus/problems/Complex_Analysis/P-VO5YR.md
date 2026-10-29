---
schema: qual/card@1
id: P-VO5YR
kind: problem
title: Invert $\sin(z)$ using geometric series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Trigonometry
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Invert $\sin(z)$ using a geometric series, heeding the warning above.", referring to a warning earlier in the source that the series of sin z has zero constant term; the statement now states that point and asks for the Laurent expansion at 0.'
---

::: {.exercise}
The power series of $\sin(z)$ at $0$ has zero constant term, so it cannot be inverted directly as a power series.
Invert $\sin(z)$ using a geometric series: find the Laurent expansion of $1/\sin(z)$ at $0$ through the $z^3$ term.
:::

::: {.solution}
Write $\sin z = z\qty(1 - p(z))$ with $p(z) \coloneqq \frac{z^2}{3!} - \frac{z^4}{5!} + \bigo(z^6)$.

::: pf

::: {.pf-step #geom}

$\dfrac{1}{1 - p(z)} = 1 + \dfrac{1}{6}z^2 + \dfrac{7}{360}z^4 + \bigo(z^6)$ near $0$.

::: pf-proof

Since $p(z) = \bigo(z^2)$, $\abs{p(z)} < 1$ near $0$ and the geometric series gives $\frac{1}{1-p} = 1 + p + p^2 + \bigo(z^6)$. Here $p^2 = \frac{z^4}{36} + \bigo(z^6)$, so the coefficient of $z^4$ is $-\frac{1}{120} + \frac{1}{36} = \frac{-3 + 10}{360} = \frac{7}{360}$.

:::

:::

::: pf-step

$\dfrac{1}{\sin z} = \boxed{\dfrac{1}{z} + \dfrac{1}{6}z + \dfrac{7}{360}z^3 + \bigo(z^5)}$.

::: pf-proof

Divide step [](#geom){.pf-ref} by $z$.

:::

:::

:::

:::
