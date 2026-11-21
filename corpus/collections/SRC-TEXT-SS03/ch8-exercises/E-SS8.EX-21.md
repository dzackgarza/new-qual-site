---
schema: qual/card@1
id: E-SS8.EX-21
kind: problem
title: Schwarz--Christoffel maps onto triangles
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Schwarz-Christoffel
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, one or two for each part, each carrying a `pf-proof`; the four answers are
    unchanged. Cited by number only: the Schwarz--Christoffel formula, the beta integral and the
    beta-gamma identity, and Euler's reflection formula. Checked: that
    $\alpha_1+\alpha_2+\alpha_3=1$ with each in $(0,1)$ when $1<\beta_1+\beta_2<2$; the exponent
    at infinity after $w=1/z$; that $\beta_3=1$ gives $F=C\log z+O(1)$ and $\beta_3>1$ gives
    $F=Cz^{1-\beta_1-\beta_2}$; and the reflection step
    $1/\Gamma(1-\alpha_3)=\Gamma(\alpha_3)\sin(\pi\alpha_3)/\pi$.
---

::: {.exercise}
We consider conformal mappings to triangles.

(a) Show that
$$
\int_0^z z^{-\beta_1} (1 - z)^{-\beta_2}\, dz,
$$
with $0 < \beta_1 < 1$, $0 < \beta_2 < 1$, and $1 < \beta_1 + \beta_2 < 2$, maps $\halfplane$ to a triangle whose vertices are the images of $0$, $1$, and $\infty$, and with angles $\alpha_1\pi$, $\alpha_2\pi$, and $\alpha_3\pi$, where $\alpha_j + \beta_j = 1$ and $\beta_1 + \beta_2 + \beta_3 = 2$.

(b) What happens when $\beta_1 + \beta_2 = 1$?

(c) What happens when $0 < \beta_1 + \beta_2 < 1$?

(d) In (a), the length of the side of the triangle opposite angle $\alpha_j\pi$ is $\frac{\sin(\alpha_j\pi)}{\pi} \Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3)$.
:::

::: {.solution}

::: pf

::: pf-step

Let $F(z)=\int_0^z\zeta^{-\beta_1}(1-\zeta)^{-\beta_2}\,d\zeta$, with the branches taken holomorphically on the upper half-plane. At the finite prevertices $0$ and $1$ the Schwarz--Christoffel exponents are $-\beta_1$ and $-\beta_2$, so the interior angles there are
$$
\alpha_1\pi=(1-\beta_1)\pi,\qquad\alpha_2\pi=(1-\beta_2)\pi.
$$

::: pf-proof

On the upper half-plane the factors $\zeta^{-\beta_1}$ and $(1-\zeta)^{-\beta_2}$ have holomorphic branches, since the half-plane is simply connected and avoids $0$ and $1$; the integrand never vanishes there, so $F'$ is holomorphic and nonvanishing. The Schwarz--Christoffel formula says that a map whose derivative is $\prod_k(\zeta-a_k)^{-\beta_k}$ with $0<\beta_k<1$ carries the half-plane onto a polygon with interior angles $(1-\beta_k)\pi$ at the images of the $a_k$; here the finite prevertices are $0$ and $1$ with exponents $\beta_1$ and $\beta_2$, which gives the two angles.

:::

:::

::: pf-step

Near infinity $F'(z)\sim Cz^{-(\beta_1+\beta_2)}$; under $w=1/z$ this becomes
$$
\frac{d}{dw}F(1/w)\sim C'w^{\beta_1+\beta_2-2}=C'w^{-\beta_3},\qquad\beta_3=2-\beta_1-\beta_2,
$$
so the angle at the image of infinity is $\alpha_3\pi=(1-\beta_3)\pi=(\beta_1+\beta_2-1)\pi$.

::: pf-proof

For large $z$ the factor $(1-z)^{-\beta_2}=(-z)^{-\beta_2}(1-1/z)^{-\beta_2}$ differs from $(-z)^{-\beta_2}$ by a factor tending to $1$, so the integrand behaves like a constant times $z^{-(\beta_1+\beta_2)}$. With $w=1/z$ and $G(w)=F(1/w)$, the chain rule gives $G'(w)=-F'(1/w)/w^2$, and substituting $F'(1/w)\sim Cw^{\beta_1+\beta_2}$ gives $G'(w)\sim-Cw^{\beta_1+\beta_2-2}$. As a prevertex of $G$ at $w=0$ this is the exponent $\beta_3=2-\beta_1-\beta_2$, so the Schwarz--Christoffel rule gives the angle $(1-\beta_3)\pi$ at the image of infinity, and $1-\beta_3=\beta_1+\beta_2-1$.

:::

:::

::: pf-step

(a) When $1<\beta_1+\beta_2<2$ all three $\alpha_j$ lie in $(0,1)$ and sum to $1$, so the image is a triangle with precisely these angles.

::: pf-proof

$\alpha_1=1-\beta_1$ and $\alpha_2=1-\beta_2$ lie in $(0,1)$ because $0<\beta_j<1$, and $\alpha_3=\beta_1+\beta_2-1$ lies in $(0,1)$ by the hypothesis $1<\beta_1+\beta_2<2$. Their sum is $3-(\beta_1+\beta_2)+(\beta_1+\beta_2)-1=1$. A polygon whose three interior angles are positive and sum to $\pi$ is a triangle, so $F$ maps the half-plane conformally onto a triangle of angles $\alpha_j\pi$ with vertices at the images of $0,1,\infty$.

:::

:::

::: pf-step

(b) If $\beta_1+\beta_2=1$ then $\alpha_3=0$: the sides issuing toward infinity become parallel and the image is a degenerate triangle, and analytically $F(z)=C\log z+O(1)$ at infinity.

::: pf-proof

With $\beta_3=1$ the exponent at infinity is $-1$, so $G'(w)\sim C'w^{-1}$ and $G(w)=C'\log w+O(1)$, that is $F(z)=-C'\log z+O(1)$ at infinity: the map is unbounded and grows logarithmically, and two of the sides of the would-be triangle meet at an angle $0$ at infinity, an infinite strip-like degenerate triangle. It is not a triangle, since one angle vanishes.

:::

:::

::: pf-step

(c) If $0<\beta_1+\beta_2<1$ then $F(z)\sim Cz^{1-\beta_1-\beta_2}$ at infinity, so the two boundary rays separate by the angle $(1-\beta_1-\beta_2)\pi$, and the image is an unbounded polygonal region with finite angles $(1-\beta_1)\pi$ and $(1-\beta_2)\pi$ and an exterior vertex at infinity rather than a bounded triangle.

::: pf-proof

Now $\beta_3=2-\beta_1-\beta_2>1$, so $\alpha_3=1-\beta_3<0$: the Schwarz--Christoffel angle at infinity is negative, the signature of an unbounded region. The exponent $1-(\beta_1+\beta_2)$ is positive, so $F$ stays bounded as $z\to\infty$ along the half-plane, and the two boundary rays of the image diverge with the angle $(1-\beta_1-\beta_2)\pi$ between them; the two finite angles are still $(1-\beta_1)\pi$ and $(1-\beta_2)\pi$ by step 1, so the image is an unbounded polygonal region and not a triangle.

:::

:::

::: pf-step

(d) The side opposite $\alpha_3\pi$ is the image of $[0,1]$, so its length is
$$
L_3=\int_0^1x^{-\beta_1}(1-x)^{-\beta_2}\,dx=B(\alpha_1,\alpha_2)=\frac{\Gamma(\alpha_1)\Gamma(\alpha_2)}{\Gamma(\alpha_1+\alpha_2)}.
$$

::: pf-proof

The boundary of the half-plane consists of the two rays and the interval $[0,1]$ between the prevertices $0$ and $1$; the image of that interval is the side joining the images of $0$ and $1$, which is opposite the vertex at the image of $\infty$. The length of a curve $F\circ\gamma$ is $\int\abs{F'(\gamma(t))}\abs{\gamma'(t)}dt$, and on $[0,1]$ with $\gamma(t)=t$ the integrand $\abs{F'}$ is $t^{-\beta_1}(1-t)^{-\beta_2}$ up to the constant modulus of the branch factors, which is $1$ for the principal choices; so the length is the displayed integral, which is $B(\alpha_1,\alpha_2)$ because $\beta_1=1-\alpha_1$ and $\beta_2=1-\alpha_2$, and $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$.

:::

:::

::: pf-step

(d) Since $\alpha_1+\alpha_2=1-\alpha_3$, Euler reflection gives $1/\Gamma(1-\alpha_3)=\frac{\sin(\pi\alpha_3)}{\pi}\Gamma(\alpha_3)$, so
$$
L_3=\frac{\sin(\pi\alpha_3)}{\pi}\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3),
$$
and the same argument after permuting the three prevertices gives $L_j=\frac{\sin(\pi\alpha_j)}{\pi}\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3)$ for each $j$.

::: pf-proof

Euler's reflection formula is $\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)$; with $z=\alpha_3$ it gives $\Gamma(\alpha_3)\Gamma(1-\alpha_3)=\pi/\sin(\pi\alpha_3)$, hence $1/\Gamma(1-\alpha_3)=\Gamma(\alpha_3)\sin(\pi\alpha_3)/\pi$. Substituting into step 6, with $\alpha_1+\alpha_2=1-\alpha_3$, gives the displayed $L_3$. The other two sides are the images of the intervals between the other pairs of prevertices; the Schwarz--Christoffel map with the prevertices permuted has the same angles relabelled, and the same computation applies, giving the formula with $\alpha_j$ in place of $\alpha_3$.

:::

:::

:::
:::
