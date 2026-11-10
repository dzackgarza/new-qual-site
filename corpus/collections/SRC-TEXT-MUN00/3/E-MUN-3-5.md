---
schema: qual/card@1
id: E-MUN-3-5
kind: problem
title: The coarsest equivalence relation on the line containing a shifted segment
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 5, printed p. 28: S is the
    segment y = x + 1 with 0 < x < 2 and S' the set of pairs with y - x an integer;
    (a) S' is an equivalence relation on the real line with S' containing S, its classes
    to be described, (b) any intersection of equivalence relations is one, (c) the
    intersection T of all equivalence relations containing S, with its classes. The
    stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.5,
    printed pp. 21-24 (tmp/sources/munkres-solutions-whitman.pdf). His answer for (c) is
    the union of the five sets S_1, ..., S_5 below; the five cases in each of the two
    inclusions are his, as is the class description - singletons off (0,3), the pair
    {1,2}, and three-point classes in between - which is checked here against the
    sixteen-case transitivity table he writes out.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked the claim of (c) independently, since it is the one place where a published
    solution could be read wrongly: for 0 < x < 1 the three points x, x+1, x+2 are
    pairwise related (S_2 twice and S_4), and no further point is, because S_1 is
    diagonal, S_2, S_3, S_4, S_5 each shift by 1 or 2 and the inequalities confine the
    chain to those three values.
---

::: {.exercise}

Let $S$ and $S'$ be the following subsets of the plane:
$$
S = \{(x, y) \mid y = x + 1 \text{ and } 0 < x < 2\},
\qquad
S' = \{(x, y) \mid y - x \text{ is an integer}\}.
$$

(a) Show that $S'$ is an equivalence relation on the real line and $S' \supset S$. Describe the equivalence classes of $S'$.

(b) Show that given any collection of equivalence relations on a set $A$, their intersection is an equivalence relation on $A$.

(c) Describe the equivalence relation $T$ on the real line that is the intersection of all equivalence relations on the real line that contain $S$. Describe the equivalence classes of $T$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.5, printed pp. 21--24** (`tmp/sources/munkres-solutions-whitman.pdf`); the three parts, the five sets $S_1,\dots,S_5$ and the class description below are his.

(a) Since $S'\subset\RR\times\RR$ it is a relation on $\RR$.

*Reflexive.* $x-x=0\in\ZZ$, so $(x,x)\in S'$.

*Symmetric.* If $n=y-x\in\ZZ$ then $x-y=-n\in\ZZ$.

*Transitive.* If $n=y-x\in\ZZ$ and $m=z-y\in\ZZ$ then $z-x=(z-y)+(y-x)=m+n\in\ZZ$.

For $(x,y)\in S$ we have $y-x=1\in\ZZ$, so $(x,y)\in S'$ and $S'\supset S$.

The class of $x$ is $x+\ZZ=\{x+n\mid n\in\ZZ\}$: indeed $y\in x+\ZZ$ exactly when $y-x\in\ZZ$, that is exactly when $xS'y$.

(b) Let $\mathcal A$ be a collection of equivalence relations on $A$ and $C=\bigcap_{D\in\mathcal A}D$. Each $D$ lies in $A\times A$, so $C\subset A\times A$. For $x\in A$ and every $D$ we have $(x,x)\in D$, so $(x,x)\in C$. If $(x,y)\in C$ then $(x,y)\in D$ for all $D$, so $(y,x)\in D$ for all $D$ and $(y,x)\in C$. If $(x,y),(y,z)\in C$ then both lie in every $D$, so $(x,z)\in D$ for every $D$ and $(x,z)\in C$.

(c) $S$ is not itself an equivalence relation, since $(x,x)\notin S$ for every $x$. Put
$$
\begin{aligned}
S_1&=\{(x,y)\mid y=x\}, & S_2&=\{(x,y)\mid y=x+1,\ 0<x<2\}=S,\\
S_3&=\{(x,y)\mid y=x-1,\ 1<x<3\}, & S_4&=\{(x,y)\mid y=x+2,\ 0<x<1\},\\
S_5&=\{(x,y)\mid y=x-2,\ 2<x<3\},
\end{aligned}
$$
and $T=S_1\cup S_2\cup S_3\cup S_4\cup S_5$. Let $\mathcal S^*$ be the collection of equivalence relations on $\RR$ containing $S$; we show $T=\bigcap_{R\in\mathcal S^*}R$.

*Every element of $T$ lies in every $R\in\mathcal S^*$.* Let $R\in\mathcal S^*$ and $(x,y)\in T$. If $(x,y)\in S_1$ then $y=x$ and $(x,x)\in R$ by reflexivity; if $(x,y)\in S_2$ then $(x,y)\in S\subset R$; if $(x,y)\in S_3$ then $x=y+1$ with $0<y<2$, so $(y,x)\in S\subset R$ and $(x,y)\in R$ by symmetry; if $(x,y)\in S_4$ then $y=x+2$ with $0<x<1$, and with $z=x+1$ we have $(x,z)\in S\subset R$ and $(z,y)\in S\subset R$ because $0<z<2$ and $y=z+1$, so $(x,y)\in R$ by transitivity; and if $(x,y)\in S_5$ then $x=y+2$ with $0<y<1$, so $(y,x)\in S_4\subset R$ by the previous case and $(x,y)\in R$ by symmetry.

*$T$ itself is an equivalence relation containing $S$, so it contains the intersection.* Clearly $T\subset\RR\times\RR$ and $S=S_2\subset T$. It is reflexive because $S_1\subset T$. For symmetry: $S_1$ is symmetric, and the four others pair off, $(x,y)\in S_2$ giving $(y,x)\in S_3$ since $y=x+1$ with $0<x<2$ means $x=y-1$ with $1<y<3$, and conversely; and $(x,y)\in S_4$ giving $(y,x)\in S_5$ since $y=x+2$ with $0<x<1$ means $x=y-2$ with $2<y<3$, and conversely. For transitivity: given $xTy$ and $yTz$ with $x\ne y\ne z$, the pair $(x,y)$ lies in exactly one of $S_2,\dots,S_5$ and $(y,z)$ in exactly one, and each of the sixteen combinations either is impossible from the ranges or yields $(x,z)\in S_j$ for some $j$:
$$
\begin{array}{c|cccc}
(x,y)\backslash(y,z) & S_2 & S_3 & S_4 & S_5\\\hline
S_2 & S_4 & S_1 & \text{impossible} & S_3\\
S_3 & S_1 & S_5 & S_2 & \text{impossible}\\
S_4 & \text{impossible} & S_2 & \text{impossible} & S_1\\
S_5 & S_3 & \text{impossible} & S_1 & \text{impossible}
\end{array}
$$
For example $(x,y)\in S_2$ and $(y,z)\in S_2$ give $z=y+1=x+2$ with $0<x<1$, hence $(x,z)\in S_4$; $(x,y)\in S_2$ and $(y,z)\in S_3$ give $z=y-1=x$, hence $(x,z)\in S_1$; and $(x,y)\in S_2$, $(y,z)\in S_4$ is impossible since $1<y<3$ contradicts $0<y<1$. The remaining entries are checked the same way from $y=x\pm1$ or $y=x\pm2$ and the stated ranges, and the cases $x=y$ or $y=z$ are settled by $S_1$.

Therefore $T$ is the least equivalence relation containing $S$, that is $T=\bigcap_{R\in\mathcal S^*}R$.

Its classes are: $\{x\}$ for $x\le0$ or $x\ge3$; $\{1,2\}$ for $x=1$ and for $x=2$; and three-point classes
$$
\{x,x+1,x+2\}\ (0<x<1),
\qquad
\{x-1,x,x+1\}\ (1<x<2),
\qquad
\{x-2,x-1,x\}\ (2<x<3).
$$
Indeed outside $(0,3)$ no set $S_2,\dots,S_5$ has a point with first coordinate $x$ or second coordinate $x$, so the class is $\{x\}$; for $0<x<1$ the three points $x,x+1,x+2$ are pairwise related through $S_2$ and $S_4$ and nothing else is, and the other two ranges are the same computation read from $S_3$ and $S_5$.
:::
