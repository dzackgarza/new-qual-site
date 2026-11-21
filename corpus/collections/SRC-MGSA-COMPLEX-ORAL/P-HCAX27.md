---
schema: qual/card@1
id: P-HCAX27
kind: problem
title: Riemann hypothesis
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's statement into numbered steps: the continuation, the trivial zeros, the
    critical strip and the hypothesis itself are unchanged in content. This card states a
    conjecture, so nothing is proved; the steps record which standard facts locate the zeros.
    Checked: that the stated form is the usual one — all nontrivial zeros on the critical line —
    and that the trivial zeros are excluded from its scope. Not checked against a printed source:
    no source for the oral examination list is retained in tmp/sources, and the card records no
    page.
---

::: {.problem}
State the Riemann hypothesis.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $\zeta$ is the Riemann zeta function and the statement asked for is the Riemann hypothesis itself; the two facts about the zeros used to locate it are part of the standard theory and are stated, not proved.

::: pf

::: {.pf-step #cont}

$\zeta$ continues meromorphically to $\CC$ with a simple pole at $s=1$ and no other pole.

::: pf-proof

This is the standard meromorphic continuation of $\sum_{n\geq1}n^{-s}$ from $\operatorname{Re}s>1$.

:::

:::

::: {.pf-step #trivial}

The zeros of $\zeta$ outside the closed strip $0\leq\operatorname{Re}s\leq1$ are exactly $s=-2,-4,-6,\dots$.

::: pf-proof

The functional equation relates $\zeta(s)$ to $\zeta(1-s)$ and supplies the trivial zeros at the negative even integers; there are no zeros with $\operatorname{Re}s>1$ because the Dirichlet series has a nowhere-vanishing Euler product there.

:::

:::

::: {.pf-step #strip}

Every remaining zero lies in the critical strip $0<\operatorname{Re}s<1$.

::: pf-proof

Steps [](#cont){.pf-ref} and [](#trivial){.pf-ref} exclude the closed half-planes and the trivial zeros; a zero in the strip cannot lie on $\operatorname{Re}s=1$ or $\operatorname{Re}s=0$ by the nonvanishing of $\zeta$ on those lines.

:::

:::

::: {.pf-step #rh}

The Riemann hypothesis: every zero of $\zeta$ with $0<\operatorname{Re}s<1$ satisfies $\operatorname{Re}s=\tfrac12$.

::: pf-proof

This is the statement to be made; steps [](#cont){.pf-ref} to [](#strip){.pf-ref} identify the zeros it concerns.

:::

:::

:::

:::
