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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 3.5, printed pp. 21-24); statement unchanged. The five sets S_1, ..., S_5 are now introduced with the identities that the proof uses and that the earlier prose left implicit -- S_1 is the diagonal, S_3 the reverse of S, S_4 = S o S, S_5 the reverse of S o S -- each proved in the step that states them, because "T_0 is contained in every R" and "T_0 is symmetric" are read off those identities. Part (c) is split into the containment in every R, the verification that T_0 is itself an equivalence relation (whose transitivity keeps the sixteen-case table, now with four entries worked rather than one), the equality with the intersection, and the class description, where the classes at x = 1 and x = 2 are now computed rather than listed. Pages: the definition of an equivalence relation is on printed p. 27.

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

Throughout, a relation on $\RR$ is a subset of $\RR\times\RR$, and it is an equivalence relation when it is reflexive, symmetric and transitive (§3). The two given relations are
$$
S=\{(x,y):y=x+1,\ 0<x<2\},\qquad S'=\{(x,y):y-x\in\ZZ\},
$$
and $T$ is the intersection of all equivalence relations on $\RR$ that contain $S$.

::: pf

::: {.pf-step #a}
(a) $S'$ is an equivalence relation on $\RR$, it contains $S$, and its classes are the sets $x+\ZZ$.

::: pf-proof

::: {.pf-step #reflexive}
$S'$ is reflexive.

::: pf-proof
$x-x=0\in\ZZ$, so $(x,x)\in S'$ for every $x\in\RR$.

:::

:::

::: {.pf-step #symmetric}
$S'$ is symmetric.

::: pf-proof
If $(x,y)\in S'$ then $n=y-x\in\ZZ$, so $x-y=-n\in\ZZ$ and $(y,x)\in S'$.

:::

:::

::: {.pf-step #transitive}
$S'$ is transitive.

::: pf-proof
If $y-x=n\in\ZZ$ and $z-y=m\in\ZZ$ then $z-x=(z-y)+(y-x)=m+n\in\ZZ$, so $(x,z)\in S'$, using that $\ZZ$ is closed under addition.

:::

:::

::: {.pf-step #contains}
$S\subset S'$.

::: pf-proof
If $(x,y)\in S$ then $y-x=1\in\ZZ$, so $(x,y)\in S'$.

:::

:::

::: {.pf-step #classes}
The class of $x$ under $S'$ is $x+\ZZ$.

::: pf-proof
$y$ is related to $x$ exactly when $y-x\in\ZZ$, that is exactly when $y\in x+\ZZ$; so the class is $\{y:y-x\in\ZZ\}=x+\ZZ$.

:::

:::

:::

:::

::: {.pf-step #b}
(b) The intersection of any collection of equivalence relations on a set $A$ is an equivalence relation on $A$.

::: pf-proof
Let $\mathcal{D}$ be such a collection and $C=\bigcap_{D\in\mathcal{D}}D$. Each $D$ is a subset of $A\times A$, so $C\subseteq A\times A$, that is $C$ is a relation on $A$. For $x\in A$ and every $D\in\mathcal{D}$ we have $(x,x)\in D$, so $(x,x)\in C$: $C$ is reflexive. If $(x,y)\in C$ then $(x,y)\in D$ for every $D$, so $(y,x)\in D$ for every $D$ by symmetry of each $D$, hence $(y,x)\in C$: $C$ is symmetric. If $(x,y),(y,z)\in C$ then both pairs lie in every $D$, so $(x,z)\in D$ for every $D$ by transitivity of each $D$, hence $(x,z)\in C$: $C$ is transitive.

:::

:::

::: {.pf-step #c}
(c) $T$ is the set $S_1\cup S_2\cup S_3\cup S_4\cup S_5$ described in step [](#five-sets){.pf-ref}, and its classes are those of step [](#classes-t){.pf-ref}.

::: pf-proof

::: {.pf-step #five-sets}
Put
$$
\begin{aligned}
S_1&=\{(x,y):y=x\}, & S_2&=\{(x,y):y=x+1,\ 0<x<2\}=S,\\
S_3&=\{(x,y):y=x-1,\ 1<x<3\}, & S_4&=\{(x,y):y=x+2,\ 0<x<1\},\\
S_5&=\{(x,y):y=x-2,\ 2<x<3\},
\end{aligned}
$$
and $T_0=S_1\cup S_2\cup S_3\cup S_4\cup S_5$. Then $S_1$ is the diagonal, $S_2=S$, $S_3=\{(x,y):(y,x)\in S\}$, $S_4=S\circ S$ and $S_5=\{(x,y):(y,x)\in S\circ S\}$.

::: pf-proof
$S_3$: $(x,y)\in S_3$ means $y=x-1$ with $1<x<3$, which says $x=y+1$ with $0<y<2$, that is $(y,x)\in S$. $S_4$: $S\circ S$ consists of pairs $(x,z)$ for which some $y$ has $y=x+1$ with $0<x<2$ and $z=y+1$ with $0<y<2$; then $z=x+2$ and $0<x<1$ (since $0<y=x+1<2$ forces $0<x<1$), and conversely $0<x<1$ gives $y=x+1\in(1,2)$ and $z=y+1$. $S_5$: the same computation read backwards, $(x,y)\in S_5$ iff $(y,x)\in S_4$.

:::

:::

::: {.pf-step #in-every}
$T_0\subseteq R$ for every equivalence relation $R$ on $\RR$ containing $S$.

::: pf-proof
Let $R\supseteq S$ be an equivalence relation. $S_1\subseteq R$ by reflexivity. $S_2=S\subseteq R$ by hypothesis. $S_3\subseteq R$ by symmetry, since $(y,x)\in S\subseteq R$ for $(x,y)\in S_3$. $S_4\subseteq R$ by transitivity, and $S_5\subseteq R$ likewise by transitivity applied to the reversed pairs. Hence every element of $T_0$ lies in $R$, so $T_0$ is contained in the intersection of all such $R$.

:::

:::

::: {.pf-step #is-equiv}
$T_0$ is an equivalence relation on $\RR$ and contains $S$.

::: pf-proof
$S=S_2\subseteq T_0$. Reflexive: $S_1\subseteq T_0$ is the diagonal. Symmetric: $S_1$ is symmetric, and by step [](#five-sets){.pf-ref} the pairs $(S_2,S_3)$ and $(S_4,S_5)$ are exchanged by reversing pairs, so $(x,y)\in T_0$ gives $(y,x)\in T_0$. Transitive: let $(x,y),(y,z)\in T_0$ with $x,y,z$ not all equal; each pair lies in exactly one of $S_2,\dots,S_5$, and each of the sixteen combinations is either impossible from the ranges or yields $(x,z)\in S_j$ for some $j$, as the table records:
$$
\begin{array}{c|cccc}
(x,y)\backslash(y,z) & S_2 & S_3 & S_4 & S_5\\\hline
S_2 & S_4 & S_1 & \text{impossible} & S_3\\
S_3 & S_1 & S_5 & S_2 & \text{impossible}\\
S_4 & \text{impossible} & S_2 & \text{impossible} & S_1\\
S_5 & S_3 & \text{impossible} & S_1 & \text{impossible}
\end{array}
$$
For example $(x,y)\in S_2$ and $(y,z)\in S_2$ give $z=y+1=x+2$ with $0<x<1$, hence $(x,z)\in S_4$; $(x,y)\in S_2$ and $(y,z)\in S_3$ give $z=y-1=x$, hence $(x,z)\in S_1$; $(x,y)\in S_3$ and $(y,z)\in S_4$ give $z=y+2=x+1$ with $1<x<2$, hence $(x,z)\in S_2$; and $(x,y)\in S_2$ with $(y,z)\in S_4$ is impossible, since $1<y<3$ contradicts $0<y<1$. Each remaining entry is read off the same way from $y=x\pm1$ or $y=x\pm2$ together with the stated ranges, and the cases $x=y$ or $y=z$ are settled by $S_1$.

:::

:::

::: {.pf-step #equals}
$T_0=\bigcap\{R: R$ an equivalence relation on $\RR$, $S\subseteq R\}$.

::: pf-proof
By step [](#in-every){.pf-ref} $T_0$ is contained in every such $R$, hence in their intersection. By step [](#is-equiv){.pf-ref} $T_0$ is itself one of them, so the intersection is contained in $T_0$. Hence the two are equal, and $T_0$ is the least equivalence relation containing $S$.

:::

:::

::: {.pf-step #classes-t}
The classes of $T_0$ are $\{x\}$ for $x\le0$ or $x\ge3$; $\{1,2\}$; and the three-point sets $\{x,x+1,x+2\}$ for $0<x<1$, $\{x-1,x,x+1\}$ for $1<x<2$, $\{x-2,x-1,x\}$ for $2<x<3$.

::: pf-proof
Outside $(0,3)$ no set $S_2,\dots,S_5$ has a point whose first or second coordinate is $x$, so the class of such $x$ is $\{x\}$ by $S_1$. For $0<x<1$ the pairs $(x,x+1)\in S_2$ and $(x+1,x+2)\in S_2$ give $(x,x+2)\in S_4$, so the class contains $\{x,x+1,x+2\}$, and no further point: $S_2,\dots,S_5$ change a coordinate by $\pm1,\pm2$, and a chain from $x$ staying in the class cannot pass below $0$ or above $3$ because those points are isolated. The ranges $1<x<2$ and $2<x<3$ are the same computation read from $S_3$ and $S_5$. At $x=1$: $(1,2)\in S_2$, while $(2,3)\notin S_2$ because $0<2<2$ fails and $(2,3)\notin S_4$ because $0<2<1$ fails, so the class of $1$ is $\{1,2\}$, and symmetrically the class of $2$ is $\{1,2\}$.

:::

:::

:::

:::

:::

:::
