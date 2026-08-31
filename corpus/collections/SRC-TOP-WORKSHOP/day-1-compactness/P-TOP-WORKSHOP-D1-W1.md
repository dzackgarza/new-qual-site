---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-W1
kind: problem
title: A compact subset of a $T_2$ space is closed (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
If $X$ is $T_2$ and $A\subseteq X$ is compact, then $A$ is closed.
:::

::: {.solution}
<1>1. It suffices to show $X \setminus A$ is open.
::: {.proof}
a set is closed iff its complement is open.
:::

<1>2. Let $x \in X \setminus A$.
::: {.proof}
take an arbitrary point outside $A$.
:::

<1>3. For each $a \in A$, there are disjoint open sets $U_a \ni x$ and $V_a \ni a$.
::: {.proof}
$X$ is Hausdorff and $x \neq a$.
:::

<1>4. $\{V_a\}_{a \in A}$ is an open cover of $A$.
::: {.proof}
each $a \in A$ lies in $V_a$.
:::

<1>5. Since $A$ is compact, there is a finite subcover $A \subseteq V_{a_1} \cup \cdots \cup V_{a_k}$.
::: {.proof}
compactness.
:::

<1>6. Let $U = U_{a_1} \cap \cdots \cap U_{a_k}$.
::: {.proof}
define a neighborhood of $x$.
:::

<1>7. $U$ is open, contains $x$, and is disjoint from $A$.
::: {.proof}
$U$ is a finite intersection of open sets containing $x$; and $U \cap V_{a_i} = \varnothing$ for each $i$ (since $U \subseteq U_{a_i}$ and $U_{a_i} \cap V_{a_i} = \varnothing$), so $U \cap A = \varnothing$ by <1>5.
:::

<1>8. Hence $x$ is an interior point of $X \setminus A$, so $X \setminus A$ is open.
::: {.proof}
<1>7 holds for every $x \in X \setminus A$.
:::

<1>9. Therefore $A$ is closed.
::: {.proof}
<1>1 and <1>8.
:::

<1>10. Q.E.D.
::: {.proof}
<1>9.
:::
:::
