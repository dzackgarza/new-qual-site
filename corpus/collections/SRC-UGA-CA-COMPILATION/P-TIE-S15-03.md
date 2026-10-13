---
schema: qual/card@1
id: P-TIE-S15-03
kind: problem
title: Analytic functions with equal modulus differ by a unimodular constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 3.
---

::: {.problem}
Let f and g be non-zero analytic functions on a region Ω. Assume $| f ( z ) | = | g ( z ) |$ for all z in Ω. Show that $f ( z ) = e ^ { i \theta } g ( z )$ in Ω for some $0 \leq \theta < 2 \pi$ .
:::

::: {.solution}
<1>1. The functions $f$ and $g$ have exactly the same zeros.

::: {.proof}
If $f(z_0)=0$, then
$$
\abs{g(z_0)}
=
\abs{f(z_0)}
=0,
$$
so $g(z_0)=0$. The converse is identical.
:::

<1>2. At every common zero $z_0$, the orders of vanishing of $f$ and $g$ are equal.

::: {.proof}
Suppose
$$
f(z)
=(z-z_0)^m u(z),
\qquad
g(z)
=(z-z_0)^n v(z),
$$
where $u$ and $v$ are holomorphic near $z_0$ and
$$
u(z_0)\ne0,
\qquad
v(z_0)\ne0.
$$
For $z\ne z_0$ near $z_0$, the hypothesis gives
$$
\abs{z-z_0}^{m-n}
\frac{\abs{u(z)}}{\abs{v(z)}}
=1.
$$
As $z\to z_0$, the quotient
$$
\frac{\abs{u(z)}}{\abs{v(z)}}
$$
tends to the positive finite number
$$
\frac{\abs{u(z_0)}}{\abs{v(z_0)}}.
$$
If $m>n$, the left-hand side would tend to $0$; if $m<n$, it would tend to $+\infty$. Therefore $m=n$.
:::

<1>3. The quotient
$$
h(z)\coloneqq\frac{f(z)}{g(z)}
$$
extends to a holomorphic nowhere-zero function on all of $\Omega$.

::: {.proof}
Away from the zeros of $g$, the quotient is holomorphic. At a common zero $z_0$, step <1>2 gives equal order $m$, so
$$
\frac{f(z)}{g(z)}
=
\frac{u(z)}{v(z)}
$$
near $z_0$, with $v(z_0)\ne0$. Thus the quotient has a removable singularity there and extends holomorphically with nonzero value $u(z_0)/v(z_0)$. Repeating this at every common zero gives the asserted extension.
:::

<1>4. The extended function $h$ satisfies
$$
\abs{h(z)}=1
$$
for every $z\in\Omega$.

::: {.proof}
At every point where $g(z)\ne0$,
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{g(z)}}
=1.
$$
These points are dense in $\Omega$, because a nonzero holomorphic function has isolated zeros. By continuity of the holomorphic extension from step <1>3, the identity $\abs{h}=1$ holds at the common zeros as well.
:::

<1>5. The function $h$ is constant.

::: {.proof}
If $h$ were nonconstant, the open mapping theorem would imply that
$$
h(\Omega)
$$
is an open subset of $\CC$. But step <1>4 gives
$$
h(\Omega)\subset\{w\in\CC:\abs{w}=1\},
$$
and the unit circle has empty interior in $\CC$. This is impossible. Hence $h$ is constant.
:::

<1>6. There exists $\theta$ with $0\le\theta<2\pi$ such that
$$
\boxed{
f(z)=e^{i\theta}g(z)
}
$$
for every $z\in\Omega$.

::: {.proof}
By step <1>5,
$$
h(z)\equiv c
$$
for some constant $c$. Step <1>4 gives $\abs{c}=1$, so
$$
c=e^{i\theta}
$$
for some unique $\theta\in[0,2\pi)$. Since $h=f/g$, the displayed identity follows.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
