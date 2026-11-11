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
---

::: {.exercise}

(a) Show that the product space $\RR^I$, where $I = [0, 1]$, has a countable dense subset.

(b) Show that if $J$ has cardinality greater than $\mathcal{P}(\ZZ_+)$, then the product space $\RR^J$ does not have a countable dense subset.
[Hint: If $D$ is dense in $\RR^J$, define $f: J \to \mathcal{P}(D)$ by the equation $f(\alpha) = D \cap \pi_\alpha^{-1}((a, b))$, where $(a, b)$ is a fixed interval in $\RR$.]
:::

::: {.solution}
(a) We construct a countable dense subset of $\RR^I$, $I=[0,1]$. Choose an injection
$$
\iota:I\hookrightarrow\mathcal P(\ZZ_+).
$$
For every finite set $F\subset\ZZ_+$ and every function
$$
\phi:\mathcal P(F)\to\QQ,
$$
define $d_{F,\phi}\in\RR^I$ by
$$
d_{F,\phi}(t)=\phi(\iota(t)\cap F).
$$
There are only countably many such pairs $(F,\phi)$, so
$$
D=\{d_{F,\phi}\}
$$
is countable.

To see $D$ is dense, let a basic open set prescribe nonempty open intervals $U_1,\dots,U_n$ at distinct coordinates $t_1,\dots,t_n$. Since the sets $\iota(t_i)$ are distinct, there is a finite $F\subset\ZZ_+$ such that their traces $\iota(t_i)\cap F$ are pairwise distinct: for each pair choose one integer where the two subsets differ, and take the finite union of these witnesses. Choose rationals $q_i\in U_i$, and define $\phi$ on the distinct traces by $\phi(\iota(t_i)\cap F)=q_i$, arbitrarily elsewhere. Then $d_{F,\phi}\in D$ lies in the given basic open set. Hence $D$ is dense.

(b) Let $D\subset\RR^J$ be countable and dense. Fix a nonempty proper open interval $U=(0,1)$. For each $\alpha\in J$, define
$$
F(\alpha)=D\cap\pi_\alpha^{-1}(U)\subset D.
$$
We claim $F:J\to\mathcal P(D)$ is injective. If $\alpha\ne\beta$, the basic open set
$$
\pi_\alpha^{-1}(U)\cap\pi_\beta^{-1}((2,3))
$$
is nonempty, so density of $D$ gives $d\in D$ with $d_\alpha\in U$ and $d_\beta\notin U$. Hence $d\in F(\alpha)\setminus F(\beta)$. Thus
$$
\cardinality{J}\le \cardinality{\mathcal P(D)}\le\cardinality{\mathcal P(\ZZ_+)}.
$$
Therefore if $J$ has larger cardinality than $\mathcal P(\ZZ_+)$, $\RR^J$ cannot be separable.
:::
