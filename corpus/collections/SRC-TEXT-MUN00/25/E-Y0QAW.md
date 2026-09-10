---
schema: qual/card@1
id: E-Y0QAW
kind: problem
title: Quotients of locally connected spaces are locally connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
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

Let $p: X \to Y$ be a quotient map.
Show that if $X$ is locally connected, then $Y$ is locally connected.
[Hint: If $C$ is a component of the open set $U$ of $Y$, show that $p^{-1}(C)$ is a union of components of $p^{-1}(U)$.]
:::

::: {.solution}
We use the characterization that a space is locally connected iff components of open sets are open.

Let $U\subseteq Y$ be open and let $C$ be a component of $U$. Since $p$ is quotient,
\[
p^{-1}(U)
\]
is open in $X$. Because $X$ is locally connected, every component of $p^{-1}(U)$ is open.

We claim that $p^{-1}(C)$ is a union of components of $p^{-1}(U)$. Let $D$ be a component of $p^{-1}(U)$ meeting $p^{-1}(C)$. Then $p(D)$ is connected, lies in $U$, and meets $C$. By maximality of the component $C$ in $U$,
\[
p(D)\subseteq C,
\]
so $D\subseteq p^{-1}(C)$. This proves the claim.

Hence $p^{-1}(C)$ is open in $X$. It is also saturated, and $p$ is a quotient map, so $C$ is open in $Y$. Thus every component of every open subset of $Y$ is open, and $Y$ is locally connected.
:::
