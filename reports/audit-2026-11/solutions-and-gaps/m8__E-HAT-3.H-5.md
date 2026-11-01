---
card: E-HAT-3.H-5
kind: gap-repair
slice: "8 — Hatcher §3.H proof gaps"
source: "Hatcher, Algebraic Topology: definition of cohomology with compact supports and its direct-limit description (tmp/hat/AT.txt 12085–12095, 12102–12110, 12160–12175), Prop. 3H.5 (16732–16736), finite cellular cochains for $H_c^*$ (16756–16766), Prop. A.1 (25888–25914), Exercise 5 (16843–16849)"
gaps-closed:
  - "the transition maps of the directed system are not split injections as claimed, and the 'choose a distinguished descendant' argument does not define a map of reduced cohomology; repaired with a proved exhaustion, a proved surjectivity of the component map, a section respecting the reduction, and an explicit description of the limit as a direct sum."
  - "the claim that the ranks tend to infinity is asserted from 'the tree has infinitely many ends'; repaired by a sphere-counting argument using the leafless core of $X$."
review: draft
---

# E-HAT-3.H-5 — repair of the $g>1$ computation of $\varinjlim\widetilde H^0$

**Exercise** (Hatcher §3.H exercise 5, AT.txt 16843–16849): *If $X$ is a finite connected graph with
$\pi_1(X)$ free on $g>0$ generators, show that $H^n(X;\ZZ[\pi_1X])$ is zero unless $n=1$, when it is
$\ZZ$ for $g=1$ and the direct sum of a countably infinite number of $\ZZ$'s for $g>1$.*

**The answer of the card is right and is not changed:**
$H^n(X;\ZZ[\pi])=0$ for $n\neq1$, $H^1(X;\ZZ[\pi])\cong\ZZ$ for $g=1$, and $\cong\bigoplus_{\NN}\ZZ$
for $g>1$. The first step (Prop. 3H.5 giving $H^n(X;\ZZ[\pi])\cong H_c^n(\widetilde X)$), the
computation $H^1(\widetilde X,\widetilde X-T_i)\cong\widetilde H^0(\widetilde X-T_i)$ and the
$g=1$ case are correct. What fails is the $g>1$ paragraph.

**The gap.** The card asserts that the transition maps
$\widetilde H^0(\widetilde X-T_i)\to\widetilde H^0(\widetilde X-T_{i+1})$ are split injections because
"each old complementary component breaks into finitely many new components, and choosing one
distinguished descendant in each component gives a splitting". Three things are wrong with this.

* The maps can fail to be injective at all: if a component of $\widetilde X-T_i$ happens to be
  contained in $T_{i+1}$, its class is killed. Whether that happens depends on the exhaustion, which the
  card leaves unspecified.
* Even when no component dies, "choosing a distinguished descendant" defines a map on *sets of
  components*, and $\widetilde H^0$ is *reduced*: to induce a homomorphism of $\widetilde H^0$ the
  assignment must send the constant function to a constant function, i.e. the choice must be made in the
  reduced model (e.g. basepoint components chosen compatibly). Without that the "splitting" is a
  splitting of the unreduced $H^0$ only and does not exhibit
  $\widetilde H^0(\widetilde X-T_i)$ as a direct summand.
* Finally "the ranks $c_i-1$ tend to infinity because the tree has infinitely many ends" is not an
  argument; a countable direct limit of free abelian groups can be of finite or of infinite rank, and
  the infiniteness has to be shown from the hypothesis $g>1$.

---

## Repair 1 of 2 — the sentence about $c_i$ (card line 64)

OLD:
```
If $c_i$ is the number of components of $\widetilde X-T_i$, this is free abelian of rank $c_i-1$.
```

NEW:
```
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
```

## Repair 2 of 2 — the case $g>1$ (card lines 71–76)

OLD:
```
If $g>1$, the universal covering tree has branching. Choose the exhaustion so that each $T_{i+1}$ is obtained by adding a finite layer of adjacent edges. Then the maps
$$
\widetilde H^0(\widetilde X-T_i)\to
\widetilde H^0(\widetilde X-T_{i+1})
$$
are split injections: each old complementary component breaks into finitely many new components, and choosing one distinguished descendant in each component gives a splitting. The ranks $c_i-1$ tend to infinity because the tree has infinitely many ends and branching repeats indefinitely. Thus the direct limit is a free abelian group on a countably infinite set of generators.
```

NEW:
```
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
```

### Why this closes the gaps

* The exhaustion is specified and the two properties the argument needs are proved: every component of
  $\widetilde X-T_i$ is infinite, hence the component map $\psi_i$ is *surjective*, whence a section
  $\sigma_i$ exists at all. This is what "each old component breaks into finitely many new components"
  was meant to say, and it is now a statement about a named exhaustion rather than a hope.
* The reduction is handled: $s_i$ is defined on the quotient $H^0/\ZZ\cdot\mathbf1$, and the one line
  $(s_i\varphi_i)[f]=[f]$ verifies the left-inverse property, so $\varphi_i$ really is a split
  injection of *reduced* groups, and $F_i$ is a direct summand. The card's "distinguished descendant"
  is exactly $\sigma_i$; the extra requirement is that it be applied in the reduced model.
* Freeness of the limit is not inferred from torsion-freeness but exhibited: the limit is the direct
  sum of the complements $G_i=\ker s_i$.
* Infiniteness of the rank now follows from $g>1$: the leafless core $X_0$ of $X$ has a vertex of
  degree $\ge3$ and no vertex of degree $\le1$ because $\chi(X_0)=1-g<0$, so its universal cover has
  nondecreasing, unbounded sphere sizes, and distinct vertices on a sphere lie in distinct components of
  $\widetilde X-T_i$.
* No statement is weakened: the conclusion $\bigoplus_{\NN}\ZZ$ is the exercise's, and the $g=1$ case
  and the vanishing in degrees $\ne1$ are untouched.
