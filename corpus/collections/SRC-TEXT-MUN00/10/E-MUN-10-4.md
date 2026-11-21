---
schema: qual/card@1
id: E-MUN-10-4
kind: problem
title: Characterizing non-well-ordered sets via $\ZZ_{-}$
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 4, printed p. 67; the stored
    statement is printed (a) and (b), Z_- being the negative integers in the usual order.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.4, printed pp.
    109-110. (a) is his: failing well-ordering gives a nonempty subset with no smallest
    element, from which the axiom of choice and the principle of recursive definition build
    a strictly decreasing sequence, i.e. a subset of order type Z_-; the converse is his
    too. (b) is his reduction of an ill-ordered A to a countable subset of type Z_-, which
    the hypothesis forbids. The recursion in (a) is written out as an application of the
    principle of recursive definition rather than left implicit.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two parts, which is what Queue D asks for on this card. Part (a) is split into the recursion that produces the strictly decreasing sequence (with the choice function and the recursive-definition principle made explicit) and the identification of its image as a subset of order type Z_-, plus the converse; part (b) is the countable-subset argument, which now says why order type transfers well-ordering. Statement re-read against Munkres, Topology (2000), §10 Exercise 4, printed p. 67, and the argument against Dan Whitman's set, Exercise 10.4, printed pp. 109-110. No statement repair.
---

::: {.exercise}

(a) Let $\ZZ_{-}$ denote the set of negative integers in the usual order.
Show that a simply ordered set $A$ fails to be well-ordered if and only if it contains a subset having the same order type as $\ZZ_{-}$ .

(b) Show that if $A$ is simply ordered and every countable subset of $A$ is well-ordered, then $A$ is well-ordered.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.4, printed pp. 109--110** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his, with the recursion used in (a) spelled out as an application of the principle of recursive definition. The statement is Munkres, *Topology*, 2nd ed. (2000), §10 Exercise 4, printed p. 67.

::: pf

::: {.pf-step #part-a}
(a) A simply ordered set $A$ fails to be well ordered if and only if it has a subset of the same order type as $\ZZ_-$.

::: pf-proof

::: {.pf-step #descending}
If $A$ is not well ordered, there is $f:\ZZ_+\to A$ with $f(n)<f(m)$ whenever $m<n$.

::: pf-proof
Some nonempty $B\subset A$ has no smallest element. For $b\in B$ the set $X_b=\{x\in B\mid x<b\}$ is nonempty, since otherwise $b$ would be the smallest element of $B$. By the axiom of choice there is a choice function $c$ on the family $\{X_b\}_{b\in B}$ of nonempty subsets of $B$. Fix $b_0\in B$ and put
$$
\rho(g)=b_0\ \ (m=1),\qquad \rho(g)=c\big(X_{g(m)}\big)\ \ (m>1),
\qquad g:\{1,\dots,m\}\to B ,
$$
which is defined for every function on a nonempty section and takes values in $B$, because $X_b\subseteq B$. The principle of recursive definition (Theorem 8.4) gives $f:\ZZ_+\to B$ with $f(1)=b_0$ and $f(n)=c(X_{f(n-1)})\in X_{f(n-1)}$ for $n>1$, that is $f(n)<f(n-1)$. By induction on $n-m$, $f(n)<f(m)$ for all $m<n$: the case $n=m+1$ is the inequality just proved, and $f(n)<f(n-1)<f(m)$ otherwise by transitivity.
:::

:::

::: {.pf-step #order-type}
The image of $h(-n)=f(n)$ is a subset of $A$ of the order type of $\ZZ_-$.

::: pf-proof
The map $h:\ZZ_-\to A$, $h(-n)=f(n)$, is injective because $f$ is strictly decreasing: if $h(-n)=h(-m)$ with $n\ne m$, say $m<n$, then $f(n)<f(m)$, a contradiction. It preserves order: $-n<-m$ means $n>m$, and then $h(-n)=f(n)<f(m)=h(-m)$. So $h$ is an order-preserving bijection of $\ZZ_-$ with its image $C=h(\ZZ_-)\subset A$, which is the definition of $C$ having the order type of $\ZZ_-$.
:::

:::

The steps [](#descending){.pf-ref} and [](#order-type){.pf-ref} give the forward implication.
:::

:::

::: {.pf-step #converse}
If $A$ has a subset $C$ of the order type of $\ZZ_-$, then $A$ is not well ordered.

::: pf-proof
$C$ is nonempty and has no smallest element: an order isomorphism of $C$ with $\ZZ_-$ would carry a smallest element of $C$ to a smallest element of $\ZZ_-$, and $\ZZ_-$ has none, since $-n-1<-n$ for every $n$. So $A$ has a nonempty subset without a smallest element and therefore fails to be well ordered. With the forward implication this is part (a).
:::

:::

::: {.pf-step #part-b}
(b) If $A$ is simply ordered and every countable subset of $A$ is well ordered, then $A$ is well ordered.

::: pf-proof
Suppose $A$ is not well ordered. By part [](#part-a){.pf-ref} it has a subset $C$ of the order type of $\ZZ_-$. Then $C$ is countable, being in bijection with the countable set $\ZZ_-$, and it is a subset of $A$, so by hypothesis it is well ordered. But $C$ has the order type of $\ZZ_-$, which is not well ordered by step [](#converse){.pf-ref}; a set and a set of the same order type are well ordered or not together, since an order isomorphism carries subsets without smallest elements to subsets without smallest elements. This contradiction shows that $A$ is well ordered, which is part (b).
:::

:::

:::
:::
