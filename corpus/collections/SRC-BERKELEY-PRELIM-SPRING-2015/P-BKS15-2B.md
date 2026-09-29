---
schema: qual/card@1
id: P-BKS15-2B
kind: problem
title: Maximum-area triangle inscribed in an ellipse
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked affine area scaling, the unit-circle chord and area formulas, and the strict concavity argument giving the equilateral maximizer.
---

::: {.problem}
Find the maximum area of all triangles that can be inscribed in an ellipse with semiaxes $a$ and $b$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The linear map
$$
T(u,v)=(au,bv)
$$
maps the unit circle onto the ellipse with semiaxes $a$ and $b$, and multiplies every triangle area by $ab$.

::: pf-proof

The unit circle has equation
$$
u^2+v^2=1.
$$
Writing $(x,y)=T(u,v)$ gives
$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,
$$
so $T$ maps the unit circle onto the given ellipse. Since
$$
\det T=ab,
$$
the absolute area-scaling factor is $ab$.

:::

:::

::: {.pf-step #s2}

Let a nondegenerate triangle inscribed in the unit circle have interior angles $A,B,C$. Its side lengths opposite these angles are respectively
$$
2\sin A,
\qquad
2\sin B,
\qquad
2\sin C.
$$

::: pf-proof

The central angle subtending the side opposite $A$ is $2A$. A chord of the unit circle subtending a central angle $2A$ has length
$$
2\sin A.
$$
The same argument applies to the other two sides.

:::

:::

::: {.pf-step #s3}

The area $K$ of such a triangle is
$$
K=2\sin A\sin B\sin C.
$$

::: pf-proof

Using the two sides adjacent to the angle $A$ and step [](#s2){.pf-ref},
$$
\begin{aligned}
K
&=
\frac12(2\sin B)(2\sin C)\sin A\\
&=
2\sin A\sin B\sin C.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

If $A,B,C>0$ and $A+B+C=\pi$, then
$$
\sin A\sin B\sin C
\leq
\left(\frac{\sqrt3}{2}\right)^3,
$$
with equality exactly when
$$
A=B=C=\frac\pi3.
$$

::: pf-proof

On $(0,\pi)$, set
$$
h(x)=\log(\sin x).
$$
Then
$$
h''(x)=-\csc^2x<0,
$$
so $h$ is strictly concave. Jensen's inequality gives
$$
\frac{h(A)+h(B)+h(C)}3
\leq
h\left(\frac{A+B+C}{3}\right)
=
h\left(\frac\pi3\right).
$$
Exponentiating yields
$$
\sin A\sin B\sin C
\leq
\sin^3\left(\frac\pi3\right)
=
\left(\frac{\sqrt3}{2}\right)^3.
$$
Strict concavity gives equality exactly when $A=B=C$.

:::

:::

::: {.pf-step #s5}

The maximum area of a triangle inscribed in the unit circle is
$$
\frac{3\sqrt3}{4}.
$$

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
K
\leq
2\left(\frac{\sqrt3}{2}\right)^3
=
\frac{3\sqrt3}{4}.
$$
Equality is attained by an equilateral triangle, whose angles are all $\pi/3$.

:::

:::

::: {.pf-step #s6}

Therefore the maximum area of a triangle inscribed in the given ellipse is
$$
\boxed{\frac{3\sqrt3}{4}ab}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, $T$ gives a bijection between triangles inscribed in the unit circle and triangles inscribed in the ellipse, multiplying all their areas by $ab$. Apply the unit-circle maximum from step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives the requested maximum.

:::

:::

:::
