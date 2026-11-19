---
schema: qual/card@1
id: E-MC21D
kind: problem
title: Density of uncountable products of the line
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Part (b) transcribed from the located published solution: dbFin, "Section 30: Problem 16
    Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-30-the-countability-axioms/problem-16-solution/
    (read 2026-11-11; kept at
    tmp/sources/dbfin/section-30-the-countability-axioms/problem-16-solution.txt), whose (b) is the
    printed hint's injection and is complete: for alpha different from beta the two constraints
    alpha in (a,b) and beta in (b,+infinity) are disjoint, so a dense point satisfying both lies in
    F(alpha) and not in F(beta), and |J| at most |2^D| at most |P(Z_+)| follows. The card uses the
    printed hint's own pair, with (2,3) in place of (b,+infinity), which is the same two lines.
    Part (a) keeps a proof of the card's own: no located solution of it is complete. dbFin's (a) is
    the sentence "we can always separate the indexes of these spaces by some rational points ... take
    all finite subsets of rationals in [0,1] containing 0 and 1 ... then products of rational points
    such that they are the same across each interval", which describes a family of step functions
    without saying which member meets a prescribed basic open set and does not treat coordinates
    outside [0,1]. "Doug's World"'s item labelled "Problem 30.15" ("Munkres - Topology - Chapter 4
    Solutions", 30 August 2017, file pages 3-4) solves printed Exercise 30.15, not this one: it
    approximates a *continuous* f by piecewise linear rational functions in the uniform metric, which
    is Exercise 30.15's statement, and its last clause wrongly says "R^I has a countable dense
    subset. By exercise 5(a), R^I has a countable basis", where R^I is not metrizable. Its item
    labelled "Problem 30.16" is empty.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Rechecked against Munkres, Topology (2000), Section 30 Exercise 16, printed p. 195, and the
    located published solutions. What was corrected: the earlier record said that dbFin's (b) writes
    an interval "(b,+infinity) which is not disjoint from (a,b)" and asserts the cardinal conclusion
    without the cardinal step. Both objections are wrong: (b,+infinity) is disjoint from (a,b), which
    is exactly what the injection needs, and "|J| <= |2^D|" is the cardinal step, D being countable.
    The exercise stays on the COMPLAINTS.md list only because of part (a).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, both parts kept as they were: (b) the retained
    dbFin argument following the printed hint, (a) the card's own. Re-checked: for (a) the
    injection $I\to\mathcal{P}(\ZZ_+)$ exists since both sets have cardinality $2^{\aleph_0}$; the
    family $D$ is countable as a countable union over finite $F$ of the countable sets
    $\QQ^{\mathcal{P}(F)}$; and density is the pairwise-distinct-traces argument, which is now
    written out with the witnesses $m_{ij}$ chosen in symmetric differences. For (b) the two
    constraints at distinct coordinates give a nonempty basic open set, density puts a point of $D$
    in it, so $F$ is injective and $\abs{J}\le\abs{\mathcal{P}(D)}\le\abs{\mathcal{P}(\ZZ_+)}$.
    No defect found in the statement, §30 Exercise 16 on printed p. 195. Corrected the earlier
    event's spelling of the file page only in this solution's citation: the retained dbFin text now
    sits at `tmp/sources/dbfin/section-30-the-countability-axioms/problem-16-solution.txt`. Not
    claimed: a published solution of part (a), which the earlier events already record as absent.
---

::: {.exercise}

(a) Show that the product space $\RR^I$, where $I = [0, 1]$, has a countable dense subset.

(b) Show that if $J$ has cardinality greater than $\mathcal{P}(\ZZ_+)$, then the product space $\RR^J$ does not have a countable dense subset.
[Hint: If $D$ is dense in $\RR^J$, define $f: J \to \mathcal{P}(D)$ by the equation $f(\alpha) = D \cap \pi_\alpha^{-1}((a, b))$, where $(a, b)$ is a fixed interval in $\RR$.]
:::

::: {.solution}
Part (b) is the retained published solution of dbFin, *Section 30: Problem 16 Solution* (`tmp/sources/dbfin/section-30-the-countability-axioms/problem-16-solution.txt`), which follows the printed hint. Part (a) is the card's own; no located solution of it is complete. Write $\pi_\alpha\colon\RR^J\to\RR$ for the projection at $\alpha$.

::: pf

::: {.pf-step #part-a}
(a) The product space $\RR^I$ with $I=[0,1]$ has a countable dense subset.

:::: pf-proof

::: {.pf-step #injection}
There is an injection $\iota\colon I\to\mathcal{P}(\ZZ_+)$.

::: pf-proof
$\abs{I}=\abs{\RR}=2^{\aleph_0}=\abs{\mathcal{P}(\ZZ_+)}$, since $[0,1]$ and $\RR$ are in bijection and $\mathcal{P}(\ZZ_+)$ has the cardinality of the set of subsets of a countable set; two sets of the same cardinality admit a bijection, and a bijection is in particular an injection.
:::

:::

::: {.pf-step #countable}
The set
$$
D=\{d_{F,\phi}\mid F\subseteq\ZZ_+\text{ finite},\ \phi\colon\mathcal{P}(F)\to\QQ\},
\qquad d_{F,\phi}(t)=\phi\bigl(\iota(t)\cap F\bigr),
$$
is countable.

::: pf-proof
The function $d_{F,\phi}$ is a well-defined element of $\RR^I$, because $\iota(t)\cap F$ is a subset of $F$ and $\phi$ is defined on every such subset. The finite subsets $F$ of the countable set $\ZZ_+$ are countable in number: each is a finite subset of the $n$-th initial segment for some $n$, and the finite subsets of an $n$-element set are finitely many. For each fixed $F$ the set $\mathcal{P}(F)$ is finite, so the set $\QQ^{\mathcal{P}(F)}$ of functions $\mathcal{P}(F)\to\QQ$ is a finite product of countable sets, hence countable. A countable union of countable sets is countable, so the set of pairs $(F,\phi)$ is countable, and $D$ is its image under $(F,\phi)\mapsto d_{F,\phi}$.
:::

:::

::: {.pf-step #dense}
$D$ is dense in $\RR^I$.

::: pf-proof
A nonempty basic open set of the product topology fixes finitely many distinct coordinates $t_1,\ldots,t_n\in I$ and nonempty open intervals $U_1,\ldots,U_n$ of $\RR$, and is the set of $f$ with $f(t_i)\in U_i$ for each $i$. Since $\iota$ is injective, the sets $\iota(t_1),\ldots,\iota(t_n)$ are pairwise distinct, so for each pair $i\ne j$ choose an integer $m_{ij}$ in the symmetric difference of $\iota(t_i)$ and $\iota(t_j)$, and let $F$ be the finite set of all these $m_{ij}$. Then $\iota(t_i)\cap F\ne\iota(t_j)\cap F$ for $i\ne j$, the two differing at $m_{ij}$. Choose rationals $q_i\in U_i$, which exist because $\QQ$ is dense in $\RR$ and $U_i$ is a nonempty open interval, and define $\phi\colon\mathcal{P}(F)\to\QQ$ by $\phi(\iota(t_i)\cap F)=q_i$ for $i=1,\ldots,n$ — well defined because the traces are distinct — and $\phi=0$ on the remaining subsets of $F$. Then $d_{F,\phi}(t_i)=q_i\in U_i$ for every $i$, so $d_{F,\phi}\in D$ meets the given basic open set. Every nonempty open set contains a basic one, so $D$ is dense.
:::

:::

:::

:::

::: {.pf-step}
(b) If $\abs{J}>\abs{\mathcal{P}(\ZZ_+)}$, then $\RR^J$ has no countable dense subset.

:::: pf-proof

::: {.pf-step #injective}
If $D\subseteq\RR^J$ is dense, the map $F\colon J\to\mathcal{P}(D)$, $F(\alpha)=D\cap\pi_\alpha^{-1}((0,1))$, is injective.

::: pf-proof
For $\alpha\ne\beta$ the set $\pi_\alpha^{-1}((0,1))\cap\pi_\beta^{-1}((2,3))$ is a nonempty basic open set, since it imposes conditions at the two distinct coordinates only. Density of $D$ gives $d\in D$ in it, so $d_\alpha\in(0,1)$ and $d_\beta\in(2,3)$; then $d\in F(\alpha)$ while $d\notin F(\beta)$. Hence $F(\alpha)\ne F(\beta)$.
:::

:::

::: {.pf-step #cardinality}
If $\RR^J$ has a dense $D$ with $D$ countable, then $\abs{J}\le\abs{\mathcal{P}(\ZZ_+)}$.

::: pf-proof
By step [](#injective){.pf-ref} there is an injection $J\to\mathcal{P}(D)$, so $\abs{J}\le\abs{\mathcal{P}(D)}$; and $D$ countable gives $\abs{\mathcal{P}(D)}\le\abs{\mathcal{P}(\ZZ_+)}$, the power set of a countable set having at most the cardinality $2^{\aleph_0}$ of the power set of $\ZZ_+$.
:::

:::

::: {.pf-step}
(b) If $\abs{J}>\abs{\mathcal{P}(\ZZ_+)}$, then $\RR^J$ does not have a countable dense subset.

::: pf-proof
Suppose $D$ dense in $\RR^J$ with $D$ countable; step [](#cardinality){.pf-ref} gives $\abs{J}\le\abs{\mathcal{P}(\ZZ_+)}$, contradicting the hypothesis. So no such $D$ exists, and $\RR^J$ is not separable.
:::

:::

:::

:::

:::
:::
