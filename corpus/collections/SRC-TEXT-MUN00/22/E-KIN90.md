---
schema: qual/card@1
id: E-KIN90
kind: problem
title: Collapsing K in the K-topology
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 6, printed p. 145, with Exercise
    17.13 and Exercise 17.16 for the K-topology; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 22.6, printed pp.
    257-258. The T1 half is his, resting on K being closed in R_K, and the card adds that
    computation: for x not in K a basis element at x avoiding K, including x = 0 via (-1,1)
    - K. The failure of Hausdorff is his: a basis element at 0 and one at a point 1/n of K
    can be made to share a point x between 1/(n+1) and 1/n, and x is outside K. Part (b) is
    his: the inverse image of the diagonal is the diagonal of R_K together with K x K,
    closed although the diagonal of Y is not. (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked both parts against Munkres §22 Exercise 6,
    printed pp. 143-144, with Theorem 17.6 and Exercise 17.13: K closed in R_K by the three
    cases x<0, x=0, x>0 with x not in K; Y T_1 through the closed fibres of a quotient map;
    the failure of Hausdorff through a point of the basis element (1/(n+1),1/n) lying in
    both preimages; and (b) through the diagonal, which is not closed in Y x Y while its
    preimage Delta_R union K x K is. Repair: the earlier proof that K is closed used min
    over m of abs(x - 1/m), a set that has no minimum for x < 0; the case division replaces
    it. Whitman, Exercise 22.6, printed pp. 257-258.
---

::: {.exercise}

Recall that $\RR_K$ denotes the real line in the $K$-topology.
(See §13.) Let $Y$ be the quotient space obtained from $\RR_K$ by collapsing the set $K$ to a point; let $p: \RR_K \to Y$ be the quotient map.

(a) Show that $Y$ satisfies the $T_1$ axiom, but is not Hausdorff.

(b) Show that $p \times p: \RR_K \times \RR_K \to Y \times Y$ is not a quotient map.
[Hint: The diagonal is not closed in $Y \times Y$, but its inverse image is closed in $\RR_K \times \RR_K$.]
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 22.6, printed pp. 257--258** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 22.6, PDF p. 28, has the same two arguments but prints $\RR_{\ell}$ for $\RR_{K}$ and asserts without proof that $K$ is closed in $\RR_{K}$; that computation is supplied below, and the earlier version of it on this card, which used the minimum of $\abs{x-1/m}$ over $m$, is replaced: that set has no minimum when $x<0$, since its values decrease to $\abs{x}$.

Let $p:\RR_{K}\to Y$ be the quotient map collapsing $K=\{1/n\mid n\in\ZZ_{+}\}$ to the point $k=p(K)$, so that $Y=\{k\}\cup\big\{\{x\}\mid x\in\RR-K\big\}$ and $p^{-1}(\{k\})=K$.

::: pf

::: {.pf-step #K-closed}
$K$ is closed in $\RR_{K}$.

:::: pf-proof

::: {.pf-step #K-outside}
Every $x\in\RR-K$ has a basis element of $\RR_{K}$ containing $x$ and disjoint from $K$.

::: pf-proof
Three cases. If $x<0$, then $(-\infty,0)=\bigcup_{m\in\ZZ_{+}}(x-m-1,x-m)$ is a union of basis elements of $\RR_{K}$, hence open and containing $x$, and every element of $K$ is positive, so it is disjoint from $K$. If $x=0$, then $(-1,1)-K$ is a basis element of $\RR_{K}$ containing $0$, since $0\notin K$, and it is disjoint from $K$. If $x>0$ and $x\notin K$: when $x>1$ the basis element $(1,x+1)$ contains $x$ and is disjoint from $K$, since every element of $K$ is at most $1$; when $0<x<1$, choose $n\in\ZZ_{+}$ with $n<1/x<n+1$, which exists by §4 Exercise 9(a), and then the basis element $\big(1/(n+1),1/n\big)$ contains $x$ and is disjoint from $K$, because $1/(n+1)<1/m<1/n$ would give $n<m<n+1$.
:::

:::

::: {.pf-step}
$K$ is closed.

::: pf-proof
By step [](#K-outside){.pf-ref} every point of $\RR_{K}-K$ has a neighbourhood disjoint from $K$, so no such point is a limit point of $K$; hence $K$ contains all its limit points and is closed (Theorem 17.6).
:::

:::

:::

:::

::: {.pf-step #part-a}
(a) $Y$ satisfies the $T_{1}$ axiom and is not Hausdorff.

:::: pf-proof

::: {.pf-step #T1}
$Y$ is $T_{1}$.

::: pf-proof
It suffices that every one-point subset of $Y$ be closed. For $U=\{k\}$ the preimage $p^{-1}(U)=K$ is closed in $\RR_{K}$ by step [](#K-closed){.pf-ref}; for $U=\{\{x\}\}$ with $x\in\RR-K$ the preimage is $\{x\}$, closed in $\RR_{K}$ because $\RR_{K}$ is Hausdorff: its topology contains the usual one, whose basis elements $(a,b)$ are also basis elements of $\RR_{K}$, so distinct points are separated by disjoint open sets. Since $p$ is a quotient map, a subset of $Y$ is closed exactly when its preimage is closed, so both kinds of singleton are closed in $Y$.
:::

:::

::: {.pf-step #not-hausdorff}
$Y$ is not Hausdorff.

::: pf-proof
Let $V_{k}$ be a neighbourhood of $k$ and $V_{0}$ a neighbourhood of $\{0\}$ in $Y$, and put $U_{k}=p^{-1}(V_{k})$, $U_{0}=p^{-1}(V_{0})$; these are open in $\RR_{K}$ with $K\subset U_{k}$ and $0\in U_{0}$ (here $0\notin K$, so $p^{-1}(\{0\})=\{0\}$). Choose a basis element $B_{0}$ of $\RR_{K}$ with $0\in B_{0}\subset U_{0}$; it is $(a,b)$ or $(a,b)-K$ with $a<0<b$, so $\tfrac1n<b$ for some $n$. Since $\tfrac1n\in K\subset U_{k}$ and $U_{k}$ is open, there is a basis element $B_{k}$ with $\tfrac1n\in B_{k}\subset U_{k}$; as $\tfrac1n\in K$, the set $B_{k}$ cannot be of the form $(c,d)-K$, so $B_{k}=(c,d)$ with $c<\tfrac1n<d$. Put $e=\max\{1/(n+1),c\}$ and $x=(e+1/n)/2$; then $e<\tfrac1n$, so $\tfrac1{n+1}\le e<x<\tfrac1n$, and
$$
a<0<\tfrac1{n+1}\le e<x<\tfrac1n<b,
$$
so $x\in(a,b)$, while $x\notin K$ because no element of $K$ lies strictly between $1/(n+1)$ and $1/n$. Hence $x\in B_{0}$ in either form of $B_{0}$, and $x\in B_{k}$ because $c\le e<x<\tfrac1n<d$. So $p(x)=\{x\}$ lies in $V_{0}=p(U_{0})$ and in $V_{k}=p(U_{k})$, and the two neighbourhoods meet. As $V_{k}$ and $V_{0}$ were arbitrary, no two points of $Y$ are separated by disjoint neighbourhoods there, and $Y$ is not Hausdorff.
:::

:::

::: {.pf-step}
(a) holds.

::: pf-proof
Steps [](#T1){.pf-ref} and [](#not-hausdorff){.pf-ref} are the two assertions of (a).
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) $p\times p:\RR_{K}\times\RR_{K}\to Y\times Y$ is not a quotient map.

:::: pf-proof

::: {.pf-step #diagonal-open}
The diagonal $\Delta_{Y}$ is not closed in $Y\times Y$.

::: pf-proof
A space is Hausdorff exactly when its diagonal is closed in its square (Exercise 17.13), and $Y$ is not Hausdorff by step [](#part-a){.pf-ref}; so $\Delta_{Y}$ is not closed.
:::

:::

::: {.pf-step #preimage-closed}
$(p\times p)^{-1}(\Delta_{Y})=\Delta_{\RR}\cup(K\times K)$ is closed in $\RR_{K}\times\RR_{K}$.

::: pf-proof
For $(x,y)\in\RR_{K}\times\RR_{K}$ one has $p(x)=p(y)$ exactly when $x=y$, or when both $x$ and $y$ lie in $K$: the fibres of $p$ are the singleton $\{x\}$ for $x\notin K$ and the set $K$, so equality of images means $x$ and $y$ lie in the same fibre. So $(p\times p)^{-1}(\Delta_{Y})=\Delta_{\RR}\cup(K\times K)$. Here $\Delta_{\RR}$ is closed in $\RR_{K}\times\RR_{K}$ because $\RR_{K}$ is Hausdorff (Exercise 17.13), and $K\times K$ is closed because $K$ is closed in $\RR_{K}$ by step [](#K-closed){.pf-ref}; a union of two closed sets is closed.
:::

:::

::: {.pf-step #not-quotient}
$p\times p$ is not a quotient map.

::: pf-proof
$p\times p$ is continuous, being a product of continuous maps. A continuous surjection $q$ is a quotient map exactly when a subset $A$ of its range is closed if and only if $q^{-1}(A)$ is closed; for $q=p\times p$ the set $A=\Delta_{Y}$ is not closed by step [](#diagonal-open){.pf-ref} while $q^{-1}(A)$ is closed by step [](#preimage-closed){.pf-ref}. So that equivalence fails and $p\times p$ is not a quotient map.
:::

:::

::: {.pf-step}
(b) holds.

::: pf-proof
Step [](#not-quotient){.pf-ref} is the assertion of (b).
:::

:::

:::

:::
:::
:::
