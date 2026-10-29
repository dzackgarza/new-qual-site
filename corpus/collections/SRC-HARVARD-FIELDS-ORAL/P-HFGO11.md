---
schema: qual/card@1
id: P-HFGO11
kind: problem
title: Degree of the algebraic closure of the rationals
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Determine $[\overline{\QQ}:\QQ]$.
:::

::: {.solution}
One has
$$
[\overline{\QQ}:\QQ]=\infty.
$$

::: pf

::: {.pf-step #s1}

For every integer $n\ge1$, the field $\overline{\QQ}$ contains a finite extension of $\QQ$ of degree $n$.

::: pf-proof

The polynomial $x^n-2\in\QQ[x]$ is irreducible by Eisenstein's criterion at $2$. Hence, for any root $\alpha_n\in\overline{\QQ}$,
$$
[\QQ(\alpha_n):\QQ]=n.
$$

:::

:::

::: pf-step

Therefore $[\overline{\QQ}:\QQ]$ is infinite.

::: pf-proof

If $[\overline{\QQ}:\QQ]=N<\infty$, then every intermediate finite extension $K/\QQ$ would satisfy
$$
[K:\QQ]\le N.
$$
Taking $K=\QQ(\alpha_n)$ with $n>N$ contradicts step [](#s1){.pf-ref}.

:::

:::

:::

:::
