---
schema: qual/card@1
id: P-BERK87S-17
kind: problem
title: A finite-dimensional differentiation-invariant function space is the kernel of a constant-coefficient ODE
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Applied Cayley-Hamilton to differentiation restricted to V. Its degree-d
    characteristic polynomial yields a monic order-d constant-coefficient
    ODE annihilating V; uniqueness from d initial values bounds the full
    solution space by dimension d, forcing equality with V.
---

::: {.problem}
Let $V$ be a finite-dimensional complex linear subspace of $C^\infty(\mathbb R)$ and suppose $V$ is invariant under differentiation:
\[
f\in V\implies Df\in V.
\]
Prove that there is a nonzero constant-coefficient differential operator
\[
L=\sum_{k=0}^{n}a_kD^k
\]
such that $V$ is exactly the space of solutions of
\[
Lf=0.
\]
:::

::: {.solution}
Let
$$
d\coloneqq\dim_{\CC}V.
$$

<1>1. If $d=0$, the assertion holds with
$$
\boxed{L=1}.
$$

::: {.proof}
Then
$$
V=\{0\},
$$
and the equation
$$
Lf=f=0
$$
has exactly the zero function as its solution.
:::

<1>2. Assume $d>0$. Differentiation restricts to a linear endomorphism
$$
T\coloneqq D|_V:V\to V.
$$

::: {.proof}
This is exactly the hypothesis that $V$ is invariant under
differentiation.
:::

<1>3. Let
$$
P(\lambda)
\coloneqq
\det(\lambda I-T)
=
\lambda^d+a_{d-1}\lambda^{d-1}+\cdots+a_0
$$
be the characteristic polynomial of $T$. Then
$$
P(T)=0
$$
on $V$.

::: {.proof}
This is the Cayley--Hamilton theorem applied to the endomorphism $T$ of
the $d$-dimensional complex vector space $V$.
:::

<1>4. Define the nonzero constant-coefficient differential operator
$$
L
\coloneqq
P(D)
=
D^d+a_{d-1}D^{d-1}+\cdots+a_0.
$$
Then
$$
V\subseteq\ker L.
$$

::: {.proof}
If $f\in V$, every derivative of $f$ that occurs in $P(D)f$ is computed
by repeated application of the restricted operator $T$. Hence
$$
Lf
=
P(D)f
=
P(T)f
=0
$$
by step <1>3.
:::

<1>5. A solution $f$ of
$$
Lf=0
$$
is uniquely determined by the $d$ initial values
$$
f(0),f'(0),\ldots,f^{(d-1)}(0).
$$

::: {.proof}
The equation is monic of order $d$:
$$
f^{(d)}
=
-a_{d-1}f^{(d-1)}
-\cdots
-a_0f.
$$
Thus it is the standard linear homogeneous initial-value problem with
continuous, in fact constant, coefficients. The uniqueness theorem for
linear ordinary differential equations says that prescribed values of
$$
f(0),f'(0),\ldots,f^{(d-1)}(0)
$$
admit at most one solution. Equivalently, a solution whose first $d$
initial derivatives vanish is identically zero.
:::

<1>6. The solution space
$$
W\coloneqq\ker L
$$
has dimension at most $d$.

::: {.proof}
Consider the linear map
$$
J:W\to\CC^d,
\qquad
J(f)
=
\bigl(f(0),f'(0),\ldots,f^{(d-1)}(0)\bigr).
$$
By step <1>5, $J$ is injective. Therefore
$$
\dim_{\CC}W
\leq
\dim_{\CC}\CC^d
=d.
$$
:::

<1>7. One has
$$
\boxed{V=\ker L}.
$$

::: {.proof}
Step <1>4 gives
$$
V\subseteq W.
$$
Since
$$
\dim V=d,
$$
this inclusion gives
$$
d\leq\dim W.
$$
Step <1>6 gives the reverse inequality
$$
\dim W\leq d.
$$
Hence the dimensions are equal, and the inclusion of finite-dimensional
spaces must be equality.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>1 settles the zero-dimensional case. For $d>0$, step <1>7 gives
a nonzero constant-coefficient operator whose solution space is exactly
$V$.
:::
:::
