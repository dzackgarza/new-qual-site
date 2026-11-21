---
schema: qual/card@1
id: E-HC37E
kind: problem
title: Nonabelian fundamental groups of higher-genus tori
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §74 Exercise 6, printed p. 454. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-1527500-E-HC37E.md, read whole.
    Math StackExchange 1527500, "Fundamental group of the n-fold torus is nonabelian for n > 1" (asked by
    Empiromancer 2015-11-13), has one answer, 1527539 by the account posting as user98602 (2015-11-13),
    which proves the exercise under Munkres' hypotheses: a homomorphism from the free group on the 2n
    generators that kills the relator, hence one that factors through the presentation of Theorem 74.3
    (printed p. 452), and whose image is F(x_1,x_2), which is nonabelian. That proof is now transcribed in the
    solution block with its URL and date, and it replaces the card's own proof, which used the printed hint's
    map instead: alpha_1, beta_1 -> gamma, the rest -> delta, relator -> [gamma,gamma][delta,delta]^{n-1} = 1.
    The two are the same argument with different maps -- the answer's needs n >= 2, which is the hypothesis,
    and the hint's works for every n -- and the answer's is kept because it is the one with a published
    source. Nothing is missing from the answer for this exercise; its presentation step is the book's
    Theorem 74.3, and the vertex check that Theorem 74.3 leaves to the reader (printed p. 452) is not needed
    once the presentation is quoted as a theorem.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 6, printed p. 454. The homomorphism of the printed hint sends the relator to [gamma,gamma][delta,delta]^{n-1} = 1 and is onto the nonabelian free group F(gamma,delta); checked with Theorem 74.3 and the free-group results of Section 68. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the presentation of the fundamental group, the map that
    kills the relator, the induced surjection, and the non-abelianness of the free group of rank two. The
    argument is the cited Math StackExchange answer 1527539 (not the printed hint's map), re-read for this
    pass; the relator computation was checked here.
---

::: {.exercise}

If $n > 1$, show that the fundamental group of the $n$-fold torus is not abelian.
[Hint: Let $G$ be the free group on the set $\theset{\alpha_1, \beta_1, \ldots, \alpha_n, \beta_n}$; let $F$ be the free group on the set $\theset{\gamma, \delta}$. Consider the homomorphism of $G$ onto $F$ that sends $\alpha_1$ and $\beta_1$ to $\gamma$ and all other $\alpha_i$ and $\beta_i$ to $\delta$.]
:::

::: {.solution}
The proof is that of Math StackExchange answer 1527539 (https://math.stackexchange.com/a/1527539), posted 2015-11-13 by the account posting as user98602 to question 1527500, "Fundamental group of the $n$-fold torus is nonabelian for $n>1$"; its homomorphism is not the one the printed hint proposes, since the hint sends $\alpha_{1},\beta_{1}\mapsto\gamma$ and all other generators to $\delta$, while the answer sends $\alpha_{1}\mapsto x_{1}$, $\beta_{1}\mapsto x_{2}$, $\alpha_{2}\mapsto x_{2}$, $\beta_{2}\mapsto x_{1}$ and every other generator to $1$. Both maps kill the relator and both are onto a free group of rank two; the answer's needs $n\ge2$, which is the hypothesis.

::: pf

::: {.pf-step #presentation}
$\pi_{1}(T^{\#n})$ is $F/N$, where $F$ is free on $\alpha_{1},\beta_{1},\dots,\alpha_{n},\beta_{n}$ and $N$ is the least normal subgroup containing $[\alpha_{1},\beta_{1}][\alpha_{2},\beta_{2}]\cdots[\alpha_{n},\beta_{n}]$.

::: pf-proof
This is Theorem 74.3: the $n$-fold torus is a cell complex whose two-cells are attached along the commutator product, and van Kampen computes its fundamental group as the quotient of the free group on the four $n$ generators by the normal closure of that product.
:::

:::

::: {.pf-step #phi}
The homomorphism $\varphi:F\to F_{2}=F(x_{1},x_{2})$ with $\alpha_{1}\mapsto x_{1}$, $\beta_{1}\mapsto x_{2}$, $\alpha_{2}\mapsto x_{2}$, $\beta_{2}\mapsto x_{1}$ and all other generators to $1$ sends the relator to $1$.

::: pf-proof
For $i\ge3$ both $\alpha_{i}$ and $\beta_{i}$ map to $1$, so $[\alpha_{i},\beta_{i}]\mapsto[1,1]=1$. The first two commutators map to $[x_{1},x_{2}]$ and $[x_{2},x_{1}]=[x_{1},x_{2}]^{-1}$, so the product maps to
$$
[x_{1},x_{2}]\,[x_{2},x_{1}]=x_{1}x_{2}x_{1}^{-1}x_{2}^{-1}\,x_{2}x_{1}x_{2}^{-1}x_{1}^{-1}=1 .
$$
Hence $\varphi$ vanishes on the relator and so on the normal subgroup it generates: $\varphi(N)=1$.
:::

:::

::: {.pf-step #induced}
$\varphi$ induces a surjective homomorphism $h:\pi_{1}(T^{\#n})\to F_{2}$.

::: pf-proof
Since $\varphi$ kills $N$, it factors through $F/N=\pi_{1}(T^{\#n})$, giving $h$ with $h([\alpha_{i}])=\varphi(\alpha_{i})$ and $h([\beta_{i}])=\varphi(\beta_{i})$. It is onto because $x_{1}=h([\alpha_{1}])$ and $x_{2}=h([\beta_{1}])$ lie in the image, and these two generate $F_{2}$.
:::

:::

::: {.pf-step}
$\pi_{1}(T^{\#n})$ is not abelian.

::: pf-proof
The group $F_{2}=\ZZ*\ZZ$ is not abelian: the words $x_{1}x_{2}$ and $x_{2}x_{1}$ are distinct reduced words, by the normal form for free products (§68). The image of an abelian group under a homomorphism is abelian, so a group admitting a surjection onto the non-abelian $F_{2}$ cannot be abelian; by step [](#induced){.pf-ref} there is such a surjection from $\pi_{1}(T^{\#n})$. Hence for $n>1$ the fundamental group of the $n$-fold torus is not abelian, as claimed.
:::

:::

:::
:::
