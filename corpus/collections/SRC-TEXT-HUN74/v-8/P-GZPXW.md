---
schema: qual/card@1
id: P-GZPXW
kind: problem
title: Degree of the maximal real cyclotomic subfield
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Number Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction of the Hungerford exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $n>2$ and $\zeta$ is a primitive $n$th root of unity over $\mathbb{Q}$, then $[\mathbb{Q}(\zeta + \zeta^{-1}): \mathbb{Q}]=\phi(n)/2.$
:::

::: {.solution}
Put
\[
L=\QQ(\zeta),
\qquad
L^+=\QQ(\zeta+\zeta^{-1}).
\]

::: pf

::: {.pf-step #s1}

One has
\[
[L:\QQ]=\phi(n).
\]

::: pf-proof

The minimal polynomial of a primitive $n$th root of unity over $\QQ$ is the
$n$th cyclotomic polynomial $\Phi_n(x)$, whose degree is $\phi(n)$. Hence
\[
[\QQ(\zeta):\QQ]=\deg\Phi_n=\phi(n).
\]

:::

:::

::: {.pf-step #s2}

The element $\zeta$ is algebraic of degree at most $2$ over $L^+$.

::: pf-proof

Let
\[
t=\zeta+\zeta^{-1}\in L^+.
\]
Then $\zeta$ satisfies
\[
x^2-tx+1=0,
\]
so
\[
[L:L^+]\le2.
\]

:::

:::

::: {.pf-step #s3}

The field $L^+$ is contained in $\RR$, whereas $\zeta\notin\RR$.

::: pf-proof

Since
\[
\zeta+\zeta^{-1}=2\cos(2\pi/n),
\]
the generator of $L^+$ is real, so $L^+\subseteq\RR$.

If a primitive $n$th root of unity is real, it must be $1$ or $-1$, whose
orders are $1$ and $2$. Since $n>2$, the primitive root $\zeta$ is not real.
Thus $\zeta\notin L^+$.

:::

:::

::: {.pf-step #s4}

Therefore
\[
[L:L^+]=2.
\]

::: pf-proof

By step [](#s2){.pf-ref} the degree is at most $2$. By step [](#s3){.pf-ref} the inclusion $L^+\subsetneq L$ is
proper, so the degree is not $1$.

:::

:::

::: pf-step

Hence
\[
[\QQ(\zeta+\zeta^{-1}):\QQ]=\frac{\phi(n)}2.
\]

::: pf-proof

The tower law and steps [](#s1){.pf-ref} and [](#s4){.pf-ref} give
\[
\phi(n)=[L:\QQ]=[L:L^+][L^+:\QQ]=2[L^+:\QQ].
\]
Solving for $[L^+:\QQ]$ gives the asserted degree.

:::

:::

:::

:::
