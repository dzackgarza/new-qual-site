---
schema: qual/card@1
id: P-GKGSD
kind: problem
title: 'A univalent branch of $\sqrt{f(z^2)}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the injectivity, normalization at zero and square-root construction with Fall 2016 problem 5 in the retained source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked nonvanishing of f(w)/w including the origin, constructed its logarithm by a primitive, and used oddness to rule out the opposite-point collision after squaring."
---

5. Let f be a one-to-one analytic function defined on the unit disk D centered at the origin and $f ( 0 ) = 0$ . Show that the function $g ( z ) = { \sqrt { f ( z ^ { 2 } ) } }$ has a single-valued branch and is also one-to-one.

::: solution
<1>1. There is a holomorphic nonvanishing function $h$ on $D$ with $f(w)=wh(w)$.

::: proof
The Taylor series of $f$ at zero has zero constant term,
so $f(w)/w$ extends holomorphically across zero with value
$h(0)=f'(0)$. An injective holomorphic function has nonzero
derivative [@SS03], hence $h(0)\ne0$. For $w\ne0$,
injectivity and $f(0)=0$ give $f(w)\ne0$, so $h(w)\ne0$.
Thus $h$ has no zero anywhere in $D$.
:::

<1>2. An explicit odd holomorphic square root exists on the whole disk.

::: proof
Since $h'/h$ is holomorphic on the simply connected disk,
it has a holomorphic primitive $L_0$ with $L_0(0)=0$
[@SS03]. Choose $c\in\mathbb C$ with $e^c=h(0)$ and set
$L=L_0+c$. Differentiation gives
$$
(he^{-L})'=e^{-L}(h'-hL')=0.
$$
Its value at zero is one, so connectedness implies
$h=e^L$ on $D$. Define
$$
g(z)=z\exp\left(\frac12L(z^2)\right),\qquad z\in D.
$$
This is a single-valued holomorphic function, and
$$
g(z)^2=z^2h(z^2)=f(z^2).
$$
It also satisfies $g(-z)=-g(z)$ and has no zero except
at $z=0$, because the exponential never vanishes.
:::

<1>3. The branch $g$ is injective.

::: proof
Suppose $g(z_1)=g(z_2)$. Squaring and using step <1>2
give $f(z_1^2)=f(z_2^2)$. Injectivity of $f$ yields
$z_1^2=z_2^2$, so $z_2=z_1$ or $z_2=-z_1$.
In the second case, oddness gives
$g(z_1)=g(-z_1)=-g(z_1)$, whence $g(z_1)=0$.
Step <1>2 then forces $z_1=0=z_2$. Thus in every case
$z_1=z_2$, proving injectivity.

Any other holomorphic square root differs from $g$ by
a constant sign: on the connected punctured disk its
quotient by $g$ takes values in $\{1,-1\}$ and is
continuous, hence constant; continuity extends this
equality across zero. Therefore either holomorphic branch
has the asserted injectivity.
:::
:::
