---
schema: qual/card@1
id: P-AZOFF-B01
kind: problem
title: Continuity and differentiability of $xy/\sqrt{x^2+y^2}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Several variables, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Bounded |xy| by (x^2+y^2)/2 to prove continuity at the origin, computed
    the derivative away from the origin, and checked both partial derivatives
    at the origin are zero. Differentiability at the origin would therefore
    have zero derivative, but along (t,t) the normalized remainder is
    identically 1/2. The source compilation contains no worked solution.
---

::: {.problem}
Discuss continuity and differentiability of the function $f : \mathbb { R } ^ { 2 } \to \mathbb { R }$ defined by

$$
f ( x , y ) = \left\{ \begin{array} { l l } { \frac { x y } { \sqrt { x ^ { 2 } + y ^ { 2 } } } , \qquad } & { ( x , y ) \neq ( 0 , 0 ) } \\ { 0 , } & { ( x , y ) = ( 0 , 0 ) } \end{array} . \right.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $f$ is continuous at $(0,0)$.

::: pf-proof

For $(x,y)\neq(0,0)$, the inequality
$$
2\abs{xy}\leq x^2+y^2
$$
gives
$$
\abs{f(x,y)}
=
\frac{\abs{xy}}{\sqrt{x^2+y^2}}
\leq
\frac12\sqrt{x^2+y^2}.
$$
The right-hand side tends to $0=f(0,0)$ as $(x,y)\to(0,0)$. Hence $f$ is
continuous at the origin.

:::

:::

::: {.pf-step #s2}

The function $f$ is differentiable at every
$$
(x,y)\neq(0,0),
$$
and there
$$
Df(x,y)(h,k)
=
\frac{y^3h+x^3k}{(x^2+y^2)^{3/2}}.
$$

::: pf-proof

Away from the origin, the denominator
$$
\sqrt{x^2+y^2}
$$
is nonzero, so $f$ is a composition of smooth functions. Direct
differentiation gives
$$
\frac{\partial f}{\partial x}
=
\frac{y^3}{(x^2+y^2)^{3/2}},
\qquad
\frac{\partial f}{\partial y}
=
\frac{x^3}{(x^2+y^2)^{3/2}}.
$$
Thus the total derivative has the displayed form.

:::

:::

::: {.pf-step #s3}

Both first partial derivatives of $f$ exist at $(0,0)$ and equal
$0$.

::: pf-proof

Along either coordinate axis, $f$ is identically zero:
$$
f(h,0)=0,
\qquad
f(0,k)=0.
$$
Therefore
$$
\frac{\partial f}{\partial x}(0,0)
=
\lim_{h\to0}\frac{f(h,0)-f(0,0)}h
=
0
$$
and similarly
$$
\frac{\partial f}{\partial y}(0,0)=0.
$$

:::

:::

::: {.pf-step #s4}

The function $f$ is not differentiable at $(0,0)$.

::: pf-proof

If $f$ were differentiable at the origin, step [](#s3){.pf-ref} would force its derivative
there to be the zero linear map. Differentiability would then imply
$$
\frac{\abs{f(h,k)}}{\sqrt{h^2+k^2}}
\longrightarrow
0
$$
as $(h,k)\to(0,0)$.

For $t\neq0$, however,
$$
f(t,t)
=
\frac{t^2}{\sqrt{2t^2}}
=
\frac{\abs t}{\sqrt2},
$$
so
$$
\frac{\abs{f(t,t)}}{\sqrt{t^2+t^2}}
=
\frac12.
$$
This does not tend to zero as $t\to0$. Hence $f$ is not differentiable at
the origin.

:::

:::

::: {.pf-step #s5}

Consequently,
$$
\boxed{
f\text{ is continuous on }\RR^2
\text{ and differentiable exactly on }\RR^2\sm\{(0,0)\}.
}
$$

::: pf-proof

Step [](#s1){.pf-ref} proves continuity at the only point where the defining formula is
not manifestly continuous; away from the origin continuity follows from
step [](#s2){.pf-ref}. Step [](#s2){.pf-ref} proves differentiability off the origin, while step
[](#s4){.pf-ref} rules it out at the origin.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the requested continuity and differentiability
classification.

:::

:::

:::
