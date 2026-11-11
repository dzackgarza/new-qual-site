---
schema: qual/card@1
id: E-CKXKK
kind: problem
title: $G_\delta$ subspaces of compact Hausdorff or complete metric spaces are Baire
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 5 was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, following the
    exercise's hint, and with Theorem 48.2 (compact Hausdorff and complete metric spaces are Baire), Theorem
    26.9 (finite intersection property) and Lemma 48.3 for the nested closed sets of the metric case. What was
    corrected: the choice of the neighbourhood U_n avoided the closure of B_n by invoking only closedness of
    B_n in Y, which does not by itself produce an X-open neighbourhood of a point of Y outside B_n whose closure
    misses the X-closure of B_n; the text now names a closed C in X with B_n = C cap Y, notes that the chosen
    point lies outside C, and takes the neighbourhood inside the X-open set X - C, which is where the avoidance
    of the closure comes from. It also now says why it suffices to run the construction from an arbitrary open
    U_0 with U_0 cap Y nonempty: every nonempty relatively open subset of Y arises that way. The remaining steps
    are the hint's: nestedness with the diameter bound gives a Cauchy sequence whose limit lies in every
    closure, the compact case uses the finite intersection property instead, and the point found lies in Y, in
    U_0, and outside every B_n.
---

::: {.exercise}

Show that if $Y$ is a $G_\delta$ set in $X$, and if $X$ is compact Hausdorff or complete metric, then $Y$ is a Baire space in the subspace topology.
[Hint: Suppose that $Y = \bigcap W_n$, where $W_n$ is open in $X$, and that $B_n$ is closed in $Y$ and has empty interior in $Y$.
Given $U_0$ open in $X$ with $U_0 \cap Y \neq \varnothing$, find a sequence of open sets $U_n$ of $X$ with $U_n \cap Y$ nonempty, such that

$$
\begin{array}{c}
\overline{U}_n \subset U_{n-1}, \\
\overline{U}_n \cap \overline{B}_n = \varnothing, \\
\operatorname{diam} U_n < 1/n \quad \text{in the metric case}, \\
\overline{U}_n \subset W_n.
\end{array}
$$
]
:::

::: {.solution}
Write $Y=\bigcap_{n\ge1}W_n$ with $W_n$ open in $X$. To prove $Y$ Baire, let $B_n$ be closed nowhere dense subsets of $Y$ and let $U_0$ be open in $X$ with $U_0\cap Y\ne\varnothing$. We construct nonempty open $U_n$ meeting $Y$ such that
$$
\overline U_n\subset U_{n-1}\cap W_n,\qquad
\overline U_n\cap\overline{B_n}^{\,X}=\varnothing,
$$
and in the metric case also $\operatorname{diam}U_n<1/n$.

Indeed, since $B_n$ has empty interior in $Y$, the nonempty relatively open set $U_{n-1}\cap W_n\cap Y$ contains a point $y$ outside $B_n$. Since $B_n$ is closed in $Y$, there is a closed $C\subset X$ with $B_n=C\cap Y$, and $y\notin C$; hence $X-C$ is an open neighbourhood of $y$ disjoint from $C\supset B_n$, so its closure avoids $\overline{B_n}^{\,X}\subset C$. Intersecting with the open set $U_{n-1}\cap W_n$, in which $y$ lies, gives an $X$-open neighbourhood of $y$ whose closure is contained in $U_{n-1}\cap W_n$ and avoids $\overline{B_n}^{\,X}$; in the metric case shrink it further to have diameter below $1/n$, possible because metric spaces are regular and have a base of balls. (In the compact-Hausdorff case regularity alone suffices.) Set $U_n$ to be that neighbourhood.

If $X$ is compact Hausdorff, the nested compact sets $\overline U_n$ have nonempty intersection. If $X$ is complete metric, choose $x_n\in\overline U_n$; nestedness and the diameter bound make $(x_n)$ Cauchy, with limit in every $\overline U_n$. Thus choose $x\in\bigcap_n\overline U_n$. Since $\overline U_n\subset W_n$, $x\in Y$; since $\overline U_n$ avoids $B_n$, $x\notin\bigcup B_n$; and $x\in\overline U_1\subset U_0$. Since every nonempty relatively open $V\subset Y$ is $U_0\cap Y$ for some open $U_0\subset X$, this shows that no nonempty relatively open subset of $Y$ is covered by countably many closed subsets of $Y$ with empty interior in $Y$; so $Y$ is a Baire space.
:::
