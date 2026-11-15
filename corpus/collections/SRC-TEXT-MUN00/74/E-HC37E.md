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
---

::: {.exercise}

If $n > 1$, show that the fundamental group of the $n$-fold torus is not abelian.
[Hint: Let $G$ be the free group on the set $\theset{\alpha_1, \beta_1, \ldots, \alpha_n, \beta_n}$; let $F$ be the free group on the set $\theset{\gamma, \delta}$. Consider the homomorphism of $G$ onto $F$ that sends $\alpha_1$ and $\beta_1$ to $\gamma$ and all other $\alpha_i$ and $\beta_i$ to $\delta$.]
:::

::: {.solution}

The proof below is that of Math StackExchange answer 1527539 (https://math.stackexchange.com/a/1527539), posted 2015-11-13 by the account posting as user98602 to question 1527500, "Fundamental group of the $n$-fold torus is nonabelian for $n>1$" (https://math.stackexchange.com/questions/1527500), asked by Empiromancer on 2015-11-13. Its homomorphism is not the one the printed hint proposes: the hint sends $\alpha_1$ and $\beta_1$ to $\gamma$ and every other generator to $\delta$, while the answer sends $\alpha_1\mapsto x_1$, $\beta_1\mapsto x_2$, $\alpha_2\mapsto x_2$, $\beta_2\mapsto x_1$ and every other generator to $1$. Both images kill the relator and both are onto a free group of rank two; the answer's map needs $n\ge2$, which is the exercise's hypothesis, and its author notes that this is where $n=1$ fails.

By Theorem 74.3 (printed p. 452), $\pi_1(T^{\#n})$ is the quotient of the free group $F$ on $\alpha_1,\beta_1,\dots,\alpha_n,\beta_n$ by the least normal subgroup $N$ containing $[\alpha_1,\beta_1][\alpha_2,\beta_2]\cdots[\alpha_n,\beta_n]$. Let $F_2=F(x_1,x_2)$ and let $\varphi:F\to F_2$ be the homomorphism determined by those images. Then
$$
\varphi\bigl([\alpha_1,\beta_1][\alpha_2,\beta_2]\cdots[\alpha_n,\beta_n]\bigr)
=[x_1,x_2][x_2,x_1]
=x_1x_2x_1^{-1}x_2^{-1}\,x_2x_1x_2^{-1}x_1^{-1}
=1,
$$
so $\varphi(N)=1$ and $\varphi$ induces a homomorphism $h:\pi_1(T^{\#n})\to F_2$ carrying $[\alpha_i]$ and $[\beta_i]$ to the images of $\alpha_i$ and $\beta_i$.

The homomorphism $h$ is onto, because $x_1=h([\alpha_1])$ and $x_2=h([\beta_1])$. The group $F_2$ is not abelian: in the free product $\ZZ*\ZZ$ the reduced words $(x_1,x_2)$ and $(x_2,x_1)$ are distinct, by the definition of the free product in §68, so $x_1x_2\ne x_2x_1$. A homomorphic image of an abelian group is abelian, and $F_2$ is not, so $\pi_1(T^{\#n})$ is not abelian.
:::
