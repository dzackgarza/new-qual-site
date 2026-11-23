---
schema: qual/card@1
id: E-HAT-4.2-28
kind: problem
title: "$\\ZZ_p \\times \\ZZ_p$ cannot act freely on spheres"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: kimi
  date: 2026-11-23
  note: >-
    Issue #191. The previous CW-model repair still formed $Z=N\cup_\beta e^{n+1}$
    before replacing the arbitrary map $\beta$ by a cellular map. Theorem 4.8 is now
    applied to $\beta:S^n\to N$ itself, whose domain and codomain are CW complexes,
    to obtain $H:\beta\simeq\gamma$ with $\gamma$ cellular; only then is
    $Z=N\cup_\gamma e^{n+1}$ defined. The path $H(s_0,t)$ and the $0$-cell
    $y=\gamma(s_0)$ make the based generator statement explicit. The higher-cell
    induction likewise replaces every based representative by a cellular map rel
    $s_0$ before attachment, as in Example 4.16. No attachment along $\beta$ or
    along an arbitrary representative remains. The relative cellular computations
    are reduced by Propositions A.5 and 2.22 to absolute cellular homology of the
    quotient, where Theorem 2.35 applies. The universal coefficient arguments now use
    Theorem 3.2 with the relevant integral homology groups named, so every Ext term
    is visibly zero. The statement and all hypotheses are unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 28, printed p. 391, and
    the covering space theory of §1.3. The proof is correct and is sharper than the
    published one where it counts: a free action of Z_p x Z_p on S^n gives a covering
    S^n -> M with M a closed n-manifold and pi_1(M) = G; building a K(G,1) from M by one
    (n+1)-cell and then cells of dimension at least n+2 bounds dim H^{n+1}(K(G,1);F_p) by
    the number of (n+1)-cells, which is 1, while Kunneth on K(Z_p,1) x K(Z_p,1) gives
    dimension n+2 there. The card's claim that no retained set solves the exercise was
    false: Sam's does, at §4.2 Exercise 28, and is now cited. Statement unchanged.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 28; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 28 (AT.txt 19430-19435) and repaired. The statement
    quantifies over any sphere S^n and the proof opened "Suppose first n>1", then handled n=1, and
    never covered S^0; the case is now disposed of in one sentence (a free action of a group of order
    p^2 >= 4 on two points is impossible). Verified as correct and left unchanged: the K(Z_p x Z_p,1)
    construction with one (n+1)-cell, the bound dim H^{n+1}(K;Z_p) <= 1, the identification
    K(Z_p x Z_p,1) = K(Z_p,1) x K(Z_p,1), and the one-dimensional degree-d part of each factor's
    cohomology (Z_p[u] for p=2; Lambda(u) tensor Z_p[v] for odd p), which gives d+1 = n+2 > 1. The n=1
    case rests on "a finite free action on S^1 is cyclic"; that classical statement is not in AT.txt,
    though it follows from covering space theory, and the card records it as such rather than proving
    it.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Checked against Hatcher, Section 4.2 Exercise 28, printed
    p. 391, and re-read every step: the $n=0$ case by orbit size; $M=S^n/G$ as a closed manifold
    with $S^n$ its universal cover, giving $\pi_1=G$, $\pi_i=0$ for $1<i<n$ and $\pi_n=Z$; the single
    $(n+1)$-cell attached along a generator of $\pi_n$, which kills $\pi_n$ because that group is
    cyclic; cells of dimension $\ge n+2$ killing the rest by induction; the count that $C^{n+1}$
    with $F_p$ coefficients is one-dimensional, since $M$ is $n$-dimensional and only one cell of
    dimension $n+1$ is added, so $\dim H^{n+1} \le 1$; the identification of $K(G,1)$ with a product
    of two $K(Z_p,1)$'s; the known cohomology of $K(Z_p,1)$ with $F_p$ coefficients (one class per
    degree for both parities of $p$); and Kunneth over a field, giving $d+1$ in degree $d$ and hence
    $n+2 > 1$. The $n=1$ case keeps the earlier note that a finite free action on $S^1$ is cyclic is
    recorded rather than proved. Not claimed: any statement for a group other than $Z_p x Z_p$, or
    for free actions on other spaces.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Item 8 of the current #163 repair split. Restored $\pi_1=G$ after the first cell and
    corrected the higher induction: cells are attached along based maps $S^k$, with no
    finite-cell or countable-generation assumption. A generator of $\pi_n(M)\cong\ZZ$ also
    generates as a $\ZZ[G]$-module. Sam's §4.2 Exercise 28 assumes that the given action
    is smooth, which Hatcher does not, so his finite-triangulation argument is recorded as
    an additional-hypothesis route, not certified. The bound is instead proved from the
    one-cell pair sequence, Theorem 3.26(c), Theorem 4.37 and the field universal
    coefficient theorem. For $n=1$, Sam's quotient-one-manifold argument is used with the
    closed $[0,1]$ alternative removed; no rotation classification is invoked. The actual
    cohomology inputs are Theorems 3.15 and 3.19 and Example 3E.2, not §4.3.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Verification of the preceding event against the body, which that event anticipated but
    the body did not yet carry. The step `circle` still argued through the rotation
    classification of periodic homeomorphisms of the circle; it is now the quotient
    argument: $M=S^1/G$ is a closed connected $1$-manifold, hence a circle, so
    $\pi_1(M)\cong\ZZ$, and Proposition 1.39, the covering being normal, makes $G$ a
    quotient of $\ZZ$. The steps `factors` and `kunneth` named no numbered statement for
    the cohomology of a $K(\ZZ_p,1)$ or for the product formula; they now cite Theorem
    3.19, Example 3E.2 and Theorem 3.15, which are the inputs the preceding event names.
    The classification of compact connected $1$-manifolds has no numbered statement in
    Hatcher, and the step says so instead of resting on an unproved citation. Steps
    `zero`, `cover` (with `manifold` and `pi`), `kgl1` (with `killn` and `killhigher`),
    `bound`, `product`, `contradiction` and the closing step were re-read and are
    unchanged.
- event: solution-reviewed
  by: kimi
  date: 2026-11-23
  note: >-
    Residue repair for issue #163, for arbitrary closed compact $M$ with no smoothness
    or CW-structure hypothesis. Step `kgl1` now uses Corollary A.12 only in its printed
    form, choosing a homotopy equivalence $r:M\to N$ with $N$ a CW complex. The
    attaching class is transported as $r_*[\alpha]$, and cellular approximation is used
    only on the genuine CW complexes $N$, $Z=N\cup_\beta e^{n+1}$, and the later
    complexes. Step `bound` transports $H^{n+1}(M;\FF_p)=0$ by the natural isomorphism
    $r^*$, then computes both pair comparisons by relative cellular homology on
    $(Z,N)$ and $(K,Z)$ and the field universal coefficient theorem. Step `product`
    applies Proposition 4.30 only to the CW complex $K$ and the CW product. No claim
    that $M$ itself has a CW structure remains, so the dimension-four case is covered.
---

::: {.problem}
Show that the group $\ZZ_p \times \ZZ_p$ with $p$ prime cannot act freely on any sphere $S^n$, by filling in details of the following argument. Such an action would define a covering space $S^n \to M$ with $M$ a closed manifold. When $n > 1$, build a $K(\ZZ_p \times \ZZ_p, 1)$ from $M$ by attaching a single $(n + 1)$-cell and then cells of higher dimension. Deduce that $H^{n+1}(K(\ZZ_p \times \ZZ_p, 1); \ZZ_p)$ is $\ZZ_p$ or 0, a contradiction. (The case $n = 1$ is more elementary.)
:::

::: {.solution}
The retained published solution is **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 28**. Its skeleton is retained: a free action gives a covering $S^n\to M$ with $\pi_1(M)=G$; one $(n+1)$-cell kills a generator of $\pi_n(M)$; and the Künneth computation for $K(\ZZ_p,1)\times K(\ZZ_p,1)$ contradicts the resulting upper bound on $H^{n+1}(K(G,1);\FF_p)$. Sam's quotient argument for $n=1$ is also used: the only connected closed $1$-manifold is $S^1$, whose fundamental group is $\ZZ$. His inclusion of $[0,1]$ among the alternatives is not applicable because $M$ is closed. Sam additionally calls the given action smooth, although Hatcher states no smoothness hypothesis, so his finite-triangulation version of the cohomology bound is not certified; the bound below transports $M$ to a CW model by Corollary A.12 and uses singular pair cohomology on genuine CW pairs, without assuming a smooth structure, triangulation, or CW structure on $M$. The book's inputs are §4.2 Exercise 28, Propositions 1.26, 1.39, 2.22, 4.1, 4.30, A.1 and A.5, Corollaries 4.12, 4.25 and A.12, Theorems 2.35, 3.2, 3.15, 3.19, 3.26 and 4.8, and Examples 1B.5, 3E.2, 4.11 and 4.16.

::: pf

::: {.pf-step #zero}
For $n=0$ there is no free action: $G$ has order $p^2\ge4$ while $S^0$ has two points.

::: pf-proof
A free action of a group on a set has orbits of size $\cardinality{G}$, so $\cardinality{S^0}=2$ must be a multiple of $p^2\ge4$, which it is not.
:::

:::

::: {.pf-step #cover}
If $n>1$ and $G$ acts freely on $S^n$, then $S^n\to M=S^n/G$ is the universal covering of a closed $n$-manifold with $\pi_1(M)=G$, $\pi_i(M)=0$ for $1<i<n$ and $\pi_n(M)\cong\ZZ$.

:::: pf-proof

::: {.pf-step #manifold}
$M$ is a closed $n$-manifold and $S^n\to M$ is a covering with deck group $G$.

::: pf-proof
A free action of a finite group on a manifold is properly discontinuous, so the quotient map is a covering and $M$ is a manifold of the same dimension; $M$ is compact because $S^n$ is, and has no boundary because $S^n$ has none.
:::

:::

::: {.pf-step #pi}
$\pi_1(M)=G$ and $\pi_i(M)\cong\pi_i(S^n)$ for $i\ge2$.

::: pf-proof
$S^n$ is simply connected for $n\ge2$, so it is the universal cover of $M$ and the deck group is $\pi_1(M)$, identifying $\pi_1(M)=G$; the covering map induces isomorphisms $\pi_i(S^n)\to\pi_i(M)$ for $i\ge2$. Since $\pi_i(S^n)=0$ for $1<i<n$ and $\pi_n(S^n)=\ZZ$, this gives the three stated groups.
:::

:::

:::

:::

::: {.pf-step #kgl1}
There are a CW complex $N$ homotopy equivalent to $M$ and a cellular attaching map $\gamma:S^n\to N$ representing a generator of $\pi_n(N)$ such that attaching one $(n+1)$-cell along $\gamma$, then cells of dimension at least $n+2$, gives a CW complex $K$ that is a $K(G,1)$.

:::: pf-proof

::: {.pf-step #cw-model}
Corollary A.12 supplies a CW complex $N$ and a homotopy equivalence $r:M\to N$, with $\pi_1(N)\cong G$, $\pi_i(N)=0$ for $1<i<n$, and $\pi_n(N)\cong\ZZ$.

::: pf-proof
This uses only the homotopy type asserted by Corollary A.12, not a CW structure on $M$. Fix $m_0\in M$ and use $x_0=r(m_0)$ as the basepoint of $N$. A homotopy equivalence induces isomorphisms on all homotopy groups, so the stated groups follow from step [](#cover){.pf-ref}. If $\alpha:(S^n,s_0)\to(M,m_0)$ represents a generator of $\pi_n(M,m_0)$, then $\beta=r\circ\alpha:(S^n,s_0)\to(N,x_0)$ represents a generator of $\pi_n(N,x_0)$.
:::

:::

::: {.pf-step #cellular-attach}
Theorem 4.8 supplies a cellular map $\gamma:S^n\to N$ and a homotopy $H:\beta\simeq\gamma$. At the $0$-cell $y=\gamma(s_0)$, the class $[\gamma]$ generates $\pi_n(N,y)$, and $Z=N\cup_\gamma e^{n+1}$ is a CW complex.

::: pf-proof
Since $S^n$ and $N$ are CW complexes, Theorem 4.8 applies directly to $\beta$ and gives $H:S^n\times I\to N$ with $H_0=\beta$ and $H_1=\gamma$ cellular. Thus $\gamma(S^n)\subset N^n$, and $y=\gamma(s_0)$ is a $0$-cell. Let $\lambda(t)=H(s_0,t)$, a path from $x_0=\beta(s_0)$ to $y$. The free homotopy $H$ shows that the change-of-basepoint isomorphism determined by $\lambda$ carries $[\beta]\in\pi_n(N,x_0)$ to $[\gamma]\in\pi_n(N,y)$. Since $[\beta]$ generates the infinite cyclic group, so does $[\gamma]$. Only now, with the cellular map $\gamma$ already chosen, attach the $(n+1)$-cell along $\gamma$; the resulting $Z$ is a CW complex containing $N$ as a subcomplex.
:::

:::

::: {.pf-step #killn}
After the single $(n+1)$-cell is attached to $N$ along $\gamma$, the resulting CW complex $Z=N\cup_\gamma e^{n+1}$ has $\pi_1(Z,y)\cong G$ and $\pi_i(Z,y)=0$ for $2\le i\le n$.

::: pf-proof
The pair $(Z,N)$ is $n$-connected by Corollary 4.12, since its only relative cell has dimension $n+1$. Hence the inclusion $N\to Z$ induces an isomorphism on $\pi_i$ for $i<n$ and an epimorphism on $\pi_n$. The class $[\gamma]$ becomes zero because $\gamma$ extends over the disc $e^{n+1}$. Since $[\gamma]$ generates the infinite cyclic group $\pi_n(N,y)$ by step [](#cellular-attach){.pf-ref}, the whole of $\pi_n(Z,y)$ vanishes. Attaching a cell of dimension $n+1\ge3$ does not change $\pi_1$ by Proposition 1.26(b), and $\lambda$ identifies $\pi_1(N,y)$ with $\pi_1(N,x_0)\cong G$, so $\pi_1(Z,y)\cong G$.
:::

:::

::: {.pf-step #killhigher}
Cells of dimension at least $n+2$ kill the remaining homotopy groups one at a time, with every attaching map cellular before its cell is attached.

::: pf-proof
Inductively, suppose that at stage $k\ge n+1$ we have a connected CW complex $X_k$, based at its $0$-cell $y$, with $\pi_1=G$ and $\pi_i=0$ for $2\le i<k$. Choose based maps $a_j:(S^k,s_0)\to(X_k,y)$ representing every element of $\pi_k(X_k,y)$. Theorem 4.8 with $A=\{s_0\}$, equivalently the relative formulation in Example 4.11, replaces each $a_j$ by a cellular map $b_j$ through a homotopy fixing $s_0$. Only after these replacements, attach $(k+1)$-cells along the cellular maps $b_j$ to form $X_{k+1}$. Corollary 4.12 shows that the inclusion preserves $\pi_i$ for $i<k$, including $\pi_1=G$, and gives a surjection from the old $\pi_k$ to the new one. Every old class has been killed, so the new $\pi_k$ is zero.

Iterating over $k=n+1,n+2,\ldots$, starting with $X_{n+1}=Z$, attaches cells only of dimensions at least $n+2$. A map of a sphere or a homotopy has compact image, which lies in a finite stage by Proposition A.1, so the union $K$ has $\pi_1(K)\cong G$ and $\pi_i(K)=0$ for $i\ge2$. This is the construction in Example 4.16, which expressly uses cellular attaching maps; it requires neither finitely many cells nor a countability assertion about $\pi_k$. Since every stage is a CW complex, $K$ is a CW $K(G,1)$.
:::

:::

:::

:::

::: {.pf-step #bound}
$\dim_{\FF_p}H^{n+1}(K(G,1);\FF_p)\le1$.

::: pf-proof
Let $r:M\to N$ and $Z=N\cup_\gamma e^{n+1}$ be as in step [](#kgl1){.pf-ref}. Theorem 3.26(a)--(c) gives $H_{n+1}(M;\ZZ)=0$ and $H_n(M;\ZZ)\cong\ZZ$ or $0$. Thus both the Hom and Ext inputs in Theorem 3.2 with $G=\FF_p$ vanish in degree $n+1$, giving $H^{n+1}(M;\FF_p)=0$. Naturality of singular cohomology makes $r^*:H^{n+1}(N;\FF_p)\to H^{n+1}(M;\FF_p)$ an isomorphism, since $r$ is a homotopy equivalence; hence $H^{n+1}(N;\FF_p)=0$.

For a CW pair $(X,A)$, Propositions A.5 and 2.22 identify $H_*(X,A)$ with $\widetilde H_*(X/A)$, and Theorem 2.35 computes the latter by the cellular chain complex of $X/A$, whose positive-degree cells are those of $X-A$. All homology groups in the following relative computations are integral. Theorem 3.2 then gives the stated $\FF_p$-cohomology groups because the lower-degree Ext input is zero in each case.

The CW pair $(Z,N)$ has exactly one relative cell, of dimension $n+1$. Its relative cellular chain complex is therefore a single $\ZZ$ in degree $n+1$, so $H_{n+1}(Z,N)\cong\ZZ$ and $H_n(Z,N)=0$. Theorem 3.2 consequently gives $H^{n+1}(Z,N;\FF_p)\cong\FF_p$. The cohomology exact sequence of $(Z,N)$ consequently makes $H^{n+1}(Z;\FF_p)$ a quotient of $\FF_p$.

Every cell of $K$ not in $Z$ has dimension at least $n+2$, so the relative cellular chain complex $C_*(K,Z)$ vanishes in degrees at most $n+1$. Hence $H_{n+1}(K,Z)=H_n(K,Z)=0$, and Theorem 3.2 gives $H^{n+1}(K,Z;\FF_p)=0$. Exactness of the cohomology sequence of the CW pair $(K,Z)$ therefore makes restriction $H^{n+1}(K;\FF_p)\to H^{n+1}(Z;\FF_p)$ injective, and the target has dimension at most $1$. Thus both relative cohomology computations use genuine CW pairs, while the only comparison with $M$ is the natural isomorphism $r^*$ above; no CW structure on $M$ is needed.
:::

:::

::: {.pf-step #product}
$K(G,1)\simeq K(\ZZ_p,1)\times K(\ZZ_p,1)$.

::: pf-proof
Example 1B.5 shows that the product $K(\ZZ_p,1)\times K(\ZZ_p,1)$ is a $K(\ZZ_p\times\ZZ_p,1)$: its fundamental group is $G$ and its universal cover is the product of the two contractible universal covers. The constructed $K$ and this product are both CW complexes, so Proposition 4.30 applies and gives the stated homotopy equivalence with $K$. Naturality of singular cohomology then identifies $H^{n+1}(K;\FF_p)$ with the product's degree-$(n+1)$ cohomology computed in step [](#cohomology){.pf-ref}.
:::

:::

::: {.pf-step #cohomology}
Each factor has exactly one $\FF_p$ in every degree, so the product has $\dim_{\FF_p}H^{d}(K(G,1);\FF_p)=d+1$ in degree $d$.

:::: pf-proof

::: {.pf-step #factors}
$H^*(K(\ZZ_p,1);\FF_p)$ is $\FF_2[u]$ with $\gradeddegree{u}=1$ when $p=2$, and $\Lambda(u)\otimes\FF_p[v]$ with $\gradeddegree{u}=1$, $\gradeddegree{v}=2$ when $p$ is odd; in either case the degree-$e$ part is one-dimensional for every $e\ge0$.

::: pf-proof
These are the standard computations. For $p=2$, $K(\ZZ_2,1)=\RP^\infty$ and Theorem 3.19 gives $H^*(\RP^\infty;\FF_2)=\FF_2[u]$. For odd $p$, $K(\ZZ_p,1)=S^\infty/\ZZ_p$ is the infinite lens space, and Example 3E.2 gives $H^*=\Lambda(u)\otimes\FF_p[v]$ with $u$ of degree $1$ and $v$ the Bockstein of $u$ in degree $2$. For $p=2$ the monomials $u^e$ give exactly one class in degree $e$; for odd $p$ the classes $v^k$ and $uv^k$ give exactly one class in degrees $2k$ and $2k+1$ respectively.
:::

:::

::: {.pf-step #kunneth}
The degree-$d$ part of the tensor product of two such algebras has dimension $d+1$.

::: pf-proof
Both factors are free over $\FF_p$ in each degree with exactly one generator per degree, and the cohomology is of finite type, so Theorem 3.15, the Künneth theorem for the cohomology of a product, applies and gives an isomorphism $H^*(K\times K)\cong H^*(K)\otimes H^*(K)$ of graded vector spaces. The degree-$d$ part of the tensor product has a basis of the products of the single degree-$i$ generator of the first factor with the single degree-$d-i$ generator of the second, for $i=0,1,\dots,d$, hence dimension $d+1$.
:::

:::

:::

:::

::: {.pf-step #contradiction}
For $n>1$ the two bounds contradict each other.

::: pf-proof
Step [](#bound){.pf-ref} gives $\dim_{\FF_p}H^{n+1}(K(G,1);\FF_p)\le1$, and steps [](#product){.pf-ref} and [](#cohomology){.pf-ref} give $\dim_{\FF_p}H^{n+1}(K(G,1);\FF_p)=n+2$. Since $n>1$, $n+2\ge4>1$, a contradiction. So no free action exists for $n>1$.
:::

:::

::: {.pf-step #circle}
For $n=1$ there is no free action either.

::: pf-proof
Here $M=S^1/G$ is a compact connected $1$-manifold without boundary, so $M\cong S^1$ by the classification of compact connected $1$-manifolds, and $\pi_1(M)\cong\ZZ$. The quotient map $S^1\to M$ is a covering whose deck group is all of $G$, and $G$ acts transitively on each fibre, so the covering is normal and Proposition 1.39 identifies $G$ with $\pi_1(M)/p_*\pi_1(S^1)$, a quotient of the infinite cyclic group $\pi_1(M)$. Every quotient of $\ZZ$ is cyclic, while $\ZZ_p\times\ZZ_p$ is not cyclic for prime $p$, so no free action on $S^1$ exists. Sam's version of this step rests on the same classification, listing $[0,1]$ among the possibilities; that alternative cannot occur, $M$ being closed. The classification of compact connected $1$-manifolds is a classical topological input with no numbered statement in Hatcher, and it is used here as such.
:::

:::

::: {.pf-step}
$\ZZ_p\times\ZZ_p$ acts freely on no sphere.

::: pf-proof
Steps [](#zero){.pf-ref}, [](#contradiction){.pf-ref} and [](#circle){.pf-ref} cover $n=0$, $n>1$ and $n=1$:
$$
\boxed{\ZZ_p\times\ZZ_p\text{ acts freely on no sphere }S^n.}
$$
:::

:::

:::
:::
