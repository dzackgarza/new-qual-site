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

The proof is the card's own; the published accounts are recorded in the remark below, and the step all three of them leave implicit is proved here.

Number the four conditions as listed: (i) $X$ is Noetherian, that is every descending chain of closed subsets stabilises; (ii) every nonempty family of closed subsets has a minimal element; (iii) $X$ satisfies the ascending chain condition on open subsets; (iv) every nonempty family of open subsets has a maximal element.

::: pf

::: {.pf-step #a}
(a) The four conditions are equivalent.

::: pf-proof

::: {.pf-step #closed-equivalence}
(i) $\Leftrightarrow$ (ii).

::: pf-proof
(i)$\Rightarrow$(ii): let $\mathcal{F}\ne\emptyset$ be a family of closed sets and choose $Y_{1}\in\mathcal{F}$; if $Y_{1}$ is not minimal in $\mathcal{F}$ there is $Y_{2}\in\mathcal{F}$ with $Y_{2}\subsetneq Y_{1}$, and continuing, either the construction stops at a minimal member or it produces a strictly descending chain $Y_{1}\supsetneq Y_{2}\supsetneq\cdots$ of closed sets, which (i) forbids; so it stops. (ii)$\Rightarrow$(i): the members of a descending chain form a nonempty family of closed sets, which has a minimal member $Y_{n}$; then $Y_{m}=Y_{n}$ for all $m\ge n$, since $Y_{m}\subset Y_{n}$ and $Y_{n}$ is minimal in the family.
:::

:::

::: {.pf-step #open-equivalence}
(i) $\Leftrightarrow$ (iii) and (ii) $\Leftrightarrow$ (iv).

::: pf-proof
Complementation is an inclusion-reversing bijection between the closed and the open subsets of $X$: $A\subset B$ holds for closed sets exactly when $X\setminus B\subset X\setminus A$, and $X\setminus(X\setminus A)=A$. So a descending chain of closed sets corresponds to an ascending chain of open sets and conversely, and a minimal member of a family of closed sets corresponds to a maximal member of the family of complements. That gives both equivalences.
:::

:::

::: {.pf-qed}
Steps [](#closed-equivalence){.pf-ref} and [](#open-equivalence){.pf-ref} show that each of the four conditions is equivalent to (i), so all four are equivalent.
:::

:::

:::

::: {.pf-step #quasicompact}
(b) $X$ is quasicompact.

::: pf-proof
Let $\{U_{i}\}_{i\in I}$ be an open cover of $X$; the family of finite unions $U_{i_{1}}\cup\cdots\cup U_{i_{n}}$ is a nonempty family of open sets, so by (iv) it has a maximal element $V$. If $V\ne X$ then some $U_{i}\not\subseteq V$, and $V\cup U_{i}$ is a finite union of members of the cover strictly larger than $V$, a contradiction. Hence $X=V$ is a finite union of members of the cover, that is a finite subcover.
:::

:::

::: {.pf-step #subspace}
(c) Every subset $Y\subseteq X$ is Noetherian in the induced topology.

::: pf-proof
Let $U_{1}\subseteq U_{2}\subseteq\cdots$ be open in $Y$; each $U_{i}=V_{i}\cap Y$ with $V_{i}$ open in $X$. Put $W_{i}=V_{1}\cup\cdots\cup V_{i}$, an increasing chain of open sets of $X$. Since the $U_{i}$ increase,
$$
W_{i}\cap Y=(V_{1}\cap Y)\cup\cdots\cup(V_{i}\cap Y)=U_{1}\cup\cdots\cup U_{i}=U_{i}.
$$
The chain $W_{1}\subseteq W_{2}\subseteq\cdots$ stabilises by (iii), so $W_{i}=W_{i+1}$ for all large $i$, and then $U_{i}=W_{i}\cap Y=W_{i+1}\cap Y=U_{i+1}$; hence every ascending chain of open subsets of $Y$ stabilises, which is (iii) for $Y$.
:::

:::

::: {.pf-step #hausdorff}
(d) A Noetherian Hausdorff space is finite and discrete.

::: pf-proof

::: {.pf-step #finite-union}
$X$ is a finite union of irreducible closed subsets.

::: pf-proof
Suppose not: then the family of closed subsets of $X$ that are not finite unions of irreducible closed subsets is nonempty, so by (ii) it has a minimal member $C$. That $C$ is not irreducible, so $C=C_{1}\cup C_{2}$ with $C_{1},C_{2}$ proper closed subsets of $C$. Each $C_{i}$ is closed in $X$ and strictly smaller than $C$, so by minimality each is a finite union of irreducible closed subsets; a subset closed in $C_{i}$ is closed in $X$, so the union of those finitely many sets expresses $C$ as a finite union of irreducible closed subsets, a contradiction. So $X=X_{1}\cup\cdots\cup X_{n}$ with each $X_{i}$ closed and irreducible, and the $X_{i}$ can be taken nonempty.
:::

:::

::: {.pf-step #points}
Every irreducible closed subset of a Hausdorff space is a single point.

::: pf-proof
Let $C$ be irreducible and suppose $x\ne y$ in $C$. Since $X$ is Hausdorff there are disjoint open sets $U\ni x$ and $V\ni y$ in $X$. Then $U\cap C$ and $V\cap C$ are disjoint nonempty open subsets of $C$, so the two subsets $C\setminus(U\cap C)$ and $C\setminus(V\cap C)$ of $C$ are closed in $C$, and each is proper because the other contains a nonempty set. Their union is $C\setminus\big((U\cap C)\cap(V\cap C)\big)=C$, since the two open pieces are disjoint. So $C$ is the union of two proper closed subsets, contradicting irreducibility; hence $C$ has at most one point, and a nonempty irreducible closed set is a point.
:::

:::

::: {.pf-qed}
By steps [](#finite-union){.pf-ref} and [](#points){.pf-ref}, $X$ is the union of finitely many points, hence finite. A finite Hausdorff space is discrete: for $x$ the set $X\setminus\{x\}$ is a finite union of closed sets $\{y\}$, $y\ne x$, each a point of the Hausdorff space and hence closed, so $X\setminus\{x\}$ is closed and $\{x\}$ is open.
:::

:::

:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.7, PDF p. 1, text version `tmp/sources/hartshorne-solutions-borcherds.md`: for (a) he pairs (i) with (iii) by complements and (ii) with (iv), and derives (ii) from (i) by choosing a descending chain with Zorn's lemma; for (b) he applies (a)(iv) to the finite unions of the cover; for (c) he says it follows from (a)(iv) without an argument; for (d) he compresses the conclusion into one sentence.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.7, PDF pp. 3--4, text version `tmp/sources/hartshorne-solutions-park.md`: he runs the four equivalences directly, builds the strictly descending chain in (b), passes (c) through $Y_i=F_i\cap Y$, and in (d) writes $X$ as a finite union of irreducible closed subsets with no argument for why that is possible.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.7, PDF p. 2, text version `tmp/sources/hartshorne-solutions-troiani.md`: (a) is "routine", (b) and (c) are one line each, and (d) decomposes $X$ into finitely many irreducible components.
The proof above gives (b) and (c) explicitly and supplies the step all three leave implicit: applying (ii) to the closed subsets that are not finite unions of irreducible closed subsets gives a minimal one, which splits into two strictly smaller members of the same family.
Agree, and the minimal-counterexample step in (d) is the argument the published sets omit.
:::
