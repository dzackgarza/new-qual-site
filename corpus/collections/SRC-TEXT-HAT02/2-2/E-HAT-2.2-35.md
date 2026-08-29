---
schema: qual/card@1
id: E-HAT-2.2-35
kind: exercise
title: Nonorientable surface or complex with torsion in $H_1$ cannot embed in $\mathbb{R}^3$ with mapping cylinder neighborhood
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer–Vietoris
  - Surfaces
  - Embeddings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Use the Mayer–Vietoris sequence to show that a nonorientable closed surface, or more generally a finite simplicial complex $X$ for which $H_1(X)$ contains torsion, cannot be embedded as a subspace of $\mathbb{R}^3$ in such a way as to have a neighborhood homeomorphic to the mapping cylinder of some map from a closed orientable surface to $X$.
[This assumption on a neighborhood is in fact not needed if one deduces the result from Alexander duality in §3.3.]

::: {.solution}
<1>1. Suppose $X$ embeds in $\RR^3$ with a neighborhood $N$ homeomorphic to the mapping cylinder of a map $f: S \to X$ from a closed orientable surface $S$.
Proof: assume the contrary.

<1>2. $N$ is a compact $3$-manifold with boundary $S$ (the closed orientable surface).
Proof: the mapping cylinder of $f: S \to X$ has boundary $S$ (the "top" of the cylinder), and $N$ is a regular neighborhood of $X$.

<1>3. Apply Mayer–Vietoris to $\RR^3 = N \cup (\RR^3 \setminus \operatorname{int} N)$ with intersection $S$.
Proof: decompose $\RR^3$ into the neighborhood $N$ and its complement, meeting along the boundary surface $S$.

<1>4. The relevant part of the Mayer–Vietoris sequence is
$$H_2(\RR^3) \to H_1(S) \to H_1(N) \oplus H_1(\RR^3 \setminus \operatorname{int} N) \to H_1(\RR^3).$$
Proof: the Mayer–Vietoris sequence in low degrees.

<1>5. $H_2(\RR^3) = 0$ and $H_1(\RR^3) = 0$.
Proof: $\RR^3$ is contractible.

<1>6. Hence $H_1(S) \to H_1(N) \oplus H_1(\RR^3 \setminus \operatorname{int} N)$ is injective.
Proof: <1>4 and <1>5 (the map is injective since its kernel is the image of $H_2(\RR^3) = 0$).

<1>7. $H_1(S)$ is free abelian (since $S$ is a closed orientable surface).
Proof: $H_1$ of a closed orientable surface of genus $g$ is $\ZZ^{2g}$.

<1>8. $H_1(N) \cong H_1(X)$ (the mapping cylinder deformation retracts onto $X$).
Proof: a mapping cylinder deformation retracts onto its base.

<1>9. The map $H_1(S) \to H_1(N) \oplus H_1(\RR^3 \setminus \operatorname{int} N)$ is an isomorphism.
Proof: it is injective (<1>6), and its cokernel maps into $H_1(\RR^3) = 0$ (<1>5), so it is also surjective.

<1>10. Hence $H_1(N) = H_1(X)$ is a direct summand of the free abelian group $H_1(S)$.
Proof: <1>9 and <1>7; a direct summand of a free abelian group is free abelian.

<1>11. But $H_1(X)$ contains torsion, so it is not free abelian.
Proof: hypothesis.

<1>12. Contradiction.
Proof: <1>10 and <1>11.

<1>13. Hence no such embedding exists.
Proof: <1>1–<1>12.

<1>14. Q.E.D.
Proof: <1>13.
:::
