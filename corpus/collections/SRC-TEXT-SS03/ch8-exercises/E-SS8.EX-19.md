---
schema: qual/card@1
id: E-SS8.EX-19
kind: problem
title: "SS 8.19: The plane slit along parallel rays is simply connected"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
19. Prove that the complex plane slit along the union of the rays $\cup _ { k = 1 } ^ { n } \{ A _ { k } + i y : y \leq 0 \}$ is simply connected.

[Hint: Given a curve, first “raise” it so that it is completely contained in the upper half-plane.]
:::

::: {.solution}
Let
\[
\Omega=\mathbb C\setminus\bigcup_{k=1}^n\{A_k+iy:y\le0\}.
\]
After deleting repetitions, assume the real numbers $A_k$ are distinct. We prove that every closed curve in $\Omega$ is null-homotopic.

Let $\gamma:[0,1]\to\Omega$ be closed. Its compact image has positive distance from the closed deleted set, so there is $\varepsilon>0$ such that the horizontal $\varepsilon$-neighborhood of $\gamma([0,1])$ still avoids every slit whenever a homotopy below crosses the real line away from the $A_k$'s. First perturb $\gamma$ slightly, if necessary, so that whenever $\Re\gamma(t)=A_k$ one has $\Im\gamma(t)>0$; compactness then gives a number $h>0$ such that
\[
\Im\gamma(t)+h>0\qquad(0\le t\le1).
\]
Consider the vertical translation homotopy
\[
H(t,s)=\gamma(t)+ish,
\qquad 0\le s\le1.
\]
If $H(t,s)$ lay on the $k$th deleted ray, then $\Re\gamma(t)=A_k$ and $\Im\gamma(t)+sh\le0$. But at every $t$ with $\Re\gamma(t)=A_k$ we arranged $\Im\gamma(t)>0$, a contradiction. Thus $H$ is a homotopy in $\Omega$ from $\gamma$ to the closed curve $\gamma+h i$, which lies entirely in the upper half-plane.

The upper half-plane is convex. Hence $\gamma+hi$ contracts there, by the straight-line homotopy to any fixed point of the upper half-plane. Since the upper half-plane is contained in $\Omega$, this is also a contraction in $\Omega$. Therefore every closed curve in $\Omega$ is null-homotopic, and $\Omega$ is simply connected.
:::
