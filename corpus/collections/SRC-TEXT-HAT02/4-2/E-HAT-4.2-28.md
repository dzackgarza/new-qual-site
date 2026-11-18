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
---

::: {.problem}
Show that the group $\ZZ_p \times \ZZ_p$ with $p$ prime cannot act freely on any sphere $S^n$, by filling in details of the following argument. Such an action would define a covering space $S^n \to M$ with $M$ a closed manifold. When $n > 1$, build a $K(\ZZ_p \times \ZZ_p, 1)$ from $M$ by attaching a single $(n + 1)$-cell and then cells of higher dimension. Deduce that $H^{n+1}(K(\ZZ_p \times \ZZ_p, 1); \ZZ_p)$ is $\ZZ_p$ or 0, a contradiction. (The case $n = 1$ is more elementary.)
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.2 Exercise 28. It is checked against Hatcher, Algebraic Topology, Section 4.2 Exercise 28, printed p. 391, against the covering space theory of Section 1.3, and against the cohomology of Eilenberg--MacLane spaces in Section 4.3.

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
Attaching one $(n+1)$-cell along a map representing a generator of $\pi_n(M)$, then cells of dimension at least $n+2$, gives a $K(G,1)$.

:::: pf-proof

::: {.pf-step #killn}
After the single $(n+1)$-cell is attached, $\pi_i=0$ for $1\le i\le n$ and $\pi_1=G$.

::: pf-proof
Let $Z=M\cup_\alpha e^{n+1}$ with $\alpha:S^n\to M$ a representative of a generator of $\pi_n(M)\cong\ZZ$. The inclusion $M\to Z$ induces an isomorphism on $\pi_i$ for $i<n$ and, since $n\ge2$, an epimorphism on $\pi_n$; the class $[\alpha]$ becomes zero because $\alpha$ extends over the disc $e^{n+1}$, and since $\pi_n(M)$ is generated by $[\alpha]$ as a $\ZZ[\pi_1]$-module, the whole of $\pi_n(Z)$ vanishes. Attaching a cell of dimension $n+1\ge3$ does not change $\pi_1$, so $\pi_1(Z)=G$.
:::

:::

::: {.pf-step #killhigher}
Cells of dimension at least $n+2$ kill the remaining homotopy groups one at a time.

::: pf-proof
Inductively, suppose $\pi_i=0$ for $2\le i<k$ with $k\ge n+1$; $\pi_k$ is a module over $\ZZ[G]$ and, the complex so far having finitely many cells in each dimension, it is countably generated, so choose generators $S^1\to X$ and attach $(k+1)$-cells along them. This kills those classes and leaves $\pi_i$ for $i<k$ unchanged, since attaching cells of dimension $k+1\ge n+2\ge3$ does not affect $\pi_1$ and the effect on $\pi_i$ for $2\le i\le k$ is only to kill the classes realized by the attaching maps. Running over $k=n+1,n+2,\dots$ gives $\pi_i=0$ for all $i\ge2$ and $\pi_1=G$.
:::

:::

:::

:::

::: {.pf-step #bound}
$\dim_{\FF_p}H^{n+1}(K(G,1);\FF_p)\le1$.

::: pf-proof
Give $M$ a finite CW structure, which exists because $M$ is a closed manifold; it has cells only in dimensions $\le n$. Attaching one $(n+1)$-cell adds exactly one cell in dimension $n+1$ and none in smaller dimensions, and the later cells have dimension at least $n+2$. So in the cellular cochain complex of $K(G,1)$ with $\FF_p$ coefficients the group $C^{n+1}$ is one-dimensional over $\FF_p$ and equals the cochain group contributed by that single cell. Since $H^{n+1}$ is a subquotient of $C^{n+1}$, it has $\FF_p$-dimension at most $1$.
:::

:::

::: {.pf-step #product}
$K(G,1)\simeq K(\ZZ_p,1)\times K(\ZZ_p,1)$.

::: pf-proof
The product $K(\ZZ_p,1)\times K(\ZZ_p,1)$ has fundamental group $\ZZ_p\times\ZZ_p=G$ and contractible universal cover, the product of the two contractible universal covers, so it is a $K(G,1)$. Two CW complexes that are both $K(G,1)$'s are homotopy equivalent, by Whitehead applied to a map inducing the identity on $\pi_1$ and hence an isomorphism on all homotopy groups.
:::

:::

::: {.pf-step #cohomology}
Each factor has exactly one $\FF_p$ in every degree, so the product has $\dim_{\FF_p}H^{d}(K(G,1);\FF_p)=d+1$ in degree $d$.

:::: pf-proof

::: {.pf-step #factors}
$H^*(K(\ZZ_p,1);\FF_p)$ is $\FF_2[u]$ with $\gradeddegree{u}=1$ when $p=2$, and $\Lambda(u)\otimes\FF_p[v]$ with $\gradeddegree{u}=1$, $\gradeddegree{v}=2$ when $p$ is odd; in either case the degree-$e$ part is one-dimensional for every $e\ge0$.

::: pf-proof
These are the standard computations: for $p=2$, $K(\ZZ_2,1)=\RP^\infty$ and $H^*(\RP^\infty;\FF_2)=\FF_2[u]$; for odd $p$, the lens space $S^\infty/\ZZ_p$ has $H^*=\Lambda(u)\otimes\FF_p[v]$ with $u$ of degree $1$ and $v$ the Bockstein of $u$ in degree $2$. For $p=2$ the monomials $u^e$ give exactly one class in degree $e$; for odd $p$ the classes $v^k$ and $uv^k$ give exactly one class in degrees $2k$ and $2k+1$ respectively.
:::

:::

::: {.pf-step #kunneth}
The degree-$d$ part of the tensor product of two such algebras has dimension $d+1$.

::: pf-proof
Both factors are free over $\FF_p$ in each degree with exactly one generator per degree, and the cohomology is of finite type, so the Künneth formula gives an isomorphism $H^*(K\times K)\cong H^*(K)\otimes H^*(K)$ of graded vector spaces. The degree-$d$ part of the tensor product has a basis of the products of the single degree-$i$ generator of the first factor with the single degree-$d-i$ generator of the second, for $i=0,1,\dots,d$, hence dimension $d+1$.
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
A finite group acting freely on $S^1$ is cyclic: an orientation-reversing homeomorphism of $S^1$ has a fixed point, so every element of the group acts preserving the orientation; a finite group of orientation-preserving homeomorphisms of $S^1$ acts by rotations after conjugation, and a group acting freely by rotations is cyclic. Since $\ZZ_p\times\ZZ_p$ is not cyclic for $p$ prime, it cannot act freely on $S^1$. This classical statement is recorded rather than proved from the covering theory of Section 1.3, which supplies it.
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
