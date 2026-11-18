---
schema: qual/card@1
id: E-QOXG5
kind: problem
title: Countable compactness equals limit point compactness for T1 spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 4, printed p. 181, with the
    definition of countable compactness printed there and Exercise 17.15; the stored
    statement and hint are printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.4, PDF pp. 18-19. Countable compactness gives
    limit point compactness with no separation hypothesis, and the converse uses T1 to
    isolate the limit point from finitely many chosen points. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3,
    Exercise 28.4, PDF pp. 18-19). Pages verified: both definitions on printed p. 178, the
    exercise on printed p. 181, and Exercise 17.15, which supplies the T1 separation used,
    on printed p. 101. One step supplied that the retained text asserts: the set A = {x_n}
    chosen against a countable cover with no finite subcover is infinite, because a value
    taken infinitely often would lie outside every U_k and hence outside their union, which
    is X. Also written out: the closed subspace step's detail that X - Y is open, and that a
    subset of a set with no limit point has no limit point, which is what lets the countably
    infinite B be used in place of A. The statement and the printed hint are unchanged; the
    T1 hypothesis is noted as used only in the second direction.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Review repair of the final step, where the argument was wrong as written: it asserted
    y is different from every x_i with i <= N and excluded x_i from a neighbourhood V_i of y,
    but the limit point of A may be one of the points of A. The neighbourhood is now built
    only over the indices i <= N with x_i != y, and intersected with U_N rather than with the
    union: W = (intersection over those i of V_i) and U_N. Then W is open and contains y, and
    every point of A in W is y itself -- for i <= N with x_i != y, x_i is excluded by V_i,
    and for n > N, x_n is outside U_1 u ... u U_n which contains U_N -- so
    W and (A - {y}) = empty, which is the contradiction with y being a limit point.
---

::: {.exercise}

A space $X$ is said to be countably compact if every countable open covering of $X$ contains a finite subcollection that covers $X$.
Show that for a $T_1$ space $X$, countable compactness is equivalent to limit point compactness.
[Hint: If no finite subcollection of $U_n$ covers $X$, choose $x_n \notin U_1 \cup \dots \cup U_n$, for each $n$.]
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.4, PDF pp. 18--19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps and following the printed hint; one step it leaves implicit is supplied below, the infinitude of the sequence chosen against the cover.

Throughout, $X$ is a space; it is countably compact when every countable open cover has a finite subcover, and limit point compact when every infinite subset has a limit point (§28, printed p. 178, where both definitions are printed). The exercise is §28 Exercise 4 (printed p. 181), and the form of the $T_1$ axiom used is that of Exercise 17.15 (printed p. 101): any two distinct points have neighbourhoods each omitting the other.

::: pf

::: {.pf-step #closed}
A closed subspace $Y$ of a countably compact space $X$ is countably compact.

::: pf-proof
Let $\{G_n\}$ be a countable cover of $Y$ by sets open in $Y$, and for each $n$ choose an open $H_n$ in $X$ with $G_n=Y\cap H_n$. Then $\{H_n\}\cup\{X-Y\}$ is a countable open cover of $X$, since $X-Y$ is open as $Y$ is closed, and by countable compactness finitely many members cover $X$; those among them different from $X-Y$ restrict to a finite subcollection of $\{G_n\}$ covering $Y$.
:::

:::

::: {.pf-step #cc-to-lpc}
If $X$ is countably compact then $X$ is limit point compact; the $T_1$ hypothesis is not used here.

::: pf-proof

::: {.pf-step #no-limit-subset}
Suppose $A\subset X$ is infinite and has no limit point. Let $B\subset A$ be countably infinite; then $B$ has no limit point either, since a limit point of $B$ would be one of $A$.

::: pf-proof
A countably infinite subset of an infinite set exists; and if every neighbourhood of $y$ met $B$ in a point other than $y$, the same neighbourhood would meet $A$ in a point other than $y$, so $y$ would be a limit point of $A$.
:::

:::

::: {.pf-step #countable-cover}
$B$ is closed and countably compact, yet the sets $U_b$ below form a countable open cover of $B$ with no finite subcover.

::: pf-proof
$B$ is closed: a point outside $B$ is not a limit point of $B$, so it has a neighbourhood meeting $B$ in no point other than itself, and as that point is not in $B$ the neighbourhood misses $B$. Hence $B$ is countably compact by step [](#closed){.pf-ref}. For $b\in B$, since $b$ is not a limit point of $B$, there is an open neighbourhood $U_b$ of $b$ with $U_b\cap B\subset\{b\}$; as $b\in U_b$ this gives $U_b\cap B=\{b\}$. The family $\{U_b\}_{b\in B}$ is countable because $B$ is, and it covers $B$ because $b\in U_b$. A finite subcollection $\{U_{b_1},\dots,U_{b_k}\}$ meets $B$ in at most $\{b_1,\dots,b_k\}$, and $B$ is infinite, so it does not cover $B$.
:::

:::

:::

:::

::: {.pf-step #lpc-to-cc}
If $X$ is limit point compact and $T_1$ then $X$ is countably compact.

::: pf-proof

::: {.pf-step #sequence}
Suppose $\{U_n\}_{n\ge1}$ is a countable open cover of $X$ with no finite subcover. Then for each $n$ there is $x_n\notin U_1\cup\cdots\cup U_n$, and the set $A=\{x_n\}$ is infinite.

::: pf-proof
$\{U_1,\dots,U_n\}$ is a finite subcollection, so it does not cover $X$ and $x_n$ exists. If some value $y$ were taken by $x_n$ for infinitely many $n$, then for those $n$ we should have $y=x_n\notin U_1\cup\cdots\cup U_n$, hence $y\notin U_k$ for every $k$ (take $n\ge k$ among those indices), and then $y\notin\bigcup_nU_n=X$, which is impossible. So every value occurs only finitely often and $A$ is infinite.
:::

:::

::: {.pf-step #contradiction}
A limit point $y$ of $A$ gives a neighbourhood meeting $A$ in nothing, which is impossible.

::: pf-proof
$A$ is infinite, so limit point compactness gives a limit point $y$; since $\{U_n\}$ covers $X$, $y\in U_N$ for some $N$. The limit point $y$ may itself be one of the points $x_i$, so the neighbourhood below is built only over the indices with $x_i\ne y$: for each $i\le N$ with $x_i\ne y$ the $T_1$ axiom gives an open neighbourhood $V_i$ of $y$ with $x_i\notin V_i$ (Exercise 17.15, printed p. 101), and we put
$$
W=\Big(\bigcap_{i\le N,\ x_i\ne y}V_i\Big)\cap U_N,
$$
the intersection over an empty set of indices being $X$. Then $W$ is open and contains $y$, since $y\in U_N$ and $y\in V_i$ for each $i$ used. Every point of $A\cap W$ equals $y$: if $n\le N$ and $x_n\ne y$, then $x_n\notin V_n\supset W$; and if $n>N$, then $x_n\notin U_1\cup\cdots\cup U_n\supset U_N\supset W$. So $W$ is a neighbourhood of the limit point $y$ with $W\cap(A-\{y\})=\emptyset$, contradicting that every neighbourhood of $y$ meets $A$ in a point other than $y$.
:::

:::

:::

:::

::: {.pf-step}
For a $T_1$ space, countable compactness and limit point compactness are equivalent.

::: pf-proof
One direction is step [](#cc-to-lpc){.pf-ref}, which needs no separation hypothesis; the other is step [](#lpc-to-cc){.pf-ref}, which uses $T_1$ only to separate the limit point from the finitely many points $x_1,\dots,x_N$.
:::

:::

:::
:::
