---
schema: qual/card@1
id: E-HAT-2.2-35
kind: problem
title: Nonorientable surface or complex with torsion in $H_1$ cannot embed in $\mathbb{R}^3$ with mapping cylinder neighborhood
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Surfaces
  - Embeddings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Use the Mayer–Vietoris sequence to show that a nonorientable closed surface, or more generally a finite simplicial complex $X$ for which $H_1(X)$ contains torsion, cannot be embedded as a subspace of $\mathbb{R}^3$ in such a way as to have a neighborhood homeomorphic to the mapping cylinder of some map from a closed orientable surface to $X$.
[This assumption on a neighborhood is in fact not needed if one deduces the result from Alexander duality in §3.3.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose $X$ embeds in $\RR^3$ with a neighborhood $N$ homeomorphic to the mapping cylinder of a map $f: S \to X$ from a closed orientable surface $S$.

::: pf-proof

assume the contrary.

:::

:::

::: {.pf-step #s2}

$N$ is a compact $3$-manifold with boundary $S$ (the closed orientable surface).

::: pf-proof

the mapping cylinder of $f: S \to X$ has boundary $S$ (the "top" of the cylinder), and $N$ is a regular neighborhood of $X$.

:::

:::

::: {.pf-step #s3}

Apply Mayer–Vietoris to $\RR^3 = N \cup (\RR^3 \setminus \operatorname{int} N)$ with intersection $S$.

::: pf-proof

decompose $\RR^3$ into the neighborhood $N$ and its complement, meeting along the boundary surface $S$.

:::

:::

::: {.pf-step #s4}

The relevant part of the Mayer–Vietoris sequence is $$H_2(\RR^3) \to H_1(S) \to H_1(N) \oplus H_1(\RR^3 \setminus \operatorname{int} N) \to H_1(\RR^3).$$ Proof: the Mayer–Vietoris sequence in low degrees.

:::

::: {.pf-step #s5}

$H_2(\RR^3) = 0$ and $H_1(\RR^3) = 0$.

::: pf-proof

$\RR^3$ is contractible.

:::

:::

::: {.pf-step #s6}

Hence $H_1(S) \to H_1(N) \oplus H_1(\RR^3 \setminus \operatorname{int} N)$ is injective.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} (the map is injective since its kernel is the image of $H_2(\RR^3) = 0$).

:::

:::

::: {.pf-step #s7}

$H_1(S)$ is free abelian (since $S$ is a closed orientable surface).

::: pf-proof

$H_1$ of a closed orientable surface of genus $g$ is $\ZZ^{2g}$.

:::

:::

::: {.pf-step #s8}

$H_1(N) \cong H_1(X)$ (the mapping cylinder deformation retracts onto $X$).

::: pf-proof

a mapping cylinder deformation retracts onto its base.

:::

:::

::: {.pf-step #s9}

The map $H_1(S) \to H_1(N) \oplus H_1(\RR^3 \setminus \operatorname{int} N)$ is an isomorphism.

::: pf-proof

it is injective (step [](#s6){.pf-ref}), and its cokernel maps into $H_1(\RR^3) = 0$ (step [](#s5){.pf-ref}), so it is also surjective.

:::

:::

::: {.pf-step #s10}

Hence $H_1(N) = H_1(X)$ is a direct summand of the free abelian group $H_1(S)$.

::: pf-proof

Steps [](#s9){.pf-ref} and [](#s7){.pf-ref}; a direct summand of a free abelian group is free abelian.

:::

:::

::: {.pf-step #s11}

But $H_1(X)$ contains torsion, so it is not free abelian.

::: pf-proof

hypothesis.

:::

:::

::: {.pf-step #s12}

Contradiction.

::: pf-proof

Steps [](#s10){.pf-ref} and [](#s11){.pf-ref}.

:::

:::

::: {.pf-step #s13}

Hence no such embedding exists.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref} and [](#s12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s13){.pf-ref}.

:::

:::

:::
