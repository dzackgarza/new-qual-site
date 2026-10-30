---
schema: qual/card@1
id: P-HFGO2
kind: problem
title: A sum of algebraic numbers is algebraic
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $\alpha$ and $\beta$ are algebraic over $\QQ$, prove that $\alpha+\beta$ is algebraic over $\QQ$.
:::

::: {.solution}
Set
$$
K=\QQ(\alpha,\beta).
$$

::: pf

::: pf-step

The extension $K/\QQ$ is finite.

::: pf-proof

Since $\alpha$ is algebraic over $\QQ$,
$$
[\QQ(\alpha):\QQ]<\infty.
$$
The element $\beta$ is algebraic over $\QQ$, hence also algebraic over
the larger field $\QQ(\alpha)$. Therefore
$$
[K:\QQ(\alpha)]<\infty.
$$
By the tower law,
$$
[K:\QQ]
=[K:\QQ(\alpha)]
[\QQ(\alpha):\QQ]
<\infty.
$$

:::

:::

::: {.pf-step #s2}

Every element of the finite extension $K/\QQ$ is algebraic over
$\QQ$.

::: pf-proof

Let $\gamma\in K$. If $d=[K:\QQ]$, then the $d+1$ elements
$$
1,\gamma,\gamma^2,\ldots,\gamma^d
$$
are linearly dependent over $\QQ$. Thus there are rational numbers
$c_0,\ldots,c_d$, not all zero, such that
$$
c_0+c_1\gamma+\cdots+c_d\gamma^d=0.
$$
Hence $\gamma$ satisfies a nonzero polynomial in $\QQ[x]$.

:::

:::

::: pf-step

Therefore $\alpha+\beta$ is algebraic over $\QQ$.

::: pf-proof

The sum $\alpha+\beta$ belongs to $K$, so apply step [](#s2){.pf-ref}.

:::

:::

:::

:::

::: {.remark title="Variations"}
The proof works unchanged over any field $F$ in place of $\QQ$, and for $\alpha-\beta$, $\alpha\beta$ and, when $\beta\ne0$, $\alpha\beta^{-1}$ in place of $\alpha+\beta$: each of these elements lies in the finite extension $F(\alpha,\beta)$, so the last step applies to it.
:::
