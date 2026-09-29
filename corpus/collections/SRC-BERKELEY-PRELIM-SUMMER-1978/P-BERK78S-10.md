---
schema: qual/card@1
id: P-BERK78S-10
kind: problem
title: Bounded partial derivatives give a continuous extension to the closure of a convex domain
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
    Used convexity to restrict f to the segment between two points. The
    scalar mean value theorem on each coordinate, together with the uniform
    bound on all partial derivatives, gives a global Lipschitz estimate
    without requiring derivative continuity. This sends every sequence
    approaching a boundary point to a Cauchy sequence; the resulting limit
    is independent of the approximating sequence, remains Lipschitz on the
    closure, and is the unique continuous extension.
---

::: {.problem}
Let $U\subset\mathbb R^n$ be a convex open set and let $f:U\to\mathbb R^n$ be differentiable. Suppose all partial derivatives of $f$ are uniformly bounded, though not necessarily continuous. Prove that $f$ has a unique continuous extension to the closure $\overline U$.
:::

::: {.solution}
Write
$$
f=(f_1,\ldots,f_n).
$$
Choose $M\geq0$ such that
$$
\abs{\frac{\partial f_i}{\partial x_j}(x)}
\leq
M
$$
for every $x\in U$ and every $1\leq i,j\leq n$.

::: pf

::: {.pf-step #s1}

For every $x,y\in U$ and every component $i$,
$$
\abs{f_i(y)-f_i(x)}
\leq
M\sum_{j=1}^n\abs{y_j-x_j}.
$$

::: pf-proof

Fix $x,y\in U$. Convexity of $U$ implies that the segment
$$
\gamma(t)=x+t(y-x),
\qquad
0\leq t\leq1,
$$
lies in $U$. Define
$$
g_i(t)=f_i(\gamma(t)).
$$
The function $g_i$ is continuous on $[0,1]$ and differentiable on
$(0,1)$. By the chain rule,
$$
g_i'(t)
=
\sum_{j=1}^n
\frac{\partial f_i}{\partial x_j}(\gamma(t))
(y_j-x_j).
$$
Hence
$$
\abs{g_i'(t)}
\leq
M\sum_{j=1}^n\abs{y_j-x_j}.
$$
The one-variable mean value theorem therefore gives
$$
\abs{g_i(1)-g_i(0)}
\leq
M\sum_{j=1}^n\abs{y_j-x_j},
$$
which is the required estimate.

:::

:::

::: {.pf-step #s2}

The map $f$ is globally Lipschitz on $U$: for all $x,y\in U$,
$$
\norm{f(y)-f(x)}
\leq
nM\norm{y-x},
$$
where $\norm{\cdot}$ is the Euclidean norm.

::: pf-proof

By Cauchy--Schwarz,
$$
\sum_{j=1}^n\abs{y_j-x_j}
\leq
\sqrt n\,\norm{y-x}.
$$
Thus step [](#s1){.pf-ref} gives, for every $i$,
$$
\abs{f_i(y)-f_i(x)}
\leq
M\sqrt n\,\norm{y-x}.
$$
Therefore
$$
\begin{aligned}
\norm{f(y)-f(x)}^2
&=
\sum_{i=1}^n
\abs{f_i(y)-f_i(x)}^2\\
&\leq
n\left(
M\sqrt n\,\norm{y-x}
\right)^2\\
&=
n^2M^2\norm{y-x}^2.
\end{aligned}
$$
Taking square roots gives the claim.

:::

:::

::: {.pf-step #s3}

If $x\in\overline U$ and $(x_k)$ is any sequence in $U$ with
$$
x_k\longrightarrow x,
$$
then $(f(x_k))$ is a Cauchy sequence in $\RR^n$.

::: pf-proof

The sequence $(x_k)$ is Cauchy. By step [](#s2){.pf-ref},
$$
\norm{f(x_k)-f(x_\ell)}
\leq
nM\norm{x_k-x_\ell}.
$$
The right-hand side tends to zero as $k,\ell\to\infty$. Hence
$(f(x_k))$ is Cauchy.

:::

:::

::: {.pf-step #s4}

For every $x\in\overline U$, define
$$
\bar f(x)
=
\lim_{k\to\infty}f(x_k),
$$
where $(x_k)$ is any sequence in $U$ converging to $x$. This definition is
independent of the chosen sequence.

::: pf-proof

Existence of the limit follows from step [](#s3){.pf-ref} and completeness of
$\RR^n$.

For independence, suppose
$$
x_k\to x
\qquad\text{and}\qquad
y_k\to x
$$
with $x_k,y_k\in U$. Step [](#s2){.pf-ref} gives
$$
\norm{f(x_k)-f(y_k)}
\leq
nM\norm{x_k-y_k}.
$$
Since
$$
\norm{x_k-y_k}
\leq
\norm{x_k-x}+\norm{y_k-x}
\longrightarrow0,
$$
the two image sequences have the same limit.

:::

:::

::: {.pf-step #s5}

The function $\bar f$ extends $f$.

::: pf-proof

If $x\in U$, choose the constant sequence
$$
x_k=x.
$$
Then step [](#s4){.pf-ref} gives
$$
\bar f(x)
=
\lim_{k\to\infty}f(x)
=
f(x).
$$

:::

:::

::: {.pf-step #s6}

The extension $\bar f$ is Lipschitz on $\overline U$ with the same
constant:
$$
\norm{\bar f(y)-\bar f(x)}
\leq
nM\norm{y-x}
$$
for all $x,y\in\overline U$.

::: pf-proof

Choose sequences
$$
x_k\in U,\qquad x_k\to x,
$$
and
$$
y_k\in U,\qquad y_k\to y.
$$
By step [](#s2){.pf-ref},
$$
\norm{f(y_k)-f(x_k)}
\leq
nM\norm{y_k-x_k}.
$$
Pass to the limit using step [](#s4){.pf-ref} and continuity of the Euclidean norm:
$$
\norm{\bar f(y)-\bar f(x)}
\leq
nM\norm{y-x}.
$$

:::

:::

::: {.pf-step #s7}

The function $\bar f$ is continuous on $\overline U$.

::: pf-proof

Every Lipschitz map is continuous, and step [](#s6){.pf-ref} shows that $\bar f$ is
Lipschitz.

:::

:::

::: {.pf-step #s8}

The continuous extension of $f$ to $\overline U$ is unique.

::: pf-proof

Suppose
$$
F,G:\overline U\longrightarrow\RR^n
$$
are continuous and both restrict to $f$ on $U$. Fix
$$
x\in\overline U
$$
and choose $x_k\in U$ with $x_k\to x$. Then
$$
\begin{aligned}
F(x)
&=
\lim_{k\to\infty}F(x_k)\\
&=
\lim_{k\to\infty}f(x_k)\\
&=
\lim_{k\to\infty}G(x_k)\\
&=
G(x).
\end{aligned}
$$
Thus $F=G$ on $\overline U$.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} construct a continuous extension, and step [](#s8){.pf-ref} proves
its uniqueness.

:::

:::

:::
