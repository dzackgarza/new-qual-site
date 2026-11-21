---
schema: qual/card@1
id: E-SS8.EX-19
kind: problem
title: The plane slit along parallel rays is simply connected
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, five of them, each with its proof, without
    changing the mathematics: the reduction to distinct $A_k$ together with the path connectivity of
    $\Omega$ that simple connectivity needs, the height $h$ from compactness, the vertical-translation
    homotopy with the argument that it never meets a deleted ray, the straight-line contraction in the
    convex upper half-plane, and the conclusion. No retained solution set covers this collection's
    Exercise 19, so the card says the argument is the card's own. Citation by numbered statement only;
    nothing paginated is written. Not checked: no certificate, and no source was consulted for the
    exercise in this pass.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Prove that the complex plane slit along the union of the rays $\bigcup_{k=1}^{n} \{A_k + iy : y \leq 0\}$ is simply connected.

[Hint: Given a curve, first "raise" it so that it is completely contained in the upper half-plane.]
:::

::: {.solution}
The argument is the card's own: the statement is not an exercise of a published solution set, and no retained set covers this collection.

::: pf

::: {.pf-step #setup}
Let $\Omega=\CC\setminus\bigcup_{k=1}^n\{A_k+iy:y\le0\}$ with the $A_k$ distinct; it suffices to show that every closed curve in $\Omega$ is null-homotopic.

::: pf-proof
Deleting repetitions from the list of $A_k$ does not change the union of the rays, so the $A_k$ may be assumed distinct. A path-connected space is simply connected exactly when each of its closed curves is null-homotopic, and $\Omega$ is path connected: it contains the upper half-plane, which is convex, and each point of $\Omega$ below the real axis can be joined to a point above it by a vertical segment avoiding the finitely many deleted rays.
:::

:::

::: {.pf-step #raise}
For a closed curve $\gamma\colon[0,1]\to\Omega$ there is $h>0$ with $\Im\gamma(t)+h>0$ for all $t$.

::: pf-proof
The image of $\gamma$ is compact, so $\Im\gamma$ attains a minimum $m$; since $\gamma(t)\in\Omega$ and no ray $\{A_k+iy:y\le0\}$ contains a point of positive imaginary part, $m$ is finite and $m>-h$ for every $h>\max(0,-m)$, which is a positive number.
:::

:::

::: {.pf-step #translation}
The vertical translation $H(t,s)=\gamma(t)+ish$ is a homotopy in $\Omega$ from $\gamma$ to the closed curve $\gamma+hi$, which lies in the upper half-plane.

::: pf-proof
$H$ is continuous and fixes $t=0$ and $t=1$ up to the translation, which is the same at both ends because $\gamma(0)=\gamma(1)$. If $H(t,s)$ lay on the $k$-th deleted ray, then $\Re\gamma(t)=A_k$ and $\Im\gamma(t)+sh\le0$, so $\Im\gamma(t)\le-sh\le0$ and $\gamma(t)$ itself lies on that ray, contradicting $\gamma(t)\in\Omega$. At $s=1$ the curve is $\gamma+hi$ and $\Im(\gamma(t)+hi)=\Im\gamma(t)+h>0$ by step [](#raise){.pf-ref}.
:::

:::

::: {.pf-step #contract}
The translated curve contracts in $\Omega$ to a point.

::: pf-proof
The upper half-plane is convex, so $\gamma+hi$ contracts there by the straight-line homotopy $F(t,s)=(1-s)(\gamma(t)+hi)+s\,p_0$ to a fixed point $p_0$ of the upper half-plane; every point of that homotopy is a convex combination of two points of the upper half-plane, hence in the upper half-plane. Since the upper half-plane is contained in $\Omega$, this is a contraction in $\Omega$, and composing it with the homotopy of step [](#translation){.pf-ref} contracts $\gamma$.
:::

:::

::: {.pf-step}
$\Omega$ is simply connected.

::: pf-proof
Steps [](#setup){.pf-ref}, [](#translation){.pf-ref} and [](#contract){.pf-ref} contract every closed curve in $\Omega$, which is the definition of simple connectivity for a path-connected space.
:::

:::

:::

:::

