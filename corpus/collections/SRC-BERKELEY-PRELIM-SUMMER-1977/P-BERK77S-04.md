---
schema: qual/card@1
id: P-BERK77S-04
kind: problem
title: Entrywise convergence of the matrix exponential series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Bounded each entry of A^n by r^(n-1)M^n, where M bounds the entries of
    A. The resulting scalar majorant is a constant multiple of the
    exponential series for rM, so every entry series converges absolutely.
---

::: {.problem}
Let $A$ be an $r\times r$ real matrix. Prove that
\[
e^A=I+A+\frac{A^2}{2!}+\cdots+\frac{A^n}{n!}+\cdots
\]
converges entrywise, and hence defines a well-defined matrix $e^A$.
:::

::: {.solution}
Let
$$
M=\max_{1\leq i,j\leq r}\abs{a_{ij}},
$$
where $A=(a_{ij})$.

<1>1. For every integer $n\geq1$ and every pair $i,j$,
$$
\abs{(A^n)_{ij}}
\leq
r^{n-1}M^n.
$$

::: {.proof}
The $(i,j)$ entry of $A^n$ is
$$
(A^n)_{ij}
=
\sum_{k_1,\ldots,k_{n-1}=1}^r
a_{ik_1}a_{k_1k_2}\cdots a_{k_{n-1}j}.
$$
There are $r^{n-1}$ summands, and each is a product of $n$ entries of $A$,
so each has absolute value at most $M^n$. The triangle inequality gives the
stated bound.
:::

<1>2. For each fixed pair $i,j$, the scalar series
$$
\sum_{n=0}^{\infty}\frac{(A^n)_{ij}}{n!}
$$
converges absolutely.

::: {.proof}
The $n=0$ term is the finite number $(I)_{ij}$. For $n\geq1$, step <1>1
gives
$$
\frac{\abs{(A^n)_{ij}}}{n!}
\leq
\frac{r^{n-1}M^n}{n!}
=
\frac1r\frac{(rM)^n}{n!}.
$$
The numerical series
$$
\sum_{n=1}^{\infty}\frac1r\frac{(rM)^n}{n!}
$$
converges because it is
$$
\frac{e^{rM}-1}{r}.
$$
Comparison therefore proves absolute convergence of the entry series.
:::

<1>3. The matrix series
$$
I+A+\frac{A^2}{2!}+\cdots
$$
converges entrywise.

::: {.proof}
There are only $r^2$ matrix entries. Step <1>2 proves convergence of the
series defining each one, which is exactly entrywise convergence.
:::

<1>4. The matrix
$$
\boxed{
e^A
=
\left(
\sum_{n=0}^{\infty}\frac{(A^n)_{ij}}{n!}
\right)_{1\leq i,j\leq r}
}
$$
is well defined.

::: {.proof}
Every scalar entry in the displayed matrix exists by step <1>2, so the
$r\times r$ matrix is well defined. Step <1>3 shows that it is the
entrywise sum of the stated matrix series.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>3--<1>4 give the required convergence and definition of $e^A$.
:::
:::
