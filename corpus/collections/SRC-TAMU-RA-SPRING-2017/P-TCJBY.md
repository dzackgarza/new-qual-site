---
schema: qual/card@1
id: P-TCJBY
kind: problem
title: A sup-norm-closed subspace of $C[0,1]$ complete in $\norm{\cdot}_2$ is finite-dimensional
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Norms
  - Closure
relations: []
review: draft
---

::: {.problem}
Consider the space $C([0,1])$ of real-valued continuous functions on $[0,1]$, with the supremum norm $\norm{f}_\infty\coloneqq\sup_{x\in[0,1]}\abs{f(x)}$ and the $L^2$-norm $\norm{f}_2\coloneqq\left(\int_0^1\abs{f(x)}^2\,dx\right)^{1/2}$.
Let $S$ be a closed linear subspace of $(C([0,1]),\norm{\cdot}_\infty)$.
Show that if $S$ is complete in the norm $\norm{\cdot}_2$, then $S$ is finite-dimensional.
:::

::: {.solution}

The argument is the card's own: the two norms are comparable, so point evaluations become bounded functionals on a Hilbert space; Bessel's inequality then bounds the cardinality of an orthonormal basis.

::: pf

::: {.pf-step #bounded}

$\norm{f}_{2}\le\norm{f}_{\infty}$ for $f\in C([0,1])$, so the identity $(S,\norm{\cdot}_{\infty})\to(S,\norm{\cdot}_{2})$ is bounded.

::: pf-proof

$\int_{0}^{1}\abs{f}^{2}\le\int_{0}^{1}\norm{f}_{\infty}^{2}=\norm{f}_{\infty}^{2}$ because $\abs{f(x)}\le\norm{f}_{\infty}$ for all $x\in[0,1]$, whose length is $1$. Taking square roots gives the inequality, and the identity map is linear.

:::

:::

::: {.pf-step #equivalent}

There is $C$ with $\norm{f}_{\infty}\le C\norm{f}_{2}$ for all $f\in S$.

::: pf-proof

$S$ is closed in the complete space $(C([0,1]),\norm{\cdot}_{\infty})$ — the uniform limit of continuous functions is continuous — so $S$ is complete for $\norm{\cdot}_{\infty}$; by hypothesis $S$ is complete for $\norm{\cdot}_{2}$. The identity is a bounded linear bijection between two Banach spaces, so by the open mapping theorem its inverse is bounded, which is the displayed inequality.

:::

:::

::: {.pf-step #evaluation}

For each $x\in[0,1]$ there is $g_{x}\in S$ with $f(x)=\inner{f}{g_{x}}$ for all $f\in S$ and $\norm{g_{x}}_{2}\le C$.

::: pf-proof

The evaluation $\delta_{x}(f)=f(x)$ is linear on $S$ and bounded: $\abs{f(x)}\le\norm{f}_{\infty}\le C\norm{f}_{2}$ by steps [](#bounded){.pf-ref} and [](#equivalent){.pf-ref}, so $\norm{\delta_{x}}\le C$. $S$ is a Hilbert space in the inner product of $L^{2}(0,1)$, being a complete subspace of $L^{2}(0,1)$ by hypothesis. By the Riesz representation theorem every bounded linear functional on it is $f\mapsto\inner{f}{g_{x}}$ for a unique $g_{x}\in S$ with $\norm{g_{x}}_{2}=\norm{\delta_{x}}\le C$.

:::

:::

::: {.pf-step #bessel}

$\cardinality{I}\le C^{2}$ for every orthonormal basis $\{f_{n}\}_{n\in I}$ of $S$.

::: pf-proof

For a finite $F\subseteq I$ and any $x$, Bessel's inequality applied to the orthonormal family $\{f_{n}\}_{n\in F}$ and the vector $g_{x}$ gives $\sum_{n\in F}\abs{\inner{f_{n}}{g_{x}}}^{2}\le\norm{g_{x}}_{2}^{2}$, and $\inner{f_{n}}{g_{x}}=f_{n}(x)$ by step [](#evaluation){.pf-ref}; so $\sum_{n\in F}\abs{f_{n}(x)}^{2}\le C^{2}$ for every $x$. Integrating over $[0,1]$ and using that the $f_{n}$ are orthonormal in $L^{2}$, so $\int_{0}^{1}\abs{f_{n}}^{2}=1$ and the integral of a finite sum is the sum of the integrals,
$$
\cardinality{F}=\sum_{n\in F}\int_{0}^{1}\abs{f_{n}(x)}^{2}dx\le C^{2}.
$$
As $F$ ranges over finite subsets, $\cardinality{I}\le C^{2}$.

:::

:::

::: {.pf-step #conclusion}

$S$ is finite-dimensional.

::: pf-proof

By step [](#bessel){.pf-ref} every orthonormal basis of $S$ has at most $C^{2}$ elements, and $C^{2}$ is a real number, hence smaller than some integer. An orthonormal basis of cardinality at most $C^{2}$ is finite, and a Hilbert space with a finite orthonormal basis of cardinality $N$ has dimension $N$:
$$
\boxed{\dim S<\infty.}
$$

:::

:::

:::

:::
