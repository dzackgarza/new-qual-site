---
schema: qual/card@1
id: P-CHAVAN-CA-9-1
kind: problem
title: Invertible complex matrices are dense
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The extraction drops the phrase "not equal to zero" after determinant; the surrounding determinant-zero-set discussion forces the invertible-matrix statement recorded here.
---

::: {.problem}
Show that the set
\[
\{A\in M_n(\mathbb C):\det A\ne0\}
\]
is dense in $M_n(\mathbb C)$.
:::

::: {.solution}
<1>1. For every $A\in M_n(\CC)$, the polynomial
$$
p(t)=\det(A+tI_n)
$$
is a nonzero polynomial of degree $n$ in $t$.

::: {.proof}
Expanding the determinant as a polynomial in $t$, the term obtained by taking
$t$ from every diagonal entry is $t^n$, and no other term has degree $n$.
Hence $p$ is monic of degree $n$.
:::

<1>2. There is a sequence $t_k\in\CC\setminus\{0\}$ such that
$$
t_k\longrightarrow0
\qquad\text{and}\qquad
p(t_k)\neq0
$$
for every $k$.

::: {.proof}
By step <1>1, the zero set of $p$ is finite. The sequence $1/m$ tends to zero,
and only finitely many of its terms can belong to that finite zero set. Deleting
those terms gives the required sequence.
:::

<1>3. The matrices
$$
A_k=A+t_kI_n
$$
are invertible and satisfy $A_k\to A$ in $M_n(\CC)$.

::: {.proof}
By step <1>2,
$$
\det A_k=p(t_k)\neq0,
$$
so each $A_k$ is invertible. Also
$$
A_k-A=t_kI_n\longrightarrow0,
$$
so $A_k\to A$ in the usual finite-dimensional topology on $M_n(\CC)$.
:::

<1>4. The set of invertible matrices is dense in $M_n(\CC)$.

::: {.proof}
The matrix $A$ was arbitrary, and step <1>3 approximates it by invertible
matrices.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
