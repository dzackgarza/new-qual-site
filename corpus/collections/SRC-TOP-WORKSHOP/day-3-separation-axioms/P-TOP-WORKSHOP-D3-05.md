---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-05
kind: problem
title: Completely normal spaces and normal subsets
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Subspace Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose. Added the equivalence of the problem's open-set definition of separated with the closure conditions, proved in the proof (U = X - closure(B) and V = X - closure(A) in one direction, U subset X - closure(B) in the other), which the prose used without proof. Checked: a closed set of a subspace is the trace of a closed set of the space, which gives the forward direction, and the converse's Y = X - (closure A cap closure B) is open, contains A and B, and its two closed sets are disjoint. One convention is now recorded: normality is taken in Munkres's sense, including T_1, which is what makes X T_1 in the converse; under a convention that omits T_1 the hypothesis has to be read as T_1 plus every subspace normal. Statement unchanged.
---

::: {.problem}
Two subsets $A,B\subseteq X$ of the space $(X,\tau)$ are called *separated* if there are $U,V\in\tau$ with $A\subseteq U\subseteq X\setminus B$ and $B\subseteq V\subseteq X\setminus A$.
We say that $X$ is *completely normal* if $X$ is $T_1$ and if for every pair of separated subsets $A,B$ there are $U,V\in\tau$ so that $A\subseteq U$, $B\subseteq V$, and $U\cap V=\varnothing$.
Show that a space $(X,\tau)$ is completely normal if and only if every subset of $X$ is normal.
:::

::: {.solution}
Read "normal" in the sense of Munkres, that is $T_1$ together with the separation property for pairs of disjoint closed sets, which is what makes the hypothesis on subspaces carry $T_1$. Then each direction is a translation of the definitions: disjoint closed sets of a subspace are separated in the whole space, and separated sets become disjoint closed sets of the subspace obtained by deleting the intersection of their closures. The argument is this card's own: no retained solution set covers this workshop problem.

::: pf

::: {.pf-step #equiv}
For $A,B\subseteq X$ the following are equivalent: (a) there are open $U,V$ with $A\subseteq U\subseteq X\setminus B$ and $B\subseteq V\subseteq X\setminus A$; (b) $\overline A\cap B=\varnothing$ and $A\cap\overline B=\varnothing$.

::: pf-proof
Assume (a). Then $U$ is open and disjoint from $B$, so $U\subseteq X\setminus\overline B$; as $A\subseteq U$ this gives $A\cap\overline B=\varnothing$. Symmetrically $B\cap\overline A=\varnothing$. Assume (b). Put $U=X\setminus\overline B$ and $V=X\setminus\overline A$; these are open, since closures are closed, and disjoint, since $U\cap V=X\setminus(\overline A\cup\overline B)$. Moreover $A\subseteq U$ by (b) and $B\subseteq V$ by (b), and $U\subseteq X\setminus B$ because $B\subseteq\overline B$, symmetrically for $V$. So (a) holds.
:::

:::


::: {.pf-step #forward}
If $X$ is completely normal then every subspace $Y\subseteq X$ is normal.

::: pf-proof
$Y$ is $T_1$ as a subspace of a $T_1$ space. Let $C,D$ be disjoint closed subsets of $Y$. Then $C=Y\cap\overline C^{\,X}$ and $D=Y\cap\overline D^{\,X}$, because a subset of $Y$ is closed in $Y$ exactly when it is the trace of a closed subset of $X$. Hence $\overline C^{\,X}\cap D\subseteq Y\cap\overline C^{\,X}=C$, and $C\cap D=\varnothing$ gives $\overline C^{\,X}\cap D=\varnothing$; symmetrically $C\cap\overline D^{\,X}=\varnothing$. By step [](#equiv){.pf-ref}, $C$ and $D$ are separated subsets of $X$. Complete normality gives disjoint open $U,V\subseteq X$ with $C\subseteq U$ and $D\subseteq V$; then $U\cap Y$ and $V\cap Y$ are disjoint, open in $Y$, and contain $C$ and $D$. So $Y$ is normal.
:::

:::


::: {.pf-step #converse}
If every subspace of $X$ is normal then $X$ is completely normal.

::: pf-proof
Taking $Y=X$, the hypothesis says $X$ is normal, hence $T_1$ — this is where the convention on normality is used. Let $A,B\subseteq X$ be separated, so by step [](#equiv){.pf-ref} $\overline A\cap B=A\cap\overline B=\varnothing$. Put $Y=X\setminus(\overline A\cap\overline B)$, which is open as the complement of a closed set. Then $A\subseteq Y$ because $A\cap\overline B=\varnothing$, and $B\subseteq Y$ because $\overline A\cap B=\varnothing$. The sets $\overline A\cap Y$ and $\overline B\cap Y$ are closed in $Y$ and disjoint, and they contain $A$ and $B$. Since $Y$ is normal, there are $U_Y,V_Y$ open in $Y$, disjoint, with $\overline A\cap Y\subseteq U_Y$ and $\overline B\cap Y\subseteq V_Y$. Because $Y$ is open in $X$, the sets $U_Y$ and $V_Y$ are open in $X$; they are disjoint and contain $A$ and $B$ respectively. So $X$ is completely normal.
:::

:::


::: {.pf-step #conclusion}
$X$ is completely normal if and only if every subset of $X$ is normal.

::: pf-proof
Steps [](#forward){.pf-ref} and [](#converse){.pf-ref} give the two implications. The only convention used is that a normal space is $T_1$; with a convention under which normality omits $T_1$, the hypothesis of the converse must be strengthened to "$T_1$ and every subspace normal", which is the same statement read in that convention.
:::

:::

:::
:::
