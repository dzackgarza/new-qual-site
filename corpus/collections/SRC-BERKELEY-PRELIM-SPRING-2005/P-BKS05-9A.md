---
schema: qual/card@1
id: P-BKS05-9A
kind: problem
title: Principal value of $\iint f(x,y)/(x+iy)^3\,dx\,dy$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained principal-value argument. Constant
    and linear Taylor terms have zero angular integral on every concentric
    annulus, while the quadratic remainder contributes O(epsilon).
---

::: {.problem}
Let $f \colon  { \mathbb { R } } ^ { 2 } \to  { \mathbb { R } }$ be an infinitely differentiable function that is zero outside some bounded subset of $\mathbb { R } ^ { 2 }$ . Prove that

$$
\operatorname * { l i m } _ { \epsilon \to 0 } \int \int _ { x ^ { 2 } + y ^ { 2 } \geq \epsilon ^ { 2 } } { \frac { f ( x , y ) } { ( x + i y ) ^ { 3 } } } d x d y
$$

exists.
:::

::: {.solution}
For $\varepsilon>0$, set
$$
I(\varepsilon)
\coloneqq
\iint_{x^2+y^2\geq\varepsilon^2}
\frac{f(x,y)}{(x+iy)^3}\,dx\,dy.
$$
Because $f$ vanishes outside a bounded set, this integral is finite for
every $\varepsilon>0$.

::: pf

::: {.pf-step #taylor-decomposition}
There are constants $a,b,c\in\RR$, $C>0$, and $\rho>0$ such
that
$$
f(x,y)=a+bx+cy+E(x,y)
$$
and
$$
|E(x,y)|\leq C(x^2+y^2)
$$
whenever $x^2+y^2<\rho^2$.

::: pf-proof
Take
$$
a=f(0,0),
\qquad
b=\frac{\partial f}{\partial x}(0,0),
\qquad
c=\frac{\partial f}{\partial y}(0,0).
$$
Taylor's theorem to first order at the origin gives a remainder bounded
by a constant times $x^2+y^2$ on a sufficiently small disk, because the
second derivatives of $f$ are continuous and therefore bounded there.
:::

:::

::: {.pf-step #constant-term-vanishes}
For every $0<\delta<\varepsilon<\rho$,
$$
\iint_{\delta^2<x^2+y^2<\varepsilon^2}
\frac{1}{(x+iy)^3}\,dx\,dy
=0.
$$

::: pf-proof
In polar coordinates $x+iy=re^{i\theta}$ and
$dx\,dy=r\,dr\,d\theta$. Hence the integral equals
$$
\int_\delta^\varepsilon r^{-2}\,dr
\int_0^{2\pi}e^{-3i\theta}\,d\theta
=0.
$$
:::

:::

::: {.pf-step #linear-terms-vanish}
For every $0<\delta<\varepsilon<\rho$, the corresponding
annular integrals with numerator $x$ or $y$ are also zero.

::: pf-proof
For the numerator $x=r\cos\theta$, the angular factor is
$$
\cos\theta\,e^{-3i\theta}
=
\frac12\left(e^{-2i\theta}+e^{-4i\theta}\right),
$$
whose integral from $0$ to $2\pi$ is zero. For
$y=r\sin\theta$, the angular factor is
$$
\sin\theta\,e^{-3i\theta}
=
\frac1{2i}\left(e^{-2i\theta}-e^{-4i\theta}\right),
$$
whose integral is likewise zero. The radial integrals are finite for
$0<\delta<\varepsilon$, so both annular integrals vanish.
:::

:::

::: {.pf-step #remainder-bound}
The remainder contribution over a small annulus tends uniformly
to zero:
$$
\left|
\iint_{\delta^2<x^2+y^2<\varepsilon^2}
\frac{E(x,y)}{(x+iy)^3}\,dx\,dy
\right|
\leq
2\pi C(\varepsilon-\delta).
$$

::: pf-proof
On the annulus, step [](#taylor-decomposition){.pf-ref} gives
$$
\frac{|E(x,y)|}{|x+iy|^3}
\leq
\frac{Cr^2}{r^3}
=
\frac Cr.
$$
Therefore polar coordinates give
$$
\begin{aligned}
\left|
\iint
\frac{E(x,y)}{(x+iy)^3}\,dx\,dy
\right|
&\leq
\int_0^{2\pi}\int_\delta^\varepsilon
\frac Cr\,r\,dr\,d\theta\\
&=
2\pi C(\varepsilon-\delta).
\end{aligned}
$$
:::

:::

::: {.pf-step #cauchy-criterion}
The family $I(\varepsilon)$ is Cauchy as
$\varepsilon\to0^+$.

::: pf-proof
For $0<\delta<\varepsilon<\rho$,
$$
I(\delta)-I(\varepsilon)
=
\iint_{\delta^2<x^2+y^2<\varepsilon^2}
\frac{f(x,y)}{(x+iy)^3}\,dx\,dy.
$$
Insert the decomposition from step [](#taylor-decomposition){.pf-ref}. Steps [](#constant-term-vanishes){.pf-ref} and [](#linear-terms-vanish){.pf-ref} show that
the constant and linear terms contribute zero, while step [](#remainder-bound){.pf-ref} gives
$$
|I(\delta)-I(\varepsilon)|
\leq2\pi C\varepsilon.
$$
The right-hand side tends to zero with $\varepsilon$, which is the
Cauchy criterion.
:::

:::

::: {.pf-step #limit-exists}
The required limit exists.

::: pf-proof
The values $I(\varepsilon)$ lie in the complete field $\CC$. By step
[](#cauchy-criterion){.pf-ref} they form a Cauchy family as $\varepsilon\to0^+$, so they
converge to a finite complex limit.
:::

:::

::: pf-qed
Step [](#limit-exists){.pf-ref} is the asserted existence of the principal-value limit.
:::

:::

:::
