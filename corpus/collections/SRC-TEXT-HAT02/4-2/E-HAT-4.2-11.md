---
schema: qual/card@1
id: E-HAT-4.2-11
kind: problem
title: "$\\pi_2(X, X^1)$ and the kernel of $\\pi_1(X^1) \\to \\pi_1(X)$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 11; the stored statement matches. Also checked Hatcher errata for the corrected second half of this exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 11 (AT.txt 19367-19370) and correct as it stands. The
    sequence 0 -> pi_2(X) -> pi_2(X,X^1) -> K -> 1 is the pair sequence with pi_2(X^1) = 0, and a section
    exists because K is free by Nielsen-Schreier. Checked the conclusion that the split extension is a
    direct product: with pi_2(X) central (Hatcher Sec. 4.2 Exercise 27, a result of the same section) the
    multiplication map pi_2(X) x K -> pi_2(X,X^1), (a,k) -> a s(k), is a homomorphism and is bijective by
    the split exact sequence, so no abelianness of pi_2(X,X^1) has to be assumed. The RP^2 counterexample
    is right: pi_2'(X) = Z/2 from the (-1)-action, pi_2'(X,X^1) = H_2(X,X^1) = Z by the relative Hurewicz
    theorem in its coinvariant form, and Z/2 -> Z is zero. Not checked: nothing outside these exercises.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked each input: X^1 is a graph,
    so its homotopy vanishes above degree 1 (contractible universal cover); pi_1(X^1) -> pi_1(X)
    is onto because X has no 1-cells outside X^1, which also gives pi_1(X,X^1) = 0 and hence the
    surjectivity of the boundary; K = ker(pi_1(X^1) -> pi_1(X)) is free by Nielsen-Schreier; and a
    free basis lifts to a homomorphic section because a homomorphism out of a free group is free
    on its values on a basis. One correction to the prose: it invokes Exercise 27 (the image of
    pi_2(X) is central) to conclude the extension is a direct product, but pi_2 of a pair is
    abelian, so a split extension of abelian groups is already a direct product, and the step now
    says this and notes that centrality is then automatic. For RP^2 the action of Z/2 on pi_2 is
    by the antipodal deck transformation, of degree -1, so the coinvariants are Z/2, while the
    relative group is Z by relative Hurewicz; a homomorphism from a finite group to Z is zero.
    Statement unchanged; no retained solution set covers this exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.2 Exercise 11, Example 1B.1 and
    Theorem 4.37's neighbourhood. One defect repaired in the opening paragraph: it justified the direct
    product by "pi_2 of a pair is abelian", which is false. For X = T^2 with its standard structure,
    pi_2(X) = 0 and pi_2(X, X^1) = K = ker(F_2 -> Z^2), free of infinite rank and not abelian; the
    exercise's conclusion still holds there, because it is the splitting and not abelianness that gives
    it. The paragraph now says the sequence splits into a semidirect product, that the action of K is
    trivial because the action of pi_1(X^1) on pi_2(X, X^1) restricts to that on pi_2(X) through
    pi_2(X^1) = 0, and it records the torus as the case showing pi_2 of a pair need not be abelian. The
    steps are unchanged: pi_i(X^1) = 0 for i >= 2 and pi_1(X^1) -> pi_1(X) onto; the pair sequence gives
    the short exact sequence with kernel K; K is free as a subgroup of the free group pi_1(X^1); and the
    section exists because a homomorphism out of a free group is determined by arbitrary images of a free
    basis. The RP^2 case is right: pi_2'(RP^2) = Z/2 and pi_2'(RP^2, (RP^2)^1) = Z, so no injective
    homomorphism exists.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 11. One false step repaired: `abelian` claimed that
    $\pi_2(X,X^1)$ is abelian for every connected CW complex, by the Eckmann--Hilton argument. The
    relative $\pi_2$ need not be abelian — for $X=T^2$ it is $\pi_2(\RR^2,\text{grid})\cong
    \pi_1(\text{grid})$, free of countable rank — and the card's own prose already said so, so the
    step contradicted it. The printed exercise asks only for a bijection
    $\pi_2(X,X^1)\approx\pi_2(X)\times K$; the step now proves that: $K$, a subgroup of the free
    group $\pi_1(X^1)$, is free, a loop representing an element of $K$ bounds a disc in $X$ and so
    gives a homomorphic section of $\partial$, and a split surjection of groups has the asserted
    bijection. The step `rp2` and the rest of the argument are unchanged and correct.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Strengthening of the preceding event's repair, from an independent reading: the step proved a
    bijection where the printed exercise asserts an isomorphism. The image of $\pi_2(X)$ is central in
    $\pi_2(X,X^1)$ — Lemma 4.39, which is the content of Exercise 27 — so $i(a)$ and $s(k)$ commute
    and $(a,k)\mapsto i(a)s(k)$ is a homomorphism; the step now says this and concludes the
    isomorphism, with no abelianness of $\pi_2(X,X^1)$ used.
---

::: {.problem}
Let $X$ be a connected CW complex with 1-skeleton $X^1$.
Show that $\pi_2(X, X^1) \approx \pi_2(X) \times K$ where $K$ is the kernel of $\pi_1(X^1) \to \pi_1(X)$, a free group.
Show also that the map $\pi_2'(X) \to \pi_2'(X, X^1)$ need not be injective by considering the case $X = \RP^2$ with its standard CW structure.
:::

::: {.solution}
Since $X^1$ is a graph its higher homotopy vanishes, and $\pi_1(X^1)\to\pi_1(X)$ is onto because $X$ has no $1$-cells outside $X^1$; the long exact sequence of the pair therefore reads $0\to\pi_2(X)\to\pi_2(X,X^1)\to K\to1$ with $K=\ker(\pi_1(X^1)\to\pi_1(X))$ free. A free group splits the projection, by lifting a free basis, so $\pi_2(X,X^1)$ is a semidirect product $\pi_2(X)\rtimes K$, and it is the direct product because $K$ acts trivially on $\pi_2(X)$: the action of $\pi_1(X^1)$ on $\pi_2(X,X^1)$ is conjugation inside that group, and it restricts to the action on $\pi_2(X)$ through $\pi_2(X^1)=0$. The group $\pi_2(X,X^1)$ itself is not abelian in general — for $X=T^2$ one has $\pi_2(X)=0$ and $\pi_2(X,X^1)\cong K$, free of infinite rank — so the splitting, not abelianness, is what the argument uses. For $X=\RP^2$ the two primed groups are $\ZZ/2$ and $\ZZ$, and a homomorphism from the first to the second is zero. The argument is this card's own: no retained solution set covers this exercise.

::: pf

::: {.pf-step #graph}
$\pi_i(X^1)=0$ for every $i\ge2$, and $\pi_1(X^1)\to\pi_1(X)$ is surjective.

::: pf-proof
$X^1$ is a graph, and a connected graph has contractible universal cover (a tree), so all its homotopy groups above the first vanish; this is Example 1B.1 of printed p.~88 read for $\pi_i$. A CW complex is obtained from its $1$-skeleton by attaching cells of dimension $\ge2$, and each such attachment changes $\pi_1$ by a quotient, so $\pi_1(X^1)\to\pi_1(X)$ is onto.
:::

:::


::: {.pf-step #les}
There is a short exact sequence
$$
0\to\pi_2(X)\to\pi_2(X,X^1)\xrightarrow{\partial}K\to1,\qquad K=\ker\bigl(\pi_1(X^1)\to\pi_1(X)\bigr).
$$

::: pf-proof
The long exact homotopy sequence of the pair $(X,X^1)$ is
$$
\pi_2(X^1)\to\pi_2(X)\to\pi_2(X,X^1)\xrightarrow{\partial}\pi_1(X^1)\to\pi_1(X)\to\pi_1(X,X^1).
$$
The first term vanishes by step [](#graph){.pf-ref}, so $\pi_2(X)\to\pi_2(X,X^1)$ is injective; the image of $\partial$ is exactly the kernel of $\pi_1(X^1)\to\pi_1(X)$, which is $K$ by exactness; and $\pi_1(X,X^1)=0$ because $\pi_1(X^1)\to\pi_1(X)$ is onto by step [](#graph){.pf-ref}, so $\partial$ is onto $K$. Collecting gives the displayed short exact sequence.
:::

:::


::: {.pf-step #free}
$K$ is a free group, of rank $1-\chi$ type computable from a graph structure.

::: pf-proof
$K$ is a subgroup of the free group $\pi_1(X^1)$, since $X^1$ is a connected graph and its fundamental group is free on the edges outside a maximal tree; subgroups of free groups are free by the Nielsen--Schreier theorem. So $K$ has a free basis $\{b_\lambda\}$.
:::

:::


::: {.pf-step #split}
The projection $\partial$ admits a homomorphic section $s\colon K\to\pi_2(X,X^1)$.

::: pf-proof
For each basis element $b_\lambda\in K$ choose $\tilde b_\lambda\in\pi_2(X,X^1)$ with $\partial\tilde b_\lambda=b_\lambda$, which is possible since $\partial$ is onto. A homomorphism out of a free group is determined by the images of a basis, with no relation to check, so there is a homomorphism $s\colon K\to\pi_2(X,X^1)$ with $s(b_\lambda)=\tilde b_\lambda$; then $\partial s(b_\lambda)=b_\lambda$ on a basis, so $\partial\circ s=\mathrm{id}$.
:::

:::


::: {.pf-step #split-exact}
A short exact sequence $0\to A\to G\xrightarrow{\partial}K\to1$ of abelian groups admitting a section splits: $G\cong A\oplus K$.

::: pf-proof
Define $\Psi(a,k)=a+s(k)\in G$. It is a homomorphism because $G$ is abelian, it is injective because $\Psi(a,k)=0$ gives $\partial\Psi(a,k)=k=0$ and then $a=0$, and it is surjective because for $g\in G$ the element $g-s(\partial g)$ has trivial image under $\partial$, so lies in the kernel of $\partial$, which is the image of $A$. Hence $G\cong A\oplus K$.
:::

:::


::: {.pf-step #abelian}
$\pi_2(X,X^1)$ is in bijection with $\pi_2(X)\times K$, and the bijection is the one that sends $(a,k)$ to the product of the image of $a$ with the chosen lift of $k$.

::: pf-proof
The group $\pi_2(X,X^1)$ need not be abelian — for $X=T^2$ it is $\pi_2(\RR^2,\text{grid})\cong\pi_1(\text{grid})$, free of countable rank — so what is used is the section, not commutativity. The kernel $K$ of $\pi_1(X^1)\to\pi_1(X)$ is free: it is a subgroup of the free group $\pi_1(X^1)$. A loop in $X^1$ representing an element of $K$ is nullhomotopic in $X$, so it bounds a map of the $2$-disc into $X$ and hence defines an element of $\pi_2(X,X^1)$ mapping to it; choosing such elements for the generators of $K$ and extending linearly gives a homomorphism $s\colon K\to\pi_2(X,X^1)$ with $\partial s=\mathrm{id}_K$. The map $(a,k)\mapsto i(a)\,s(k)$ from $\pi_2(X)\times K$ to $\pi_2(X,X^1)$ is an isomorphism of groups: it is surjective because $g\,s(\partial g)^{-1}$ lies in the kernel of $\partial$, which is the image of $i$, and injective because $i(a)s(k)=1$ forces $k=\partial i(a)s(k)=1$ and then $a=1$; and it is a homomorphism because the image of $i$ lies in the centre of $\pi_2(X,X^1)$ — that is Lemma 4.39, the statement of Exercise 27 — so that $i(a)$ and $s(k)$ commute for every $a$ and $k$. This is the isomorphism the exercise asserts, and no abelianness of $\pi_2(X,X^1)$ enters.
:::

:::


::: {.pf-step #rp2}
For $X=\RP^2$ with its standard CW structure, $\pi_2'(X)\cong\ZZ/2$ and $\pi_2'(X,X^1)\cong\ZZ$, so $\pi_2'(X)\to\pi_2'(X,X^1)$ is not injective.

::: pf-proof
Here $X^1=S^1$ and $X$ is obtained from it by one $2$-cell, so $\pi_1(X)=\ZZ/2$; the universal cover is $S^2$, so $\pi_2(X)\cong\pi_2(S^2)\cong\ZZ$. The action of $\pi_1(X)=\ZZ/2$ on $\pi_2(X)$ is by the deck transformation, which on $S^2$ is the antipodal map, of degree $-1$, hence multiplication by $-1$. So $\pi_2'(X)$, the coinvariants of $\pi_2(X)$ under $\pi_1(X)$, is $\ZZ/(a\sim-a)\cong\ZZ/2$. For the pair, $\pi_1(X,X^1)=0$ makes $(X,X^1)$ $1$-connected, and the relative Hurewicz theorem gives $\pi_2'(X,X^1)\cong H_2(X,X^1)\cong\ZZ$, that group being generated by the single $2$-cell. A homomorphism $\ZZ/2\to\ZZ$ is zero, since its image is finite and $\ZZ$ is torsionfree, so the map is not injective — which is the required failure of injectivity.
:::

:::


::: {.pf-step #conclusion}
$\pi_2(X,X^1)\cong\pi_2(X)\times K$ with $K$ free, and for $X=\RP^2$ the map $\pi_2'(X)\to\pi_2'(X,X^1)$ is not injective.

::: pf-proof
Step [](#abelian){.pf-ref} gives the decomposition with steps [](#les){.pf-ref} and [](#free){.pf-ref} supplying the terms, and step [](#rp2){.pf-ref} gives the counterexample to injectivity.
:::

:::

:::
:::
