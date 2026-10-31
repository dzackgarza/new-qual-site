---
schema: qual/card@1
id: E-YQUO1
kind: problem
title: Peano spaces and the Hahn-Mazurkiewicz theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Let $X$ be a Hausdorff space.
Show that if there is a continuous surjective map $f: I \to X$, then $X$ is compact, connected, weakly locally connected, and metrizable.
[Hint: Show $f$ is a perfect map.]

(b) The converse of the result in (a) is a famous theorem of point-set topology called the Hahn-Mazurkiewicz theorem (see [H-Y], p. 129). Assuming this theorem, show there is a continuous surjective map $f: I \to I^\omega$.

A Hausdorff space that is the continuous image of the closed unit interval is often called a Peano space.
:::

::: {.solution}
(a) Let $f:I\to X$ be continuous and surjective, with $X$ Hausdorff. Since $I$ is compact, $X=f(I)$ is compact. Since $I$ is connected, $X$ is connected.

The map $f$ is closed: a closed subset of $I$ is compact, and its image is compact, hence closed in the Hausdorff space $X$. Its fibers are closed subsets of $I$, hence compact. Thus $f$ is a perfect quotient map.

Let $x\in X$ and let $U$ be an open neighborhood of $x$. The compact fiber $F=f^{-1}(x)$ lies in the open set $f^{-1}(U)$. Cover $F$ by finitely many connected open intervals $V_1,\ldots,V_m$ contained in $f^{-1}(U)$. Each $f(V_i)$ is connected and contains $x$, so $C=\bigcup_i f(V_i)$ is connected and lies in $U$. Since $f$ is closed and $\bigcup_i V_i$ is an open neighborhood of $F$, the set $X\setminus f(I\setminus\bigcup_i V_i)$ is an open neighborhood of $x$ contained in $C$. Thus $C$ is a connected neighborhood of $x$ inside $U$, and $X$ is weakly locally connected.

Finally, $I$ is second countable, and perfect maps preserve second countability by [[E-Y4MFU]](d). Thus $X$ is second countable. A compact Hausdorff space is regular, so the Urysohn metrization theorem implies that $X$ is metrizable.

Therefore every Hausdorff continuous image of $I$ is compact, connected, weakly locally connected, and metrizable.

(b) The Hilbert cube
$$
I^\omega=\prod_{n\ge1}I
$$
is compact by the Tychonoff theorem, connected because a product of connected spaces is connected, and metrizable because it is a countable product of metrizable spaces. It is also locally connected: a basic product neighborhood restricts only finitely many coordinates, and in those coordinates we can choose connected open intervals; the resulting product is connected and gives a connected neighborhood basis.

Hence $I^\omega$ satisfies the hypotheses of the Hahn--Mazurkiewicz theorem. Therefore there exists a continuous surjection
$$
I\twoheadrightarrow I^\omega.
$$
:::
