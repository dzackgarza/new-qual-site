---
schema: qual/card@1
id: P-TOPF20B
kind: problem
title: 'Any map from a space with finite $\pi_1$ to a torus is null-homotopic'
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Fundamental Group
  - Tori
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $X$ be a path connected CW complex whose fundamental group is finite.
Show that any continuous map $f : X \to T^n$ is null homotopic.
(Here $T^n = S^1 \times \cdots \times S^1$ is the $n$-dimensional torus.)
:::

::: {.solution}

::: pf

::: pf-step

$T^n$ is a $K(\ZZ^n, 1)$.

::: pf-proof

$T^n = (S^1)^n$ has contractible universal cover $\mathbb{R}^n$ and $\pi_1 = \ZZ^n$, with all higher homotopy groups trivial.

:::

:::

::: {.pf-step #s2}

Hence $[X, T^n] \cong \operatorname{Hom}(\pi_1(X), \pi_1(T^n)) = \operatorname{Hom}(\pi_1(X), \ZZ^n)$.

::: pf-proof

for a CW complex $X$ and a $K(G,1)$, homotopy classes of maps are classified by homomorphisms on $\pi_1$.

:::

:::

::: {.pf-step #s3}

$\pi_1(X)$ is finite, so every homomorphism $\pi_1(X) \to \ZZ^n$ is trivial.

::: pf-proof

$\ZZ^n$ is torsion-free, so a finite group has no nontrivial homomorphism into it.

:::

:::

::: {.pf-step #s4}

Hence $[X, T^n]$ has a single element, so every map $f : X \to T^n$ is null-homotopic.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref}.

:::

:::

:::
