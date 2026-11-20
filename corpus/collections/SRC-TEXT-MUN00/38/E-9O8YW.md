---
schema: qual/card@1
id: E-9O8YW
kind: problem
title: $X$ is connected if and only if $\beta(X)$ is connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
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
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.6, page 1 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the sheet is dated
    2 April 2005 and its section-38 items name no author; Internet Archive snapshot 20181222125939 of
    web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf); the sheet also cites Engelking, General Topology (1989),
    Theorem 6.1.14 for the statement. Checked against Munkres, Topology (2000), Section 38 Exercise 6,
    printed p. 242, Theorem 38.4, Theorem 23.4 and Theorem 18.1. The sheet's chain is: X is not connected
    iff there is a continuous surjection X -> {0,1} (the two preimages are a separation, by Theorem 18.1);
    by Theorem 38.4 such a surjection extends to beta(X) -> {0,1} and is still surjective, so beta(X) is
    not connected; and if X is connected then so is beta(X), because beta(X) has the connected dense
    subset X (Theorem 23.4, the closure of a connected set is connected). What was corrected: the card
    carried the same two implications as fifteen unlabelled nested steps, several of them assertions with
    no stated justification, and the reverse implication was written as a contradiction argument through
    {f}^{-1}({0,1}); the card's proof is now the sheet's two implications, with the density and closedness
    of the two-point target's preimage stated where they are used.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the closure of a connected set is
    connected (Theorem 23.4) for one direction, and for the other the two-valued map of a
    separation, its extension to the compactification (Theorem 38.4) and the separation of
    the compactification it produces. The argument is the card's own; no retained set is
    cited. Munkres §38 Exercise 1, printed p. 241. The printed statement needed no repair.
---

::: {.exercise}

Let $X$ be completely regular.
Show that $X$ is connected if and only if $\beta(X)$ is connected.
[Hint: If $X = A \cup B$ is a separation of $X$, let $f(x) = 0$ for $x \in A$ and $f(x) = 1$ for $x \in B$.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §38 Exercise 1, with Theorem 23.4 (the closure of a connected set is connected) and Theorem 38.4 (the Stone--Čech extension property).

Let $i:X\to\beta(X)$ be the inclusion of $X$ as a dense subspace of its Stone--Čech compactification.

::: pf

::: {.pf-step #connected-forward}
If $X$ is connected, then $\beta(X)$ is connected.

::: pf-proof
The subspace $i(X)$ is homeomorphic to $X$, hence connected, and it is dense in $\beta(X)$. The closure of a connected subset is connected (Theorem 23.4), so $\beta(X)=\overline{i(X)}$ is connected.
:::

:::

::: {.pf-step #not-connected-forward}
If $X$ is not connected, then $\beta(X)$ is not connected.

:::: pf-proof

::: {.pf-step #separation}
A separation $X=A\cup B$ gives a continuous surjection $f:X\to\{0,1\}$ with $A=f^{-1}(0)$ and $B=f^{-1}(1)$.

::: pf-proof
A separation is a pair of disjoint nonempty open sets with union $X$. Define $f(a)=0$ for $a\in A$ and $f(b)=1$ for $b\in B$; then $f^{-1}(0)=A$ and $f^{-1}(1)=B$ are open, and the preimages of the four open sets of the discrete two-point space are among $\varnothing,A,B,X$, all open, so $f$ is continuous. It is onto because $A$ and $B$ are nonempty.
:::

:::

::: {.pf-step #extension}
$f$ extends to a continuous surjection $\tilde f:\beta(X)\to\{0,1\}$.

::: pf-proof
$\{0,1\}$ is compact and Hausdorff, so by the extension property of $\beta(X)$ (Theorem 38.4) the continuous map $f$ defined on the subspace $X$ extends to a continuous $\tilde f:\beta(X)\to\{0,1\}$. It is onto, since $\tilde f\big(\beta(X)\big)\supset\tilde f\big(i(X)\big)=f(X)=\{0,1\}$.
:::

:::

::: {.pf-step}
$\beta(X)$ is not connected.

::: pf-proof
The sets $\tilde f^{-1}(0)$ and $\tilde f^{-1}(1)$ are disjoint, open, nonempty, and their union is $\beta(X)$; so they separate $\beta(X)$.
:::

:::

:::

:::

::: {.pf-step}
$X$ is connected if and only if $\beta(X)$ is connected.

::: pf-proof
Steps [](#connected-forward){.pf-ref} and [](#not-connected-forward){.pf-ref} are the two implications.
:::

:::

:::
:::
