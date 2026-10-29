---
schema: qual/card@1
id: P-UCLAB13F-05
kind: problem
title: Monotonicity of the gradient implies convexity
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
A function $f:\RR^d\to\RR$ is convex if
\[
f(tx+(1-t)y)\le tf(x)+(1-t)f(y)
\]
for all $x,y\in\RR^d$ and $0\le t\le1$.

Assume that $f$ is continuously differentiable and
\[
(\nabla f(x)-\nabla f(y))\cdot(x-y)\ge0
\]
for all $x,y\in\RR^d$. Prove that $f$ is convex.
:::

::: {.solution}

Fix $x,y\in\RR^d$ and put
\[
v=x-y,
\qquad
g(t)=f(y+tv),
\qquad
0\le t\le1.
\]

::: pf

::: {.pf-step #s1-1}

One has
\[
g'(t)=\nabla f(y+tv)\cdot v.
\]


::: pf-proof

This is the chain rule applied to the affine path
\[
t\longmapsto y+tv.
\]

:::

:::

::: {.pf-step #s1-2}

If $0\le s<t\le1$, then
\[
g'(t)\ge g'(s).
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
g'(t)-g'(s)
=
\bigl(
\nabla f(y+tv)-\nabla f(y+sv)
\bigr)\cdot v.
\]
Apply the hypothesis to
\[
x_t=y+tv,
\qquad
x_s=y+sv.
\]
Since
\[
x_t-x_s=(t-s)v,
\]
the hypothesis gives
\[
\bigl(
\nabla f(x_t)-\nabla f(x_s)
\bigr)\cdot((t-s)v)
\ge0.
\]
Dividing by $t-s>0$ yields
\[
g'(t)-g'(s)\ge0.
\]

:::

:::

::: {.pf-step #s1-3}

For every $0<\alpha<1$,
\[
\frac{g(\alpha)-g(0)}{\alpha}
\le
\frac{g(1)-g(\alpha)}{1-\alpha}.
\]


::: pf-proof

By the fundamental theorem of calculus,
\[
g(\alpha)-g(0)
=
\int_0^\alpha g'(t)\,dt
\]
and
\[
g(1)-g(\alpha)
=
\int_\alpha^1g'(t)\,dt.
\]
Since $g'$ is nondecreasing by step [](#s1-2){.pf-ref}, every value of $g'$ on $[0,\alpha]$ is at most every value on $[\alpha,1]$.
Hence the average of $g'$ on the first interval is at most its average on the second:
\[
\frac1\alpha\int_0^\alpha g'(t)\,dt
\le
\frac1{1-\alpha}\int_\alpha^1g'(t)\,dt.
\]
Substitute the two integral identities.

:::

:::

::: {.pf-step #s1-4}

For every $0\le\alpha\le1$,
\[
g(\alpha)
\le
(1-\alpha)g(0)+\alpha g(1).
\]


::: pf-proof

For $0<\alpha<1$, multiply step [](#s1-3){.pf-ref} by $\alpha(1-\alpha)$:
\[
(1-\alpha)(g(\alpha)-g(0))
\le
\alpha(g(1)-g(\alpha)).
\]
Rearranging gives the displayed inequality.
For $\alpha=0$ or $1$, it is equality.

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
f(\alpha x+(1-\alpha)y)
\le
\alpha f(x)+(1-\alpha)f(y)
\]
for all $x,y$ and $0\le\alpha\le1$.


::: pf-proof

By definition,
\[
g(0)=f(y),
\qquad
g(1)=f(x),
\]
and
\[
g(\alpha)
=
f(y+\alpha(x-y))
=
f(\alpha x+(1-\alpha)y).
\]
Substitute these identities into step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Thus
\[
\boxed{f\text{ is convex}}.
\]


::: pf-proof

Step [](#s1-5){.pf-ref} is exactly the defining convexity inequality.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
