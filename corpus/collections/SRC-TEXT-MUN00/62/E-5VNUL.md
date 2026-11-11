---
schema: qual/card@1
id: E-5VNUL
kind: problem
title: The Borsuk lemma fails without injectivity
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 1, printed p. 384. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. Two counterexamples have now been discarded. The
    original took A = [0,1] and f(t) = (cos 2 pi t, sin 2 pi t) with a = 0, b = infinity and claimed f was
    nullhomotopic because A is contractible; a nullhomotopy has to lie in S^2 - a - b, where that loop winds once
    about a, so the hypothesis fails. A first replacement used varphi(theta) = theta on [0, pi] and 2 pi - theta on
    [pi, 2 pi], which takes values in [0, pi] only, so the image was an arc of C rather than C; an arc does not
    separate S^2 (Theorem 63.2, printed p. 389), so the Borsuk conclusion held for it and it proved nothing. The
    map below doubles the parameter on each half, so it runs once round all of C and back, and every step is
    checked: image C, continuity, f(0) = f(2 pi), non-injectivity, and the explicit homotopy. Checked against
    Lemma 62.2 (printed p. 382) and Theorem 61.3 (printed p. 379).
---

::: {.exercise}

Give an example to show that the conclusion of the Borsuk lemma need not hold if $f$ is not injective.
:::

::: {.solution}

The Borsuk lemma is Lemma 62.2 (printed p. 382): if $a,b$ are points of $S^2$, $A$ is compact, and $f:A\to S^2-\theset{a,b}$ is a continuous injective nullhomotopic map, then $a$ and $b$ lie in the same component of $S^2-f(A)$. The example keeps every hypothesis but injectivity.

::: pf

::: pf-step

Take $C$ to be a round circle in $S^2$ bounding a disk $D$ that contains $a$ and not $b$, and let $g:S^1\to C$ be a homeomorphism.

::: pf-proof

A small circle about $a$ in a coordinate chart is such a $C$: the closed disk it bounds lies in the chart, so after possibly shrinking it, $b\notin D$. The circle is compact and $S^2$ is Hausdorff, so $g$ is a continuous bijection from a compact space onto a Hausdorff space, hence a homeomorphism onto $C$ (Theorem 26.6, printed p. 167).

:::

:::

::: pf-step

Define $f:S^1\to S^2-\theset{a,b}$ by running once round all of $C$ and back, and note that $f$ is continuous with image exactly $C$.

::: pf-proof

Let $\varphi:[0,2\pi]\to[0,2\pi]$ be $\varphi(\theta)=2\theta$ for $0\le\theta\le\pi$ and $\varphi(\theta)=2(2\pi-\theta)$ for $\pi\le\theta\le2\pi$, and set $f(\theta)=g(e^{i\varphi(\theta)})$. On $[0,\pi]$ the map $\varphi$ runs through $[0,2\pi]$ and on $[\pi,2\pi]$ it runs through $[2\pi,0]$, so $\varphi$ takes every value of $[0,2\pi]$ and $\operatorname{im}f=g(S^1)=C\subseteq S^2-\theset{a,b}$. Continuity: $\varphi$ is continuous on each closed half and the two formulas agree at $\theta=\pi$, where both give $2\pi$, so $\varphi$ is continuous by the pasting lemma, and $f$ is a composite of continuous maps.

:::

:::

::: pf-step

$f(0)=f(2\pi)$ and $f$ is not injective.

::: pf-proof

$\varphi(0)=0$ and $\varphi(2\pi)=0$, so $f(0)=g(1)=f(2\pi)$, as a map of the circle must satisfy. For $0<\theta<\pi$ we have $\varphi(\theta)=2\theta$ and $\varphi(2\pi-\theta)=2\theta$, so $f(\theta)=f(2\pi-\theta)$ while $\theta\ne2\pi-\theta$; hence $f$ is not injective.

:::

:::

::: pf-step

$f$ is nullhomotopic.

::: pf-proof

Define $H:S^1\times I\to C$ by $H(\theta,s)=g\bigl(e^{i(1-s)\varphi(\theta)}\bigr)$. It is continuous, $H(\theta,0)=f(\theta)$, and $H(\theta,1)=g(1)$ for every $\theta$, a constant. So $f$ is homotopic to a constant within $C\subseteq S^2-\theset{a,b}$.

:::

:::

::: pf-step

$a$ and $b$ lie in different components of $S^2-f(S^1)$.

::: pf-proof

$f(S^1)=C$ bounds the disk $D$ with $a\in D$ and $b\notin D$. By Theorem 61.3 (printed p. 379) the simple closed curve $C$ separates $S^2$, so $S^2-C$ has at least two components, and $\operatorname{Int}D$ and $S^2-D$ are disjoint nonempty open sets whose union is $S^2-C$; each is therefore a union of components, and $a\in\operatorname{Int}D$, $b\in S^2-D$. Hence $a$ and $b$ lie in different components.

:::

:::

::: pf-qed

$f$ is continuous with compact domain and image in $S^2-\theset{a,b}$ and is nullhomotopic, but is not injective and its image separates $a$ from $b$; the Borsuk lemma therefore needs injectivity.

:::

:::
:::
