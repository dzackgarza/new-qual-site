---
schema: qual/card@1
id: P-HWBXR
kind: problem
title: A polynomial of degree $2$ or $3$ in $k[x]$ is irreducible iff it has no root
  in $k$
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
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
Let $k$ be a field and let $f(x) \in k[x]$ be a polynomial of degree $\deg(f) \in \{2, 3\}$.
Prove that $f(x)$ is irreducible in $k[x]$ if and only if $f(x)$ has no roots in $k$.
:::

::: {.solution}

::: pf

::: pf-step
If $f$ is irreducible, then $f$ has no root in $k$.

::: pf-proof
If $f$ had a root $a\in k$, the factor theorem would give
$$
f(x)=(x-a)g(x)
$$
with $\deg g=\deg f-1\ge1$, a factorization into two nonunits.
:::

:::

::: pf-step
If $f$ is reducible, then $f$ has a root in $k$.

::: pf-proof
Write $f=gh$ with $\deg g,\deg h\ge1$ and
$$
\deg g+\deg h=\deg f\in\{2,3\}.
$$
Then at least one factor has degree $1$. Write that factor as $ax+b$ with $a\ne0$. It vanishes at $-b/a\in k$, so $f$ has a root in $k$.
:::

:::

:::

:::
