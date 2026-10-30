---
schema: qual/card@1
id: P-UNLJ04-03
kind: problem
title: Separating disjoint finite subsets in a Hausdorff space
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Revised_packet_-_Separation_Counterexamples_and_Definitions_extracted.md, which reproduces June 2004 A3 with containment targets U and V; the retained old exam extraction had corrupted them as \mathcal U and \nu.
---

::: {.problem}
Show that if $X$ is a Hausdorff space and $A,B\subseteq X$ are disjoint finite subsets of $X$, then there are disjoint open sets $U,V$ in $X$ with $A\subseteq U$ and $B\subseteq V$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If either
$$
A=\varnothing
$$
or
$$
B=\varnothing,
$$
the conclusion is immediate.


::: pf-proof

If
$$
A=\varnothing,
$$
take
$$
U=\varnothing,
\qquad
V=X.
$$
If
$$
B=\varnothing,
$$
take
$$
U=X,
\qquad
V=\varnothing.
$$

:::

:::

::: {.pf-step #s1-2}

Assume now that
$$
A\ne\varnothing
\quad\text{and}\quad
B\ne\varnothing.
$$
For every pair
$$
(a,b)\in A\times B,
$$
choose disjoint open sets
$$
U_{a,b},
\qquad
V_{a,b}
$$
such that
$$
a\in U_{a,b},
\qquad
b\in V_{a,b}.
$$


::: pf-proof

Because
$$
A\cap B=\varnothing,
$$
one has
$$
a\ne b
$$
for every
$$
(a,b)\in A\times B.
$$
Since
$$
X
$$
is Hausdorff, distinct points admit disjoint open neighborhoods.

:::

:::

::: {.pf-step #s1-3}

For each
$$
a\in A,
$$
define
$$
U_a
\coloneqq
\bigcap_{b\in B}U_{a,b}.
$$
Then
$$
U_a
$$
is open and contains
$$
a.
$$


::: pf-proof

The set
$$
B
$$
is finite, so
$$
U_a
$$
is a finite intersection of open sets and is therefore open.

Every
$$
U_{a,b}
$$
contains
$$
a,
$$
so their intersection contains
$$
a.
$$

:::

:::

::: {.pf-step #s1-4}

For each
$$
b\in B,
$$
define
$$
V_b
\coloneqq
\bigcap_{a\in A}V_{a,b}.
$$
Then
$$
V_b
$$
is open and contains
$$
b.
$$


::: pf-proof

The proof is identical to step [](#s1-3){.pf-ref}, using finiteness of
$$
A.
$$

:::

:::

::: {.pf-step #s1-5}

For every
$$
a\in A
$$
and
$$
b\in B,
$$
one has
$$
\boxed{
U_a\cap V_b=\varnothing}.
$$


::: pf-proof

By definition,
$$
U_a\subseteq U_{a,b}
$$
and
$$
V_b\subseteq V_{a,b}.
$$
Step [](#s1-2){.pf-ref} gives
$$
U_{a,b}\cap V_{a,b}
=
\varnothing.
$$
Therefore
$$
U_a\cap V_b
=
\varnothing.
$$

:::

:::

::: {.pf-step #s1-6}

Define
$$
U
\coloneqq
\bigcup_{a\in A}U_a,
\qquad
V
\coloneqq
\bigcup_{b\in B}V_b.
$$
Then
$$
U
$$
and
$$
V
$$
are open,
$$
A\subseteq U,
$$
and
$$
B\subseteq V.
$$


::: pf-proof

Unions of open sets are open.

For every
$$
a\in A,
$$
step [](#s1-3){.pf-ref} gives
$$
a\in U_a\subseteq U.
$$
Thus
$$
A\subseteq U.
$$
Similarly, step [](#s1-4){.pf-ref} gives
$$
B\subseteq V.
$$

:::

:::

::: {.pf-step #s1-7}

The open sets
$$
U
$$
and
$$
V
$$
are disjoint.


::: pf-proof

Suppose
$$
x\in U\cap V.
$$
Then
$$
x\in U_a
$$
for some
$$
a\in A,
$$
and
$$
x\in V_b
$$
for some
$$
b\in B.
$$
Hence
$$
x\in U_a\cap V_b,
$$
contradicting step [](#s1-5){.pf-ref}.

Therefore
$$
U\cap V=\varnothing.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} handles the empty cases, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} construct the required disjoint open neighborhoods when both finite sets are nonempty.

:::

:::

:::
