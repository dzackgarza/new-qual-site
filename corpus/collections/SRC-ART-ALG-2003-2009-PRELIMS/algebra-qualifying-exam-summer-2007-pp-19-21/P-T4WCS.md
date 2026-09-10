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
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared both parts and the generator exclusions with the retained Summer 2007 Groups 4 extraction, lines 766-770."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: "Checked the two support-intersection cases, eight distinct three-cycles in the four-point subgroup, and the five-point orbit-stabilizer argument."
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

::: solution
Write $H=\langle x,y\rangle$, and let $X$ and $Y$ be the supports of
$x$ and $y$, respectively. A $3$-cycle is even, since
$(a\,b\,c)=(a\,c)(a\,b)$, so $H\subseteq A_5$.

<1>1. The supports $X$ and $Y$ are distinct three-element sets.

::: proof
On any fixed three-element set there are exactly two $3$-cycles, and
they are inverses. Thus $X=Y$ would imply $x=y$ or $x=y^{-1}$,
both excluded. Since $|X|=|Y|=3$ and $|X\cup Y|\leq5$, their
intersection consequently has size either $1$ or $2$.
:::

<1>2. If $x$ and $y$ have a common fixed point, then $H\cong A_4$.

::: proof
<2>1. A common fixed point lies outside $X\cup Y$, so
$|X\cup Y|\leq4$. Step <1>1 now gives $|X\cap Y|=2$ and
$|X\cup Y|=4$. Relabeling the five points conjugates the subgroup
and therefore preserves its isomorphism type. We may label the two
shared points $1,2$, the point in $X\setminus Y$ by $3$, and the
point in $Y\setminus X$ by $4$. Replacing either generator by its
inverse leaves its generated subgroup unchanged. We may therefore
assume
$$
x=(1\,2\,3),\qquad y=(1\,2\,4).
$$

<2>2. The elements $x$, $y$, $xyx^{-1}$, and $x^2yx^{-2}$
have respective supports
$$
\{1,2,3\},\quad\{1,2,4\},\quad\{2,3,4\},\quad\{1,3,4\}.
$$
Here conjugation relabels a cycle:
$g(a\,b\,c)g^{-1}=(g(a)\,g(b)\,g(c))$, as follows by applying
both permutations to each point. These four cycles and their
inverses are eight distinct elements of $H$: different supports
distinguish the four pairs, and a $3$-cycle is not its own inverse.
Together with the identity they give $|H|\geq9$.

<2>3. Every element of $H$ fixes point $5$ and is even, so
$H$ is a subgroup of the alternating group on $\{1,2,3,4\}$.
That group has $4!/2=12$ elements: multiplication by a fixed
transposition bijects the even and odd permutations. Its cosets of
$H$ partition its $12$ elements into sets of size $|H|$, so
$|H|$ divides $12$. The only divisor of $12$ at least $9$ is $12$.
Hence $H$ is the entire alternating group on those four points,
which is isomorphic to $A_4$.
:::

<1>3. If $x$ and $y$ have no common fixed point, then $H=A_5$.

::: proof
<2>1. The hypothesis says $X\cup Y=\{1,2,3,4,5\}$, so
$|X\cap Y|=1$. Relabel the common point as $1$, the other points
of $X$ as $2,3$, and the other points of $Y$ as $4,5$. As in
step <1>2, inversion of generators allows us to assume
$$
x=(1\,2\,3),\qquad y=(1\,4\,5).
$$
The $H$-orbit of $1$ contains $1,2,3$ by applying powers of $x$,
and contains $1,4,5$ by applying powers of $y$. Thus $H$ is
transitive on the five points.

<2>2. The conjugate $z=yxy^{-1}=(4\,2\,3)$ belongs to $H$.
The two $3$-cycles $x,z$ have different supports and both fix $5$.
By step <1>2, the subgroup $K=\langle x,z\rangle$ has order $12$.
It lies in the point stabilizer $H_5=\{h\in H:h(5)=5\}$.

<2>3. The map from left cosets $H/H_5$ to the orbit of $5$,
$hH_5\mapsto h(5)$, is well-defined and bijective: two images
coincide exactly when the corresponding representatives differ by
an element of $H_5$. Transitivity therefore gives
$$
|H|=5|H_5|\geq5|K|=60.
$$
But $H\subseteq A_5$, whose order is $5!/2=60$ by the same
parity argument as above. It follows that $H=A_5$.
:::
:::
