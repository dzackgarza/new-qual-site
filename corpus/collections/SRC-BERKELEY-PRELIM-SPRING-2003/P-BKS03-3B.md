---
schema: qual/card@1
id: P-BKS03-3B
kind: problem
title: An entire function bounded below in real part is constant
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's proof into numbered steps; the exponential substitution, Liouville's
    theorem and the discreteness argument are unchanged, with the connectedness of C and the
    continuity of f named. Checked: the bound on |g|, the nonvanishing of g, and the discreteness
    of the fibre of the exponential. Not checked against a printed source: the Berkeley
    preliminary examinations are not retained in tmp/sources and the card records no page.
---

::: {.problem}
Let $f$ be entire and suppose
$$
\operatorname{Re}f(z)\ge-2
$$
for all $z\in\CC$.
Show that $f$ is constant.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f$ is entire with $\operatorname{Re}f(z)\geq-2$ for all $z$; the criteria used are Liouville's theorem and the continuity of $f$ on the connected set $\CC$.

::: pf

::: {.pf-step #bound}

$g(z)\coloneqq e^{-f(z)}$ is entire and $\abs{g(z)}\leq e^{2}$.

::: pf-proof

$g$ is a composite of entire functions, hence entire, and $\abs{g(z)}=e^{-\operatorname{Re}f(z)}\leq e^{2}$ because $\operatorname{Re}f(z)\geq-2$.

:::

:::

::: {.pf-step #const}

$g$ is constant, and the constant is nonzero.

::: pf-proof

Liouville's theorem applied to the bounded entire function $g$ of step [](#bound){.pf-ref}; $g=e^{-f}$ never vanishes, so its constant value $c$ is nonzero.

:::

:::

::: {.pf-step #discrete}

$f$ takes values in the discrete set $\log c+2\pi i\ZZ$.

::: pf-proof

If $e^{-f(z)}=c$ then $-f(z)$ is a logarithm of $c$, so $f(z)\in-\log c+2\pi i\ZZ$ for any fixed branch of the logarithm of $c$; that set is discrete, its points being at distance at least $2\pi$ apart.

:::

:::

::: {.pf-step #done}

$f$ is constant.

::: pf-proof

$f$ is continuous on the connected set $\CC$ and its image lies in the discrete set of step [](#discrete){.pf-ref}; a continuous image of a connected set is connected, and a connected subset of a discrete set is a single point.

:::

:::

:::

:::
