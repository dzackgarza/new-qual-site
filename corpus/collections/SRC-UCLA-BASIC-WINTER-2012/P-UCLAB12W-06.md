---
schema: qual/card@1
id: P-UCLAB12W-06
kind: problem
title: Integral around a loop winding once clockwise around the origin
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let $\gamma$ be a smooth curve from $(1,0)$ to $(1,0)$ in $\RR^2\setminus\{(0,0)\}$ winding once around the origin in the clockwise direction.
Compute
$$
I(\gamma)=\int_\gamma\frac{y\,dx-x\,dy}{x^2+y^2}.
$$
:::

::: {.solution}

Choose a smooth parametrization
$$
\gamma(t)=(x(t),y(t)),
\qquad 0\le t\le1,
$$
with $\gamma(0)=\gamma(1)=(1,0)$.

::: pf

::: pf-step

There is a smooth real-valued argument function $\theta(t)$ such that
$$
\frac{x(t)+iy(t)}{\sqrt{x(t)^2+y(t)^2}}
=e^{i\theta(t)}
$$
for all $t$, with $\theta(0)=0$.


::: pf-proof

The normalized path
$$
t\longmapsto \frac{x(t)+iy(t)}{\sqrt{x(t)^2+y(t)^2}}
$$
lands in the unit circle and begins at $1$. The covering map
$$
\RR\to S^1,
\qquad
\theta\longmapsto e^{i\theta}
$$
has the path-lifting property, so the normalized path has a unique lift beginning at $0$. Because the original path is smooth, the lift is smooth.

:::

:::

::: {.pf-step #s1-2}

Along the path,
$$
\theta'(t)
=
\frac{x(t)y'(t)-y(t)x'(t)}{x(t)^2+y(t)^2}.
$$


::: pf-proof

Write
$$
x(t)=r(t)\cos\theta(t),
\qquad
y(t)=r(t)\sin\theta(t),
$$
where
$$
r(t)=\sqrt{x(t)^2+y(t)^2}>0.
$$
Differentiating gives
$$
\begin{aligned}
x'&=r'\cos\theta-r\theta'\sin\theta,\\
y'&=r'\sin\theta+r\theta'\cos\theta.
\end{aligned}
$$
Therefore
$$
x y'-y x'
=r^2\theta'
=(x^2+y^2)\theta',
$$
which yields the formula.

:::

:::

::: {.pf-step #s1-3}

The integral satisfies
$$
I(\gamma)
=-\bigl(\theta(1)-\theta(0)\bigr).
$$


::: pf-proof

Using the parametrization and step [](#s1-2){.pf-ref},
$$
\begin{aligned}
I(\gamma)
&=\int_0^1
\frac{y(t)x'(t)-x(t)y'(t)}{x(t)^2+y(t)^2}\,dt\\
&=-\int_0^1\theta'(t)\,dt\\
&=-\bigl(\theta(1)-\theta(0)\bigr).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Since $\gamma$ winds once clockwise around the origin,
$$
\theta(1)-\theta(0)=-2\pi.
$$


::: pf-proof

For a closed loop in $\RR^2\setminus\{0\}$, the total change of a lifted argument is $2\pi$ times its winding number about the origin. A single clockwise winding has winding number $-1$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{I(\gamma)=2\pi}.
$$


::: pf-proof

Substitute the value from step [](#s1-4){.pf-ref} into step [](#s1-3){.pf-ref}:
$$
I(\gamma)=-(-2\pi)=2\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested value of the integral.

:::

:::

:::
