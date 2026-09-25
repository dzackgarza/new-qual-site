---
schema: qual/card@1
id: P-BKS09-5B
kind: problem
title: Asymptotics of the Newtonian potential of a compactly supported function
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the codomain R and the arrows in the map and limit against s09solutions.pdf page 5 problem 5B.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked local integrability of the Newton kernel and the uniform support estimate proving the limit.
---

::: {.problem}
Let $f : \mathbb{R}^3 \to \mathbb{R}$ be a continuous function of compact support. Show that $u(x) = \int_{\mathbb{R}^3} \frac{f(y)}{|x - y|} \, dy$ is well defined and that $\lim_{|x| \to \infty} u(x) |x| = \int_{\mathbb{R}^3} f(y) \, dy$.
:::

::: {.solution}
Choose $R>0$ such that
$$
\operatorname{supp}f\subseteq\{y\in\RR^3:\abs y\leq R\},
$$
and set
$$
M\coloneqq\sup_{y\in\RR^3}\abs{f(y)}<\infty.
$$

<1>1. For every fixed $x\in\RR^3$, the integral defining $u(x)$ is
absolutely convergent.

::: {.proof}
Since $f$ vanishes outside the ball of radius $R$,
$$
\int_{\RR^3}
\frac{\abs{f(y)}}{\abs{x-y}}\,dy
\leq
M\int_{\abs y\leq R}\frac{dy}{\abs{x-y}}.
$$
Put $z=y-x$. If $\abs y\leq R$, then
$$
\abs z
=
\abs{y-x}
\leq
R+\abs x.
$$
Therefore
$$
\begin{aligned}
\int_{\abs y\leq R}\frac{dy}{\abs{x-y}}
&\leq
\int_{\abs z\leq R+\abs x}\frac{dz}{\abs z}\\
&=
4\pi\int_0^{R+\abs x}r\,dr
<\infty.
\end{aligned}
$$
Thus $u(x)$ is well defined.
:::

<1>2. If $L>R$, $\abs x\geq L$, and $y\in\operatorname{supp}f$, then
$$
\left|
\frac{\abs x}{\abs{x-y}}-1
\right|
\leq
\frac{R}{L-R}.
$$

::: {.proof}
The reverse triangle inequality gives
$$
\bigl|\abs x-\abs{x-y}\bigr|
\leq
\abs y
\leq
R,
$$
while
$$
\abs{x-y}
\geq
\abs x-\abs y
\geq
L-R.
$$
Consequently
$$
\left|
\frac{\abs x}{\abs{x-y}}-1
\right|
=
\frac{\bigl|\abs x-\abs{x-y}\bigr|}{\abs{x-y}}
\leq
\frac{R}{L-R}.
$$
:::

<1>3. If $L>R$ and $\abs x\geq L$, then
$$
\left|
\abs x\,u(x)-\int_{\RR^3}f(y)\,dy
\right|
\leq
\frac{R}{L-R}
\int_{\RR^3}\abs{f(y)}\,dy.
$$

::: {.proof}
For such $x$, the denominator $\abs{x-y}$ is nonzero on
$\operatorname{supp}f$. Hence
$$
\abs x\,u(x)-\int f(y)\,dy
=
\int
f(y)
\left(
\frac{\abs x}{\abs{x-y}}-1
\right)dy.
$$
Taking absolute values and applying step <1>2 on the support of $f$ gives
the stated estimate.
:::

<1>4. One has
$$
\boxed{
\lim_{\abs x\to\infty}\abs x\,u(x)
=
\int_{\RR^3}f(y)\,dy
}.
$$

::: {.proof}
The integral
$$
\int_{\RR^3}\abs{f(y)}\,dy
$$
is finite because $f$ is continuous with compact support. The right-hand
side of the estimate in step <1>3 tends to $0$ as $L\to\infty$.
Therefore, given $\varepsilon>0$, choosing $L$ sufficiently large makes
the difference in step <1>3 smaller than $\varepsilon$ for every
$\abs x\geq L$. This is exactly the asserted limit.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves that $u$ is well defined, and step <1>4 proves the required
asymptotic formula.
:::
:::
