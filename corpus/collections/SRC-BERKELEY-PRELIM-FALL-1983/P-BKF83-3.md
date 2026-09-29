---
schema: qual/card@1
id: P-BKF83-3
kind: problem
title: Bounded partial derivatives allow a punctured-space function to extend continuously
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the radial Cauchy limit, the great-circle oscillation estimate for n at least two, and the disconnected one-dimensional counterexample.
---

::: {.problem}
Let
\[
f:\mathbb R^n\setminus\{0\}\to\mathbb R
\]
be $C^1$, and suppose all partial derivatives are uniformly bounded:
\[
\left|\frac{\partial f}{\partial x_i}(x)\right|\le M
\]
for every $x\ne0$ and every $i$.

1. If $n\ge2$, prove that $f$ extends continuously to all of $\mathbb R^n$.
2. Show by counterexample that the assertion is false for $n=1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The gradient is uniformly bounded by
$$
\norm{\nabla f(x)}\le M\sqrt n
$$
for every $x\ne0$.

::: pf-proof

The hypothesis gives
$$
\norm{\nabla f(x)}^2
=
\sum_{i=1}^n
\left|
\frac{\partial f}{\partial x_i}(x)
\right|^2
\le
nM^2.
$$
Taking square roots gives the claim.

:::

:::

::: {.pf-step #s2}

Along the positive first coordinate axis, the limit
$$
L\coloneqq
\lim_{r\downarrow0}f(re_1)
$$
exists.

::: pf-proof

Define
$$
g(r)\coloneqq f(re_1),
\qquad
r>0.
$$
Then
$$
g'(r)
=
\frac{\partial f}{\partial x_1}(re_1),
$$
so $\abs{g'(r)}\le M$. Hence for $r,s>0$, the mean value theorem gives
$$
\abs{g(r)-g(s)}
\le
M\abs{r-s}.
$$
Thus $g(r)$ is Cauchy as $r\downarrow0$, and completeness of $\mathbb R$
gives a finite limit $L$.

:::

:::

::: {.pf-step #s3}

Assume $n\ge2$. If $x\ne0$ and $r=\norm{x}$, then
$$
\abs{f(x)-f(re_1)}
\le
\pi M\sqrt n\,r.
$$

::: pf-proof

Because $n\ge2$, the sphere
$$
\{y\in\mathbb R^n:\norm y=r\}
$$
contains a great-circle arc joining $x$ to $re_1$ of length at most
$\pi r$. Indeed, use the plane spanned by $x$ and $e_1$ when the two
directions are not antipodal, and any $2$-plane containing $e_1$ in the
antipodal case.

Parametrize such an arc by a piecewise $C^1$ curve $\gamma$. Then
step [](#s1){.pf-ref} and the chain rule give
$$
\left|
\frac{d}{dt}f(\gamma(t))
\right|
\le
M\sqrt n\,\norm{\gamma'(t)}.
$$
Integrating along the arc yields
$$
\abs{f(x)-f(re_1)}
\le
M\sqrt n\,\operatorname{length}(\gamma)
\le
\pi M\sqrt n\,r.
$$

:::

:::

::: {.pf-step #s4}

If $n\ge2$, defining
$$
\widetilde f(0)\coloneqq L,
\qquad
\widetilde f(x)\coloneqq f(x)
\quad(x\ne0),
$$
gives a continuous function
$$
\widetilde f:\mathbb R^n\longrightarrow\mathbb R.
$$

::: pf-proof

Continuity away from $0$ is inherited from $f$. Let $x\to0$, $x\ne0$,
and put $r=\norm{x}$. By steps [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\begin{aligned}
\abs{f(x)-L}
&\le
\abs{f(x)-f(re_1)}
+
\abs{f(re_1)-L}\\
&\le
\pi M\sqrt n\,r+\abs{g(r)-L}
\longrightarrow0.
\end{aligned}
$$
Thus $\widetilde f$ is continuous at $0$.

:::

:::

::: {.pf-step #s5}

For $n=1$, the assertion is false.

::: pf-proof

Define
$$
f(x)
\coloneqq
\begin{cases}
0,&x<0,\\
1,&x>0.
\end{cases}
$$
This function is $C^1$ on
$$
\mathbb R\setminus\{0\},
$$
and
$$
f'(x)=0
$$
there, so its derivative is uniformly bounded. But
$$
\lim_{x\uparrow0}f(x)=0,
\qquad
\lim_{x\downarrow0}f(x)=1,
$$
so no continuous extension to $0$ exists.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the extension statement for $n\ge2$, and step [](#s5){.pf-ref} gives
the required one-dimensional counterexample.

:::

:::

:::
