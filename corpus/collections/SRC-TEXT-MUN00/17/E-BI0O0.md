---
schema: qual/card@1
id: E-BI0O0
kind: problem
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
Throughout, $\overline{X-A}=X-\operatorname{Int}A$, since $\operatorname{Int}A$ is the largest open set contained in $A$ and $\overline{X-A}$ is the smallest closed set containing $X-A$.

<1>1. (a) $\operatorname{Int}A\cap\operatorname{Bd}A=\varnothing$ and $\overline A=\operatorname{Int}A\cup\operatorname{Bd}A$.

::: {.proof}
$\operatorname{Bd}A\subseteq\overline{X-A}=X-\operatorname{Int}A$, so $\operatorname{Bd}A$ misses $\operatorname{Int}A$.
Since $\operatorname{Int}A\subseteq\overline A$,
$$
\overline A=\operatorname{Int}A\cup\bigl(\overline A\cap(X-\operatorname{Int}A)\bigr)=\operatorname{Int}A\cup\bigl(\overline A\cap\overline{X-A}\bigr)=\operatorname{Int}A\cup\operatorname{Bd}A.
$$
:::

<1>2. (b) $\operatorname{Bd}A=\varnothing$ if and only if $A$ is both open and closed.

::: {.proof}
If $\operatorname{Bd}A=\varnothing$, step <1>1 gives $\overline A=\operatorname{Int}A$, so $A\subseteq\overline A=\operatorname{Int}A\subseteq A$.
Hence $A=\operatorname{Int}A$ is open and $A=\overline A$ is closed.
Conversely, if $A$ is open and closed, then $\overline A=A$ and $\overline{X-A}=X-A$, so $\operatorname{Bd}A=A\cap(X-A)=\varnothing$.
:::

<1>3. (c) $U$ is open if and only if $\operatorname{Bd}U=\overline U-U$.

::: {.proof}
Since $\overline{X-U}\supseteq X-U$ and $\overline U\cap(X-U)=\overline U-U$,
$$
\operatorname{Bd}U=(\overline U-U)\cup\bigl(\overline U\cap(\overline{X-U}-(X-U))\bigr).
$$
The set $\overline{X-U}-(X-U)$ is contained in $U\subseteq\overline U$, so the second term equals $\overline{X-U}-(X-U)$, which is disjoint from $\overline U-U$.
Hence $\operatorname{Bd}U=\overline U-U$ if and only if $\overline{X-U}=X-U$, that is, if and only if $X-U$ is closed, that is, if and only if $U$ is open.
:::

<1>4. (d) An open set $U$ need not equal $\operatorname{Int}(\overline U)$.

::: {.proof}
In $\RR$, the open set $U=\RR-\{0\}$ has $\overline U=\RR$, so $\operatorname{Int}(\overline U)=\RR\ne U$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, <1>3, and <1>4 answer (a), (b), (c), and (d).
:::
:::
