---
schema: qual/card@1
id: P-CHAVAN-CA-7-2
kind: problem
title: The complex plane minus a half-line is simply connected
classification: {areas: [complex-analysis], topics: [Simply Connected Domains]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
---

::: {.problem}
Show that the complex plane minus a half-line is simply connected.
:::

::: {.solution}

Write the removed half-line as
$$
L=\{p+re^{i\alpha}:r\geq0\}
$$
for some $p\in\CC$ and $\alpha\in\RR$.

::: pf

::: {.pf-step #s1-1}

The affine map
$$
T(z)=e^{-i\alpha}(z-p)
$$
is a homeomorphism
$$
\CC\setminus L\longrightarrow\CC\setminus[0,\infty).
$$


::: pf-proof

The map $T$ is a homeomorphism of $\CC$ with inverse
$T^{-1}(w)=p+e^{i\alpha}w$, and it sends $L$ exactly onto the nonnegative real
axis.

:::

:::

::: {.pf-step #s1-2}

Polar coordinates give a homeomorphism
$$
P:\CC\setminus[0,\infty)
\longrightarrow
(0,\infty)\times(0,2\pi),
\qquad
P(re^{i\theta})=(r,\theta).
$$


::: pf-proof

Every point of the slit plane has a unique representation
$re^{i\theta}$ with $r>0$ and $0<\theta<2\pi$. The corresponding branch of
argument is continuous on $\CC\setminus[0,\infty)$, so $P$ is continuous. Its
inverse
$$
(r,\theta)\longmapsto re^{i\theta}
$$
is continuous as well.

:::

:::

::: {.pf-step #s1-3}

Any two curves in $(0,\infty)\times(0,2\pi)$ with the same endpoints are
homotopic relative to those endpoints.


::: pf-proof

The set $(0,\infty)\times(0,2\pi)$ is convex. If
$\gamma_0,\gamma_1:[a,b]\to(0,\infty)\times(0,2\pi)$ have the same endpoints,
then
$$
H(s,t)=(1-s)\gamma_0(t)+s\gamma_1(t)
$$
stays in the set for every $(s,t)\in[0,1]\times[a,b]$, is jointly continuous,
and fixes both endpoints throughout the homotopy.

:::

:::

::: {.pf-step #s1-4}

Any two curves in $\CC\setminus L$ with the same endpoints are homotopic
relative to those endpoints.


::: pf-proof

Transport the curves by the homeomorphism $P\circ T$, use the homotopy from
step [](#s1-3){.pf-ref}, and transport that homotopy back by $(P\circ T)^{-1}$.

:::

:::

::: {.pf-step #s1-5}

Therefore $\CC\setminus L$ is simply connected.


::: pf-proof

Step [](#s1-4){.pf-ref} is precisely the homotopy definition of simple connectivity used in
the source. In particular, the space is a region because steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}
identify it with the connected open set $(0,\infty)\times(0,2\pi)$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
