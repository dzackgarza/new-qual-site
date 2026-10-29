---
schema: qual/card@1
id: P-S2LCU
kind: problem
title: Separable extensions are normal iff they are splitting fields
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Separability
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $L/K$ be a finite separable field extension.
Prove that $L/K$ is normal if and only if $L$ is the splitting field of some separable polynomial $p(x) \in K[x]$.
:::

::: {.solution}

Let $\Omega$ be an algebraic closure of $L$, hence of $K$.

::: pf

::: pf-step

If $L/K$ is normal, then $L$ is the splitting field of a separable polynomial in $K[x]$.

::: pf-proof

By the primitive element theorem, $L=K(\alpha)$ for some $\alpha\in L$. Let $m_\alpha\in K[x]$ be the minimal polynomial of $\alpha$. It is separable because $L/K$ is separable, and it splits in $L$ because $L/K$ is normal and $m_\alpha$ is irreducible with a root in $L$. The field generated over $K$ by its roots contains $\alpha$ and lies in $L$, so it is $L$.

:::

:::

::: pf-qed

Conversely, let $L$ be the splitting field over $K$ of a separable $p\in K[x]$, and let $\sigma\colon L\hookrightarrow\Omega$ be a $K$-embedding. For each root $\beta\in L$ of $p$, $p(\sigma(\beta))=\sigma(p(\beta))=0$, so $\sigma$ maps the roots of $p$ in $L$ injectively into themselves, hence onto them. Since those roots generate $L$ over $K$, $\sigma(L)=L$. Every $K$-embedding of $L$ into $\Omega$ therefore has image $L$, so $L/K$ is normal.

:::

:::

:::
