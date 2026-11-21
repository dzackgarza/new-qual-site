---
schema: qual/card@1
id: E-N7AOD
kind: problem
title: The fundamental group of a topological group is abelian
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 52: Problem 7 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-7-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-52-the-fundamental-group/problem-7-solution.txt), and against Munkres, Topology (2000), Section 52
    Exercise 7, printed p. 335. dbFin answers all four parts. What was corrected: in part (c) dbFin's displayed computation of (f star e) tensor (e star g) reads f(s) on [0,1/2] and g(s) on [1/2,1], which forgets the reparametrisation; the correct values are f(2s) and g(2s-1), and the card has them. Part (d) is dbFin's argument by the interchange law, written out.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and the retained dbFin solution is now cited in the
    solution section rather than only here. Pages checked against the book: §52 Exercise 7
    on printed p. 335; Theorem 51.2, which supplies the right and left identities for *,
    on printed p. 331; the definition of a topological group, with continuous multiplication
    and inversion, on printed p. 145 in the supplementary exercises of §22. Each part
    re-checked: the product of two loops is a loop because (s,t) to (f(s),g(s)) and
    multiplication are continuous and the endpoints multiply to e; inversion of loops is
    continuous by continuity of inversion in G; the homotopy F(s,t)G(s,t) of part (b) is
    based because F(0,t)G(0,t) = e times e; in part (c) the product (f*e) tensor (e*g) is
    f(2s) on the lower half and g(2s-1) on the upper, the reparametrisation that dbFin's
    display drops, and the two halves agree at s = 1/2 since f(1) = g(0) = e; and the
    interchange law holds at each s on each half of the interval, which is why it is an
    identity of loops and not merely of classes. No repair to the statement.
---

::: {.exercise}

Let $G$ be a topological group with operation $\cdot$ and identity element $x_0$.
Let $\Omega(G, x_0)$ denote the set of all loops in $G$ based at $x_0$.
If $f, g \in \Omega(G, x_0)$, let us define a loop $f \otimes g$ by the rule

$$
(f \otimes g)(s) = f(s) \cdot g(s).
$$

(a) Show that this operation makes the set $\Omega(G, x_0)$ into a group.

(b) Show that this operation induces a group operation $\otimes$ on $\pi_1(G, x_0)$.

(c) Show that the two group operations $*$ and $\otimes$ on $\pi_1(G, x_0)$ are the same.
[Hint: Compute $(f * e_{x_0}) \otimes (e_{x_0} * g)$.]

(d) Show that $\pi_1(G, x_0)$ is abelian.
:::

::: {.solution}
The argument is the retained published solution, **dbFin, "Section 52: Problem 7 Solution"**, https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-7-solution/ (read 2026-11-11; kept at `tmp/sources/dbfin/section-52-the-fundamental-group/problem-7-solution.txt`), restructured into steps; it answers all four parts. In part (c) its computation writes $f(s)$ on $[0,1/2]$ and $g(s)$ on $[1/2,1]$, which forgets the reparametrisation; the values below are $f(2s)$ and $g(2s-1)$, and they are what the printed hint's product actually is.

Throughout, $G$ is a topological group with identity $e=x_0$, so that multiplication $G\times G\to G$ and inversion $G\to G$ are continuous (Supplementary Exercises: Topological Groups, printed p. 145), $\Omega(G,e)$ is the set of loops based at $e$, $(f\otimes g)(s)=f(s)\cdot g(s)$, and $\ast$ is concatenation with $[f]\ast[g]$ the product in $\pi_1(G,e)$ (Theorem 51.2, printed p. 331). The exercise is §52 Exercise 7 (printed p. 335).

::: pf

::: {.pf-step #a}
(a) $\otimes$ makes $\Omega(G,e)$ into a group.

::: pf-proof

::: {.pf-step #loop}
If $f,g\in\Omega(G,e)$ then $f\otimes g\in\Omega(G,e)$.

::: pf-proof
$s\mapsto(f(s),g(s))$ is continuous into $G\times G$ and multiplication is continuous, so $f\otimes g$ is continuous; its endpoint values are $(f\otimes g)(0)=e\cdot e=e=(f\otimes g)(1)$.
:::

:::

::: {.pf-step #axioms}
$\otimes$ is associative, the constant loop $e_e$ is a two-sided identity, and $f\otimes \inverseof{f}$ is $e_e$, where $\inverseof{f}(s)=\inverseof{f(s)}$.

::: pf-proof
Associativity is the associativity of the product in $G$, read at each $s$. The equality $(f\otimes e_e)(s)=f(s)\cdot e=f(s)=(e_e\otimes f)(s)$ makes $e_e$ a two-sided identity. Inversion in $G$ is continuous, so $\inverseof{f}$ is a continuous loop based at $\inverseof{e}=e$; and $(f\otimes \inverseof{f})(s)=f(s)\inverseof{f(s)}=e$, so $f\otimes \inverseof{f}=e_e=\inverseof{f}\otimes f$.
:::

:::

:::

:::

::: {.pf-step #b}
(b) $\otimes$ induces a well-defined operation on $\pi_1(G,e)$.

::: pf-proof
Let $f\simeq f'$ and $g\simeq g'$ through based homotopies $F,G:I\times I\to G$, so that $F(s,0)=f(s)$, $F(s,1)=f'(s)$, $F(0,t)=F(1,t)=e$, and likewise for $G$. Put $H(s,t)=F(s,t)\cdot G(s,t)$. It is continuous, being a composite of $(s,t)\mapsto(F(s,t),G(s,t))$ with multiplication; $H(s,0)=f(s)g(s)=(f\otimes g)(s)$ and $H(s,1)=(f'\otimes g')(s)$; and $H(0,t)=e\cdot e=H(1,t)$. So $H$ is a based homotopy from $f\otimes g$ to $f'\otimes g'$, and $[f]\otimes[g]=[f\otimes g]$ is independent of the representatives. The group axioms on classes follow from those proved in step [](#a){.pf-ref}, since $\otimes$ is defined by a formula on representatives.
:::

:::

::: {.pf-step #c}
(c) $\otimes$ and $\ast$ coincide on $\pi_1(G,e)$.

::: pf-proof

::: {.pf-step #identities}
$[f]\ast[e_e]=[f]=[e_e]\ast[f]$ for every $f\in\Omega(G,e)$.

::: pf-proof
This is part (2) of Theorem 51.2 (printed p. 331), the right and left identities for $\ast$.
:::

:::

::: {.pf-step #product}
$(f\ast e_e)\otimes(e_e\ast g)=f\ast g$ as loops.

::: pf-proof
For $s\le1/2$ we have $(f\ast e_e)(s)=f(2s)$ and $(e_e\ast g)(s)=e_e(2s)=e$, so the product at $s$ is $f(2s)\cdot e=f(2s)$, which is $(f\ast g)(s)$. For $s\ge1/2$ we have $(f\ast e_e)(s)=e_e(2s-1)=e$ and $(e_e\ast g)(s)=g(2s-1)$, so the product at $s$ is $e\cdot g(2s-1)=g(2s-1)=(f\ast g)(s)$. At $s=1/2$ both computations give $f(1)=e=g(0)$. Hence the two loops agree at every $s$.
:::

:::

::: {.pf-step #same}
$[f]\otimes[g]=[f]\ast[g]$.

::: pf-proof
By step [](#identities){.pf-ref} and the well-definedness of step [](#b){.pf-ref},
$$
[f]\otimes[g]=[f\ast e_e]\otimes[e_e\ast g]=[(f\ast e_e)\otimes(e_e\ast g)]=[f\ast g]=[f]\ast[g],
$$
where the middle equality is step [](#product){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #d}
(d) $\pi_1(G,e)$ is abelian.

::: pf-proof
For loops $a,b,c,d$ the interchange law
$$
(a\ast b)\otimes(c\ast d)=(a\otimes c)\ast(b\otimes d)
$$
holds: at $s\le1/2$ both sides equal $a(2s)c(2s)$, and at $s\ge1/2$ both equal $b(2s-1)d(2s-1)$, the products being taken in $G$. So the two sides are the same loop, hence the same class in $\pi_1(G,e)$. Write $1=[e_e]$, the identity of both operations by step [](#identities){.pf-ref} and step [](#a){.pf-ref}. Then, using step [](#c){.pf-ref} for the first and last equalities and the interchange law for the middle one,
$$
[f]\ast[g]=[f]\otimes[g]=(1\ast[f])\otimes([g]\ast1)=(1\otimes[g])\ast([f]\otimes1)=[g]\ast[f],
$$
where $1\otimes[g]=[e_e\otimes g]=[g]$ and $[f]\otimes1=[f\otimes e_e]=[f]$ because $(e_e\otimes g)(s)=e\cdot g(s)=g(s)$ and $(f\otimes e_e)(s)=f(s)$. Hence $[f]\ast[g]=[g]\ast[f]$ for all classes, and $\pi_1(G,e)$ is abelian.
:::

:::

:::
:::
