---
schema: qual/card@1
id: P-TRIV-PR10
kind: problem
title: Buffon's needle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
”Buffon’s needle” A needle of length l is thrown randomly on a plane lined with parallel lines with distance d between them, $l < d .$ Find the probability that the needle will cross some line.
:::

::: {.solution}

Let $X$ be the distance from the needle's center to the nearest parallel line, and let $\Theta$ be the acute angle between the needle and the lines. Under the usual uniform random-throw model,
$$
X\sim\operatorname{Unif}[0,d/2],
\qquad
\Theta\sim\operatorname{Unif}[0,\pi/2],
$$
independently.

::: pf

::: {.pf-step #s1-1}

The needle crosses a line exactly when
$$
X\leq\frac l2\sin\Theta.
$$


::: pf-proof

The component of half the needle length perpendicular to the parallel lines is $(l/2)\sin\Theta$. A crossing occurs precisely when this perpendicular reach is at least the center's distance to the nearest line.

:::

:::

::: {.pf-step #s1-2}

For a fixed angle $\theta$, the conditional crossing probability is
$$
P(\text{cross}\mid\Theta=\theta)
=\frac{(l/2)\sin\theta}{d/2}
=\frac ld\sin\theta.
$$


::: pf-proof

Because $l<d$, one has $(l/2)\sin\theta<d/2$, so step [](#s1-1){.pf-ref} selects an interval of $X$ of length $(l/2)\sin\theta$ inside the uniform interval $[0,d/2]$.

:::

:::

::: {.pf-step #s1-3}

Averaging over the uniformly distributed angle gives
$$
P(\text{cross})
=\frac2\pi\int_0^{\pi/2}\frac ld\sin\theta\,d\theta.
$$


::: pf-proof

The density of $\Theta$ on $[0,\pi/2]$ is $2/\pi$. Apply the law of total probability to the conditional probability in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{P(\text{cross})=\frac{2l}{\pi d}}.
$$


::: pf-proof

Since $\int_0^{\pi/2}\sin\theta\,d\theta=1$, step [](#s1-3){.pf-ref} evaluates to $2l/(\pi d)$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives Buffon's needle crossing probability for $l<d$.

:::

:::

:::
