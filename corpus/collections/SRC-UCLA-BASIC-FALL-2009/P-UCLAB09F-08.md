---
schema: qual/card@1
id: P-UCLAB09F-08
kind: problem
title: Matrix exponentials solve constant-coefficient systems
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
For $A\in M_n(\mathbb R)$ define
\[
e^A:=\sum_{k=0}^\infty \frac{A^k}{k!}.
\]
Let $v_0\in\mathbb R^n$.
Prove that
\[
v(t)=e^{At}v_0
\]
solves
\[
v'(t)=Av(t),\qquad v(0)=v_0.
\]
Explain precisely which theorems from calculus you use and why they apply.
:::

::: {.solution}
Fix any submultiplicative matrix norm $\|\cdot\|$ on $M_n(\mathbb R)$, for example the operator norm induced by the Euclidean norm.

<1>1. For every $R>0$, the matrix series
\[
E(t)
=
\sum_{k=0}^{\infty}\frac{A^kt^k}{k!}
\]
converges uniformly for $|t|\le R$.

::: {.proof}
For $|t|\le R$,
\[
\left\|
\frac{A^kt^k}{k!}
\right\|
\le
\frac{\|A\|^kR^k}{k!}.
\]
The scalar series
\[
\sum_{k=0}^{\infty}\frac{\|A\|^kR^k}{k!}
=
e^{\|A\|R}
\]
converges. The Weierstrass $M$-test therefore gives uniform convergence of the matrix series on $[-R,R]$, equivalently uniform convergence of each entry series.
:::

<1>2. For every $R>0$, the series obtained by differentiating each term,
\[
\sum_{k=1}^{\infty}
\frac{kA^kt^{k-1}}{k!},
\]
also converges uniformly for $|t|\le R$.

::: {.proof}
For $|t|\le R$,
\[
\left\|
\frac{kA^kt^{k-1}}{k!}
\right\|
\le
\frac{\|A\|^kR^{k-1}}{(k-1)!}.
\]
The scalar majorant satisfies
\[
\sum_{k=1}^{\infty}
\frac{\|A\|^kR^{k-1}}{(k-1)!}
=
\|A\|e^{\|A\|R},
\]
so the Weierstrass $M$-test again gives uniform convergence.
:::

<1>3. The function $E:\mathbb R\to M_n(\mathbb R)$ is differentiable and may be differentiated term by term:
\[
E'(t)
=
\sum_{k=1}^{\infty}
\frac{A^kt^{k-1}}{(k-1)!}.
\]

::: {.proof}
Apply the standard termwise-differentiation theorem for series of $C^1$ functions on a compact interval: if the derivative series converges uniformly and the original series converges at one point, then the original series converges to a differentiable function whose derivative is the sum of the derivative series.

For each fixed $R$, step <1>2 gives uniform convergence of the derivative series on $[-R,R]$, and at $t=0$ the original series converges trivially to $I$. Applying the theorem entrywise gives the displayed derivative on $[-R,R]$. Since $R$ is arbitrary, the formula holds for every real $t$.
:::

<1>4. One has
\[
\boxed{E'(t)=AE(t)}.
\]

::: {.proof}
By step <1>3,
\[
\begin{aligned}
E'(t)
&=
\sum_{k=1}^{\infty}
\frac{A^kt^{k-1}}{(k-1)!}\\
&=
A
\sum_{j=0}^{\infty}
\frac{A^jt^j}{j!}\\
&=
AE(t),
\end{aligned}
\]
where $j=k-1$. Multiplication by the fixed matrix $A$ may be pulled through the convergent series because matrix multiplication is continuous and linear in the second factor.
:::

<1>5. The function
\[
v(t)=E(t)v_0
\]
is differentiable and satisfies
\[
v'(t)=Av(t).
\]

::: {.proof}
Multiplication by the fixed vector $v_0$ is a linear continuous map
\[
M_n(\mathbb R)\to\mathbb R^n.
\]
Hence
\[
v'(t)=E'(t)v_0.
\]
Using step <1>4,
\[
v'(t)
=
AE(t)v_0
=
Av(t).
\]
:::

<1>6. One has
\[
v(0)=v_0.
\]

::: {.proof}
At $t=0$,
\[
E(0)
=
\sum_{k=0}^{\infty}\frac{A^k0^k}{k!}
=
I.
\]
Therefore
\[
v(0)=Iv_0=v_0.
\]
:::

<1>7. Hence
\[
\boxed{v(t)=e^{At}v_0}
\]
solves
\[
v'(t)=Av(t),
\qquad
v(0)=v_0.
\]

::: {.proof}
Step <1>5 proves the differential equation and step <1>6 proves the initial condition.
:::

<1>8. Q.E.D.

::: {.proof}
The calculus inputs used are the Weierstrass $M$-test and the termwise-differentiation theorem for uniformly convergent derivative series, with their hypotheses verified in steps <1>1--<1>3.
:::
:::
