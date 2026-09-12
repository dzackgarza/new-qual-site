---
schema: qual/card@1
id: E-RWKRJ
kind: problem
title: Continuous maps with continuous sections are quotient maps
classification:
  areas:
  - topology
  topics:
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

(a) Let $p: X \to Y$ be a continuous map.
Show that if there is a continuous map $f: Y \to X$ such that $p \circ f$ equals the identity map of $Y$, then $p$ is a quotient map.

(b) If $A \subset X$, a retraction of $X$ onto $A$ is a continuous map $r: X \to A$ such that $r(a) = a$ for each $a \in A$.
Show that a retraction is a quotient map.
:::

::: {.solution}
(a) Since $p\circ f=\operatorname{id}_Y$, the map $p$ is surjective. Let $U\subseteq Y$ and suppose $p^{-1}(U)$ is open in $X$. Then
\[
U=(p\circ f)^{-1}(U)=f^{-1}(p^{-1}(U)).
\]
Because $f$ is continuous, $U$ is open. Thus $U$ is open iff $p^{-1}(U)$ is open, so $p$ is a quotient map.

(b) If $r:X\to A$ is a retraction, the inclusion $j:A\hookrightarrow X$ is continuous and
\[
r\circ j=\operatorname{id}_A.
\]
Part (a), with $p=r$ and $f=j$, shows that every retraction is a quotient map.
:::
