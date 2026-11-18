---
schema: qual/card@1
id: E-1XT8N
kind: problem
title: Continuity of the affine map in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 7, printed p. 127, referring to
    Exercise 8 of §19, with the uniform metric of printed p. 124; the stored statement is
    the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.7, PDF pp. 19-20. The uniform distance between
    the images is sup min{a_i |x_i - y_i|, 1}: bounded coefficients make the map continuous,
    an unbounded coefficient sequence destroys continuity at the origin by stretching a
    small constant sequence to uniform distance 1, and the two conditions on a_i and 1/a_i
    give the answer for the map and for its inverse. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Consider the map $h: \RR^\omega \to \RR^\omega$ defined in Exercise 8 of §19; give $\RR^\omega$ the uniform topology.
Under what conditions on the numbers $a_i$ and $b_i$ is $h$ continuous?
a homeomorphism?
:::

::: {.solution}

The three answers are those of **"positron0802"**, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.7, PDF pp. 19--20 (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the $\varepsilon$-$\delta$ and the counterexample at $\mathbf{0}$ are its arguments, the second checked below with the constant sequence $(r,r,\ldots)$ rather than an arbitrary point. The statement was checked against Munkres, *Topology* (2000), §20 Exercise 7, printed p. 127, the map $h$ being the one of §19 Exercise 8, printed p. 118, and the uniform metric the one of §20, printed p. 124.

Throughout, $h(\mathbf{x})\coloneqq(a_{1}x_{1}+b_{1},a_{2}x_{2}+b_{2},\ldots)$ with $a_{i}>0$ and $b_{i}$ real, $\mathbb{R}^{\omega}$ carries the uniform metric
$$
\bar\rho(\mathbf{x},\mathbf{y})\coloneqq\sup_{i}\min\theset{\abs{x_{i}-y_{i}},1},
$$
and $\mathbf{0}$ denotes the sequence of zeros.

::: pf

::: {.pf-step #bijection}
$h$ is a bijection, with $h^{-1}(\mathbf{y})=\big((y_{1}-b_{1})/a_{1},(y_{2}-b_{2})/a_{2},\ldots\big)$.

::: pf-proof
In each coordinate the map $x_{i}\mapsto a_{i}x_{i}+b_{i}$ is a bijection of $\RR$ with inverse $y_{i}\mapsto(y_{i}-b_{i})/a_{i}$, which is defined because $a_{i}>0$. A self-map of a product is a bijection exactly when each coordinate map is one, and the displayed formula is then the coordinatewise inverse.
:::

:::

::: {.pf-step #distance-formula}
For all $\mathbf{x},\mathbf{y}$,
$$
\bar\rho(h(\mathbf{x}),h(\mathbf{y}))=\sup_{i}\min\theset{a_{i}\abs{x_{i}-y_{i}},1}.
$$

::: pf-proof
The $i$-th coordinate of $h(\mathbf{x})-h(\mathbf{y})$ is $a_{i}x_{i}-a_{i}y_{i}=a_{i}(x_{i}-y_{i})$. Substitute this in the definition of $\bar\rho$; the $b_{i}$ cancel and play no further role.
:::

:::

::: {.pf-step #bounded-continuous}
If $(a_{i})$ is bounded, say $a_{i}\leq M$ for all $i$, then $h$ is continuous.

:::: pf-proof

::: {.pf-step #delta}
Let $\mathbf{x}\in\mathbb{R}^{\omega}$ and $\varepsilon>0$, and put $\delta\coloneqq\min\theset{\varepsilon/M,1/M}$, where $M>0$ because $a_{i}>0$.

::: pf-proof
$M\geq a_{1}>0$ under the hypothesis that $a_{i}\leq M$ for all $i$, and $\varepsilon>0$, so both quotients are positive and so is their minimum.
:::

:::

::: {.pf-step #ball-mapped}
$h$ maps the ball $B_{\bar\rho}(\mathbf{x},\delta)$ into $B_{\bar\rho}(h(\mathbf{x}),\varepsilon)$.

::: pf-proof
Let $\bar\rho(\mathbf{x},\mathbf{y})<\delta$. Then $\min\theset{\abs{x_{i}-y_{i}},1}<\delta$ for every $i$, and since $\delta\leq1/M\leq1$ this forces $\abs{x_{i}-y_{i}}<\delta$. Hence by step [](#distance-formula){.pf-ref}
$$
\bar\rho(h(\mathbf{x}),h(\mathbf{y}))=\sup_{i}\min\theset{a_{i}\abs{x_{i}-y_{i}},1}\leq\sup_{i}a_{i}\abs{x_{i}-y_{i}}\leq M\delta\leq\varepsilon,
$$
the last inequality by $\delta\leq\varepsilon/M$.
:::

:::

::::

:::

::: {.pf-step #unbounded-discontinuous}
If $(a_{i})$ is unbounded, then $h$ is not continuous at $\mathbf{0}$.

::: pf-proof
Take $0<\varepsilon<1$ and let $V$ be the ball $B_{\bar\rho}(h(\mathbf{0}),\varepsilon)$. Let $\delta>0$ and choose a real $r$ with $0<r<\min\theset{\delta,1}$, and let $\mathbf{y}\coloneqq(r,r,\ldots)$, so that $\bar\rho(\mathbf{0},\mathbf{y})=\min\theset{r,1}=r<\delta$. Since $(a_{i})$ is unbounded there is $N$ with $a_{N}r>1$, and then $\min\theset{a_{N}r,1}=1$, so by step [](#distance-formula){.pf-ref}
$$
\bar\rho(h(\mathbf{0}),h(\mathbf{y}))=\sup_{i}\min\theset{a_{i}r,1}=1>\varepsilon.
$$
Hence for this $\mathbf{y}$, which lies in the ball of radius $\delta$ about $\mathbf{0}$, the image $h(\mathbf{y})$ lies outside $V$; since $\delta>0$ was arbitrary, no ball about $\mathbf{0}$ is mapped into $V$, so $h$ is not continuous at $\mathbf{0}$.
:::

:::

::: {.pf-step #inverse}
$h^{-1}$ is continuous exactly when $(1/a_{i})$ is bounded.

::: pf-proof
By step [](#bijection){.pf-ref}, $h^{-1}(\mathbf{y})=\big((1/a_{1})(y_{1}-b_{1}),(1/a_{2})(y_{2}-b_{2}),\ldots\big)$, which is the map of the same form as $h$ with $a_{i}$ replaced by the positive numbers $1/a_{i}$ and $b_{i}$ replaced by $-b_{i}/a_{i}$. Steps [](#bounded-continuous){.pf-ref} and [](#unbounded-discontinuous){.pf-ref} applied to those coefficients give that $h^{-1}$ is continuous when $(1/a_{i})$ is bounded and discontinuous at $\mathbf{0}$ when it is not.
:::

:::

::: pf-step
Therefore
$$
\boxed{h\text{ is continuous}\iff (a_{i})\text{ is bounded},\qquad
h\text{ is a homeomorphism}\iff (a_{i})\text{ and }(1/a_{i})\text{ are both bounded},}
$$
with no condition on the $b_{i}$; the homeomorphism case is $0<\inf_{i}a_{i}$ and $\sup_{i}a_{i}<\infty$.

::: pf-proof
Steps [](#bounded-continuous){.pf-ref} and [](#unbounded-discontinuous){.pf-ref} give the continuity criterion, and no step used a hypothesis on $b_{i}$: they cancel in step [](#distance-formula){.pf-ref} and are part of the translation in step [](#inverse){.pf-ref}. Since $h$ is a bijection by step [](#bijection){.pf-ref}, it is a homeomorphism exactly when $h$ and $h^{-1}$ are both continuous, which by step [](#inverse){.pf-ref} is exactly the boundedness of $(a_{i})$ and of $(1/a_{i})$; that the latter says the $a_{i}$ are bounded away from $0$ is the definition of boundedness of the sequence of reciprocals of positive numbers.
:::

:::

:::

:::
