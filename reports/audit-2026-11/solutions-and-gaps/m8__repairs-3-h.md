CARD: corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-2.md
BOOK: Hatcher §3.H
OLD: |
::: pf-step
By Poincaré Duality for manifolds with local coefficients, for any closed $n$-manifold:
$$
H_k(M; \mathcal{L}) \cong H^{n-k}(M; \ZZ).
$$
For $n = 2$, this gives $H_k(M; \mathcal{L}) \cong H^{2-k}(M; \ZZ)$.
:::
|
NEW: |
::: pf-step
Duality must be applied to the *orientation* system, not to an arbitrary one. In the generality stated,
Poincaré duality with local coefficients is false: for $M=N_g$ and $\mathcal{L}=\ZZ$ the trivial
system, $H_2(M;\ZZ)=0$ (Theorem 3.26: $H_n(M;\ZZ)$ is $\ZZ$ for $M$ closed, connected and orientable and $0$ otherwise; Example 3H.3 uses exactly this), whereas $H^0(M;\ZZ)=\ZZ$ because $M$ is connected; so
"$H_k(M;\mathcal L)\cong H^{n-k}(M;\ZZ)$ for any closed $n$-manifold and any local system" fails
already for $k=n=2$. What is true, and all that is used, is the following.

Write $\widetilde{\ZZ}=M_\ZZ$ for the system with fibre $\ZZ$ on which a loop acts by $+1$ or $-1$
according to its orientation character $w_1\colon\pi_1M\to\{\pm1\}$; this is the $\mathcal L$ of the
present computation, and $M$ is closed, connected and nonorientable.

(i) *Fundamental class.* By Example 3H.3 (the exact sequence of the twofold orientable cover
$\widetilde M\to M$): $H_n(M;\widetilde{\ZZ})\approx H_n(\widetilde M)\approx\ZZ$; Hatcher identifies
the resulting class as a fundamental class for the nonorientable manifold $M$. In the paragraph
preceding Theorem 3H.6 he states the version of duality that the cap product with a fundamental class
gives for a bundle of rings $E$, under the assumption "that there exists a fundamental class
$[M]\in H_n(M;E)$ restricting to a generator of $H_n(M,M-\{x\};E)$ for all $x\in M$", and notes that
the class just constructed from $H_n(M;\widetilde{\ZZ})$ can be viewed as such a class — the *pure
imaginary fundamental class* $[M]\in H_n(M;E)$ for $E$ the bundle of rings $\ZZ[i]$ with conjugation
acting by $\omega=w_1$.

(ii) *The duality in the form used.* Cap product with that class is an isomorphism
$$
[M]\frown(-)\colon H^{k}(M;\ZZ)\;\xrightarrow{\ \approx\ }\;H_{n-k}(M;\widetilde{\ZZ})
$$
(Theorem 3H.6, first displayed isomorphism). Replacing $k$ by $n-j$ gives, for all $j$,
$$
H_j(M;\mathcal M_{\ZZ})=H_j(M;\widetilde{\ZZ})\;\cong\;H^{\,n-j}(M;\ZZ).
$$
For the surface $n=2$ this is exactly $H_j(M;\mathcal L)\cong H^{2-j}(M;\ZZ)$, $j=0,1,2$.

(For an *orientable* closed connected $n$-manifold the analogous statement with $\mathcal L=\ZZ$ is ordinary Poincaré duality, Theorem 3.30; the $M$ of this exercise is nonorientable, so Theorem 3H.6 is the applicable form.)
:::
|
WHY: accepted gap repair

CARD: corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-4.md
BOOK: Hatcher §3.H
OLD: |
We first show these lifts are proper. Let $K_X\subset\widetilde X$ and $K_Y\subset\widetilde Y$ be finite unions of lifted closed cells mapping onto $X$ and $Y$. Every compact subset of a universal cover of a finite CW complex meets only finitely many deck translates of such a fundamental finite subcomplex. By equivariance, the inverse image under $\widetilde f$ of a finite union of translates of $K_Y$ lies in a finite union of translates of $K_X$. Hence inverse images of compact sets are compact, so $\widetilde f$ is proper; likewise $\widetilde g$.

Choose homotopies
$$
gf\simeq\operatorname{id}_X,
\qquad
fg\simeq\operatorname{id}_Y.
$$
They lift to homotopies
$$
\widetilde g\widetilde f\simeq\operatorname{id}_{\widetilde X},
\qquad
\widetilde f\widetilde g\simeq\operatorname{id}_{\widetilde Y}
$$
after the endpoint lifts are chosen compatibly. These lifted homotopies are proper: they are equivariant lifts of homotopies on the compact finite CW quotients $X\times I$ and $Y\times I$, so the same finite-fundamental-domain argument applies uniformly in the parameter.

Thus $\widetilde f$ and $\widetilde g$ are proper maps and proper homotopy inverses.
|
NEW: |
We first record the properness criterion that the argument actually needs. Its hypothesis that $h$ be injective on $\pi_1$ cannot be dropped: the pinch $S^1\vee S^1\to S^1$ induces $\ZZ*\ZZ\twoheadrightarrow\ZZ$, and its lift to universal covers is a map from the $4$-valent tree onto $\RR$ whose fibre over a vertex is infinite, hence not proper.

**Lemma.** Let $W$ and $Z$ be finite CW complexes, $h\colon W\to Z$ a map with $h(w_0)=z_0$, and $\widetilde h\colon\widetilde W\to\widetilde Z$ a lift of $h$ to universal covers with $\widetilde h(\widetilde w_0)=\widetilde z_0$. If $h_*\colon\pi_1(W,w_0)\to\pi_1(Z,z_0)$ is injective, then $\widetilde h$ is proper.

*Proof.* Give $\widetilde W,\widetilde Z$ the CW structures lifting those of $W,Z$ (as in the proof of Proposition 3H.5). Identify $\pi_1(W,w_0)$ and $\pi_1(Z,z_0)$ with the respective deck groups by Proposition 1.39. Then
$$
\widetilde h(\alpha x)=h_*(\alpha)\,\widetilde h(x)\qquad\text{for all }\alpha\in\pi_1(W,w_0),\ x\in\widetilde W :
$$
both sides are lifts of $h\circ p$ and they agree at $x=\widetilde w_0$, so Proposition 1.34 applies. Fix one lift $\tilde e\subset\widetilde Z$ of each cell $e$ of $Z$. Because a nontrivial deck transformation fixes no point (Proposition 1.34 again; deck transformations are determined by their value at one point), every cell of $\widetilde Z$ is $\beta\tilde e$ for a *unique* $\beta\in\pi_1(Z,z_0)$ and a unique cell $e$; the same holds in $\widetilde W$.

Let $C\subset\widetilde Z$ be compact. By Proposition A.1 the set $C$ meets only finitely many cells, so $C$ lies in a finite subcomplex $c_1\cup\cdots\cup c_m$. Fix a cell $e$ of $W$, with lift $\tilde e$, and put $L_e:=\widetilde h(\tilde e)$, a compact subset of $\widetilde Z$. If a cell $\alpha\tilde e$ of $\widetilde W$ meets $\widetilde h^{-1}(C)$ then, by equivariance,
$$
\emptyset\neq\widetilde h(\alpha\tilde e)\cap C=h_*(\alpha)L_e\cap C .
$$
The set $S_e:=\{\beta\in\pi_1(Z,z_0):\beta L_e\cap C\neq\emptyset\}$ is finite: if $\beta L_e\cap C\neq\emptyset$ then $\beta L_e$ meets some $c_j$, so $L_e$ meets the cell $\beta^{-1}c_j$; by Proposition A.1 the compact set $L_e$ meets only finitely many cells $d_1,\dots,d_r$, and writing $d_k=\beta_k\tilde e_k$ and $c_j=\gamma_k\tilde e_k$ uniquely, $\beta^{-1}c_j=d_k$ forces $\beta=\gamma_k\beta_k^{-1}$. Hence only finitely many $\beta$ occur. Therefore the cells of $\widetilde W$ meeting $\widetilde h^{-1}(C)$ lie among the cells $\alpha\tilde e$ with $e$ a cell of $W$ (finitely many) and $\alpha\in h_*^{-1}(S_e)$, which is finite because $h_*$ is injective. So $\widetilde h^{-1}(C)$ meets only finitely many cells and is contained in a finite subcomplex; it is closed ($\widetilde h$ is continuous and $C$ is compact), hence compact. Thus $\widetilde h$ is proper. $\square$

A homotopy equivalence induces an isomorphism on $\pi_1$, so the lemma applies to $f$ and to $g$: $f_*$ is an isomorphism, and $g_*$ is injective because $(gf)_*$ is an isomorphism and $f_*$ is one. Hence the lifts $\widetilde f$ and $\widetilde g$ are proper. It applies just as well to a homotopy $H\colon X\times I\to X$ with $H_1=\operatorname{id}_X$, since then $H_*\colon\pi_1(X\times I)\to\pi_1(X)$ is an isomorphism and the lift $\widetilde H\colon\widetilde X\times I=\widetilde{X\times I}\to\widetilde X$ is proper; we use this below.

Choose homotopies $H\colon gf\simeq\operatorname{id}_X$ and $K\colon fg\simeq\operatorname{id}_Y$. By Proposition 1.30 (the homotopy lifting property), applied to the covering $\widetilde X\to X$, to the homotopy $\widetilde X\times I\to X$, $(x,t)\mapsto H(p(x),t)$, whose $t=0$ term $H_0\circ p=gf\circ p$ has the lift $\widetilde g\widetilde f$, the homotopy $H$ lifts to a homotopy (proper, by the lemma applied to $H\colon X\times I\to X$)
$$
\widetilde H\colon\widetilde X\times I\longrightarrow\widetilde X,
\qquad
\widetilde H_0=\widetilde g\widetilde f .
$$
For each $x\in\widetilde X$ the point $\widetilde H_1(x)$ lies over $x$, and a deck transformation is determined by its value at one point (Proposition 1.34), so there is a single $\gamma\in\pi_1(X,x_0)$ — identified with the deck group of $\widetilde X$ by Proposition 1.39 — such that
$$
\widetilde H_1=\gamma .
$$
So $H$ lifts to a proper homotopy $\widetilde g\widetilde f\simeq_p\gamma$, and *not* in general to one ending at $\operatorname{id}_{\widetilde X}$. This is the point the original step glossed over; the deck transformation is absorbed by changing the lift of $g$. Set
$$
\widetilde G:=\gamma^{-1}\widetilde g .
$$
Since $\gamma^{-1}$ is a deck transformation of $\widetilde X$, the map $\widetilde G$ is again a lift of $g$, hence proper by the lemma; and $\gamma^{-1}\widetilde H$ is a proper homotopy (a proper homotopy followed by the homeomorphism $\gamma^{-1}$), giving
$$
\widetilde G\widetilde f=\gamma^{-1}\widetilde g\widetilde f\ \simeq_p\ \gamma^{-1}\gamma=\operatorname{id}_{\widetilde X}.
$$
In the same way $K$ lifts to a proper homotopy $\widetilde f\widetilde g\simeq_p\delta$ with $\delta\in\pi_1(Y,y_0)$. By equivariance of $\widetilde f$ and $f_*(\gamma^{-1})=f_*(\gamma)^{-1}$,
$$
\widetilde f\widetilde G=\widetilde f\gamma^{-1}\widetilde g=f_*(\gamma)^{-1}\widetilde f\widetilde g\ \simeq_p\ f_*(\gamma)^{-1}\delta=:\varepsilon\in\pi_1(Y,y_0),
$$
a proper homotopy because $f_*(\gamma)^{-1}$ is a homeomorphism of $\widetilde Y$. Thus $\widetilde f$ has the left proper homotopy inverse $\widetilde G$ and the right proper homotopy inverse $\widetilde G\varepsilon^{-1}$:
$$
\widetilde G\widetilde f\simeq_p\operatorname{id}_{\widetilde X},
\qquad
\widetilde f\,(\widetilde G\varepsilon^{-1})\simeq_p\varepsilon\varepsilon^{-1}=\operatorname{id}_{\widetilde Y}.
$$
(In the homotopy category of spaces and proper maps, $AL\simeq1$ and $AR\simeq1$ imply $AL\simeq AL(AR)=A(LA)R\simeq A\cdot1\cdot R=AR\simeq1$; take $A=\widetilde f$, $L=\widetilde G$, $R=\widetilde G\varepsilon^{-1}$.) Hence
$$
\widetilde f\widetilde G\simeq_p\operatorname{id}_{\widetilde Y}
\qquad\text{as well,}
$$
so $\widetilde G$ is a two-sided proper homotopy inverse of $\widetilde f$. Therefore $\widetilde f$ and $\widetilde G$ are proper maps and proper homotopy inverses.
|
WHY: accepted gap repair

CARD: corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-5.md
BOOK: Hatcher §3.H
OLD: |
If $c_i$ is the number of components of $\widetilde X-T_i$, this is free abelian of rank $c_i-1$.
|
NEW: |
If $c_i$ is the number of components of $\widetilde X-T_i$, this is free abelian of rank $c_i-1$. Two
points are used below and are recorded here.

First, $c_i<\infty$: only finitely many edges of $\widetilde X$ have exactly one endpoint in the finite
subtree $T_i$ (finiteness of $T_i$ and local finiteness of $\widetilde X$); every component $C$ of
$\widetilde X-T_i$ contains such an edge, because $\widetilde X$ is connected so the closure of $C$
meets $T_i$; and distinct components contain distinct such edges, since an edge with one endpoint in
$T_i$ and the other outside $T_i$ has its open part in exactly one component.

Second, the isomorphism of the preceding step identifies $\widetilde H^0(\widetilde X-T_i)$ with
$H^0(\widetilde X-T_i)/\ZZ\cdot\mathbf 1$: the exact sequence of the pair in degree $1$ is
$$
H^0(\widetilde X)=\ZZ\ \xrightarrow{\ \text{image}=\text{constants}\ }\ H^0(\widetilde X-T_i)
\ \longrightarrow\ H^1(\widetilde X,\widetilde X-T_i)\ \longrightarrow\ H^1(\widetilde X)=0,
$$
because $\widetilde X$ is connected, so the connecting map has cokernel
$H^0(\widetilde X-T_i)/\ZZ\cdot\mathbf 1$, which is free of rank $c_i-1$.
|
WHY: accepted gap repair

CARD: corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-5.md
BOOK: Hatcher §3.H
OLD: |
If $g>1$, the universal covering tree has branching. Choose the exhaustion so that each $T_{i+1}$ is obtained by adding a finite layer of adjacent edges. Then the maps
$$
\widetilde H^0(\widetilde X-T_i)\to
\widetilde H^0(\widetilde X-T_{i+1})
$$
are split injections: each old complementary component breaks into finitely many new components, and choosing one distinguished descendant in each component gives a splitting. The ranks $c_i-1$ tend to infinity because the tree has infinitely many ends and branching repeats indefinitely. Thus the direct limit is a free abelian group on a countably infinite set of generators.
|
NEW: |
If $g>1$ the universal covering tree has branching, and the argument needs care. The transition maps of the directed system are
$$
\varphi_i\colon\widetilde H^0(\widetilde X-T_i)\longrightarrow\widetilde H^0(\widetilde X-T_{i+1}),
\qquad
\varphi_i[f]=[f\circ\psi_i],
$$
where $\psi_i\colon\pi_0(\widetilde X-T_{i+1})\to\pi_0(\widetilde X-T_i)$ sends a component of $\widetilde X-T_{i+1}$ to the component of $\widetilde X-T_i$ containing it; this is the map on complements induced by the inclusion of pairs $(\widetilde X,\widetilde X-T_{i+1})\subseteq(\widetilde X,\widetilde X-T_i)$, transported through the isomorphisms of the preceding step, by naturality of the connecting homomorphism. These maps are *not* automatically injective — a component of $\widetilde X-T_i$ lying inside $T_{i+1}$ has its class killed — and "choosing a descendant for each component" does not by itself split $\varphi_i$, since $\widetilde H^0$ is reduced: the induced map must carry constants to constants.

(a) *Choice of exhaustion.* Let $B_i$ be the ball of radius $i$ about a base vertex $v_0$ and set
$$
T_i:=B_i\ \cup\ \bigl(\text{all finite components of }\widetilde X-B_i\bigr).
$$
This is a finite subtree: there are only finitely many components of $\widetilde X-B_i$, one for each vertex at distance $i+1$ of the locally finite tree $\widetilde X$, and the finite ones are finite. Also $T_i\subset T_{i+1}$ (a vertex of a finite component of $\widetilde X-B_i$ lies either in $B_{i+1}$ or in a finite component of $\widetilde X-B_{i+1}$ contained in it), $\bigcup_iT_i=\widetilde X$, and $T_i$ contains every vertex at distance $\le i$ from $v_0$. Because a finite component of $\widetilde X-B_i$ is entirely contained in $T_i$, the components of $\widetilde X-T_i$ are exactly the *infinite* components of $\widetilde X-B_i$; in particular every component of $\widetilde X-T_i$ is infinite. It follows that every component of $\widetilde X-T_i$ contains a component of $\widetilde X-T_{i+1}$: it has vertices of arbitrarily large distance from $v_0$, hence a vertex outside the finite set $T_{i+1}$, and the component of $\widetilde X-T_{i+1}$ through that vertex lies inside it. So $\psi_i$ is surjective, and we may choose a section
$$
\sigma_i\colon\pi_0(\widetilde X-T_i)\to\pi_0(\widetilde X-T_{i+1}),
\qquad
\psi_i\sigma_i=\operatorname{id}.
$$
The $T_i$ are cofinal among compact subsets of $\widetilde X$: every compact set lies in a finite subcomplex by Proposition A.1, and a subcomplex lies in $T_i$ as soon as its vertices do, since $T_i$ contains every edge whose two endpoints lie in it; so Hatcher's description of $H_c^*$ as the direct limit over compact sets applies to this sequence.

(b) *The splitting.* Realise the reduced group as $\widetilde H^0(Y)=H^0(Y)/\ZZ\cdot\mathbf 1$, the quotient by constant functions, and define
$$
s_i\colon\widetilde H^0(\widetilde X-T_{i+1})\to\widetilde H^0(\widetilde X-T_i),
\qquad
s_i[g]=[g\circ\sigma_i].
$$
This is a well-defined homomorphism of reduced groups: $g$ and $g+\text{constant}$ give the same class, and a constant function pulls back to a constant function, so constants go to constants. Moreover
$$
(s_i\varphi_i)[f]=[\,f\circ\psi_i\circ\sigma_i\,]=[f]
\qquad\text{for all }[f]\in\widetilde H^0(\widetilde X-T_i),
$$
so $\varphi_i$ is a split injection and $\widetilde H^0(\widetilde X-T_i)\cong\ZZ^{c_i-1}$ is a direct summand of $\widetilde H^0(\widetilde X-T_{i+1})$. (Equivalently, if one uses the model $\widetilde H^0(Y)=\{f:f(c^0)=0\}$ for a chosen component $c^0$, one must choose the components $c^0_i$ and the section $\sigma_i$ compatibly, $\psi_i(c^0_{i+1})=c^0_i$ and $\sigma_i(c^0_i)=c^0_{i+1}$; the quotient model avoids that bookkeeping.)

(c) *The limit is free.* Put $F_i:=\widetilde H^0(\widetilde X-T_i)$. Since $s_i$ is a left inverse of $\varphi_i$,
$$
F_{i+1}=\varphi_i(F_i)\oplus G_i,
\qquad
G_i:=\ker s_i ,
$$
and $G_i$ is free, being a subgroup of the free abelian group $F_{i+1}$. Hence
$$
\varinjlim_iF_i=\bigcup_i\varphi_i(F_i)=F_1\oplus\bigoplus_{i\ge1}G_i ,
$$
a countable direct sum of finitely generated free abelian groups — in particular a free abelian group, not merely a torsion-free one, with a basis obtained by taking the union of a basis of $F_1$ with bases of the direct summands $G_i$. It is countably generated because $\widetilde X$, the universal cover of a finite graph, has countably many cells, so $F_i\cong\ZZ^{c_i-1}$ is finitely generated for each $i$.

(d) *The rank is infinite.* Let $\nu_i$ be the number of vertices of $\widetilde X$ at distance $i+1$ from $v_0$; we may take $v_0$ to be a lift of a vertex of $X_0$, since nothing in (a)–(c) depends on which base vertex is used. Distinct such vertices lie in distinct components of $\widetilde X-T_i$: the path joining two of them passes through the vertex at which the two geodesics from $v_0$ separate, which is at distance $\le i$, hence lies in $T_i$. Therefore $c_i\ge\nu_i$. To bound $\nu_i$ from below, delete vertices of degree $1$ from the finite graph $X$ one at a time (deleting a leaf and its edge is a deformation retraction, so this changes neither $\pi_1$ nor $\chi$); the result is a connected subgraph $X_0\subset X$ with no vertex of degree $\le1$, with $\pi_1(X_0)\cong\pi_1(X)=F_g$, and with $\chi(X_0)=1-g<0$, so $\sum_{v\in X_0}(2-\deg v)=2\chi(X_0)=2-2g<0$ and $X_0$ has a vertex of degree $\ge3$. The preimage $\widetilde X_0\subset\widetilde X$ is connected, because $\pi_1(X_0)\to\pi_1(X)$ is onto, and is the universal cover of $X_0$; so $\widetilde X_0$ is a locally finite tree all of whose vertex degrees are $\ge2$ and which has a vertex of degree $\ge3$. A connected subgraph of a tree is geodesically convex (the unique path between two of its vertices lies in it), so the sphere sizes $\nu^0_i$ of $\widetilde X_0$ about $v_0$ satisfy $\nu^0_i\le\nu_i$. For these,
$$
\nu^0_{i+1}=\sum_{w:\,d(w)=i}\bigl(\deg_{\widetilde X_0}w-1\bigr)\ \ge\ \nu^0_i ,
$$
since each vertex at distance $i\ge1$ has exactly one neighbour at distance $i-1$ and, its degree being $\ge2$, at least one at distance $i+1$. And $\nu^0_i$ is not eventually constant: $\nu^0_{i+1}=\nu^0_i$ forces every vertex at distance $i$ to have degree exactly $2$, whereas $\pi_1(X_0)$ acts freely and cocompactly on $\widetilde X_0$, so the orbit of a vertex of degree $\ge3$ is infinite and meets spheres of arbitrarily large radius. Hence $\nu^0_i\to\infty$, so $c_i\to\infty$ and
$$
\operatorname{rank}H_c^1(\widetilde X)\ \ge\ \operatorname{rank}\widetilde H^0(\widetilde X-T_i)=c_i-1\ \longrightarrow\ \infty .
$$
A countably generated free abelian group of infinite rank is $\bigoplus_{\NN}\ZZ$, which is the case $g>1$.
|
WHY: accepted gap repair

