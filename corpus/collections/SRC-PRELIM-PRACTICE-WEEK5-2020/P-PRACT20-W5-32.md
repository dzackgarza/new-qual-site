---
schema: qual/card@1
id: P-PRACT20-W5-32
kind: problem
title: Laurent expansions of $\frac1{z(z^2+1)}$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 32).
---

::: {.problem}
Find two different Laurent expansions for $f(z) = \frac{1}{z(z^2 + 1)}$ and specify the regions in which they converge.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
0<|z|<1,
$$
one has
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}(-1)^n z^{2n-1}
=
\frac1z-z+z^3-z^5+\cdots }.
$$


::: pf-proof

When $|z|<1$, the geometric series gives
$$
\frac1{1+z^2}
=
\sum_{n=0}^{\infty}(-1)^n z^{2n}.
$$
Multiplying by $1/z$ yields
$$
\frac1{z(1+z^2)}
=
\sum_{n=0}^{\infty}(-1)^n z^{2n-1}.
$$
The center $z=0$ is a pole, so the region of convergence is the punctured
disk $0<|z|<1$.

:::

:::

::: {.pf-step #s1-2}

For
$$
|z|>1,
$$
one has
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}(-1)^n z^{-2n-3}
=
\frac1{z^3}-\frac1{z^5}+\frac1{z^7}-\cdots }.
$$


::: pf-proof

Rewrite
$$
f(z)
=
\frac1{z^3}\frac1{1+z^{-2}}.
$$
When $|z|>1$, one has $|z^{-2}|<1$, so the geometric series gives
$$
\frac1{1+z^{-2}}
=
\sum_{n=0}^{\infty}(-1)^n z^{-2n}.
$$
Multiplying by $z^{-3}$ gives the displayed Laurent series. It converges
exactly for $|z|>1$.

:::

:::

::: pf-step

The two Laurent expansions are therefore separated by the circle
$$
|z|=1,
$$
which contains the additional poles $z=\pm i$.


::: pf-proof

The singularities of $f$ are
$$
0,\qquad i,\qquad -i.
$$
Thus the maximal annuli centered at $0$ on which $f$ is holomorphic are
$0<|z|<1$ and $|z|>1$, exactly the regions in steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the two requested Laurent expansions and their
regions of convergence.

:::

:::

:::
