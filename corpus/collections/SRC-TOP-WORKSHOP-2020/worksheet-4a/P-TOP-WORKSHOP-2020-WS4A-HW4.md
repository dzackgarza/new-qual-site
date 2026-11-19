---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW4
kind: problem
title: Mayer–Vietoris homology sequence for an open cover
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The statement of Mayer-Vietoris is separated into
    the hypotheses on the cover, the sequence itself, and the exactness, which is what the worksheet asks for
    rather than a proof of the theorem. The maps are identified by their effect on chains. Not checked: the
    worksheet, which the collection retains as a problem file only; the statement is as transcribed on the card.
    No retained solution set covers the question, and the theorem is cited as such rather than reproved. No
    statement repair.
---

::: {.problem}
Let $X$ be a topological space and $A,B\subset X$ open subspaces with $X=A\cup B$.
What does the Mayer--Vietoris theorem say about the homology groups of $X$ and its subspaces?
:::

::: {.solution}
The worksheet asks for the statement of the theorem, so what follows states it, with the hypotheses that the cover must satisfy. No retained solution set covers the question: the collection's provenance is the worksheet alone.

::: pf

::: {.pf-step #hypotheses}
Let $X$ be a topological space and $A,B\subseteq X$ open with $X=A\cup B$. Then there is a long exact sequence, natural in maps of such covers.

::: pf-proof
These are the hypotheses of the theorem as stated on the card: the cover must consist of two open sets whose union is $X$. Naturality means that a continuous map $f:X\to X'$ carrying a cover $(A,B)$ into a cover $(A',B')$ induces a map of the sequences, commuting with all the maps below.
:::

:::

::: {.pf-step #sequence}
The sequence is
$$
\cdots\to H_n(A\cap B)\xrightarrow{(i_*,-j_*)}H_n(A)\oplus H_n(B)\xrightarrow{k_*+\ell_*}H_n(X)\xrightarrow{\partial}H_{n-1}(A\cap B)\to\cdots
$$
with $i,j,k,\ell$ the inclusions of $A\cap B$ into $A$ and $B$ and of $A$ and $B$ into $X$.

::: pf-proof
The maps are the ones induced on homology by the inclusions: $(i_*,-j_*)$ sends a class to the pair of its images with a sign, $k_*+\ell_*$ adds the two images in $H_n(X)$, and $\partial$ is the connecting homomorphism, which lowers degree by one. Writing the maps explicitly is part of stating the theorem, since the two signs are what make the sequence exact rather than merely a diagram of groups.
:::

:::

::: {.pf-step #exactness}
The sequence is exact at every term, and $\partial$ is the boundary of a chain-level construction: a class in $H_n(X)$ is represented by a chain that splits as a sum of chains in $A$ and in $B$ (a subdivision), and $\partial$ records the common boundary in $A\cap B$.

::: pf-proof
Exactness at $H_n(A)\oplus H_n(B)$ says a pair of classes with equal image in $H_n(X)$ comes from $H_n(A\cap B)$ — this is where the openness of $A$ and $B$ enters, through a subdivision of a chain into pieces lying in $A$ or in $B$. Exactness at $H_n(X)$ says a class restricts to zero in both $H_n(A)$ and $H_n(B)$ exactly when it is the boundary of something in $A\cap B$. Exactness at $H_n(A\cap B)$ says a class there dies in both summands exactly when it bounds in one of them. These are the three exactness statements that the theorem asserts; the card states the theorem, not its proof.
:::

:::

:::

:::
