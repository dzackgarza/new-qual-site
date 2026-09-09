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

::: problem
Let $k$ be a field and let $f(x) \in k[x]$ be a polynomial of degree $\deg(f) \in \{2, 3\}$.
Prove that $f(x)$ is irreducible in $k[x]$ if and only if $f(x)$ has no roots in $k$.
:::

::: solution
If $f$ is irreducible and had a root $a\in k$, then the factor theorem would give
\[
f(x)=(x-a)g(x)
\]
with $\deg g=\deg f-1\ge1$, a nontrivial factorization. Hence an irreducible polynomial of degree $2$ or $3$ has no root in $k$.

Conversely, suppose $f$ is reducible. Then
\[
f=gh
\]
with $\deg g,\deg h\ge1$ and
\[
\deg g+\deg h=\deg f\in\{2,3\}.
\]
Therefore at least one factor has degree $1$. Write that factor as $ax+b$ with $a\ne0$. It vanishes at $-b/a\in k$, so $f$ has a root in $k$.

Thus, for degrees $2$ and $3$,
\[
f\text{ irreducible}\quad\Longleftrightarrow\quad f\text{ has no root in }k.
\]
:::
