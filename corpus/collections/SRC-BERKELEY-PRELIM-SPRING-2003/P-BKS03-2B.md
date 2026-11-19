---
schema: qual/card@1
id: P-BKS03-2B
kind: problem
title: Products of solutions to constant-coefficient linear ODEs
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
  date: 2026-11-19
  note: >-
    Structured the three-line argument into numbered steps and supplied what it used silently: the
    Leibniz rule behind the expression of F^{(k)}, the reduction of every f^{(i)} with i >= n by the
    equation satisfied by f (and likewise for g), the induction that keeps every derivative inside
    the span of the mn products f^{(i)}g^{(j)}, and the dimension count that turns mn + 1 vectors in
    an mn-dimensional space into a nontrivial relation. Every macro used is one the preamble defines.
    No source text is retained for this examination, so nothing was checked against a printed page.

---

::: {.problem}
Suppose entire functions $f,g$ satisfy constant-coefficient linear differential equations of orders $n$ and $m$, respectively.
Show that $F=fg$ satisfies a nontrivial constant-coefficient linear differential equation of order at most $mn$.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Let $f$ satisfy $f^{(n)}=\sum_{i<n}c_{i}f^{(i)}$ and $g$ satisfy $g^{(m)}=\sum_{j<m}d_{j}g^{(j)}$ with complex constants $c_{i},d_{j}$; this is what "constant-coefficient linear differential equation of order $n$" gives, the leading coefficient having been divided out.

::: pf

::: {.pf-step #span}
Let $V$ be the complex vector space spanned by the $mn$ functions $f^{(i)}g^{(j)}$ with $0\leq i<n$ and $0\leq j<m$. Then $\dim_{\CC}V\leq mn$.

::: pf-proof
$V$ is spanned by $mn$ vectors, so its dimension is at most $mn$.
:::

:::

::: {.pf-step #derivatives-of-f}
Every $f^{(k)}$ with $k\geq0$ lies in $\operatorname{span}\{f^{(0)},\dots,f^{(n-1)}\}$.

::: pf-proof
Induction on $k$. For $k<n$ this is clear. For $k\geq n$, differentiate the relation $f^{(k-1)}=\sum_{i<n}\alpha_{i}f^{(i)}$ guaranteed by the inductive hypothesis, giving $f^{(k)}=\sum_{i<n}\alpha_{i}f^{(i+1)}$; the terms with $i+1<n$ are already basis elements, and the term $i=n-1$ is $\alpha_{n-1}f^{(n)}=\alpha_{n-1}\sum_{i<n}c_{i}f^{(i)}$, again in the span. So the assertion holds for $k$.
:::

:::

::: {.pf-step #in-V}
$F^{(k)}\in V$ for every $k\geq0$.

::: pf-proof
Induction on $k$. For $k=0$ there is nothing to show. If $F^{(k)}\in V$, write $F^{(k)}=\sum_{i<n,j<m}\gamma_{ij}f^{(i)}g^{(j)}$; differentiating with the Leibniz rule and using step [](#derivatives-of-f){.pf-ref} and its analogue for $g$, each $f^{(i+1)}$ and each $g^{(j+1)}$ is a combination of derivatives of order below $n$, respectively $m$, so $F^{(k+1)}\in V$.
:::

:::

::: {.pf-step #dependence}
The $mn+1$ functions $F^{(0)},\dots,F^{(mn)}$ are linearly dependent over $\CC$.

::: pf-proof
They all lie in $V$ by step [](#in-V){.pf-ref}, and $\dim V\leq mn$ by step [](#span){.pf-ref}; any $mn+1$ vectors in a space of dimension at most $mn$ are dependent.
:::

:::

::: {.pf-step}
$F=fg$ satisfies a nontrivial constant-coefficient linear differential equation of order at most $mn$.

::: pf-proof
A dependence $\sum_{k=0}^{mn}a_{k}F^{(k)}=0$ with not all $a_{k}$ zero, which step [](#dependence){.pf-ref} provides, is such an equation. Let $K$ be the largest index with $a_{K}\neq0$; then $K\leq mn$ and the equation has order exactly $K$, its highest term being the nonzero constant $a_{K}$ times $F^{(K)}$.
:::

:::

:::

:::
