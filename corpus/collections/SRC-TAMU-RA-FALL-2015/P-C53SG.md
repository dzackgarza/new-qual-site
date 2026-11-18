---
schema: qual/card@1
id: P-C53SG
kind: problem
title: Equality of the iterated integrals of $\frac{(x-y)\sin(xy)}{x^2+y^2}$ on $[0,1]^2$
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 4.2 in the preserved TAMU August 2015 source notes; the statement and polar-coordinate estimate agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked measurability with the single exceptional
    point, the bound |f| <= |x-y|/(x^2+y^2), the inclusion of the unit square in the quarter
    disk of radius sqrt2, the polar computation with the angular integral evaluated as
    2(sqrt2-1) giving the total bound 4 - 2 sqrt2, and that Fubini then applies with both
    iterated integrals equal to the double integral. The argument is the card's own; no
    retained set is cited. No repair needed.
---

::: {.problem}
Justify the statement that
$$
\int_0^1\int_0^1 \frac{(x-y)\sin(xy)}{x^2+y^2}\,dx\,dy=\int_0^1\int_0^1\frac{(x-y)\sin(xy)}{x^2+y^2}\,dy\,dx.
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write
$$
f(x,y)=\frac{(x-y)\sin(xy)}{x^{2}+y^{2}}
$$
on $[0,1]^{2}$ except at the origin, where it is undefined.

::: pf

::: {.pf-step #bound}
$f$ is measurable and $\abs{f(x,y)}\le\dfrac{\abs{x-y}}{x^{2}+y^{2}}$ for $(x,y)\ne(0,0)$, a single excluded point.

::: pf-proof
The formula defines a continuous function off the origin, hence a Borel measurable one there; adding an arbitrary value at the origin keeps it measurable, and the value at one point does not affect any integral. The inequality is $\abs{\sin(xy)}\le1$ together with $x^{2}+y^{2}>0$ for $(x,y)\ne(0,0)$.
:::

:::

::: {.pf-step #polar}
$\displaystyle\int_{[0,1]^{2}}\frac{\abs{x-y}}{x^{2}+y^{2}}\,dx\,dy\le2\sqrt2\,(\sqrt2-1)<\infty$.

::: pf-proof
$[0,1]^{2}$ lies in the quarter disk $D=\{0\le r\le\sqrt2,\ 0\le\theta\le\tfrac{\pi}{2}\}$, since every point of $[0,1]^{2}$ has $x,y\ge0$ and $x^{2}+y^{2}\le2$. On $D$ use $x=r\cos\theta$, $y=r\sin\theta$: then $x^{2}+y^{2}=r^{2}$, $\abs{x-y}=r\abs{\cos\theta-\sin\theta}$, and the area element is $r\,dr\,d\theta$, so
$$
\int_{D}\frac{\abs{x-y}}{x^{2}+y^{2}}\,dx\,dy=\int_{0}^{\pi/2}\!\!\int_{0}^{\sqrt2}\frac{r\abs{\cos\theta-\sin\theta}}{r^{2}}\,r\,dr\,d\theta=\sqrt2\int_{0}^{\pi/2}\abs{\cos\theta-\sin\theta}\,d\theta .
$$
By symmetry about $\pi/4$,
$$
\int_{0}^{\pi/2}\abs{\cos\theta-\sin\theta}\,d\theta=2\int_{0}^{\pi/4}\big(\cos\theta-\sin\theta\big)d\theta=2\big[\sin\theta+\cos\theta\big]_{0}^{\pi/4}=2(\sqrt2-1),
$$
so the bound is $2\sqrt2(\sqrt2-1)=4-2\sqrt2$.
:::

:::

::: {.pf-step #l1}
$f\in L^{1}([0,1]^{2})$.

::: pf-proof
Steps [](#bound){.pf-ref} and [](#polar){.pf-ref} bound $\int\abs{f}$ by the finite number $4-2\sqrt2$.
:::

:::

::: {.pf-step #fubini}
The two iterated integrals are equal.

::: pf-proof
$f$ is integrable over the product of the $\sigma$-finite spaces $[0,1]$ and $[0,1]$ by step [](#l1){.pf-ref}; Fubini's theorem then says that $f$ is integrable in each variable separately for almost every value of the other, that both iterated integrals exist as Lebesgue integrals, and that both equal $\int_{[0,1]^{2}}f$, hence each other.
:::

:::

::: {.pf-step}
$\displaystyle\int_0^1\!\!\int_0^1 f\,dx\,dy=\int_0^1\!\!\int_0^1 f\,dy\,dx$.

::: pf-proof
Step [](#fubini){.pf-ref} is the statement.
:::

:::

:::
:::
