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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 30 Exercise 16, printed p. 195,
    and Theorem 19.6: part (a) needs a separable product of continuum many factors, and its
    functions d_{F,phi} are constant on the traces iota(t) cap F, which separates any prescribed
    finite set of coordinates; part (b) is the printed hint's function alpha -> D cap
    pi_alpha^{-1}((a,b)) made injective by the second interval (2,3). No complete published
    solution was located: "Doug's World", "Munkres - Topology - Chapter 4 Solutions", printed p. 4,
    prints "Problem 30.16. Solution:" and then nothing; Orellana's contents stop at Section 30
    Exercise 14; Rajaraman's notes stop at Exercise 4.30.10; positron0802, Whitman, shenapse and
    9beach do not reach Chapter 4. The search is recorded in the COMPLAINTS.md entry for this
    batch.
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
