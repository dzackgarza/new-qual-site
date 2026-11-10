---
schema: qual/card@1
id: E-71YOD
kind: problem
title: Regular spaces have disjoint closure neighborhoods of points
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 31 Exercise 1, printed p. 32
    (tmp/sources/munkres-solutions-anadeore.pdf), and "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 31.1, printed p. 4
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 31 Exercise 1, printed p. 199, and Lemma 31.1(a), printed p. 196. What was corrected:
    Doug's World writes that the two shrunken neighbourhoods V_x and V_y "are disjoint", whereas
    what its own construction gives is that their closures lie in the disjoint open sets U_x and
    U_y, which is the disjointness of the closures that the exercise asks for; the card states the
    conclusion at the level of closures.
---

::: {.exercise}

Show that if $X$ is regular, every pair of points of $X$ have neighborhoods whose closures are disjoint.
:::

::: {.solution}

::: pf

::: {.pf-step #separate-by-disjoint-opens}
Separation of distinct points by disjoint open sets:
Let $x, y \in X$ be distinct points ($x \neq y$).
There exist disjoint open sets $U_0, V_0 \subseteq X$ such that $x \in U_0$ and $y \in V_0$.

::: pf-proof

::: pf-step
In a regular space, one-point sets are closed ($T_1$ axiom), so $\{y\}$ is closed in $X$.
:::

::: pf-step
Because $x \neq y$, $x \notin \{y\}$.
:::

::: pf-step
By regularity of $X$, there exist disjoint open sets $U_0$ containing $x$ and $V_0$ containing $\{y\}$ such that $U_0 \cap V_0 = \varnothing$.
:::

:::

:::

::: {.pf-step #shrink-to-closed-containment}
Shrinking to open neighborhoods with closed containment:
There exist open neighborhoods $U \subseteq X$ of $x$ and $V \subseteq X$ of $y$ such that $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.

::: pf-proof

::: pf-step
By the standard characterization of regularity (Munkres Lemma 31.1), for any point $p$ and open neighborhood $W$ of $p$, there exists an open neighborhood $N$ of $p$ with $\overline{N} \subseteq W$.
:::

::: pf-step
Applying this to the point $x$ and its open neighborhood $U_0$, there exists an open neighborhood $U$ of $x$ such that $\overline{U} \subseteq U_0$.
:::

::: pf-step
Applying this to the point $y$ and its open neighborhood $V_0$, there exists an open neighborhood $V$ of $y$ such that $\overline{V} \subseteq V_0$.
:::

:::

:::

::: pf-step
Disjointness of the closures:

::: pf-proof

::: pf-step
By step [](#shrink-to-closed-containment){.pf-ref}, $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.
:::

::: pf-step
Therefore:
$$\overline{U} \cap \overline{V} \subseteq U_0 \cap V_0.$$
:::

::: pf-step
By step [](#separate-by-disjoint-opens){.pf-ref}, $U_0 \cap V_0 = \varnothing$, so $\overline{U} \cap \overline{V} = \varnothing$.
:::

:::

:::

::: pf-step
Conclusion:
$U$ and $V$ are open neighborhoods of $x$ and $y$ respectively with $\overline{U} \cap \overline{V} = \varnothing$. Q.E.D.
:::

:::

:::
