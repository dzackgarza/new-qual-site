---
schema: qual/card@1
id: P-BERK87S-13
kind: problem
title: Bounded first partial derivatives force a removable puncture for a $C^1$ real function
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
    Bounded partial derivatives give a uniform gradient bound. Any two points
    in a punctured disk of radius r can be joined away from the origin by
    radial segments and a circular arc of length at most (2+pi)r, so the
    oscillation of f there is O(r). This makes values along any sequence
    approaching the puncture converge to one common limit.
---

::: {.problem}
Let $f:\mathbb R^2\setminus\{(0,0)\}\to\mathbb R$ be $C^1$. Suppose there is $M>0$ such that
\[
\left|\frac{\partial f}{\partial x}\right|\le M,
\qquad
\left|\frac{\partial f}{\partial y}\right|\le M
\]
throughout the punctured plane. Prove that
\[
\lim_{(x,y)\to(0,0)}f(x,y)
\]
exists.
:::

::: {.solution}
Set
$$
C\coloneqq\sqrt2\,M.
$$

::: pf

::: {.pf-step #gradient-bound}
At every point of the punctured plane,
$$
\norm{\nabla f}\leq C.
$$

::: pf-proof
The hypotheses give
$$
\abs{f_x}\leq M,
\qquad
\abs{f_y}\leq M.
$$
Therefore
$$
\norm{\nabla f}
=
\sqrt{f_x^2+f_y^2}
\leq
\sqrt{M^2+M^2}
=
\sqrt2\,M
=C.
$$
:::

:::

::: {.pf-step #path-exists}
If $p,q\in\RR^2\setminus\{0\}$ satisfy
$$
\norm{p}<r,
\qquad
\norm{q}<r,
$$
then there is a piecewise $C^1$ path in the punctured disk
$$
\{z:0<\norm{z}<r\}
$$
joining $p$ to $q$ whose length is less than
$$
(2+\pi)r.
$$

::: pf-proof
Put
$$
R\coloneqq\max\{\norm{p},\norm{q}\}<r.
$$
Move radially from $p$ to the point on the same ray having norm $R$,
then along the shorter circular arc of radius $R$ to the ray through
$q$, and finally radially to $q$.

The two radial pieces have total length at most $2R$, and the shorter
arc has length at most $\pi R$. Thus the total length is at most
$$
(2+\pi)R
<
(2+\pi)r.
$$
Every point on the path has positive norm at most $R$, so the path avoids
the origin.
:::

:::

::: {.pf-step #oscillation-bound}
For any $p,q$ as in step [](#path-exists){.pf-ref},
$$
\abs{f(p)-f(q)}
<
C(2+\pi)r.
$$

::: pf-proof
Let $\gamma$ be the path from step [](#path-exists){.pf-ref}, parametrized piecewise by arc
length. Along each smooth piece,
$$
\frac{d}{dt}f(\gamma(t))
=
\inner{\nabla f(\gamma(t))}{\gamma'(t)}.
$$
Hence, by step [](#gradient-bound){.pf-ref},
$$
\abs{\frac{d}{dt}f(\gamma(t))}
\leq
C\norm{\gamma'(t)}.
$$
Integrating along all pieces gives
$$
\abs{f(p)-f(q)}
\leq
C\,\operatorname{length}(\gamma)
<
C(2+\pi)r.
$$
:::

:::

::: {.pf-step #sequence-converges}
The sequence
$$
a_n\coloneqq f(1/n,0)
$$
is Cauchy and therefore converges to some $L\in\RR$.

::: pf-proof
Let $\varepsilon>0$. Choose $N$ so large that
$$
\frac{C(2+\pi)}{N}<\varepsilon.
$$
If $m,n>N$, then both points
$$
(1/m,0),
\qquad
(1/n,0)
$$
have norm less than $1/N$. Step [](#oscillation-bound){.pf-ref}, with $r=1/N$, gives
$$
\abs{a_m-a_n}<\varepsilon.
$$
Thus $(a_n)$ is Cauchy. Completeness of $\RR$ gives a limit $L$.
:::

:::

::: {.pf-step #limit-boxed}
One has
$$
\boxed{
\lim_{p\to0}f(p)=L
}.
$$

::: pf-proof
Let $\varepsilon>0$. Choose $r>0$ such that
$$
C(2+\pi)r<\frac{\varepsilon}{2}.
$$
By step [](#sequence-converges){.pf-ref}, choose $n$ large enough that
$$
\frac1n<r
$$
and
$$
\abs{f(1/n,0)-L}<\frac{\varepsilon}{2}.
$$
If
$$
0<\norm{p}<r,
$$
then step [](#oscillation-bound){.pf-ref}, applied to $p$ and $(1/n,0)$, gives
$$
\abs{f(p)-f(1/n,0)}
<
\frac{\varepsilon}{2}.
$$
Therefore
$$
\begin{aligned}
\abs{f(p)-L}
&\leq
\abs{f(p)-f(1/n,0)}
+
\abs{f(1/n,0)-L}\\
&<
\varepsilon.
\end{aligned}
$$
This is precisely the definition of the limit at the puncture.
:::

:::

::: pf-qed
Step [](#limit-boxed){.pf-ref} proves that the required finite limit exists.
:::

:::
:::
