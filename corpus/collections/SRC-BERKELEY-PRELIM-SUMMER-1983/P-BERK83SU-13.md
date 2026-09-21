---
schema: qual/card@1
id: P-BERK83SU-13
kind: problem
title: A unipotent complex matrix with bounded positive powers is the identity
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
    With N=A-I, all eigenvalues of N are zero, so Cayley--Hamilton makes N
    nilpotent. If N^r is its highest nonzero power, then for a suitable vector
    v and linear functional ell, ell(A^m v) is a scalar polynomial in m of
    degree r with nonzero leading coefficient, contradicting bounded powers.
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix all of whose eigenvalues are equal to $1$. Suppose the set
\[
\{A^n:n=1,2,\ldots\}
\]
is bounded.
Prove that $A=I$.
:::

::: {.solution}
Let
$$
N=A-I.
$$

<1>1. The matrix $N$ is nilpotent.

::: {.proof}
Every eigenvalue of $N=A-I$ is obtained by subtracting $1$ from an
eigenvalue of $A$, so every eigenvalue of $N$ is $0$. Thus the
characteristic polynomial of $N$ is $t^n$. By the Cayley--Hamilton
theorem,
$$
N^n=0.
$$
:::

<1>2. If $N\neq0$, there exist an integer $r\ge1$, a vector $v$,
and a linear functional $\ell$ such that
$$
N^r\neq0,
\qquad
N^{r+1}=0,
\qquad
\ell(N^r v)\neq0.
$$

::: {.proof}
By step <1>1, the positive powers of $N$ eventually vanish. If
$N\neq0$, let $r\ge1$ be maximal with $N^r\neq0$. Choose $v$ with
$N^r v\neq0$. Since linear functionals separate points in a
finite-dimensional vector space, there is a linear functional
$\ell$ such that $\ell(N^r v)\neq0$.
:::

<1>3. Under the assumption $N\neq0$, the sequence
$$
\ell(A^m v),
\qquad
m=1,2,\ldots,
$$
is unbounded.

::: {.proof}
Since $A=I+N$ and $N^{r+1}=0$, the binomial theorem gives
$$
A^m
=
(I+N)^m
=
\sum_{j=0}^r\binom{m}{j}N^j.
$$
Therefore
$$
\ell(A^m v)
=
\sum_{j=0}^r
\binom{m}{j}\ell(N^jv).
$$
As a function of the integer variable $m$, the right-hand side is a
polynomial of degree $r$. Its leading coefficient is
$$
\frac{\ell(N^rv)}{r!},
$$
which is nonzero by step <1>2. Hence its absolute value is unbounded
as $m\to\infty$.
:::

<1>4. One must have $N=0$.

::: {.proof}
If the matrices $A^m$ form a bounded set, then for every fixed vector
$v$ the vectors $A^m v$ form a bounded set, and applying a fixed
linear functional $\ell$ preserves boundedness. Step <1>3 would
contradict this if $N\neq0$. Therefore $N=0$.
:::

<1>5. Consequently,
$$
\boxed{A=I}.
$$

::: {.proof}
By definition, $N=A-I$. Step <1>4 gives $A-I=0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
