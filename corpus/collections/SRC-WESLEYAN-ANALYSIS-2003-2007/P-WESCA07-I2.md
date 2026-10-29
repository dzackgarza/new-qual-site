---
schema: qual/card@1
id: P-WESCA07-I2
kind: problem
title: "Define a branch of an inverse function"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section I, item 2 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f:U\to\CC$ be analytic, and let $D\subset f(U)$ be a domain.
Define what it means for $g$ to be a branch of $f^{-1}$ on $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A **branch of $f^{-1}$ on $D$** is an analytic function
$$
\boxed{g:D\to U}
$$
such that
$$
\boxed{f(g(w))=w\qquad\text{for every }w\in D.}
$$


::: pf-proof

This is the definition: $g$ chooses, analytically on the domain $D$, one preimage under $f$ of each point of $D$.

:::

:::

::: {.pf-step #s1-2}

Such a branch is automatically injective, and
$$
g\circ f=\operatorname{id}
$$
on the subset $g(D)\subseteq U$.


::: pf-proof

If $g(w_1)=g(w_2)$, applying $f$ gives
$$
w_1=f(g(w_1))=f(g(w_2))=w_2,
$$
so $g$ is injective. If $z=g(w)\in g(D)$, then
$$
g(f(z))=g(f(g(w)))=g(w)=z.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested definition; step [](#s1-2){.pf-ref} records its immediate consequences.

:::

:::

:::
