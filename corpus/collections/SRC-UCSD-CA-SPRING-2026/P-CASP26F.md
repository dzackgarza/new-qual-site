---
schema: qual/card@1
id: P-CASP26F
kind: problem
title: "Simultaneous polynomial approximation and separation on disjoint compact sets"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomial Approximation
  - Runge Theorem
  - Mergelyan Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the three parts already on the card, correct as
    it stood. Added: that h on A union B is well defined because A and B are disjoint and that
    it is continuous because the two sets are closed; the holomorphy of h on the interior of A
    union B, which the prose simply asserted — an open subset of the union of two disjoint
    closed sets lies in one of them, so h agrees there with an entire function; the reverse
    triangle bound 2000 - |p - h| > 1000 on B; the choice of m making |c| 2^-m small in (ii);
    and the observation closing part (iii) that 2 lies outside the disc bounded by the circle
    while 0 lies inside, which is exactly why the maximum modulus principle applies to one pair
    and not the other. Not claimed: a retained solution set; the provenance names the
    examination paper.
---

::: {.problem}
Let $A, B \subset \CC$ be two disjoint nonempty compact sets.
Consider the following property:

**Property (P):** For any two entire functions $f, g$, there exists a polynomial $p$ such that $\abs{p(z) - f(z)} < \frac{1}{1000}$ for $z \in A$ and $\abs{p(z) - g(z)} > 1000$ for $z \in B$.

(i) Assume $\CC \setminus (A \cup B)$ is connected.
Show that property (P) is true.

(ii) Show that property (P) holds for the compact sets $A = \{z \in \CC : \abs{z} = 1\}$, $B = \{2\}$.
In this case, $\CC \setminus (A \cup B)$ is disconnected.

(iii) Exhibit two disjoint nonempty compact sets $A, B$ for which property (P) is false.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2026 complex-analysis examination paper, which carries no solutions. The three parts are the card's own and follow the card's previous prose: (i) Mergelyan, (ii) the polynomial $q$ plus a sharply peaked monomial, (iii) the maximum modulus principle.

Throughout $A,B\subset\CC$ are disjoint nonempty compact sets, and property (P) is: for all entire $f,g$ there is a polynomial $p$ with $\abs{p-f}<1/1000$ on $A$ and $\abs{p-g}>1000$ on $B$.

::: pf

::: {.pf-step #part-i}
If $\CC\setminus(A\cup B)$ is connected, property (P) holds.

::: pf-proof
Let $f,g$ be entire and $K=A\cup B$, a nonempty compact set with $\CC\setminus K$ connected. Define $h$ on $K$ by $h=f$ on $A$ and $h=g+2000$ on $B$. This is well defined, since $A\cap B=\varnothing$, and continuous: on $A$ and on $B$ it agrees with continuous functions, and $A$, $B$ are disjoint closed sets, so continuity at each point of $K$ is immediate. A point $a\in\operatorname{int}K$ has an open neighbourhood $U\subseteq K=A\cup B$. Since $U$ is connected and $U=(U\cap A)\cup(U\cap B)$ with both sets closed in $U$, and $A,B$ are disjoint, $U$ lies entirely in $A$ or entirely in $B$; correspondingly $h$ equals $f$, or $g+2000$, on $U$. Either way $h$ is holomorphic at $a$, since $f$ and $g$ are entire. So $h$ is holomorphic on $\operatorname{int}K$. By Mergelyan's theorem there is a polynomial $p$ with $\sup_K\abs{p-h}<1/1000$. Then on $A$, $\abs{p-f}=\abs{p-h}<1/1000$; and on $B$, $\abs{p-g}\ge\abs{h-g}-\abs{p-h}=2000-\abs{p-h}>1000$.

:::

:::

::: {.pf-step #part-ii}
Property (P) holds for $A=\circlegroup$ and $B=\set2$.

::: pf-proof
Let $f,g$ be entire and let $q$ be a polynomial with $\sup_{\abs z=1}\abs{q-f}<1/2000$, which exists by Mergelyan applied to the circle (its complement is connected, and $f$ is continuous on it). Put $c=2001+g(2)-q(2)$ and, for a positive integer $m$, $p(z)=q(z)+c(z/2)^m$. On $\abs z=1$ we have $\abs{c(z/2)^m}=\abs c2^{-m}$, so $\sup_{\abs z=1}\abs{p-f}\le1/2000+\abs c2^{-m}<1/1000$ for $m$ large. At $z=2$, $p(2)=q(2)+c=g(2)+2001$, so $\abs{p(2)-g(2)}=2001>1000$.

:::

:::

::: {.pf-step #part-iii}
Property (P) fails for $A=\circlegroup$ and $B=\set0$.

::: pf-proof
Take $f=g=0$; then (P) would give a polynomial $p$ with $\abs{p(z)}<1/1000$ for $\abs z=1$ and $\abs{p(0)}>1000$. By the maximum modulus principle applied to $p$ on the unit disk, $\abs{p(0)}\le\max_{\abs z=1}\abs{p(z)}<1/1000$, contradicting $\abs{p(0)}>1000$. So these compact sets, which are disjoint and nonempty, satisfy the hypotheses of the problem and fail (P).

:::

:::

::: {.pf-step #conclusion}
(i) (P) holds whenever $\CC\setminus(A\cup B)$ is connected; (ii) (P) still holds for the circle and the point $2$, whose complement is disconnected; (iii) (P) fails for the circle and the point $0$.

::: pf-proof
Steps [](#part-i){.pf-ref}, [](#part-ii){.pf-ref} and [](#part-iii){.pf-ref}. The pair in (ii) differs from that in (iii) in that $2$ lies outside the disk bounded by the circle while $0$ lies inside it, which is what makes the maximum modulus principle bite in (iii) and fail to bite in (ii).

:::

:::

:::
:::
