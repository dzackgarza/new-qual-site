---
schema: qual/card@1
id: P-BERK83SU-17
kind: problem
title: A Hermitian solution of $A^5+A^3+A=3I$ is the identity
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The scalar polynomial p(t)=t^5+t^3+t-3 is strictly increasing on the
    reals because p'(t)=5t^4+3t^2+1>0, and p(1)=0. The spectral theorem makes
    every eigenvalue of A real, while the matrix equation forces each to be a
    zero of p. Hence every eigenvalue is 1 and the Hermitian matrix is I.
---

::: {.problem}
Let $A$ be an $n\times n$ Hermitian matrix satisfying
\[
A^5+A^3+A=3I.
\]
Prove that $A=I$.
:::

::: {.solution}
Let
$$
p(t)=t^5+t^3+t-3.
$$

<1>1. The polynomial $p$ has exactly one real zero, namely $1$.

::: {.proof}
For every $t\in\RR$,
$$
p'(t)=5t^4+3t^2+1>0.
$$
Thus $p$ is strictly increasing on $\RR$. Since
$$
p(1)=1+1+1-3=0,
$$
the unique real zero of $p$ is $1$.
:::

<1>2. Every eigenvalue $\lambda$ of $A$ is real and satisfies
$$
p(\lambda)=0.
$$

::: {.proof}
Because $A$ is Hermitian, the spectral theorem implies that all of
its eigenvalues are real. If $Av=\lambda v$ with $v\neq0$, then
the matrix equation gives
$$
0
=
(A^5+A^3+A-3I)v
=
(\lambda^5+\lambda^3+\lambda-3)v
=
p(\lambda)v.
$$
Since $v\neq0$, one has $p(\lambda)=0$.
:::

<1>3. Every eigenvalue of $A$ is equal to $1$.

::: {.proof}
By step <1>2, every eigenvalue is a real zero of $p$. Step <1>1
shows that the only such zero is $1$.
:::

<1>4. One has
$$
\boxed{A=I}.
$$

::: {.proof}
By the spectral theorem there is a unitary matrix $U$ and a real
diagonal matrix $D$ such that
$$
A=UDU^*.
$$
Step <1>3 shows that every diagonal entry of $D$ is $1$, so $D=I$.
Hence
$$
A=UIU^*=I.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
