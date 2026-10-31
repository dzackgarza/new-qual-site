---
schema: qual/card@1
id: P-FHW1-12
kind: problem
title: Degrees of the factors of $f(g(x))$ for irreducible $f$
classification:
  areas: [algebra]
  topics: [Field Extensions, Polynomials]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image. The source reads "divided"; the statement reads "divides".
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $f(x)\in K[x]$ be an irreducible polynomial and let $g(x)\in K[x]$ be any non-constant polynomial. Let $p(x)$ be a non-constant polynomial that divides $f(g(x))$. Show that $\deg f$ divides $\deg p$.
:::

::: {.solution}
Let $q\in K[x]$ be an irreducible factor of $p$, and let $\alpha$ be a root of $q$ in an extension field of $K$.

::: pf

::: {.pf-step #g-alpha-root-of-f}
$g(\alpha)$ is a root of $f$.

::: pf-proof
Since $q$ divides $p$ and $p$ divides $f(g)$, the polynomial $q$ divides $f(g)$; evaluating at $\alpha$ gives $f(g(\alpha))=0$.
:::

:::

::: {.pf-step #degrees}
$\deg f$ divides $\deg q$.

::: pf-proof
The polynomial $f$ is irreducible over $K$ and has the root $g(\alpha)$, so $f$ is the minimal polynomial of $g(\alpha)$ up to a scalar and $[K(g(\alpha)):K]=\deg f$.
The field $K(g(\alpha))$ is an intermediate field of $K\subseteq K(g(\alpha))\subseteq K(\alpha)$, so $\deg f$ divides $[K(\alpha):K]$ by the tower law.
Since $q$ is irreducible with root $\alpha$, $[K(\alpha):K]=\deg q$.
:::

:::

::: {.pf-step #divides-degree-of-p}
$\deg f$ divides $\deg p$.

::: pf-proof
Factor $p$ over $K$ as $p=c\prod_i q_i^{e_i}$ with $c\in K^\times$, the $q_i$ monic and irreducible.
Then $\deg p=\sum_ie_i\deg q_i$, and each $\deg q_i$ is divisible by $\deg f$ by step [](#degrees){.pf-ref}; hence so is the whole sum.
:::

:::

:::

:::
