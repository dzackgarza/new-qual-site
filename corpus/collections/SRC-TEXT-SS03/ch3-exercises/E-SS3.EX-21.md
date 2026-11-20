---
schema: qual/card@1
id: E-SS3.EX-21
kind: problem
title: Convex and star-shaped open sets are simply connected
classification:
  areas:
    - complex-analysis
  topics: [Simply Connected Domains, Convex Sets, Star-Shaped Domains]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: convexity gives the straight-line homotopy $H(s,t)=(1-s)\gamma(t)+sz_0$ inside $\Omega$; star-shapedness gives the same formula; and the two examples, the slit plane from the point $1$ and a sector from a point of its bisecting ray, are genuinely star-shaped about the stated centre.
---

::: {.exercise}
Certain sets have geometric properties that guarantee they are simply connected.

(a) An open set $\Omega \subset \CC$ is convex if for any two points in $\Omega$, the straight line segment between them is contained in $\Omega$. Prove that a convex open set is simply connected.

(b) More generally, an open set $\Omega \subset \CC$ is star-shaped if there exists a point $z_0 \in \Omega$ such that for any $z \in \Omega$, the straight line segment between $z_0$ and $z$ is contained in $\Omega$. Prove that a star-shaped open set is simply connected. Conclude that the slit plane $\CC - \{(-\infty, 0]\}$ (and more generally any sector, convex or not) is simply connected.

(c) What are other examples of open sets that are simply connected?
:::

::: {.solution}
The statement is Exercise 21 of Stein--Shakarchi, *Complex Analysis* [@SS03, ch. 3, §8, Exercise 21], printed beginning "Certain sets have geometric properties that guarantee that they are simply connected".

No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own.

::: pf

::: {.pf-step #a}
(a) A convex open set is simply connected.

::: pf-proof
Fix $z_0\in\Omega$. For a closed curve $\gamma:[0,1]\to\Omega$ put $H(s,t)=(1-s)\gamma(t)+sz_0$. For each $(s,t)$ this is a convex combination of two points of $\Omega$, hence lies in $\Omega$ by convexity; $H(0,t)=\gamma(t)$, $H(1,t)=z_0$ and $H(s,0)=H(s,1)$, so $H$ is a homotopy of loops in $\Omega$ from $\gamma$ to the constant loop at $z_0$. Hence every loop is null-homotopic and $\Omega$ is simply connected.
:::
:::

::: {.pf-step #b}
(b) A star-shaped open set is simply connected.

::: pf-proof
Take the point $z_0$ of the definition. The same formula $H(s,t)=(1-s)\gamma(t)+sz_0$ runs inside $\Omega$ because each segment from $z_0$ to a point of $\Omega$ lies there, and the same three identities show $H$ contracts every loop to $z_0$.
:::
:::

::: {.pf-step #slit}
The slit plane $\CC\setminus(-\infty,0]$ is star-shaped, hence simply connected.

::: pf-proof
Take $z_0=1$. If $z$ is not on the nonpositive real axis, the segment from $1$ to $z$ meets that ray at most at an endpoint, which is excluded; so the segment lies in the slit plane and the set is star-shaped about $1$.
:::
:::

::: {.pf-step #sector}
A sector $\{z\neq0:\alpha<\arg z<\beta\}$ with $0<\beta-\alpha\le2\pi$ is star-shaped, hence simply connected.

::: pf-proof
Take $c$ on the bisecting ray. Every $z$ of the sector has argument within $(\beta-\alpha)/2\le\pi$ of $\arg c$, so along the segment from $c$ to $z$ the argument varies continuously between the two values and the segment never contains $0$; hence it lies in the sector.
:::
:::

::: {.pf-step #c}
(c) Discs, half-planes, strips, convex polygons and the whole plane are further examples.

::: pf-proof
Each of these is convex, so part (a) applies to it.
:::
:::

:::
:::
