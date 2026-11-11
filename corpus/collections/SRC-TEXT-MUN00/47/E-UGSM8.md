---
schema: qual/card@1
id: E-UGSM8
kind: problem
title: The general Ascoli theorem implies the classical version
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 3 was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Theorem 47.1 (the general Ascoli
    theorem as the book states it, printed p. 290), Theorem 45.4 (the classical version), Theorem 46.7 (compact
    convergence equals uniform convergence on a compact space) and Theorem 27.3 plus Theorem 26.3. The argument
    is: on a compact space the two topologies agree and the space of functions is metrizable, hence Hausdorff;
    in R^n a set has compact closure iff it is bounded; so pointwise boundedness of F is pointwise relative
    compactness of the closures F_a, and part (a) of Theorem 47.1 puts F inside a compact subspace, which is
    closed in the Hausdorff function space, so the closure of F is compact; conversely if the closure of F is
    compact then F is contained in a compact subspace and part (b) of Theorem 47.1, whose hypothesis of local
    compactness holds for the compact Hausdorff X, gives equicontinuity and compact closures of the F_a. Nothing
    needed correction.
---

::: {.exercise}

Show that the general version of Ascoli's theorem implies the classical version (Theorem 45.4) when $X$ is Hausdorff.
:::

::: {.solution}
The classical version (Theorem 45.4) states: for $X$ compact and $\mathcal C(X, \RR^n)$ in the uniform topology, a subset $\mathcal F$ has compact closure if and only if $\mathcal F$ is equicontinuous and pointwise bounded.

The general version states: for a space $X$, a metric space $(Y, d)$, and $\mathcal C(X, Y)$ in the topology of compact convergence, if $\mathcal F \subseteq \mathcal C(X, Y)$ is equicontinuous and each set $\mathcal F_a = \{f(a) : f \in \mathcal F\}$ has compact closure, then $\mathcal F$ is contained in a compact subspace of $\mathcal C(X, Y)$; the converse holds if $X$ is locally compact Hausdorff.

Let $X$ be compact Hausdorff and $Y = \RR^n$.

::: pf

::: {.pf-step #s1}

On $\mathcal C(X, \RR^n)$, the topology of compact convergence equals the uniform topology, and it is Hausdorff.

::: pf-proof

$X$ is compact, so the two topologies coincide by [[E-2AWO8]]. The uniform topology is induced by a metric.

:::

:::

::: {.pf-step #s2}

For $a \in X$, $\mathcal F_a$ has compact closure in $\RR^n$ if and only if $\mathcal F_a$ is bounded.

::: pf-proof

The closure of a bounded subset of $\RR^n$ is closed and bounded, hence compact by the Heine--Borel theorem; a set with compact closure is bounded.

:::

:::

::: {.pf-step #s3}

If $\mathcal F$ is equicontinuous and pointwise bounded, then $\overline{\mathcal F}$ is compact.

::: pf-proof

By step [](#s2){.pf-ref} each $\mathcal F_a$ has compact closure, so the general version puts $\mathcal F$ inside a compact subspace $K$. By step [](#s1){.pf-ref}, $K$ is closed in the Hausdorff space $\mathcal C(X, \RR^n)$, so $\overline{\mathcal F} \subseteq K$ is a closed subset of a compact space, hence compact.

:::

:::

::: {.pf-step #s4}

If $\overline{\mathcal F}$ is compact, then $\mathcal F$ is equicontinuous and pointwise bounded.

::: pf-proof

$\mathcal F$ is contained in the compact subspace $\overline{\mathcal F}$. A compact Hausdorff space is locally compact Hausdorff, so the converse in the general version shows that $\mathcal F$ is equicontinuous and each $\mathcal F_a$ has compact closure; by step [](#s2){.pf-ref}, each $\mathcal F_a$ is bounded.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} are the two implications of the classical version.

:::

:::

:::
