---
schema: qual/card@1
id: P-BERK91S-11
kind: problem
title: Convergence of $\sum (\sqrt{n+1}-\sqrt n)/n^x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared the summand, lower summation limit, and real parameter with Problem 11 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
For which real numbers $x$ does
$$
\sum_{n=1}^\infty\frac{\sqrt{n+1}-\sqrt n}{n^x}
$$
converge?
:::

::: {.solution}
Fix $x\in\RR$, and put $p\coloneqq x+\tfrac12$. For each
integer $n\ge1$, let
$$
a_n\coloneqq\frac{\sqrt{n+1}-\sqrt n}{n^x}.
$$

::: pf

::: {.pf-step #s1}

For every $n\ge1$,
$$
\frac{1}{1+\sqrt2}\frac{1}{n^p}
\le a_n\le\frac12\frac{1}{n^p}.
$$

::: pf-proof

Rationalizing the numerator gives
$$
a_n
=\frac{1}{n^x(\sqrt{n+1}+\sqrt n)}
=\frac{1}{n^p(\sqrt{1+1/n}+1)}.
$$
Since $1\le\sqrt{1+1/n}\le\sqrt2$, its denominator satisfies
the bounds in the claim. All factors are positive for every
real $x$.

:::

:::

::: {.pf-step #s2}

The series converges precisely for $\boxed{x>\tfrac12}$.

::: pf-proof

The $p$-series criterion states that $\sum_{n=1}^{\infty}n^{-p}$
converges if and only if $p>1$. If $x>\tfrac12$, then $p>1$,
so the upper bound in step [](#s1){.pf-ref} and the
[[PR-P6NHI|comparison test]] prove convergence.
If $x\le\tfrac12$, then $p\le1$, so the lower bound and the
[[PR-P6NHI|comparison test]] prove divergence. This includes
$x=\tfrac12$, for which the lower bound is a positive constant
multiple of the harmonic-series summand.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} determines convergence for every real parameter $x$.

:::

:::

:::
