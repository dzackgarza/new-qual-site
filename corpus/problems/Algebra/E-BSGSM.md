---
schema: qual/card@1
id: E-BSGSM
kind: exercise
title: Normal subgroups are unions of conjugacy classes
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Show that normal groups absorb conjugacy classes: if $N\normal G$ and $[g_i]$ is a conjugacy class in $g$, either $[g_i] \subseteq N$ or $[g_i] \intersect N = \emptyset$.
:::

::: {.solution}
<1>1. Suppose $[g_i] \cap N \neq \varnothing$, and let $h \in [g_i] \cap N$.
Proof: assume the intersection is nonempty.

<1>2. Then $[g_i] = \{x h x^{-1} : x \in G\}$ (the conjugacy class of $h$).
Proof: $h \in [g_i]$, so $[g_i]$ is the conjugacy class of $h$.

<1>3. For every $x \in G$, $x h x^{-1} \in N$.
Proof: $N$ is normal, so it is closed under conjugation.

<1>4. Hence $[g_i] \subseteq N$.
Proof: <1>2 and <1>3.

<1>5. Therefore either $[g_i] \subseteq N$ or $[g_i] \cap N = \varnothing$.
Proof: <1>1–<1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
