---
schema: qual/card@1
id: P-CAFA25D
kind: problem
title: "Holomorphic function with constant modulus on circles is a monomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Holomorphic Functions
  - Radial Symmetry
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, (i) and (ii) as the top-level parts with (ii) as
    the QED step. Re-checked: if $f$ vanished at $z_0\ne0$ then $\varphi(\abs{z_0})=0$ and the
    identity theorem would make $f\equiv0$, contradicting $f(0)\ne0$; $1/f$ is holomorphic near the
    closed disc because $f$ has no zero there; the maximum principle on $f$ and on $1/f$ sandwiches
    $\abs f$ between $M$ and $M$ on $\abs z<r$; a nonconstant holomorphic function is open, so its
    modulus cannot be constant on an open set; and the order-$m$ factorisation $z^mh$ has
    $h(0)\ne0$ with $\abs h$ radially constant, so (i) applies to $h$. Added: the explicit
    definition of $\varphi$, the positivity of $M$, and the open-mapping step which the prose only
    named. No defect found in the statement. The collection's provenance is the Fall 2025
    examination paper, so no retained solution set covers the problem.
---

::: {.problem}
Let $f : \DD \to \CC$ be a holomorphic function in the unit disk.
Assume that $\abs{f(z)}$ is constant on each circle $\abs{z} = r$ for $0 < r < 1$; i.e., $\abs{f(re^{i\theta})} = \varphi(r)$, for some non-negative function $\varphi$ on $0 < r < 1$.

(i) Assume that $f(0) \neq 0$.
Show that $f$ is constant.

(ii) Assume that $f$ has a zero of order $m > 0$ at $z = 0$.
Show that $f(z) = cz^m$ for some constant $c$.
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own. Write $\varphi(r)=\abs{f(re^{i\theta})}$, which by hypothesis does not depend on $\theta$.

::: pf

::: {.pf-step #no-zeros}
(i) If $f(0)\ne0$ then $f$ has no zero in $\DD$.

::: pf-proof
Suppose $f(z_0)=0$ with $\abs{z_0}=r>0$. Then $\varphi(r)=\abs{f(z_0)}=0$, so $f$ vanishes on the whole circle $\abs z=r$, a set with an accumulation point in $\DD$; by the identity theorem $f\equiv0$, contradicting $f(0)\ne0$. And $z_0=0$ is excluded by hypothesis.
:::

:::

::: {.pf-step #radial-bound}
(i) For $0<r<1$, $\abs f$ is constant on the disc $\abs z<r$.

::: pf-proof
By step [](#no-zeros){.pf-ref} the function $f$ has no zero in $\DD$, so $1/f$ is holomorphic on a neighbourhood of the closed disc $\abs z\le r$. On the circle $\abs z=r$ the modulus $\abs f$ takes the constant value $M=\varphi(r)>0$ and $\abs{1/f}$ the constant value $1/M$. The maximum modulus principle applied to $f$ on $\abs z<r$ gives $\abs{f(z)}\le M$ there, and applied to $1/f$ gives $\abs{1/f(z)}\le1/M$, that is $\abs{f(z)}\ge M$. Hence $\abs{f(z)}=M$ throughout the disc.
:::

:::

::: {.pf-step #constant}
(i) If $f(0)\ne0$ then $f$ is constant.

::: pf-proof
Let $0<r<1$. By step [](#radial-bound){.pf-ref}, $\abs f$ is constant on the disc $\abs z<r$; a nonconstant holomorphic function is an open map, so its modulus cannot be constant on a nonempty open set. Hence $f$ is constant on $\abs z<r$, and since $r<1$ was arbitrary, $f$ is constant on $\DD$.
:::

:::

::: {.pf-step}
(ii) If $f$ has a zero of order $m>0$ at $0$, then $f(z)=cz^m$ for a constant $c$.

:::: pf-proof

::: {.pf-step #factor}
$f(z)=z^mh(z)$ with $h$ holomorphic on $\DD$ and $h(0)\ne0$, and $\abs h$ is constant on each circle $\abs z=r$.

::: pf-proof
The order of vanishing at $0$ being $m$ means $f(z)=z^mh(z)$ with $h$ holomorphic and $h(0)\ne0$, by the definition of the order of a zero. For $0<r<1$ and every $\theta$,
$$
\abs{h(re^{i\theta})}=\frac{\abs{f(re^{i\theta})}}{r^m}=\frac{\varphi(r)}{r^m},
$$
which does not depend on $\theta$.
:::

:::

::: {.pf-step}
(ii) $h$ is constant, so $f(z)=cz^m$.

::: pf-proof
The function $h$ is holomorphic on $\DD$ and $\abs h$ is constant on each circle $\abs z=r$ by step [](#factor){.pf-ref}, and $h(0)\ne0$; so step [](#constant){.pf-ref} applies to $h$ and gives $h\equiv c$ for some constant $c$, which is nonzero. Then $f(z)=cz^m$.
:::

:::

:::

:::

:::
:::
