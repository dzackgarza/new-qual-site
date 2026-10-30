---
schema: qual/card@1
id: P-UCLARA11S-07
kind: problem
title: Goursat's theorem for triangular contours
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Prove Goursat's theorem: if $f:\CC\to\CC$ is complex differentiable (and hence continuous), then for every triangle $\Delta\subset\CC$,
$$
\oint_{\partial\Delta}f(z)\,dz=0,
$$
where the line integral is over the three sides of the triangle.
:::

::: {.solution}

Let
$$
I(\Delta)
\coloneqq
\oint_{\partial\Delta}f(z)\,dz.
$$

::: pf

::: {.pf-step #s1-1}

If a triangle $\Delta$ is subdivided by joining the midpoints of its three sides into four congruent triangles $\Delta_1,\dots,\Delta_4$, then
$$
I(\Delta)
=
\sum_{j=1}^4 I(\Delta_j).
$$


::: pf-proof

Each interior segment of the subdivision occurs twice in the sum of the four oriented boundary integrals, once in each direction, so those contributions cancel. The remaining oriented segments are exactly the three sides of $\partial\Delta$.

:::

:::

::: {.pf-step #s1-2}

Among the four subtriangles, at least one satisfies
$$
\abs{I(\Delta_j)}
\ge
\frac14\abs{I(\Delta)}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and the triangle inequality,
$$
\abs{I(\Delta)}
\le
\sum_{j=1}^4\abs{I(\Delta_j)}.
$$
If every term on the right were strictly smaller than $\abs{I(\Delta)}/4$, their sum would be strictly smaller than $\abs{I(\Delta)}$, a contradiction.

:::

:::

::: {.pf-step #s1-3}

Starting from $\Delta_0=\Delta$, one can choose nested closed triangles
$$
\Delta_0\supset\Delta_1\supset\Delta_2\supset\cdots
$$
such that
$$
\abs{I(\Delta_n)}
\ge
4^{-n}\abs{I(\Delta_0)},
$$
while
$$
\operatorname{diam}(\Delta_n)
=
2^{-n}\operatorname{diam}(\Delta_0)
$$
and
$$
\operatorname{per}(\Delta_n)
=
2^{-n}\operatorname{per}(\Delta_0).
$$


::: pf-proof

At each stage subdivide $\Delta_n$ into four congruent midpoint triangles and choose a child satisfying step [](#s1-2){.pf-ref}. Each such child has all side lengths halved, hence both diameter and perimeter are halved. Iterating the integral estimate gives
$$
\abs{I(\Delta_n)}
\ge
4^{-n}\abs{I(\Delta_0)}.
$$

:::

:::

::: pf-step

There is a unique point
$$
z_0\in\bigcap_{n=0}^{\infty}\Delta_n.
$$


::: pf-proof

The sets $\Delta_n$ are nonempty compact and nested, so their intersection is nonempty. Their diameters tend to zero by step [](#s1-3){.pf-ref}, hence the intersection contains at most one point.

:::

:::

::: {.pf-step #s1-5}

For every $\varepsilon>0$, there is $N$ such that whenever $z\in\Delta_N$,
$$
f(z)
=
f(z_0)
+
f'(z_0)(z-z_0)
+
(z-z_0)\eta(z),
$$
with
$$
\abs{\eta(z)}<\varepsilon.
$$


::: pf-proof

Complex differentiability at $z_0$ means
$$
\frac{f(z)-f(z_0)}{z-z_0}
\longrightarrow
f'(z_0)
\qquad
(z\to z_0).
$$
Thus for sufficiently small $\delta>0$,
$$
0<\abs{z-z_0}<\delta
$$
implies
$$
\abs{
\frac{f(z)-f(z_0)}{z-z_0}
-
f'(z_0)
}
<
\varepsilon.
$$
By step [](#s1-3){.pf-ref}, choose $N$ so large that
$$
\operatorname{diam}(\Delta_N)<\delta.
$$
Since $z_0\in\Delta_N$, every $z\in\Delta_N$ satisfies $\abs{z-z_0}<\delta$. Define $\eta(z)$ by the displayed remainder formula for $z\ne z_0$ and set $\eta(z_0)=0$.

:::

:::

::: {.pf-step #s1-6}

For every $n\ge N$,
$$
I(\Delta_n)
=
\oint_{\partial\Delta_n}
(z-z_0)\eta(z)\,dz.
$$


::: pf-proof

Insert the expansion from step [](#s1-5){.pf-ref} into the contour integral. The constant term contributes
$$
f(z_0)\oint_{\partial\Delta_n}dz
=0.
$$
The linear term contributes
$$
f'(z_0)
\oint_{\partial\Delta_n}(z-z_0)\,dz
=
\frac{f'(z_0)}2
\oint_{\partial\Delta_n}d\bigl((z-z_0)^2\bigr)
=0.
$$
Only the remainder remains.

:::

:::

::: {.pf-step #s1-7}

For every $n\ge N$,
$$
\abs{I(\Delta_n)}
\le
\varepsilon
\operatorname{diam}(\Delta_n)
\operatorname{per}(\Delta_n).
$$


::: pf-proof

By steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref},
$$
\abs{(z-z_0)\eta(z)}
\le
\varepsilon \abs{z-z_0}
\le
\varepsilon\operatorname{diam}(\Delta_n)
$$
on $\partial\Delta_n$. The ML inequality then gives the stated bound.

:::

:::

::: {.pf-step #s1-8}

The original integral satisfies
$$
\abs{I(\Delta_0)}
\le
\varepsilon
\operatorname{diam}(\Delta_0)
\operatorname{per}(\Delta_0).
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-7){.pf-ref},
$$
4^{-n}\abs{I(\Delta_0)}
\le
\abs{I(\Delta_n)}
\le
\varepsilon
\frac{\operatorname{diam}(\Delta_0)}{2^n}
\frac{\operatorname{per}(\Delta_0)}{2^n}.
$$
The right-hand side is
$$
\varepsilon
4^{-n}
\operatorname{diam}(\Delta_0)
\operatorname{per}(\Delta_0).
$$
Multiply by $4^n$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
\oint_{\partial\Delta}f(z)\,dz=0.
}
$$


::: pf-proof

The estimate in step [](#s1-8){.pf-ref} holds for every $\varepsilon>0$. Letting $\varepsilon\downarrow0$ forces
$$
\abs{I(\Delta_0)}=0.
$$
Since $\Delta_0=\Delta$, this is the desired conclusion.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} proves Goursat's theorem for the given triangle.

:::

:::

:::
