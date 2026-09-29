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

::: pf

::: {.pf-step #u-well-defined}
For every fixed $x\in\RR^3$, the integral defining $u(x)$ is
absolutely convergent.

::: pf-proof
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

:::

::: {.pf-step #ratio-estimate}
If $L>R$, $\abs x\geq L$, and $y\in\operatorname{supp}f$, then
$$
\left|
\frac{\abs x}{\abs{x-y}}-1
\right|
\leq
\frac{R}{L-R}.
$$

::: pf-proof
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

:::

::: {.pf-step #difference-bound}
If $L>R$ and $\abs x\geq L$, then
$$
\left|
\abs x\,u(x)-\int_{\RR^3}f(y)\,dy
\right|
\leq
\frac{R}{L-R}
\int_{\RR^3}\abs{f(y)}\,dy.
$$

::: pf-proof
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
Taking absolute values and applying step [](#ratio-estimate){.pf-ref} on the support of $f$ gives
the stated estimate.
:::

:::

::: {.pf-step #limit-formula}
One has
$$
\boxed{
\lim_{\abs x\to\infty}\abs x\,u(x)
=
\int_{\RR^3}f(y)\,dy
}.
$$

::: pf-proof
The integral
$$
\int_{\RR^3}\abs{f(y)}\,dy
$$
is finite because $f$ is continuous with compact support. The right-hand
side of the estimate in step [](#difference-bound){.pf-ref} tends to $0$ as $L\to\infty$.
Therefore, given $\varepsilon>0$, choosing $L$ sufficiently large makes
the difference in step [](#difference-bound){.pf-ref} smaller than $\varepsilon$ for every
$\abs x\geq L$. This is exactly the asserted limit.
:::

:::

::: pf-qed
Step [](#u-well-defined){.pf-ref} proves that $u$ is well defined, and step [](#limit-formula){.pf-ref} proves the required
asymptotic formula.
:::

:::

:::
