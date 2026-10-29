---
schema: qual/card@1
id: P-UCLAB17F-09
kind: problem
title: A fixed point from summable iterate Lipschitz constants
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $(X,\rho)$ be complete and $f:X\to X$. For $n\ge1$ set
$$
c_n=\sup_{x\ne y}\frac{\rho(f^n(x),f^n(y))}{\rho(x,y)}.
$$
If $\sum_{n=1}^\infty c_n<\infty$, prove that $f$ has a unique fixed point.
:::

::: {.solution}

Fix an arbitrary point
$$
x_0\in X
$$
and define
$$
x_n=f^n(x_0),
\qquad
n\ge0.
$$

::: pf

::: {.pf-step #s1-1}

For every $n\ge1$,
$$
\rho(x_{n+1},x_n)
\le
c_n\,\rho(x_1,x_0).
$$


::: pf-proof

Since
$$
x_{n+1}
=
f^n(x_1)
$$
and
$$
x_n
=
f^n(x_0),
$$
the definition of $c_n$ gives
$$
\rho(x_{n+1},x_n)
=
\rho(f^n(x_1),f^n(x_0))
\le
c_n\rho(x_1,x_0).
$$

:::

:::

::: {.pf-step #s1-2}

The sequence $(x_n)$ is Cauchy.


::: pf-proof

If $m>n$, the triangle inequality and step [](#s1-1){.pf-ref} give
$$
\begin{aligned}
\rho(x_m,x_n)
&\le
\sum_{k=n}^{m-1}\rho(x_{k+1},x_k)\\
&\le
\rho(x_1,x_0)
\sum_{k=n}^{m-1}c_k\\
&\le
\rho(x_1,x_0)
\sum_{k=n}^{\infty}c_k.
\end{aligned}
$$
Because
$$
\sum_{k=1}^{\infty}c_k
$$
converges, its tails tend to zero.
Therefore
$$
\rho(x_m,x_n)\to0
$$
uniformly for $m>n\to\infty$.

:::

:::

::: pf-step

There exists
$$
p\in X
$$
such that
$$
x_n\to p.
$$


::: pf-proof

The space $X$ is complete and $(x_n)$ is Cauchy by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

The map $f$ is Lipschitz, hence continuous.


::: pf-proof

By definition,
$$
c_1
=
\sup_{x\ne y}
\frac{\rho(f(x),f(y))}
{\rho(x,y)}.
$$
The convergence of
$$
\sum c_n
$$
implies in particular that
$$
c_1<\infty.
$$
Thus
$$
\rho(f(x),f(y))
\le
c_1\rho(x,y)
$$
for all $x,y$.
Hence $f$ is Lipschitz and therefore continuous.

:::

:::

::: {.pf-step #s1-5}

The limit point $p$ is a fixed point:
$$
\boxed{f(p)=p}.
$$


::: pf-proof

By continuity of $f$,
$$
f(p)
=
f\left(\lim_{n\to\infty}x_n\right)
=
\lim_{n\to\infty}f(x_n)
=
\lim_{n\to\infty}x_{n+1}
=
p.
$$

:::

:::

::: {.pf-step #s1-6}

Since
$$
\sum_{n=1}^{\infty}c_n<\infty,
$$
one has
$$
c_n\to0.
$$


::: pf-proof

Every convergent series has terms tending to zero.

:::

:::

::: {.pf-step #s1-7}

The fixed point is unique.


::: pf-proof

Suppose
$$
p,q\in X
$$
are fixed points.
Then for every $n$,
$$
f^n(p)=p,
\qquad
f^n(q)=q.
$$
Hence
$$
\rho(p,q)
=
\rho(f^n(p),f^n(q))
\le
c_n\rho(p,q).
$$
By step [](#s1-6){.pf-ref}, choose $n$ such that
$$
c_n<1.
$$
If
$$
\rho(p,q)>0,
$$
dividing the inequality by $\rho(p,q)$ gives
$$
1\le c_n<1,
$$
a contradiction.
Thus
$$
\rho(p,q)=0,
$$
so $p=q$.

:::

:::

::: {.pf-step #s1-8}

Therefore $f$ has a unique fixed point in $X$.


::: pf-proof

Step [](#s1-5){.pf-ref} proves existence, and step [](#s1-7){.pf-ref} proves uniqueness.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
