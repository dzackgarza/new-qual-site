---
schema: qual/card@1
id: P-BKF14-3A
kind: problem
title: Bounding $f'$ in terms of bounds on $f$ and $f''$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet and its
    triangular lower bound for f' coming from |f''|<=1.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Lipschitz estimate for f', the area bound M^2<=2, and the
    equality case needed to obtain the strict bound |f'|<sqrt(2).
---

::: {.problem}
Suppose that $f$ is a twice-differentiable real-valued function on the real line such that $\abs{f(x)}\le1$ and $\abs{f''(x)}\le1$ for all $x$. Find, with proof, a constant $b$ such that $\abs{f'(x)}<b$ for all $x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For all $x,y\in\RR$,
$$
|f'(x)-f'(y)|\le|x-y|.
$$

::: pf-proof

If $x\ne y$, the mean value theorem applied to $f'$ gives a point
$c$ between $x$ and $y$ such that
$$
f'(x)-f'(y)=f''(c)(x-y).
$$
Since $|f''(c)|\le1$, the claimed estimate follows. The case $x=y$ is
immediate.

:::

:::

::: {.pf-step #s2}

Fix $x_0\in\RR$ and put $M\coloneqq|f'(x_0)|$. After replacing
$f$ by $-f$ if necessary, one may assume $f'(x_0)=M\ge0$, and then
$$
f'(x_0+t)\ge M-|t|
\qquad
(-M\le t\le M).
$$

::: pf-proof

Replacing $f$ by $-f$ preserves the hypotheses and the value of
$|f'(x_0)|$. Under the resulting assumption $f'(x_0)=M$, step [](#s1){.pf-ref}
gives
$$
f'(x_0+t)
\ge
f'(x_0)-|t|
=
M-|t|.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
M^2\le2.
$$

::: pf-proof

Since $f'$ is continuous, the fundamental theorem of calculus and step
[](#s2){.pf-ref} give
$$
\begin{aligned}
f(x_0+M)-f(x_0-M)
&=
\int_{-M}^{M}f'(x_0+t)\,dt\\
&\ge
\int_{-M}^{M}(M-|t|)\,dt\\
&=
M^2.
\end{aligned}
$$
On the other hand, $|f|\le1$, so
$$
f(x_0+M)-f(x_0-M)\le2.
$$
Combining the inequalities yields $M^2\le2$.

:::

:::

::: {.pf-step #s4}

In fact,
$$
M^2<2.
$$

::: pf-proof

Suppose instead that $M^2=2$. Then every inequality in step [](#s3){.pf-ref} must
be an equality. In particular, the continuous nonnegative function
$$
q(t)\coloneqq
f'(x_0+t)-(M-|t|)
$$
has integral $0$ on $[-M,M]$, so $q(t)=0$ throughout that interval.
Hence
$$
f'(x_0+t)=
\begin{cases}
M+t,&-M\le t\le0,\\
M-t,&0\le t\le M.
\end{cases}
$$
The left derivative of $f'$ at $x_0$ would then be $1$, while its right
derivative would be $-1$. This contradicts the existence of
$f''(x_0)$. Thus equality is impossible.

:::

:::

::: {.pf-step #s5}

The choice
$$
\boxed{b=\sqrt2}
$$
works.

::: pf-proof

The point $x_0$ was arbitrary. By step [](#s4){.pf-ref},
$$
|f'(x_0)|^2=M^2<2,
$$
and therefore $|f'(x_0)|<\sqrt2$ for every $x_0\in\RR$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} supplies the required constant and bound.

:::

:::

:::
