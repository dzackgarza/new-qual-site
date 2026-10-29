---
schema: qual/card@1
id: E-AMD-4TXVF5CA
kind: problem
title: An irreducible in $\FF_p[x]$ divides $x^{p^n}-x$ iff its degree divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove that an irreducible polynomial $\pi(x)\in \FF_p[x]$ divides $x^{p^n}-x \iff \deg \pi(x)$ divides $n$.
:::

::: {.solution}
Let $\pi\in\FF_p[x]$ be irreducible of degree $d$, and let $\alpha\in\overline{\FF}_p$ be a root of $\pi$.

::: pf

::: {.pf-step #root-field}
$\FF_p(\alpha)$ has $p^d$ elements, and $\pi\mid x^{p^n}-x$ if and only if $\alpha^{p^n}=\alpha$.

::: pf-proof
$\pi$ is a scalar multiple of the minimal polynomial of $\alpha$ over $\FF_p$, so $[\FF_p(\alpha):\FF_p]=d$. A polynomial over $\FF_p$ has $\alpha$ as a root exactly when the minimal polynomial divides it.
:::

:::

::: pf-step
If $\pi\mid x^{p^n}-x$, then $d\mid n$.

::: pf-proof
The roots of $x^{p^n}-x$ in $\overline{\FF}_p$ form the field $\FF_{p^n}$. By step [](#root-field){.pf-ref}, $\alpha\in\FF_{p^n}$, so $\FF_p(\alpha)\subseteq\FF_{p^n}$, and the tower law gives $n=d\cdot[\FF_{p^n}:\FF_p(\alpha)]$.
:::

:::

::: pf-step
If $d\mid n$, then $\pi\mid x^{p^n}-x$.

::: pf-proof
The multiplicative group of the field $\FF_p(\alpha)$ of order $p^d$ has order $p^d-1$, so $\alpha^{p^d}=\alpha$. Iterating $n/d$ times gives $\alpha^{p^n}=\alpha$, and step [](#root-field){.pf-ref} gives $\pi\mid x^{p^n}-x$.
:::

:::

:::

:::
