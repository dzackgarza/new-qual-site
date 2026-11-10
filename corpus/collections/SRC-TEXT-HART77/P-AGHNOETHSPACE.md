---
schema: qual/card@1
id: P-AGHNOETHSPACE
kind: problem
title: Four characterisations of a Noetherian space, and what they force
classification:
  areas:
  - algebraic-geometry
  topics:
  - Noetherian Spaces
  - Quasicompactness
  - Irreducibility
relations:
- kind: uses
  target: D-9DIKB
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.7 (scan page
    23 of the retained PDF). What was checked: parts (a), (c), (d) against the
    card word for word — the four equivalent conditions, subsets of Noetherian
    spaces, and the Hausdorff case — all agree. Part (b) differs: the book
    reads "A noetherian topological space is quasi-compact, i.e., every open
    cover has a finite subcover", and the card had dropped the gloss after
    i.e., which is the definition the part turns on; restored. What was not
    checked: the solution was read only for consistency, not re-derived.
---

::: {.problem}
(a) Show that the following are equivalent for a topological space $X$:

- $X$ is Noetherian;

- every nonempty family of closed subsets has a minimal element;

- $X$ satisfies the ascending chain condition on open subsets;

- every nonempty family of open subsets has a maximal element.

(b) A Noetherian topological space is quasicompact, i.e. every open cover has a finite subcover.

(c) Any subset of a Noetherian topological space is Noetherian in its induced topology.

(d) A Noetherian space which is also Hausdorff is a finite set with the discrete topology.
:::

::: {.solution}
**(a)** Call the conditions (i)-(iv) in the order listed.
(i) $\implies$ (ii): given a nonempty family of closed sets, choose $Y_1$ in it; if it is not minimal there is $Y_2 \subsetneq Y_1$ in the family, and so on.
The resulting descending chain stabilises, and where it stabilises is a minimal element.
(ii) $\implies$ (i): the members of a descending chain of closed sets form a nonempty family, and the chain stabilises at a minimal member.
(i) $\iff$ (iii) and (ii) $\iff$ (iv) follow by taking complements.

**(b)** Let $\theset{U_i}$ be an open cover of $X$.
By (iv), the family of finite unions of the $U_i$ has a maximal element $V$.
If $V \neq X$, some $U_i \not\subseteq V$, and $V \union U_i$ is a larger finite union, a contradiction.
So $V = X$ is a finite subcover.

**(c)** Let $Y \subseteq X$ and let $U_1 \subseteq U_2 \subseteq \cdots$ be opens in $Y$, so $U_i = V_i \intersect Y$ with $V_i$ open in $X$.
Put $W_i = V_1 \union \cdots \union V_i$.
Since the $U_i$ increase, $W_i \intersect Y = U_i$.
The chain $W_1 \subseteq W_2 \subseteq \cdots$ stabilises by (iii), so the chain $U_i$ stabilises.

**(d)** Suppose some closed subset of $X$ is not a finite union of irreducible closed subsets, and take a minimal one $C$ among them by (ii).
Then $C$ is not irreducible, so $C = C_1 \union C_2$ with $C_1, C_2$ proper closed subsets of $C$.
By minimality each $C_i$ is a finite union of irreducible closed subsets; those sets are closed in $C$ and hence in $X$, so $C$ is such a union, a contradiction.
Hence $X$ is a finite union $X = \Union_{i \leq n} C_i$ of irreducible closed subsets.
An irreducible Hausdorff space is a point: if $x \neq y$ in $C_i$ had disjoint open neighbourhoods $U \ni x$, $V \ni y$ in $C_i$, then $U$ would be a nonempty open subset that is not dense, contradicting Ex. 1.6.
So $X$ is finite, and a finite Hausdorff space is discrete, because each point is closed and so every subset is closed.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.7, PDF p. 1: for (a) he pairs (i) with (iii) by complements and (ii) with (iv), and derives (ii) from (i) by choosing a descending chain with Zorn's lemma; for (b) he applies (a)(iv) to the finite unions of the cover; for (c) he says it follows from (a)(iv) without an argument; for (d) he compresses the conclusion into one sentence.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.7, PDF pp. 3--4: he runs the four equivalences directly, builds the strictly descending chain in (b), passes (c) through $Y_i=F_i\cap Y$, and in (d) writes $X$ as a finite union of irreducible closed subsets with no argument for why that is possible.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.7, PDF p. 2: (a) is "routine", (b) and (c) are one line each, and (d) decomposes $X$ into finitely many irreducible components.
The proof above gives (b) and (c) explicitly and supplies the step all three leave implicit: applying (ii) to the closed subsets that are not finite unions of irreducible closed subsets gives a minimal one, which splits into two strictly smaller members of the same family.
Agree, and the minimal-counterexample step in (d) is the argument the published sets omit.
:::
