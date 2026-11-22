---
schema: qual/card@1
id: E-HAT-4.2-21
kind: problem
title: "Constructing spaces with arbitrary $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the prose solution as a Lamport proof, and recorded what the retained sets give for this
    exercise. The statement was re-checked in the book's text version at Section 4.2 Exercise 21,
    printed p. 390 (PDF p. 399), and is the printed one. Steven V. Sam's set, the only retained set
    that indexes this exercise (PDF p. 23), does not prove it: its solution builds a K(pi_n(X), n)
    from X by attaching cells and computes H_{n+1}(X)/h(pi_{n+1}(X)), never identifying pi_n(X) with
    G_n, so the card uses its own argument and says so in the solution's first paragraph. The five
    steps are the prose's argument with its two appeals made explicit: that a compact subspace of a
    CW complex lies in a finite subcomplex (Hatcher, Proposition A.1), for the passage to the direct
    limit, and that each bonding map inserts the trivial factor pi_n(K(G_{n+1}, n+1)) = 0 and is
    therefore an isomorphism. The conclusion, pi_n(X) = G_n, is unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 21. One false provenance sentence repaired: the card said
    Sam's entry for this exercise is not a proof of it and described an argument about
    $H_{n+1}(X)/h(\pi_{n+1}(X))$, which is Sam's Exercise 23. Sam's §4.2 Exercise 21 does prove the
    exercise, by the compactness argument that a map $S^n\to X$ lands in some $X_m$ and then
    $\pi_n(X_m)\cong G_n$, and the step now says so; the card's own argument is kept.
---

::: {.problem}
Given a sequence of CW complexes $K(G_n, n)$, $n = 1, 2, \ldots$, let $X_n$ be the CW complex formed by the product of the first $n$ of these $K(G_n, n)$'s. Via the inclusions $X_{n-1} \subset X_n$ coming from regarding $X_{n-1}$ as the subcomplex of $X_n$ with $n$th coordinate equal to a basepoint 0-cell of $K(G_n, n)$, we can then form the union of all the $X_n$'s, a CW complex $X$.
Show $\pi_n(X) \approx G_n$ for all $n$.
:::

::: {.solution}
Hatcher, *Algebraic Topology*, §4.2 Exercise 21. The retained set of Steven V. A retained solution covers this exercise: Sam's §4.2 Exercise 21 proves it, by the compactness argument that a map $S^n\to X$ lands in some single $X_m$ and then $\pi_n(X_m)\cong G_n$. The card's own argument is kept. The argument is the card's own, from the product formula and compactness. Write $X_{N}=\prod_{i=1}^{N}K(G_{i},i)$ and $X=\bigcup_{N}X_{N}$.

::: pf

::: {.pf-step #compact}
Every map from a compact space into $X$ has image in some $X_{N}$, and likewise for homotopies.

::: pf-proof
$X$ is a CW complex and $X_{1}\subset X_{2}\subset\cdots$ is an increasing family of subcomplexes whose union is $X$. The image of a compact space under a continuous map is compact, and a compact subspace of a CW complex lies in a finite subcomplex (Hatcher, Proposition A.1); a finite subcomplex uses finitely many cells, each of which lies in some $X_{N}$, so the image lies in $X_{N}$ for $N$ large. Applying this to $S^{n}\times I$, which is compact, gives the statement for homotopies.
:::

:::

::: {.pf-step #colimit}
$\pi_{n}(X)\cong\varinjlim_{N}\pi_{n}(X_{N})$, the bonding maps being induced by the inclusions.

::: pf-proof
By step [](#compact){.pf-ref} every class in $\pi_{n}(X)$ is represented by a map $S^{n}\to X_{N}$ for some $N$, and every homotopy between such maps has image in some $X_{N'}$; so the natural map from the direct limit to $\pi_{n}(X)$ is surjective and injective. This is the standard description of homotopy groups of a union of an increasing family of subcomplexes.
:::

:::

::: {.pf-step #product}
For $N\ge n$, $\pi_{n}(X_{N})\cong G_{n}$.

::: pf-proof
$\pi_{n}$ of a product of spaces is the product of the homotopy groups, so $\pi_{n}(X_{N})\cong\prod_{i=1}^{N}\pi_{n}(K(G_{i},i))$. An Eilenberg–MacLane space $K(G_{i},i)$ has $\pi_{n}(K(G_{i},i))=0$ for $n\ne i$ and $\pi_{i}(K(G_{i},i))=G_{i}$. Hence all factors with $i\ne n$ are trivial, and the factor $i=n$ occurs once because $N\ge n$, so the product is $G_{n}$.
:::

:::

::: {.pf-step #stabilises}
For $N\ge n$ the bonding map $\pi_{n}(X_{N})\to\pi_{n}(X_{N+1})$ is an isomorphism.

::: pf-proof
The inclusion $X_{N}\hookrightarrow X_{N+1}$ is the map $\prod_{i\le N}K(G_{i},i)\to\prod_{i\le N+1}K(G_{i},i)$ inserting a basepoint in the last factor, so on $\pi_{n}$ it is the corresponding insertion of a factor $\pi_{n}(K(G_{n+1},n+1))=0$ into the product. By step [](#product){.pf-ref} both groups are $G_{n}$ and the map is the identity on the $n$-th factor, hence an isomorphism.
:::

:::

::: {.pf-step #answer}
$\boxed{\pi_{n}(X)\cong G_{n}}$ for every $n\ge1$.

::: pf-proof
Fix $n$. By step [](#stabilises){.pf-ref} the sequence $\pi_{n}(X_{N})$ is constant from $N=n$ on, with every bonding map an isomorphism onto $G_{n}$; the direct limit of a sequence that is eventually constant with isomorphisms as bonding maps is the stable value, so $\varinjlim_{N}\pi_{n}(X_{N})\cong G_{n}$. Step [](#colimit){.pf-ref} identifies that limit with $\pi_{n}(X)$.
:::

:::

:::
:::
