---
schema: qual/card@1
id: P-AGH5411WEYLGROUPS
kind: problem
title: Weyl groups and the automorphisms of the configuration of 27 lines
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Picard Group
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.11, the retained Egbert note (which explicitly leaves
    the group theory undone), the cubic-surface Picard description, the 27
    line classes and incidence relations, and the quadratic transformation
    formulas. The proof below is therefore original rather than an integrated
    source solution. Part (a) bounds the A_n presentation by n! via n cosets
    of the preceding parabolic subgroup. For (b), the generators are the
    reflections in e_i-e_{i+1} and h-e_1-e_2-e_3; the 27-line incidence graph
    has exactly 72 unordered sixes of pairwise skew lines, and these
    reflections act transitively on them while the stabilizer of the standard
    six is S_6. Part (c) uses the standard faithful geometric representation
    of a Coxeter group, enumerates the 72 E_6 roots in K^perp, and identifies
    the stabilizer of 2h-sum e_i with the A_5 root subsystem of order 6!.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete three-part proof. Checked the A_n coset reduction,
    every 27-line incidence formula, the classification/count of all 72
    sixes and the four Cremona moves connecting their five S_6-orbits, and
    the 72-root enumeration in K^perp. Made the small intersecting-edge
    arguments and root-sign conjugation explicit. The final order calculation
    uses only the standard faithful geometric representation and root-
    stabilizer theorem for finite Coxeter/Weyl groups.
---

::: {.problem}
Given any diagram consisting of points and line segments joining some of them, we define an abstract group, given by generators and relations, as follows:

- Each point represents a generator $x_i$. The relations are
- $x_i^2=1$ for each $i$;
- $\left(x_i x_j\right)^2=1$ if $i$ and $j$ are not joined by a line segment, and
- $\left(x_i x_j\right)^3=1$ if $i$ and $j$ are joined by a line segment.

a. The Weyl group $\mathbf{A}_n$ is defined using the diagram of $n-1$ points, each joined to the next:

    \begin{tikzcd}
    	\circ & \circ & \cdots & \circ
    	\arrow[dash, from=1-1, to=1-2]
    	\arrow[dash, from=1-2, to=1-3]
    	\arrow[dash, from=1-3, to=1-4]
    \end{tikzcd}

    Show that it is isomorphic to the symmetric group $\Sigma_n$ as follows:
    - Map the generators of $\mathbf{A}_n$ to the elements $(12),(23), \ldots, (n-1,n)$ of $\Sigma_n$, to get a surjective homomorphism $\mathbf{A}_n \rightarrow \Sigma_n$.
    - Then estimate the number of elements of $\mathbf{A}_n$ to show in fact it is an isomorphism.

b. The Weyl group $\mathbf{E}_6$ is defined using the diagram

    \begin{tikzcd}
    	\circ & \circ & \circ & \circ & \circ \\
    	&& \circ
    	\arrow[dash, from=1-1, to=1-2]
    	\arrow[dash, from=1-2, to=1-3]
    	\arrow[dash, from=1-3, to=1-4]
    	\arrow[dash, from=1-4, to=1-5]
    	\arrow[dash, from=1-3, to=2-3]
    \end{tikzcd}

    Call the generators $x_1, \ldots, x_5$ and $y$. Show that one obtains a surjective homomorphism $\mathbf{E}_6 \rightarrow G$, the group of automorphisms of the configuration of 27 lines $(4.10.1)$, by sending $x_1, \ldots, x_5$ to the permutations $(12),(23), \ldots,(56)$ of the $E_i$, respectively, and $y$ to the element associated with the quadratic transformation based at $P_1, P_2, P_3$.

c. Estimate the number of elements in $\mathbf{E}_6$, and thus conclude that $\mathbf{E}_6 \cong G$.

Note: See Manin $[3, \S 25,26]$ for more about Weyl groups, root systems, and exceptional curves.
:::

::: {.solution}
We write the Coxeter generators of part (a) as
$$
s_1,\ldots,s_{n-1}.
$$
For the cubic surface in parts (b)--(c), write
$$
\Pic S
=
\ZZ h\oplus\bigoplus_{i=1}^6\ZZ e_i,
\qquad
h^2=1,
\qquad
e_i^2=-1,
$$
with all other pairings zero. Then
$$
K_S=-3h+\sum_{i=1}^6e_i.
$$
We use the standard names
$$
E_i=e_i,
\qquad
F_{ij}=h-e_i-e_j,
\qquad
G_i=2h-\sum_{j\ne i}e_j
$$
for the $6+15+6=27$ line classes [[FE-SRFCUBIC]].

<1>1. The assignment
$$
s_i\longmapsto(i,i+1)
$$
defines a surjective homomorphism
$$
\mathbf A_n\longrightarrow\Sigma_n.
$$

::: {.proof}
Each adjacent transposition is an involution. Two adjacent transpositions
with disjoint supports commute, so their product has order two, while
$$
((i,i+1)(i+1,i+2))^3=1.
$$
Thus the defining Coxeter relations are satisfied. The adjacent
transpositions generate the full symmetric group, so the homomorphism is
surjective.
:::

<1>2. Let
$$
W_n=\mathbf A_n,
\qquad
W_{n-1}=\langle s_1,\ldots,s_{n-2}\rangle.
$$
Every right coset of $W_{n-1}$ in $W_n$ is represented by one of
$$
1,
\quad
s_{n-1},
\quad
s_{n-1}s_{n-2},
\quad\ldots\quad,
s_{n-1}s_{n-2}\cdots s_1.
$$

::: {.proof}
Put
$$
r_j=s_{n-1}s_{n-2}\cdots s_j
\qquad(1\le j\le n-1),
$$
and put $r_n=1$. We show that the union
$$
\mathcal U=\bigcup_{j=1}^nW_{n-1}r_j
$$
is stable under right multiplication by every generator $s_i$.

If $i<j-1$, then $s_i$ commutes with every factor of $r_j$, so
$$
r_js_i=s_ir_j
$$
and the coset is unchanged. If $i=j-1$, then
$$
r_js_{j-1}=r_{j-1}.
$$
If $i=j$, the last factor cancels and
$$
r_js_j=r_{j+1}.
$$

Finally suppose $i>j$. Repeatedly using the braid relation
$$
s_is_{i-1}s_i=s_{i-1}s_is_{i-1}
$$
and commuting nonadjacent generators gives
$$
r_js_i=s_{i-1}r_j.
$$
Since $i-1\le n-2$, the left factor lies in $W_{n-1}$. Thus every
$W_{n-1}r_j$ is carried into one of the displayed cosets by right
multiplication by a generator. Because $1\in\mathcal U$, every word in the
generators lies in $\mathcal U$.
:::

<1>3. One has
$$
\boxed{|\mathbf A_n|\le n!}.
$$

::: {.proof}
Step <1>2 gives at most $n$ right cosets of $W_{n-1}$. Hence
$$
|W_n|\le n|W_{n-1}|.
$$
Starting with $|W_2|\le2$ and iterating gives
$$
|W_n|\le n!.
$$
:::

<1>4. Therefore
$$
\boxed{\mathbf A_n\cong\Sigma_n.}
$$

::: {.proof}
Step <1>1 gives a surjection onto the group of order $n!$, while step <1>3
gives at most $n!$ elements in the source. Thus the source has exactly
$n!$ elements and the surjection is injective. This proves part (a).
:::

We now turn to the cubic surface.

<1>5. Put
$$
\alpha_i=e_i-e_{i+1}
\qquad(1\le i\le5),
$$
and
$$
\beta=h-e_1-e_2-e_3.
$$
All six classes have square $-2$ and are orthogonal to $K_S$.

::: {.proof}
For each $i$,
$$
\alpha_i^2=e_i^2+e_{i+1}^2=-2,
$$
and
$$
K_S\cdot\alpha_i=0.
$$
Also
$$
\beta^2=1-1-1-1=-2
$$
and
$$
K_S\cdot\beta=-3+1+1+1=0.
$$
:::

<1>6. For a class $\gamma$ with $\gamma^2=-2$, define
$$
s_\gamma(D)=D+(D\cdot\gamma)\gamma.
$$
Then $s_{\alpha_i}$ interchanges $e_i,e_{i+1}$ and fixes the other standard
basis classes, while $s_\beta$ is the action on $\Pic S$ of the quadratic
transformation based at $P_1,P_2,P_3$.

::: {.proof}
For $\alpha_i=e_i-e_{i+1}$,
$$
e_i\cdot\alpha_i=-1,
\qquad
e_{i+1}\cdot\alpha_i=1,
$$
so
$$
s_{\alpha_i}(e_i)=e_{i+1},
\qquad
s_{\alpha_i}(e_{i+1})=e_i.
$$
Every other basis vector is orthogonal to $\alpha_i$.

For $\beta$, one finds
$$
s_\beta(h)=2h-e_1-e_2-e_3,
$$
and
$$
\begin{aligned}
s_\beta(e_1)&=h-e_2-e_3,\\
s_\beta(e_2)&=h-e_1-e_3,\\
s_\beta(e_3)&=h-e_1-e_2,
\end{aligned}
$$
while $e_4,e_5,e_6$ are fixed. These are exactly the pullback formulas for
the standard quadratic transformation centered at the first three points,
as in [[P-AGH542QUADTRANSFORM]].
:::

<1>7. The six reflections of step <1>6 satisfy the Coxeter relations of the
$E_6$ diagram, with $s_\beta$ attached to $s_{\alpha_3}$.

::: {.proof}
The only nonzero pairings between distinct simple roots are
$$
\alpha_i\cdot\alpha_{i+1}=1
\qquad(1\le i\le4)
$$
and
$$
\beta\cdot\alpha_3=1.
$$
All other distinct pairings are zero.

If two square-$-2$ roots are orthogonal, their reflections commute, so the
product has order two. If $\gamma^2=\delta^2=-2$ and
$$
\gamma\cdot\delta=1,
$$
then on the span of $\gamma,\delta$ the two reflections are represented in
that ordered basis by
$$
\begin{pmatrix}-1&1\\0&1\end{pmatrix},
\qquad
\begin{pmatrix}1&0\\1&-1\end{pmatrix},
$$
whose product has order three. Thus the defining $E_6$ Coxeter relations
hold.
:::

<1>8. Hence the assignments in part (b) define a homomorphism
$$
\Phi:\mathbf E_6\longrightarrow G.
$$

::: {.proof}
Every reflection in step <1>6 preserves the intersection form and fixes
$K_S$. It therefore preserves the set of classes satisfying
$$
L^2=-1,
\qquad
K_S\cdot L=-1,
$$
which is exactly the set of $27$ line classes [[FE-SRFCUBIC]]. Since it also
preserves pairwise intersection numbers, it preserves the incidence graph of
the $27$ lines. Thus the reflections define elements of $G$, and step <1>7
shows that the Coxeter presentation gives the asserted homomorphism.
:::

<1>9. The incidence relations between the three families of lines are:
$$
\begin{aligned}
E_i\cdot E_j&=0 &&(i\ne j),\\
E_i\cdot F_{jk}&=
\begin{cases}1&i\in\{j,k\},\\0&i\notin\{j,k\},\end{cases}\\
E_i\cdot G_j&=
\begin{cases}0&i=j,\\1&i\ne j,\end{cases}\\
F_{ij}\cdot F_{kl}&=1-|\{i,j\}\cap\{k,l\}|,\\
F_{ij}\cdot G_k&=
\begin{cases}1&k\in\{i,j\},\\0&k\notin\{i,j\},\end{cases}\\
G_i\cdot G_j&=0 &&(i\ne j).
\end{aligned}
$$

::: {.proof}
Substitute the divisor classes
$$
E_i=e_i,
\quad
F_{ij}=h-e_i-e_j,
\quad
G_i=2h-\sum_{r\ne i}e_r
$$
into the intersection form
$$
h^2=1,
\qquad
e_i^2=-1,
\qquad
h\cdot e_i=e_i\cdot e_j=0\quad(i\ne j).
$$
Each displayed formula follows immediately.
:::

Call an unordered set of six mutually skew lines a **six**.

<1>10. There are exactly
$$
\boxed{72}
$$
sixes in the configuration of $27$ lines.

::: {.proof}
We classify a six by the number of $E$-lines it contains, using step <1>9.

If it contains all six $E_i$, we obtain the standard six
$$
\{E_1,\ldots,E_6\}.
$$
If it contains at least two but fewer than six $E$-lines, no $G$-line can
occur, because a $G_j$ is skew to only the single $E_j$. Every accompanying
$F_{ab}$ must have both indices outside the chosen $E$-indices. Distinct
$F$-lines are mutually skew exactly when their two-element index sets meet.

For three chosen $E$-lines, the complementary index set has size three and
its three pairs form a mutually intersecting family; this gives one six for
each three-element subset, hence
$$
\binom63=20.
$$
For two, four, or five chosen $E$-lines, there are not enough pairwise
intersecting two-element subsets to complete a six. Indeed, on four vertices
a pairwise-intersecting family of edges has size at most three: if three
edges form a triangle, no fourth edge meets all three, while otherwise all
edges share one vertex. On two or one vertices the bound is immediate.

Now suppose there is exactly one $E_i$. The only possible $G$-line is
$G_i$. Without $G_i$, one would need five pairwise-intersecting edges of the
complete graph on the remaining five indices, but the largest such family
has size four. With $G_i$, one needs four such edges. A family of four
pairwise-intersecting edges on five vertices is necessarily a star: after
two edges $12,13$, any edge avoiding vertex $1$ must be $23$, and then no
fourth distinct edge can meet all three $12,13,23$. Thus a four-edge family
has a common vertex. There are five choices for its center. Hence this case
contributes
$$
6\cdot5=30
$$
sixes.

The same argument with $E$ and $G$ interchanged gives $20$ sixes containing
three $G$-lines and one six containing all six $G_i$. No other number of
$G$-lines can occur. Therefore the total is
$$
1+20+30+20+1=72.
$$
:::

<1>11. Under permutations of the six indices, the $72$ sixes fall into five
orbits represented by
$$
\begin{aligned}
\mathcal S_0&=\{E_1,E_2,E_3,E_4,E_5,E_6\},\\
\mathcal S_1&=\{F_{12},F_{13},F_{23},E_4,E_5,E_6\},\\
\mathcal S_2&=\{F_{12},F_{13},F_{14},F_{15},E_6,G_6\},\\
\mathcal S_3&=\{G_1,G_2,G_3,F_{45},F_{46},F_{56}\},\\
\mathcal S_4&=\{G_1,G_2,G_3,G_4,G_5,G_6\}.
\end{aligned}
$$

::: {.proof}
The five cases in step <1>10 are distinguished by the numbers of $E$- and
$G$-lines:
$$
(6,0),
\quad
(3,0),
\quad
(1,1),
\quad
(0,3),
\quad
(0,6).
$$
The symmetric group on the six indices is transitive on each combinatorial
choice occurring in the classification: on three-element subsets, and on
ordered pairs consisting of the index $i$ of the unique $E_i$ and the center
of the four-edge star among the other five indices. Thus the displayed five
sets are orbit representatives.
:::

<1>12. Let $s_{ijk}$ denote the conjugate of $s_\beta$ corresponding to the
quadratic transformation centered at $P_i,P_j,P_k$. Then
$$
\begin{aligned}
s_{123}(\mathcal S_0)&=\mathcal S_1,\\
s_{145}(\mathcal S_1)&=\mathcal S_2,\\
s_{456}(\mathcal S_1)&=\mathcal S_3,\\
s_{123}(\mathcal S_3)&=\mathcal S_4.
\end{aligned}
$$

::: {.proof}
The subgroup generated by $x_1,\ldots,x_5$ is the full permutation group on
the six indices by part (a), so every $s_{ijk}$ is a conjugate of $s_\beta$
and belongs to the image of $\Phi$.

For
$$
\beta_{ijk}=h-e_i-e_j-e_k,
$$
the reflection formula gives the following useful rules. It sends an
$E$-line indexed by one of $i,j,k$ to the $F$-line on the other two indices;
it fixes an $F_{ab}$ having exactly one index in $\{i,j,k\}$; and if neither
$a$ nor $b$ lies in that triple, it sends $F_{ab}$ to the $G$-line whose
index is the unique remaining sixth index. Applying these rules to the four
displayed representatives gives exactly the stated identities.
:::

<1>13. The image
$$
H=\operatorname{im}(\Phi)\subseteq G
$$
acts transitively on all $72$ sixes.

::: {.proof}
The index-permutation subgroup is transitive on each of the five orbit types
from step <1>11. Step <1>12 connects all five types to the standard type.
Hence every six lies in the $H$-orbit of $\mathcal S_0$.
:::

<1>14. The stabilizer in $G$ of the standard six
$$
\mathcal S_0=\{E_1,\ldots,E_6\}
$$
is exactly the symmetric group $\Sigma_6$ permuting its six members.

::: {.proof}
Every permutation of the $E_i$ is realized by the elements
$x_1,\ldots,x_5$, so $\Sigma_6$ is contained in the stabilizer.

Conversely, an automorphism of the incidence configuration preserving
$\mathcal S_0$ induces a permutation of its six lines. Once that permutation
is known, all other $21$ lines are determined by incidence with
$\mathcal S_0$: the line $F_{ij}$ is the unique line meeting exactly
$E_i,E_j$ among the six, while $G_i$ is the unique line meeting exactly the
five $E_j$ with $j\ne i$. Thus an element fixing every $E_i$ fixes all
$27$ lines. The stabilizer therefore embeds in $\Sigma_6$, and equality
follows.
:::

<1>15. The homomorphism
$$
\Phi:\mathbf E_6\longrightarrow G
$$
is surjective, and
$$
\boxed{|G|=72\cdot6!=51840.}
$$

::: {.proof}
By step <1>13, the subgroup $H=\operatorname{im}(\Phi)$ is transitive on
the $72$ sixes. It contains the full stabilizer $\Sigma_6$ of
$\mathcal S_0$. Hence orbit--stabilizer gives
$$
|H|\ge72\cdot6!=51840.
$$

On the other hand $G$ also acts on the $72$ sixes, and step <1>14 says that
the stabilizer of $\mathcal S_0$ in $G$ has order $6!$. Therefore
$$
|G|\le72\cdot6!=51840.
$$
Since
$$
H\subseteq G,
$$
both inequalities are equalities and
$$
H=G.
$$
This proves part (b).
:::

We finish by estimating the abstract Coxeter group itself.

<1>16. In the lattice
$$
K_S^\perp\subseteq\Pic S,
$$
the classes of square $-2$ are exactly the following $72$ roots:
$$
\begin{aligned}
&e_i-e_j &&(i\ne j),\\
&\pm(h-e_i-e_j-e_k) &&(i<j<k),\\
&\pm\left(2h-\sum_{i=1}^6e_i\right).
\end{aligned}
$$

::: {.proof}
Write a root as
$$
r=ah-\sum_{i=1}^6b_ie_i.
$$
The conditions
$$
K_S\cdot r=0,
\qquad
r^2=-2
$$
are
$$
\sum_i b_i=3a,
\qquad
\sum_i b_i^2=a^2+2.
$$
Cauchy--Schwarz gives
$$
9a^2
=
\left(\sum_i b_i\right)^2
\le
6\sum_i b_i^2
=
6a^2+12,
$$
so
$$
|a|\le2.
$$

If $a=0$, the equations become
$$
\sum b_i=0,
\qquad
\sum b_i^2=2,
$$
so exactly one $b_i$ is $1$, one is $-1$, and the rest are zero. This gives
$30$ roots $e_i-e_j$.

If $a=1$, then
$$
\sum_i b_i=\sum_i b_i^2=3.
$$
Since $m(m-1)\ge0$ for every integer $m$, equality of these sums forces
each $b_i$ to be $0$ or $1$; exactly three are $1$. This gives
$$
\binom63=20
$$
roots. The case $a=-1$ gives their negatives, for another $20$.

If $a=2$, the same argument gives
$$
\sum b_i=\sum b_i^2=6,
$$
so every $b_i=1$, giving one root; $a=-2$ gives its negative. Thus the total
number is
$$
30+20+20+1+1=72.
$$
:::

<1>17. The Weyl group acts transitively on these $72$ roots.

::: {.proof}
The subgroup generated by $s_{\alpha_1},\ldots,s_{\alpha_5}$ permutes the
indices, so it is transitive on the roots $e_i-e_j$ up to the evident change
of ordered pair.

Now
$$
s_\beta(e_3-e_4)
=
h-e_1-e_2-e_4,
$$
which is a root of the second type. Permuting indices reaches every positive
root of that type. If $\eta=w(\alpha_3)$ is any root already reached from a
simple root, then
$$
s_\eta=w s_{\alpha_3}w^{-1}
$$
belongs to the Weyl group and sends $\eta$ to $-\eta$. Hence all roots of
the second type, with both signs, lie in the same orbit.

Finally, for
$$
\gamma=h-e_4-e_5-e_6
$$
one has
$$
\gamma\cdot\beta=1,
$$
and therefore
$$
s_\beta(\gamma)
=
2h-\sum_{i=1}^6e_i.
$$
Thus the final pair of roots also belongs to the same orbit.
:::

<1>18. Let
$$
\rho=2h-\sum_{i=1}^6e_i.
$$
The roots orthogonal to $\rho$ are precisely
$$
e_i-e_j
\qquad(i\ne j),
$$
which form a root system of type $A_5$ with Weyl group $\Sigma_6$ of order
$720$.

::: {.proof}
Directly,
$$
\rho\cdot(e_i-e_j)=0.
$$
For a root
$$
h-e_i-e_j-e_k,
$$
the intersection with $\rho$ is
$$
2-3=-1,
$$
and $\rho^2=-2$, so neither of the other two root types is orthogonal to
$\rho$. Hence the orthogonal root subsystem consists exactly of the
$30$ differences $e_i-e_j$, with simple roots
$$
e_1-e_2,
e_2-e_3,
\ldots,
e_5-e_6.
$$
This is type $A_5$, whose Weyl group is $\Sigma_6$ by part (a).
:::

<1>19. The standard faithful geometric representation of a Coxeter group
gives
$$
\boxed{|\mathbf E_6|=72\cdot720=51840.}
$$

::: {.proof}
The geometric representation theorem for Coxeter groups identifies the
abstract group given by the Coxeter presentation with the reflection group
generated by the six simple-root reflections of step <1>7; in particular
this representation is faithful.

For a finite Weyl group, the stabilizer of a root is the Weyl group of the
root subsystem orthogonal to that root. By step <1>18, the stabilizer of
$\rho$ is therefore the type-$A_5$ Weyl group, of order $720$. Step <1>17
shows that the orbit of $\rho$ consists of all $72$ roots. Orbit--stabilizer
now gives
$$
|\mathbf E_6|
=
72\cdot720
=
51840.
$$
:::

<1>20. The map of part (b) is an isomorphism:
$$
\boxed{\mathbf E_6\cong G.}
$$

::: {.proof}
Step <1>15 gives a surjective homomorphism
$$
\mathbf E_6\twoheadrightarrow G
$$
and shows
$$
|G|=51840.
$$
Step <1>19 gives
$$
|\mathbf E_6|=51840.
$$
A surjection between finite groups of equal order is an isomorphism. This
proves part (c).
:::

<1>21. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove part (a), steps <1>5--<1>15 prove part (b), and
steps <1>16--<1>20 prove part (c).
:::
:::
