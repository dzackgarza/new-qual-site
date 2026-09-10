---
schema: qual/card@1
id: P-T4WCS
kind: problem
title: Two $3$-cycles in $S_5$ generate $A_4$ or $A_5$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both alternatives and the exclusion of equal or inverse cycles with Summer 2007 Groups 4 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the support intersections, transitivity, conjugate-cycle support, and order arguments without assuming simplicity of A5."
---

::: problem
Let $x, y$ be $3$-cycles in $S_5$, $x$ not equal to $y$ or $y^{-1}$.

a. If there is some element of $\{1,2,3,4,5\}$ fixed by both $x$ and $y$, show that $\langle x, y \rangle$ is isomorphic to $A_4$.

b. If there is no such element fixed by both, show that $\langle x, y \rangle = A_5$.
:::

::: solution
Write $S=\operatorname{supp}(x)$, $T=\operatorname{supp}(y)$, and
$H=\langle x,y\rangle$. Here the support of a permutation is the set
of points it moves.

<1>1. The supports are distinct, intersect nontrivially, and $H$ acts
transitively on $S\cup T$.

::: proof
There are exactly two $3$-cycles on a given set of three points,
and they are inverses. Thus the hypothesis on $x,y$ implies $S\ne T$.
Since each support has three points in a five-point set, their
intersection is nonempty and their union has size four or five.

Choose $c\in S\cap T$. Powers of $x$ carry $c$ through all of $S$,
and powers of $y$ carry $c$ through all of $T$. Consequently the
$H$-orbit of $c$ contains $S\cup T$. Both generators preserve this
union and fix every point outside it. The orbit is therefore exactly
$S\cup T$, proving transitivity there.
:::

<1>2. If there is a common fixed point, then $H\cong A_4$.

::: proof
A common fixed point lies outside $S\cup T$, so this union has size
four. Put $U=S\cup T$. A $3$-cycle is even, since
$(a\ b\ c)=(a\ c)(a\ b)$ is a product of two transpositions.
Thus $H$ is contained in the group $A(U)$ of even permutations of
$U$, extended by the identity on the remaining point.
The group $A(U)$ has order $4!/2=12$.

By step <1>1, an $H$-orbit has size $4$, so $4\mid |H|$ by
orbit-stabilizer. Also $3\mid |H|$, since $H$ contains $x$ of order
$3$, by Lagrange's theorem [@DF04]. Hence $12\mid |H|$.
The inclusion in $A(U)$ now forces $|H|=12$ and $H=A(U)\cong A_4$.
:::

<1>3. If there is no common fixed point, then $H=A_5$.

::: proof
Now $S\cup T$ is the entire five-point set, so $S\cap T=\{c\}$
for one point $c$. Let $z=yxy^{-1}\in H$. Conjugating a cycle
applies the conjugating permutation to its entries, so
$$
\operatorname{supp}(z)=y(S)
=(S\setminus\{c\})\cup\{y(c)\}.
$$
Here $y$ fixes both points of $S\setminus\{c\}$, while
$y(c)\in T\setminus\{c\}$ is not in $S$. Therefore $x$ and $z$
have distinct supports whose union has size four. In particular they
are neither equal nor inverse, and have a common fixed point.
Step <1>2 applies to them and gives
$$
|\langle x,z\rangle|=12,\qquad \langle x,z\rangle\leq H,
\qquad 12\mid |H|.
$$
Step <1>1 also makes $H$ transitive on five points, so $5\mid |H|$.
It follows that $60\mid |H|$. Both original generators are even,
so $H\subseteq A_5$, whose order is $5!/2=60$.
Thus $H=A_5$.
:::
:::
