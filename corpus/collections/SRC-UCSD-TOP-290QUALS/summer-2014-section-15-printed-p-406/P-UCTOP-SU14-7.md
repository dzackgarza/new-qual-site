---
schema: qual/card@1
id: P-UCTOP-SU14-7
kind: problem
title: Degree ±1 map induces surjection on fundamental group
classification:
  areas:
  - topology
  topics:
  - Degree Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Suppose $f : M \to N$ is a map between two closed connected oriented $n$-manifolds which induces an isomorphism $H_*(M) \cong H_*(N)$ (that is, it is a map of degree $\pm 1$). Prove that the induced map $\pi_1(M) \to \pi_1(N)$ must be surjective.

::: {.solution}
**Goal.** For a degree $\pm 1$ map $f: M \to N$ between closed connected oriented $n$-manifolds, show $f_*: \pi_1(M) \to \pi_1(N)$ is surjective.

<1>1. $f$ induces an isomorphism $H_1(M;\ZZ) \to H_1(N;\ZZ)$.
<2>1. $f$ induces an isomorphism on all homology groups (degree $\pm 1$).
Proof: by hypothesis, $f_*: H_*(M) \to H_*(N)$ is an isomorphism.
<2>2. In particular $f_*: H_1(M;\ZZ) \to H_1(N;\ZZ)$ is an isomorphism.
Proof: the degree-$1$ case of <1>1.1.

<1>2. $H_1(X;\ZZ) \cong \pi_1(X)^{\mathrm{ab}}$ for any path-connected space $X$.
Proof: the Hurewicz theorem identifies $H_1$ with the abelianization of $\pi_1$.

<1>3. Hence $f_*: \pi_1(M)^{\mathrm{ab}} \to \pi_1(N)^{\mathrm{ab}}$ is an isomorphism.
Proof: <1>1.2 and <1>2.

<1>4. $f_*: \pi_1(M) \to \pi_1(N)$ is surjective.
<2>1. Suppose $f_*(\pi_1(M))$ is a proper subgroup of $\pi_1(N)$.
Proof: assume for contradiction.
<2>2. Then the induced map on abelianizations $f_*^{\mathrm{ab}}: \pi_1(M)^{\mathrm{ab}} \to \pi_1(N)^{\mathrm{ab}}$ is not surjective.
Proof: if $H \le G$ is a proper subgroup, then $H^{\mathrm{ab}} \to G^{\mathrm{ab}}$ is not surjective (the abelianization of a proper subgroup maps to a proper subgroup of the abelianization — more precisely, if $f_*(\pi_1(M))$ is proper, its image in $\pi_1(N)^{\mathrm{ab}}$ is a proper subgroup, since a subgroup whose abelianization surjects onto $G^{\mathrm{ab}}$ must be all of $G$).
<2>3. This contradicts <1>3 (which says $f_*^{\mathrm{ab}}$ is an isomorphism, hence surjective).
Proof: contradiction.

<1>5. Q.E.D.
Proof: <1>4 shows $f_*$ is surjective.
:::
