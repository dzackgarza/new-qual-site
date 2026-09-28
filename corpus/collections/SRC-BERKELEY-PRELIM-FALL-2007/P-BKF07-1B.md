---
schema: qual/card@1
id: P-BKF07-1B
kind: problem
title: A polynomial orbit is never dense in the complex plane
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the bounded-orbit case, the explicit affine iterates,
    and the escape-radius argument for degree at least two against the vendored
    solution.
---

::: {.problem}
Let \(f\in\mathbb C[z]\) and \(a\in\mathbb C\). Prove that the forward orbit
\[
\{a,f(a),f(f(a)),\ldots\}
\]
is not dense in \(\mathbb C\).
:::

::: {.solution}
Write
$$
z_n\coloneqq f^{\circ n}(a)
\qquad(n\ge0),
$$
and let $S\coloneqq\{z_n:n\ge0\}$.

<1>1. If $S$ is bounded, then $S$ is not dense in $\CC$.

::: {.proof}
Choose $R>0$ with $S\subseteq\{z:\abs{z}\le R\}$. Then the nonempty
open set
$$
\{z:\abs{z}>R\}
$$
is disjoint from $S$, so $S$ is not dense.
:::

<1>2. If $f$ is constant, then $S$ is not dense in $\CC$.

::: {.proof}
If $f(z)=c$ for every $z$, then
$$
S\subseteq\{a,c\},
$$
so $S$ is finite and hence is not dense in $\CC$.
:::

<1>3. If $\deg f=1$, then $S$ is not dense in $\CC$.

::: {.proof}
Write $f(z)=sz+t$ with $s\ne0$. If $s=1$, then
$$
z_n=a+nt,
$$
so $S$ lies in the affine real line $a+\RR t$ and is not dense in
$\CC$.

Suppose $s\ne1$. The point
$$
c\coloneqq\frac{t}{1-s}
$$
is fixed by $f$, and induction gives
$$
z_n-c=s^n(a-c).
$$
If $S$ is bounded, step <1>1 applies. If $S$ is unbounded, then
$a\ne c$ and $\abs{s}>1$. Consequently
$$
\abs{z_n-c}=\abs{s}^n\abs{a-c}\ge\abs{a-c}
$$
for every $n\ge0$. Thus the open disk
$$
\left\{z:\abs{z-c}<\frac{\abs{a-c}}2\right\}
$$
is disjoint from $S$, proving that $S$ is not dense.
:::

<1>4. If $\deg f\ge2$, then $S$ is not dense in $\CC$.

::: {.proof}
If $S$ is bounded, step <1>1 applies. Assume therefore that $S$ is
unbounded. Since
$$
\frac{\abs{f(z)}}{\abs{z}}\longrightarrow\infty
\qquad\text{as }\abs{z}\longrightarrow\infty,
$$
there exists $R>0$ such that
$$
\abs{z}>R
\quad\Longrightarrow\quad
\abs{f(z)}>\abs{z}.
$$
Unboundedness gives an index $n_0$ with $\abs{z_{n_0}}>R$. Inductively,
$$
\abs{z_n}>R
$$
for every $n\ge n_0$. Hence
$$
S\cap\{z:\abs{z}<R\}
$$
is contained in the finite set
$\{z_0,\ldots,z_{n_0-1}\}$.

Choose a point $w$ in the disk $\{z:\abs{z}<R\}$ different from each
of those finitely many points. A sufficiently small open disk about
$w$ is still contained in $\{z:\abs{z}<R\}$ and avoids
$z_0,\ldots,z_{n_0-1}$. It also avoids every $z_n$ with $n\ge n_0$.
Thus this open disk is disjoint from $S$, so $S$ is not dense.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 handles constant polynomials, step <1>3 handles degree $1$,
and step <1>4 handles degree at least $2$. These cases exhaust all
polynomials.
:::
:::
