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
---

::: {.exercise}

Let $X$ be completely regular.
Show that $X$ is connected if and only if $\beta(X)$ is connected.
[Hint: If $X = A \cup B$ is a separation of $X$, let $f(x) = 0$ for $x \in A$ and $f(x) = 1$ for $x \in B$.]
:::

::: {.solution}
Let $i:X\to\beta(X)$ be the inclusion of the dense subspace.

If $X$ is connected, then $\beta(X)$ is connected: $i(X)=\beta(X)$ is the closure of the connected set $i(X)$ in $\beta(X)$, and the closure of a connected set is connected (Theorem 23.4).

Conversely, suppose $X$ is not connected, and let $X=A\cup B$ be a separation: $A,B$ nonempty, disjoint and open (hence also closed) in $X$. The function $f:X\to\{0,1\}$, $f(a)=0$ for $a\in A$ and $f(b)=1$ for $b\in B$, is continuous, because $\{0\}$ and $\{1\}$ are the two preimages of points of the discrete space $\{0,1\}$ and $A=f^{-1}(0)$, $B=f^{-1}(1)$ are open; it is onto. The space $\{0,1\}$ is compact Hausdorff, so by Theorem 38.4 the map $f$ extends to a continuous $\tilde f:\beta(X)\to\{0,1\}$. This extension is onto, since $\tilde f(\beta(X))\supset\tilde f(i(X))=f(X)=\{0,1\}$. Then
$$
\beta(X)=\tilde f^{-1}(0)\cup\tilde f^{-1}(1)
$$
is a separation of $\beta(X)$ into two disjoint nonempty sets open in $\beta(X)$: the space $\beta(X)$ is not connected.

So $X$ is connected if and only if $\beta(X)$ is connected.
:::
