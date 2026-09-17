---
schema: qual/card@1
id: P-AGH344REFINEMENTH1
kind: problem
title: Čech cohomology in the limit over coverings computes $H^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Refinements
  - Sheaf Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts and the quotient-complex hint with the retained Hartshorne Chapter III section 4 transcription. Checked refinement homotopies and the double-complex comparison against Stacks Project sections 20.15 and 20.11. The proof handles arbitrary covers, proves independence of index choices, and identifies the degree-one comparison on explicit cocycles.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
On an arbitrary topological space $X$ with an arbitrary abelian sheaf $\mcf$, Čech cohomology may not give the same result as the derived functor cohomology.
But here we show that for $H^1$, there is an isomorphism if one takes the limit over all coverings.

(a) Let $\mathfrak{U}=(U_i)_{i \in I}$ be an open covering of the topological space $X$.
A refinement of $\mathfrak{U}$ is a covering $\mathfrak{V}=(V_j)_{j \in J}$, together with a map $\lambda: J \to I$ of the index sets, such that for each $j \in J$, $V_j \subseteq U_{\lambda(j)}$.
If $\mathfrak{V}$ is a refinement of $\mathfrak{U}$, show that there is a natural induced map on Čech cohomology, for any abelian sheaf $\mcf$, and for each $i$,
$$
\lambda^i: \check{H}^i(\mathfrak{U}, \mcf) \to \check{H}^i(\mathfrak{V}, \mcf).
$$
The coverings of $X$ form a directed preorder under refinement; passing to mutual-refinement classes gives a partially ordered set.
Show that the induced map is independent of the chosen index map, so that we can consider the Čech cohomology in the limit
$$
\colim_{\mathfrak{U}} \check{H}^i(\mathfrak{U}, \mcf).
$$

(b) For any abelian sheaf $\mcf$ on $X$, show that the natural maps (4.4) for each covering
$$
\check{H}^i(\mathfrak{U}, \mcf) \to H^i(X, \mcf)
$$
are compatible with the refinement maps above.

(c) Now prove the following theorem.
Let $X$ be a topological space, $\mcf$ a sheaf of abelian groups.
Then the natural map
$$
\colim_{\mathfrak{U}} \check{H}^1(\mathfrak{U}, \mcf) \to H^1(X, \mcf)
$$
is an isomorphism.
:::

::: {.hint}
Embed $\mcf$ in a flasque sheaf $\mcg$, and let $\mcr=\mcg/\mcf$, so that we have an exact sequence $0 \to \mcf \to \mcg \to \mcr \to 0$.
Define a complex $D^\bullet(\mathfrak{U})$ by
$$
0 \to C^\bullet(\mathfrak{U}, \mcf) \to C^\bullet(\mathfrak{U}, \mcg) \to D^\bullet(\mathfrak{U}) \to 0.
$$
Then use the exact cohomology sequence of this sequence of complexes, and the natural map of complexes $D^\bullet(\mathfrak{U}) \to C^\bullet(\mathfrak{U}, \mcr)$, and see what happens under refinement.
:::

::: {.solution}
Use the [[D-PTIW0|alternating Čech complex]], with an order on each index set.
Write $U_{i_0\cdots i_p}=U_{i_0}\cap\cdots\cap U_{i_p}$.
Extend a cochain from increasing tuples to all tuples by the alternating rule, giving value zero on a tuple with repeated indices.
Its differential is
$$
(dc)_{i_0\cdots i_{p+1}}
=\sum_{a=0}^{p+1}(-1)^a c_{i_0\cdots\widehat{i_a}\cdots i_{p+1}}|_{U_{i_0\cdots i_{p+1}}}.
$$
All degrees considered are nonnegative.

<1>1. A refinement map $\lambda:J\to I$ induces a natural map of cochain complexes.

::: {.proof}
For $c\in C^p(\mathfrak U,\mcf)$, set
$$
(\lambda^*c)_{j_0\cdots j_p}
=c_{\lambda(j_0)\cdots\lambda(j_p)}|_{V_{j_0\cdots j_p}}
\qquad(j_0<\cdots<j_p).
$$
The restriction is defined because each $V_j$ lies in $U_{\lambda(j)}$.
The alternating convention covers unordered or repeated image indices.
In the displayed differential, deletion of an index commutes with applying $\lambda$ and restricting.
If image indices repeat, the terms deleting the repeated occurrences cancel with opposite signs.
Hence $d\lambda^*=\lambda^*d$.
This gives homomorphisms on cohomology in every degree, and the formula commutes with every morphism of coefficient sheaves.
Composition of two refinement maps gives composition of these cochain maps, by the same formula.
:::

<1>2. Two index maps for the same refinement induce the same map on cohomology.
The groups therefore form a directed system over covers ordered by refinement.

::: {.proof}
Let $\lambda,\mu:J\to I$ both describe the refinement.
For $p\ge1$, define $h:C^p(\mathfrak U,\mcf)\to C^{p-1}(\mathfrak V,\mcf)$ on increasing tuples by
$$
(hc)_{j_0\cdots j_{p-1}}
=\sum_{a=0}^{p-1}(-1)^a
c_{\lambda(j_0)\cdots\lambda(j_a)\mu(j_a)\cdots\mu(j_{p-1})}
|_{V_{j_0\cdots j_{p-1}}},
$$
and set $h=0$ on degree zero.
Every term is defined because the relevant intersection of the $V_j$ is contained in both possible cover members for each index.
Expanding the two alternating sums gives
$$
dh+hd=\mu^*-\lambda^*.
$$
Terms deleting an index away from the change from $\lambda$ to $\mu$ cancel in pairs; the terms at consecutive change positions telescope, leaving the all-$\mu$ term and the negative all-$\lambda$ term.
In degree zero the same identity reads $(hdc)_j=c_{\mu(j)}-c_{\lambda(j)}$.
Thus the two maps are chain homotopic and induce the same cohomology map; this is the [refinement homotopy](https://stacks.math.columbia.edu/tag/09UY).

Any two covers have a common refinement consisting of their pairwise intersections.
The identity cover map induces the identity on cohomology, and compositions agree by step <1>1.
Mutually refining covers consequently give canonically inverse maps, since each composite is a refinement map of a cover to itself and is homotopic to its identity map.
This proves that the directed preorder, or its mutual-refinement quotient, gives the asserted direct system.
Covers without repeated members suffice: deleting repetitions gives mutual refinements and hence the same groups in the system.
These covers form a set of families of open subsets of $X$.
This completes (a).
:::

<1>3. The comparison maps to derived-functor cohomology commute with refinement, proving (b).

::: {.proof}
Choose one injective resolution $\mcf\to I^\bullet$ on $X$.
For each cover use the first-quadrant double complex
$$
B_{\mathfrak U}^{p,q}=C^p(\mathfrak U,I^q),
$$
with total differential $d_{\mathrm{tot}}=d_{\mathrm{Cech}}+(-1)^p d_I$ on bidegree $(p,q)$.
There are natural maps
$$
C^\bullet(\mathfrak U,\mcf)\longrightarrow\operatorname{Tot}B_{\mathfrak U},
\qquad
\Gamma(X,I^\bullet)\longrightarrow\operatorname{Tot}B_{\mathfrak U}.
$$
The first is induced by $\mcf\hookrightarrow I^0$; the second is restriction of global sections into Čech degree zero.
Every $I^q$ is flasque and has zero positive-degree Čech cohomology on any open cover [@Har10a, Proposition III.4.3].
The rows, augmented by $\Gamma(X,I^q)$, are therefore exact.
The horizontal-first filtration of this first-quadrant double complex shows that the second map is a quasi-isomorphism: its only horizontal cohomology is the global-section complex in horizontal degree zero.
The comparison map on cohomology is the first map followed by the inverse of this quasi-isomorphism on cohomology [@Har10a, Lemma III.4.4].
This is the [double-complex construction of the comparison map](https://stacks.math.columbia.edu/tag/01EO).

Apply the cochain map of step <1>1 in every row.
It commutes with $d_I$ by naturality and therefore gives a map of the double complexes and their total complexes.
It commutes with the map from $C^\bullet(\mathfrak U,\mcf)$ and with the augmented map from $\Gamma(X,I^\bullet)$, on which refinement acts as the identity.
Passing to cohomology and inverting the two augmented quasi-isomorphisms proves the required compatibility in every degree.
:::

<1>4. For any fixed cover, the comparison $\check H^1(\mathfrak U,\mcf)\to H^1(X,\mcf)$ is injective.

::: {.proof}
Put $G=I^0$ and $R=G/\mcf$.
This is the flasque extension in the hint, with $G$ in fact injective.
Its long exact sequence gives
$$
H^1(X,\mcf)\cong\Gamma(X,R)/\im\Gamma(X,G).
$$
For the complex $D^\bullet=C^\bullet(\mathfrak U,G)/C^\bullet(\mathfrak U,\mcf)$ in the hint, its natural map into $C^\bullet(\mathfrak U,R)$ is injective in every degree.
Its degree-zero cocycles correspond exactly to the global sections of $R$ that have lifts to $G$ on every $U_i$.
Indeed, representatives $b_i\in G(U_i)$ define a cycle in $D^0$ exactly when their differences lie in $\mcf$ on overlaps, equivalently when their images in $R$ glue.
Two such families represent the same element of $D^0$ exactly when their differences on each $U_i$ lie in $\mcf(U_i)$.

The long exact sequence of the quotient complex, and $\check H^1(\mathfrak U,G)=0$, identify $\check H^1(\mathfrak U,\mcf)$ with $H^0(D^\bullet)/\im\Gamma(X,G)$.
Fix the sign of this identification by sending the images of $b_i$ to the cocycle
$$
c_{ij}=b_i-b_j\in\mcf(U_i\cap U_j).
$$
Under the comparison of step <1>3 this cocycle maps to the connecting class of the glued section $r\in\Gamma(X,R)$.
To verify the sign and this assertion, the sections $d_Ib_i$ agree on overlaps and give the global degree-one cocycle $z$ representing that connecting class.
In the total complex one has $d_{\mathrm{tot}}b=-c+z$, so $c$ and $z$ have the same cohomology class there.

Thus the comparison is the inclusion
$$
H^0(D^\bullet)/\im\Gamma(X,G)
\longrightarrow\Gamma(X,R)/\im\Gamma(X,G),
$$
which is injective because $H^0(D^\bullet)$ is a subgroup of $\Gamma(X,R)$ containing the indicated image.
This proves the assertion for arbitrary covers.
:::

<1>5. The all-cover comparison is surjective and hence is an isomorphism:
$$
\boxed{\varinjlim_{\mathfrak U}\check H^1(\mathfrak U,\mcf)
\xrightarrow{\cong}H^1(X,\mcf).}
$$

::: {.proof}
Every class on the right is represented by a section $r\in\Gamma(X,R)$, by step <1>4.
The sheaf surjection $G\to R$ gives local lifts of $r$ on some open cover $\mathfrak U$.
For these lifts $b_i$, the differences $b_i-b_j$ give a Čech cocycle whose comparison class is the given class, again by step <1>4.
Thus the induced map from the direct limit is surjective.

If a class in the direct limit maps to zero, represent it on one cover.
The fixed-cover comparison is injective by step <1>4, so that representative is already zero on its cover and therefore zero in the direct limit.
This gives injectivity.
The limit map is defined and natural by steps <1>1--<1>3, completing (c).
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), step <1>3 proves (b), and steps <1>4--<1>5 prove (c).
:::
:::

::: {.remark title="Refinement is initially a preorder"}
For a nonempty space, the indexed covers $(X)$ and $(X,X)$ are distinct and refine each other.
Thus refinement is not literally antisymmetric on indexed covers.
Step <1>2 proves the independence and composition properties that allow the directed-limit notation, either on the preorder or on its mutual-refinement classes.
:::
