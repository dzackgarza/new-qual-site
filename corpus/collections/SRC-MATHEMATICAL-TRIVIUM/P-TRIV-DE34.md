---
schema: qual/card@1
id: P-TRIV-DE34
kind: problem
title: $\int_{-\infty}^\infty \delta''(x-2)\frac{dx}{1+x^2}$
classification:
  areas: [prelim]
  topics:
  - Dirac Delta
  - Distributions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 34, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked by direct computation: pairing delta''(x-2) with
    the test function f(x) = 1/(1+x^2) gives f''(2) by the two integrations by parts that the delta
    derivative performs, and f''(x) = 2(3x^2-1)/(x^2+1)^3, so f''(2) = 2*11/125 = 22/125. That is
    the card's answer, and I confirmed the derivative and the value with a computer algebra system.
    The smoothness and decay hypotheses the pairing needs hold for this test function. Not claimed:
    any interpretation of delta'' beyond pairing with a smooth compactly supported function.
---

::: {.problem}
Compute $\int_{-\infty}^{\infty} \delta''(x - 2)\frac{1}{1 + x^2}\, \mathrm{d}x$.
:::

::: {.solution}

Set
$$
f(x)=\frac1{1+x^2}.
$$

::: pf

::: {.pf-step #s1-1}

The distributional derivative identity gives
$$
\int_{-\infty}^{\infty}\delta''(x-2)f(x)\,dx=f''(2).
$$


::: pf-proof

For a smooth test function $f$,
$$
\langle\delta_a^{(n)},f\rangle=(-1)^nf^{(n)}(a).
$$
Here $n=2$ and $a=2$, so the sign is positive.

:::

:::

::: {.pf-step #s1-2}

The second derivative of $f$ is
$$
f''(x)=\frac{6x^2-2}{(1+x^2)^3}.
$$


::: pf-proof

Differentiate twice:
$$
f'(x)=-\frac{2x}{(1+x^2)^2},
$$
and hence
$$
f''(x)=-\frac2{(1+x^2)^2}+\frac{8x^2}{(1+x^2)^3}
=\frac{6x^2-2}{(1+x^2)^3}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\int_{-\infty}^{\infty}\delta''(x-2)\frac{dx}{1+x^2}
=\frac{22}{125}}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
f''(2)=\frac{6\cdot4-2}{(1+4)^3}
=\frac{22}{125}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
