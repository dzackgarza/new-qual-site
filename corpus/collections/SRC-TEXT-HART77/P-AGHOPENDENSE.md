---
schema: qual/card@1
id: P-AGHOPENDENSE
kind: problem
title: Opens are dense in an irreducible space, and closures stay irreducible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Zariski Topology
relations:
- kind: uses
  target: D-9DIKB
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.6 (scan page
    23 of the retained PDF). What was checked: both printed sentences — that a
    nonempty open subset of an irreducible space is dense and irreducible, and
    that a subset which is irreducible in its induced topology has irreducible
    closure — against the card, which states them as two sentences of the same
    content. No difference; no repair needed; the exercise carries no star.
    What was not checked: the solution was read only for consistency, not re-
    derived.
---

::: {.problem}
Any nonempty open subset of an irreducible topological space is dense and irreducible.
If $Y$ is a subset of a topological space $X$ which is irreducible in its induced topology, then the closure $\bar{Y}$ is also irreducible.
:::

::: {.solution}

The proof is the card's own; it writes out the finite-union form of irreducibility that the argument uses and that the "union of three closed sets" step assumes.

Throughout, $\cl_{X}(S)$ is the closure of $S$ in $X$, and a space is irreducible when it is nonempty and is not the union of two proper closed subsets.

::: pf

::: {.pf-step #finite-union}
If $X$ is irreducible and $X=F_{1}\cup\cdots\cup F_{n}$ with each $F_{i}$ closed and $n\ge1$, then $X=F_{i}$ for some $i$.

::: pf-proof
Induction on $n$. For $n=1$ it is trivial, and for $n=2$ it is the definition of irreducibility. For $n\ge3$ put $F=F_{1}\cup\cdots\cup F_{n-1}$, a closed set; then $X=F\cup F_{n}$, so $X=F$ or $X=F_{n}$ by irreducibility, and in the first case the induction hypothesis applied to $F$ gives $X=F_{i}$ for some $i\le n-1$.
:::

:::

::: {.pf-step #dense}
Every nonempty open subset of an irreducible space $X$ is dense.

::: pf-proof
Let $U\subseteq X$ be open and nonempty. The set $X\setminus U$ is closed and proper, since $U\ne\emptyset$. If $\cl_{X}(U)\ne X$ then $\cl_{X}(U)$ is also closed and proper, and
$$
X=(X\setminus U)\cup\cl_{X}(U),
$$
because $X\setminus U$ and $U\subseteq\cl_{X}(U)$ already cover $X$. That writes $X$ as a union of two proper closed sets, contradicting irreducibility; so $\cl_{X}(U)=X$.
:::

:::

::: {.pf-step #open-irreducible}
Every nonempty open subset of an irreducible space $X$ is irreducible.

::: pf-proof
Let $U\subseteq X$ be open and nonempty, and suppose $U=(A\cap U)\cup(B\cap U)$ with $A,B$ closed in $X$; that is the form every decomposition of $U$ into closed subsets of $U$ takes. Then
$$
X=A\cup B\cup(X\setminus U)
$$
is a union of three closed sets: a point of $U$ lies in $A\cap U$ or in $B\cap U$, and a point outside $U$ lies in $X\setminus U$. By step [](#finite-union){.pf-ref} $X$ equals one of the three. It is not $X\setminus U$, because $U\ne\emptyset$. So $X=A$ or $X=B$, and then $U=A\cap U$ or $U=B\cap U$. Hence every decomposition of $U$ into two closed subsets of $U$ is trivial, and $U$ is irreducible and nonempty.
:::

:::

::: {.pf-step #closure}
If $Y\subseteq X$ is irreducible in the induced topology, so is $\cl_{X}(Y)$.

::: pf-proof
Suppose $\cl_{X}(Y)=A\cup B$ with $A,B$ closed in $X$. Intersecting with $Y$,
$$
Y=(A\cap Y)\cup(B\cap Y),
$$
and $A\cap Y$, $B\cap Y$ are closed in $Y$, so by irreducibility of $Y$ one has $Y=A\cap Y$ or $Y=B\cap Y$; after relabelling, $Y\subseteq A$. Then $\cl_{X}(Y)\subseteq\cl_{X}(A)=A$, because $A$ is closed, so $\cl_{X}(Y)=A$ and the decomposition was trivial. Hence $\cl_{X}(Y)$ is irreducible; it is nonempty because $Y$ is.
:::

:::

:::

:::


::: {.remark}
Irreducible is strictly stronger than connected: connected forbids a decomposition into two proper *disjoint* closed sets, irreducible forbids it without disjointness.
$V(xy)$ is connected and reducible.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.6, PDF p. 1, text version `tmp/sources/hartshorne-solutions-borcherds.md`: for density he writes $X=(X\sm U)\cup\bar U$ and concludes $\bar U=X$; for irreducibility of $U$ he uses that a decomposition $U\subseteq C_1\cup C_2$ gives $X=\bar C_1\cup\bar C_2$; for the closure he uses $X=\bar C_1\cup\bar C_2$ on a decomposition of $\bar Y$.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.6, PDF p. 3, text version `tmp/sources/hartshorne-solutions-park.md`, proves the same two claims, with a lemma that a space is irreducible when every nonempty open set is dense.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.6, PDF p. 2, text version `tmp/sources/hartshorne-solutions-troiani.md`, answers only "See [3]" and gives no proof.
The proof above runs Borcherds' density and closure arguments and replaces his closure step by the finite-union form of irreducibility, $X=A\cup B\cup(X\sm U)$.
Agree with Borcherds and Park; Troiani contains no solution to compare.
:::
