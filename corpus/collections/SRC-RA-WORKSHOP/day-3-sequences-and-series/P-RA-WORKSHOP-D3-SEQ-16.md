---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-16
kind: problem
title: Interchange two nonnegative double-series summations
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(January 2006 #5) Let $a_{m,n}\ge0$ for $m,n\in\mathbb N$ and assume that the partial sums
$$
\sum_{m=1}^{M}\sum_{n=1}^{N}a_{m,n}
$$
are bounded above.
Prove carefully that
$$
\sum_{m=1}^{\infty}\left(\sum_{n=1}^{\infty}a_{m,n}\right)
\quad\text{and}\quad
\sum_{n=1}^{\infty}\left(\sum_{m=1}^{\infty}a_{m,n}\right)
$$
exist and are equal.
:::

::: {.solution}
Set $S_{M,N}=\sum_{m=1}^{M}\sum_{n=1}^{N}a_{m,n}$ and $B=\sup_{M,N\geq1}S_{M,N}<\infty$.

<1>1. The inner series $A_m=\sum_{n=1}^{\infty}a_{m,n}$ and $C_n=\sum_{m=1}^{\infty}a_{m,n}$ exist as finite real numbers.

::: {.proof}
For fixed $m$, the partial sums $\sum_{n=1}^{N}a_{m,n}$ are nondecreasing and bounded above by $S_{m,N}\leq B$. They therefore converge to a finite $A_m$. Exchanging the two indices proves existence and finiteness of every $C_n$.
:::

<1>2. For each $M,N\geq1$,
\[
\sum_{m=1}^{M}A_m=\sup_{N'\geq1}S_{M,N'},
\qquad
\sum_{n=1}^{N}C_n=\sup_{M'\geq1}S_{M',N}.
\]

::: {.proof}
By step <1>1, each of the finitely many series defining $A_1,\ldots,A_M$ converges. Passing the limit through this finite sum gives
\[
\sum_{m=1}^{M}A_m
=\lim_{N'\to\infty}\sum_{m=1}^{M}\sum_{n=1}^{N'}a_{m,n}
=\sup_{N'\geq1}S_{M,N'},
\]
where the last equality follows from nonnegativity. The other identity follows by interchanging $m$ and $n$.
:::

<1>3. Both iterated series converge and have the same sum:
\[
\boxed{
\sum_{m=1}^{\infty}\left(\sum_{n=1}^{\infty}a_{m,n}\right)
=\sum_{n=1}^{\infty}\left(\sum_{m=1}^{\infty}a_{m,n}\right)
=B}.
\]

::: {.proof}
The identities in step <1>2 imply that the partial sums of both iterated series are bounded above by $B$. They are nondecreasing because all their terms are nonnegative, hence each converges. Moreover,
\[
\sum_{m=1}^{\infty}A_m
=\sup_M\sup_N S_{M,N}
=B
=\sup_N\sup_M S_{M,N}
=\sum_{n=1}^{\infty}C_n.
\]
Here iterated suprema agree because both range over the same set of rectangular partial sums.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves existence of the inner sums, and step <1>3 proves existence and equality of the finite iterated sums.
:::
:::
