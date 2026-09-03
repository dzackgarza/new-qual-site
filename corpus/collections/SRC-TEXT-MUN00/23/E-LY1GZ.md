---
schema: qual/card@1
id: E-LY1GZ
kind: problem
title: Connected sets crossing a set and its complement meet the boundary
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Boundary
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $A \subset X$.
Show that if $C$ is a connected subspace of $X$ that intersects both $A$ and $X - A$, then $C$ intersects $\operatorname{Bd} A$.
:::

::: {.solution}
<1>1. Suppose for contradiction that $C \cap \operatorname{Bd} A = \varnothing$.
::: {.proof}
assume the conclusion fails.
:::

<1>2. Then $C \subseteq X - \operatorname{Bd} A = \operatorname{Int} A \cup \operatorname{Int}(X - A)$.
::: {.proof}
$X$ is the disjoint union $\operatorname{Int} A \sqcup \operatorname{Bd} A \sqcup \operatorname{Int}(X - A)$.
:::

<1>3. Hence $C = (C \cap \operatorname{Int} A) \cup (C \cap \operatorname{Int}(X - A))$, a union of two disjoint sets open in $C$.
::: {.proof}
<1>2, and $\operatorname{Int} A \cap \operatorname{Int}(X - A) = \varnothing$.
:::

<1>4. Since $C$ is connected, one of these two sets is empty.
::: {.proof}
<1>3 and the definition of connectedness (no separation by disjoint nonempty open sets).
:::

<1>5. If $C \cap \operatorname{Int} A = \varnothing$, then $C \subseteq \operatorname{Int}(X - A) \subseteq X - A$, contradicting $C \cap A \neq \varnothing$.
::: {.proof}
<1>4, first case.
:::

<1>6. If $C \cap \operatorname{Int}(X - A) = \varnothing$, then $C \subseteq \operatorname{Int} A \subseteq A$, contradicting $C \cap (X - A) \neq \varnothing$.
::: {.proof}
<1>4, second case.
:::

<1>7. Both cases contradict the hypotheses, so $C \cap \operatorname{Bd} A \neq \varnothing$.
::: {.proof}
<1>5 and <1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
