---
schema: qual/card@1
id: P-BKS17-4B
kind: problem
title: Existence and uniqueness of polynomial interpolation
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 15 problem 4B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 Lagrange-interpolation solution. The construction is correct; the solution below proves uniqueness directly from the root bound for a nonzero polynomial.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the Lagrange basis denominators, interpolation values, degree bound, and uniqueness from the $n$ prescribed roots of a difference polynomial.
---

::: {.problem}
Given $n$ distinct points $z_j \in \CC$ and $n$ values $f_j \in \CC$, show that there is a unique polynomial $P$ of degree at most $n - 1$ such that

$$
P(z_j) = f_j
$$

for $1 \leq j \leq n$.
:::

::: {.solution}

For $1\leq j\leq n$, define
$$
L_j(z)
\coloneqq
\prod_{\substack{1\leq k\leq n\\k\neq j}}
\frac{z-z_k}{z_j-z_k}.
$$

::: pf

::: {.pf-step #s1-1}

Each $L_j$ has degree at most $n-1$ and satisfies
$$
L_j(z_k)=\delta_{jk}
\qquad(1\leq k\leq n).
$$


::: pf-proof

Every denominator $z_j-z_k$ is nonzero because the nodes are distinct. The defining product has $n-1$ linear factors, so $\deg L_j\leq n-1$. If $k\neq j$, the factor with index $k$ vanishes at $z=z_k$, hence $L_j(z_k)=0$. If $k=j$, every factor equals $1$, hence $L_j(z_j)=1$.

:::

:::

::: {.pf-step #s1-2}

The polynomial
$$
\boxed{P(z)=\sum_{j=1}^n f_jL_j(z)}
$$
has degree at most $n-1$ and satisfies $P(z_k)=f_k$ for every $1\leq k\leq n$.


::: pf-proof

The degree bound follows from step [](#s1-1){.pf-ref}. For each $k$,
$$
P(z_k)
=
\sum_{j=1}^n f_jL_j(z_k)
=
\sum_{j=1}^n f_j\delta_{jk}
=f_k.
$$
Thus the required polynomial exists.

:::

:::

::: {.pf-step #s1-3}

The polynomial in step [](#s1-2){.pf-ref} is unique among polynomials of degree at most $n-1$ with the prescribed values.


::: pf-proof

Suppose $P$ and $Q$ both have degree at most $n-1$ and satisfy
$$
P(z_j)=Q(z_j)=f_j
$$
for every $j$. Then $R\coloneqq P-Q$ has degree at most $n-1$ and has the $n$ distinct roots $z_1,\ldots,z_n$. A nonzero polynomial of degree at most $n-1$ has at most $n-1$ distinct roots. Hence $R=0$, so $P=Q$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves existence and step [](#s1-3){.pf-ref} proves uniqueness.

:::

:::

:::
