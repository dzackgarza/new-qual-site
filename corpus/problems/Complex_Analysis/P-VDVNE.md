---
schema: qual/card@1
id: P-VDVNE
kind: problem
title: Singularities at infinity of entire functions with finitely or infinitely many zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Singularities
  - Essential Singularities
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $f$ be entire, and discuss (with proofs and examples) the types of singularities $f$ might have (removable, pole, or essential) at $z=\infty$ in the following cases:

(a) $f$ has at most finitely many zeros in $\CC$.

(b) $f$ has infinitely many zeros in $\CC$.
:::

::: {.solution}
Write $f(z) = \sum_{k\geq 0} c_k z^k$. The type of the singularity of $f$ at $\infty$ is the type of the singularity of $g(z) \coloneqq f(1/z) = \sum_{k \geq 0} c_k z^{-k}$ at $0$.

::: pf

::: {.pf-step #trichotomy}

For an entire $f$: $\infty$ is removable if and only if $f$ is constant; $\infty$ is a pole if and only if $f$ is a nonconstant polynomial; otherwise $\infty$ is an essential singularity.

::: pf-proof

The Laurent series of $g$ at $0$ has principal part $\sum_{k \geq 1} c_k z^{-k}$. The singularity is removable when this part is zero, that is, $f = c_0$; it is a pole when only finitely many $c_k$ with $k\geq 1$ are nonzero and at least one is, that is, $f$ is a nonconstant polynomial; and it is essential when infinitely many $c_k$ are nonzero.

:::

:::

::: pf-step

(a) If $f$ has finitely many zeros, all three types occur: $f(z) = 1$ has a removable singularity at $\infty$, $f(z) = z$ has a pole, and $f(z) = e^z$ has an essential singularity.

::: pf-proof

Each example has finitely many zeros (none, one, and none), and step [](#trichotomy){.pf-ref} gives the type: $1$ is constant, $z$ is a nonconstant polynomial, and $e^z = \sum z^k/k!$ has infinitely many nonzero coefficients.

:::

:::

::: pf-step

(b) If $f$ has infinitely many zeros, then either $f \equiv 0$ and $\infty$ is removable, or $\infty$ is an essential singularity; $f(z) = \sin z$ is an example of the second case.

::: pf-proof

If $f \not\equiv 0$, then $f$ is not a polynomial, since a nonzero polynomial has finitely many zeros. By step [](#trichotomy){.pf-ref}, $\infty$ is essential. The function $\sin z$ vanishes at every $n\pi$, $n \in \ZZ$.

:::

:::

:::

:::
