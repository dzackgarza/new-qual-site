---
schema: qual/card@1
id: E-BI0O0
kind: exercise
title: Interior and boundary of a subset
classification:
  areas:
  - topology
  topics:
  - Boundary
  - Interior
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

If $A \subset X$, we define the boundary of $A$ by the equation

$$
\operatorname{Bd} A = \overline{A} \cap \overline{(X - A)}.
$$

(a) Show that $\operatorname{Int} A$ and $\operatorname{Bd} A$ are disjoint, and $\overline{A} = \operatorname{Int} A \cup \operatorname{Bd} A$.

(b) Show that $\operatorname{Bd} A = \varnothing$ if and only if $A$ is both open and closed.

(c) Show that $U$ is open if and only if $\operatorname{Bd} U = \overline{U} - U$.

(d) If $U$ is open, is it true that $U = \operatorname{Int}(\overline{U})$?
Justify your answer.
:::

::: {.solution}
**Part (a).**

<1>1. $\operatorname{Int} A \cap \operatorname{Bd} A = \varnothing$.
::: {.proof}
$\operatorname{Int} A \subseteq A$ and $\operatorname{Bd} A \subseteq \overline{X - A} = X - \operatorname{Int} A$, so they are disjoint.
:::

<1>2. $\overline A = \operatorname{Int} A \cup \operatorname{Bd} A$.
::: {.proof}
$\overline A = \operatorname{Int} A \cup (\overline A \setminus \operatorname{Int} A)$, and $\overline A \setminus \operatorname{Int} A = \overline A \cap (X - \operatorname{Int} A) = \overline A \cap \overline{X - A} = \operatorname{Bd} A$.
:::

**Part (b).**

<1>1. ($\Rightarrow$) If $\operatorname{Bd} A = \varnothing$, then $A$ is both open and closed.
<2>1. $\overline A = \operatorname{Int} A$ (by part (a), since $\operatorname{Bd} A = \varnothing$).
::: {.proof}
part (a).
:::
<2>2. Hence $A \subseteq \overline A = \operatorname{Int} A \subseteq A$, so $A = \operatorname{Int} A$, i.e. $A$ is open.
::: {.proof}
<2>1.
:::
<2>3. Also $\overline A = \operatorname{Int} A \subseteq A$, so $A$ is closed.
::: {.proof}
<2>1.
:::

<1>2. ($\Leftarrow$) If $A$ is both open and closed, then $\operatorname{Bd} A = \varnothing$.
::: {.proof}
if $A$ is open and closed, then $\overline A = A$ and $\overline{X - A} = X - A$, so $\operatorname{Bd} A = A \cap (X - A) = \varnothing$.
:::

**Part (c).**

<1>1. ($\Rightarrow$) If $U$ is open, then $\operatorname{Bd} U = \overline U - U$.
::: {.proof}
$\operatorname{Bd} U = \overline U \cap \overline{X - U} = \overline U \cap (X - U)$ (since $U$ is open, $X - U$ is closed, so $\overline{X - U} = X - U$), which equals $\overline U - U$.
:::

<1>2. ($\Leftarrow$) If $\operatorname{Bd} U = \overline U - U$, then $U$ is open.
::: {.proof}
$\operatorname{Bd} U = \overline U \cap \overline{X - U} = \overline U - U$ means $\overline U \cap \overline{X - U} = \overline U \cap (X - U)$, which holds iff $\overline{X - U} = X - U$, i.e. $X - U$ is closed, i.e. $U$ is open.
:::

**Part (d).**

<1>1. No, $U = \operatorname{Int}(\overline U)$ is not always true for open $U$.
::: {.proof}
exhibit a counterexample.
:::

<1>2. Counterexample: $U = \RR \setminus \{0\}$ in $\RR$ (open).
::: {.proof}
$U$ is open.
:::

<1>3. $\overline U = \RR$, so $\operatorname{Int}(\overline U) = \RR \neq U$.
::: {.proof}
$\overline{\RR \setminus \{0\}} = \RR$, and $\operatorname{Int}(\RR) = \RR \neq \RR \setminus \{0\}$.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 (a), <1>1–<1>2 (b), <1>1–<1>2 (c), and <1>3 (d).
:::
:::
