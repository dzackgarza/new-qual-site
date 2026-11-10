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
---

::: {.exercise}

Recall that $\RR_K$ denotes the real line in the $K$-topology.
(See §13.) Let $Y$ be the quotient space obtained from $\RR_K$ by collapsing the set $K$ to a point; let $p: \RR_K \to Y$ be the quotient map.

(a) Show that $Y$ satisfies the $T_1$ axiom, but is not Hausdorff.

(b) Show that $p \times p: \RR_K \times \RR_K \to Y \times Y$ is not a quotient map.
[Hint: The diagonal is not closed in $Y \times Y$, but its inverse image is closed in $\RR_K \times \RR_K$.]
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 22.6, printed pp. 257--258** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 22.6, PDF p. 28, has the same two arguments, but prints $\RR_{\ell}$ for $\RR_{K}$ and asserts without proof that $K$ is closed in $\RR_{K}$; that computation is supplied on the card.

Let $p:\RR_{K}\to Y$ be the quotient map collapsing $K=\{1/n\mid n\in\ZZ_{+}\}$ to the point $k=p(K)$; thus $Y=\{k\}\cup\{\{x\}\mid x\in\RR-K\}$ and $p^{-1}(\{k\})=K$.

(a) *$Y$ is $T_{1}$.* First, $K$ is closed in $\RR_{K}$: for $x\notin K$ the set
$$
B_{x}=\begin{cases}(x-1,x+1)-K,& x=0,\\ (x-\varepsilon,x+\varepsilon)\ \text{with}\ 2\varepsilon=\min\abs{x-1/m},& x\ne0\end{cases}
$$
is a basis element of $\RR_{K}$ containing $x$ and disjoint from $K$ (for $x=0$ note $0\in(-1,1)-K$ because $0\notin K$). So no point outside $K$ is a limit point of $K$, and $K$ is closed.

Now let $U$ be a one-point subset of $Y$. If $U=\{k\}$ then $p^{-1}(U)=K$ is closed in $\RR_{K}$; if $U=\{\{x\}\}$ with $x\notin K$ then $p^{-1}(U)=\{x\}$ is closed in $\RR_{K}$, a Hausdorff space. Since $p$ is a quotient map, $U$ is closed in $Y$ in either case.

*$Y$ is not Hausdorff.* Let $V_{k}$ be a neighbourhood of $k$ and $V_{0}$ a neighbourhood of $\{0\}$ in $Y$; put $U_{k}=p^{-1}(V_{k})$ and $U_{0}=p^{-1}(V_{0})$, which are open in $\RR_{K}$ with $K\subset U_{k}$ and $0\in U_{0}$.

Choose a basis element $B_{0}$ of $\RR_{K}$ with $0\in B_{0}\subset U_{0}$; it is $(a,b)$ or $(a,b)-K$ with $a<0<b$. Choose $n$ with $1/n<b$. Since $1/n\in K\subset U_{k}$ and $U_{k}$ is open, there is a basis element $B_{k}$ with $1/n\in B_{k}\subset U_{k}$; because $1/n\in K$, the basis element $B_{k}$ cannot be of the form $(c,d)-K$, so $B_{k}=(c,d)$ with $c<1/n<d$. Put $e=\max\{1/(n+1),c\}$ and $x=(e+1/n)/2$, so that $1/(n+1)\le e<x<1/n$; then $x\notin K$, and
$$
a<0<\tfrac1{n+1}\le e<x<\tfrac1n<b,
$$
so $x\in(a,b)$ and, since $x\notin K$, also $x\in(a,b)-K$: in either case $x\in B_{0}\subset U_{0}$. And $c\le e<x<1/n<d$ gives $x\in B_{k}\subset U_{k}$. Hence $p(x)=\{x\}$ lies in $V_{0}=p(U_{0})$ and in $V_{k}=p(U_{k})$, so the two neighbourhoods meet. As they were arbitrary, $Y$ is not Hausdorff.

(b) The diagonal $\Delta_{Y}$ is not closed in $Y\times Y$, by part (a) and Exercise 17.13. But
$$
(p\times p)^{-1}(\Delta_{Y})=\{(x,y)\mid p(x)=p(y)\}=\Delta_{\RR}\cup(K\times K),
$$
where $\Delta_{\RR}$ is the diagonal of $\RR_{K}$: indeed $p(x)=p(y)$ holds exactly when $x=y$ (both outside $K$, or the same point) or both $x,y$ lie in $K$. This set is closed in $\RR_{K}\times\RR_{K}$, since $\Delta_{\RR}$ is closed ($\RR_{K}$ is Hausdorff, Exercise 17.13) and $K\times K$ is closed (part (a)). So $p\times p$ pulls a non-closed set back to a closed set and is not a quotient map.
:::
