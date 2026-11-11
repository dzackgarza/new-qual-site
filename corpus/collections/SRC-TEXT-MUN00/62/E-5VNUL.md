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
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The earlier counterexample was wrong and is
    replaced: it took A = [0,1] and f(t) = (cos 2 pi t, sin 2 pi t) with a = 0, b = infinity, and claimed that
    f was nullhomotopic because A is contractible. A nullhomotopy of f has to lie in the target S^2 - a - b,
    where that loop winds once about a and is not nullhomotopic, so the example does not satisfy the
    hypothesis of the lemma, and it proved nothing. The replacement folds the circle once around and back, which
    is nullhomotopic by an explicit homotopy in the image. Checked against Lemma 62.2 (printed p. 382), whose
    statement is restated on the card, and Theorem 61.3 (printed p. 379).
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

A small circle about $a$ in a coordinate chart is such a $C$: the closed disk it bounds lies in the chart, so after possibly shrinking it, $b\notin D$. The circle is compact and $S^2$ Hausdorff, so $g$ has continuous inverse and is a homeomorphism onto $C$.

:::

:::

::: pf-step

Define $f:S^1\to S^2-\theset{a,b}$ by running once around $C$ and back, and note that it is continuous, non-injective, and has image $C$.

::: pf-proof

Let $\varphi:[0,2\pi]\to[0,2\pi]$ be $\varphi(\theta)=\theta$ for $0\le\theta\le\pi$ and $\varphi(\theta)=2\pi-\theta$ for $\pi\le\theta\le2\pi$, and set $f(\theta)=g(e^{i\varphi(\theta)})$. It is continuous by the pasting lemma, and its image is $C\subseteq S^2-\theset{a,b}$ because $C$ avoids $a$ and $b$. It is not injective: $f(\theta)=f(2\pi-\theta)$ for $0<\theta<\pi$, so the two points $\theta$ and $2\pi-\theta$ of $S^1$ have the same image.

:::

:::

::: pf-step

$f$ is nullhomotopic.

::: pf-proof

Define $H:S^1\times I\to C$ by $H(\theta,s)=g\bigl(e^{i(1-s)\varphi(\theta)}\bigr)$. It is continuous, $H(\theta,0)=f(\theta)$, and $H(\theta,1)=g(1)$ is constant. So $f$ is homotopic, within $S^2-\theset{a,b}$, to a constant map.

:::

:::

::: pf-step

$a$ and $b$ lie in different components of $S^2-f(A)$.

::: pf-proof

$f(A)=C$ bounds the disk $D$ with $a\in D$ and $b\notin D$. By Theorem 61.3 (printed p. 379) the simple closed curve $C$ separates $S^2$; its complement is $\operatorname{Int}D\cup(S^2-D)$, two disjoint nonempty open sets, and $a$ lies in the first while $b$ lies in the second (both being nonempty open connected sets, they are the components). So $a$ and $b$ are in different components.

:::

:::

::: pf-qed

$f$ is continuous, has compact domain and image in $S^2-\theset{a,b}$, and is nullhomotopic, but is not injective and its image separates $a$ from $b$; so the Borsuk lemma needs the injectivity hypothesis.

:::

:::
:::
