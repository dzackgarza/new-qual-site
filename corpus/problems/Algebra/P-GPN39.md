---
schema: qual/card@1
id: P-GPN39
kind: problem
title: A linear operator with $1\notin\Spec(L)$ has unique fixed point $0$
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $V$ be a vector space over a field $F$, and let $L: V \to V$ be a linear operator.
Suppose that $1$ is not an eigenvalue of $L$ (that is, $1 \notin \operatorname{spec}(L)$). Prove that $x = 0$ is the unique fixed point of $L$ (i.e. $L(x) = x \implies x = 0$). Moreover, if $V$ is finite-dimensional, show that $I - L$ is an invertible linear operator on $V$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\ker(I-L)=0$; that is, $0$ is the only fixed point of $L$.

::: pf-proof

If $L(x)=x$, then $(I-L)x=0$.
A nonzero such $x$ would be an eigenvector of $L$ with eigenvalue $1$, contrary to hypothesis.

:::

:::

::: pf-step

If $\dim V<\infty$, then $I-L$ is invertible.

::: pf-proof

By step [](#s1){.pf-ref}, $I-L$ is injective, and rank-nullity gives $\dim\operatorname{im}(I-L)=\dim V$, so $I-L$ is also surjective.

:::

:::

:::

:::
