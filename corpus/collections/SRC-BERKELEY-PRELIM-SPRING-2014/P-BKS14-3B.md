---
schema: qual/card@1
id: P-BKS14-3B
kind: problem
title: $\abs{P(0)}$ is bounded by the $L^1[0,1]$ norm on polynomials of bounded degree
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
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the finite-dimensional compactness argument, positivity of the L1 norm on the coefficient sphere, and the resulting uniform evaluation bound.
---

::: {.problem}
Prove that there exists a constant $C$ such that every polynomial $P$ of degree at most $2014$ satisfies
$$
P(0)\le C\int_0^1 |P(x)|\,dx.
$$
:::

::: {.solution}
Let
$$
V
\coloneqq
\{P\in\RR[x]:\deg P\leq2014\}.
$$
For
$$
P(x)=\sum_{k=0}^{2014}a_kx^k,
$$
define the coefficient norm
$$
\norm{P}_{\mathrm{coef}}
\coloneqq
\max_{0\leq k\leq2014}\abs{a_k}
$$
and the integral norm
$$
N(P)
\coloneqq
\int_0^1\abs{P(x)}\,dx.
$$

<1>1. The function $N$ is a norm on $V$.

::: {.proof}
Nonnegativity, homogeneity, and the triangle inequality follow from the
corresponding properties of absolute value and the integral.

If
$$
N(P)=0,
$$
then the continuous nonnegative function $\abs{P(x)}$ has integral zero,
so
$$
P(x)=0
$$
for every $x\in[0,1]$. A polynomial with infinitely many zeros is the zero
polynomial. Hence $P=0$.
:::

<1>2. The map
$$
P\longmapsto N(P)
$$
is continuous with respect to the coefficient norm.

::: {.proof}
Let
$$
P(x)-Q(x)
=
\sum_{k=0}^{2014}c_kx^k.
$$
For $0\leq x\leq1$,
$$
\abs{P(x)-Q(x)}
\leq
\sum_{k=0}^{2014}\abs{c_k}
\leq
2015\norm{P-Q}_{\mathrm{coef}}.
$$
Therefore
$$
\begin{aligned}
\abs{N(P)-N(Q)}
&\leq
\int_0^1
\bigl|\abs{P(x)}-\abs{Q(x)}\bigr|\,dx\\
&\leq
\int_0^1\abs{P(x)-Q(x)}\,dx\\
&\leq
2015\norm{P-Q}_{\mathrm{coef}}.
\end{aligned}
$$
Thus $N$ is continuous.
:::

<1>3. The coefficient-unit sphere
$$
\Sigma
\coloneqq
\{P\in V:\norm{P}_{\mathrm{coef}}=1\}
$$
is compact.

::: {.proof}
Under the coefficient identification
$$
V\cong\RR^{2015},
$$
the set $\Sigma$ is closed and bounded. The Heine--Borel theorem therefore
gives compactness.
:::

<1>4. There exists a number
$$
m>0
$$
such that
$$
N(P)\geq m
$$
for every $P\in\Sigma$.

::: {.proof}
By steps <1>2 and <1>3, the continuous function $N$ attains a minimum
$m$ on $\Sigma$.

Every $P\in\Sigma$ is nonzero, so step <1>1 gives
$$
N(P)>0.
$$
In particular the attained minimum satisfies $m>0$.
:::

<1>5. For every $P\in V$,
$$
\norm{P}_{\mathrm{coef}}
\leq
\frac1mN(P).
$$

::: {.proof}
The assertion is immediate for $P=0$. If $P\neq0$, set
$$
Q
\coloneqq
\frac{P}{\norm{P}_{\mathrm{coef}}}.
$$
Then $Q\in\Sigma$, so step <1>4 gives
$$
N(Q)\geq m.
$$
By homogeneity,
$$
\frac{N(P)}{\norm{P}_{\mathrm{coef}}}
\geq
m,
$$
which rearranges to the claim.
:::

<1>6. For every polynomial $P$ of degree at most $2014$,
$$
\abs{P(0)}
\leq
\frac1m
\int_0^1\abs{P(x)}\,dx.
$$

::: {.proof}
Since
$$
P(0)=a_0,
$$
one has
$$
\abs{P(0)}
\leq
\norm{P}_{\mathrm{coef}}.
$$
Apply step <1>5.
:::

<1>7. Thus there exists a constant
$$
\boxed{C=\frac1m}
$$
such that every polynomial of degree at most $2014$ satisfies
$$
P(0)
\leq
C\int_0^1\abs{P(x)}\,dx.
$$

::: {.proof}
Step <1>6 gives the stronger inequality with $\abs{P(0)}$ on the left.
Since
$$
P(0)\leq\abs{P(0)},
$$
the stated inequality follows.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 proves the required uniform bound.
:::
:::
