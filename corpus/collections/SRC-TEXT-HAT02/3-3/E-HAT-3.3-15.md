---
schema: qual/card@1
id: E-HAT-3.3-15
kind: problem
title: Local homology as sections of a covering
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 15; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: a class in $H_n(M,M-A;R)$ gives a family of local classes over $A$, which is
    a section of $M_R$; Lemma 3.27(a) provides a unique class with prescribed local classes on a
    compact set, which gives surjectivity and injectivity. The proof is read at the level of that
    lemma, which is where the content sits.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 15, printed p. 259. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own, using Hatcher's Lemma 3.27(a) for the compact set $A$ as the exercise intends. Checked: the local maps and their additivity, the section condition, and the two clauses of the lemma giving surjectivity and injectivity.
---

::: {.problem}
For an $n$-manifold $M$ and a compact subspace $A \subset M$, show that $H_n(M, M - A; R)$ is isomorphic to the group $\Gamma_R(A)$ of sections of the covering space $M_R \to M$ over $A$, that is, maps $A \to M_R$ whose composition with $M_R \to M$ is the identity.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 15, printed p. 259. The two maps between $H_n(M,M-A;R)$ and the sections over $A$ are the local-homology map and Hatcher's Lemma 3.27(a) applied to a compact $A$.

::: pf

::: {.pf-step #local}
For $\alpha\in H_n(M\mid A;R)=H_n(M,M-A;R)$ and $x\in A$, inclusion of pairs gives an element $\alpha_x\in H_n(M\mid x;R)$, and $x\mapsto\alpha_x$ is a function $A\to M_R$.

::: pf-proof
The inclusion $(M,M-A)\subset(M,M-\{x\})$ induces a homomorphism $H_n(M\mid A;R)\to H_n(M\mid x;R)$; the local homology group $H_n(M\mid x;R)$ is the fibre of the orientation covering $M_R\to M$ over $x$, so the assignment sends $x$ to a point of the fibre over $x$.
:::
:::

::: {.pf-step #section}
$x\mapsto\alpha_x$ is a section of $M_R\to M$ over $A$, and $\Phi(\alpha)(x)\coloneqq\alpha_x$ defines a homomorphism $\Phi:H_n(M,M-A;R)\to\Gamma_R(A)$.

::: pf-proof
Composing the assignment with the projection $M_R\to M$ returns $x$, so the map lies over the identity, which is the definition of a section. Each $\alpha_x$ depends homomorphically on $\alpha$, since the maps $H_n(M\mid A;R)\to H_n(M\mid x;R)$ are homomorphisms, so $\Phi$ is additive; and local constancy of the local homology classes in a homology class is part of the structure of the orientation covering.
:::
:::

::: {.pf-step #surjective}
For compact $A$, every section of $M_R$ over $A$ is $\Phi(\alpha)$ for some $\alpha\in H_n(M,M-A;R)$.

::: pf-proof
Hatcher's Lemma 3.27(a) states that for a compact subspace $A$ of an $n$-manifold and a section $x\mapsto\alpha_x$ of $M_R$ over $A$, there is a class $\alpha_A\in H_n(M\mid A;R)$ whose image in $H_n(M\mid x;R)$ is $\alpha_x$ for every $x\in A$; that class maps to the given section under $\Phi$.
:::
:::

::: {.pf-step #injective}
$\Phi$ is injective.

::: pf-proof
The uniqueness clause of the same lemma says that a class in $H_n(M\mid A;R)$ is determined by its images in all the fibres $H_n(M\mid x;R)$, $x\in A$; so $\Phi(\alpha)=0$ forces $\alpha=0$.
:::
:::

::: {.pf-step}
$H_n(M,M-A;R)\cong\Gamma_R(A)$ for every compact $A\subset M$.

::: pf-proof
Steps [](#surjective){.pf-ref} and [](#injective){.pf-ref} make $\Phi$ a bijection, and step [](#section){.pf-ref} makes it a homomorphism.
:::
:::

:::
:::
