---
schema: qual/card@1
id: P-APAS21F
kind: problem
title: 'Indecomposable versus irreducible complex representations of $\RR_+$'
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the counterexample into numbered steps and supplied the two steps the prose ran
    together: that a line is invariant under every rho(t) if and only if it is invariant under the
    single matrix N, using rho(e) = I + N and rho(1/e) = I - N to recover N, and that N has exactly
    one invariant line, ker N, with the calculation for a vector with nonzero second coordinate.
    Also recorded why a two-dimensional module with a decomposition must split as two invariant
    lines. Every macro used is one the preamble defines. Nothing was checked against a printed page.
---

::: {.problem}
Let $\RR_+$ be the group of positive real numbers under multiplication.
Is every indecomposable $\RR_+$-module over the complex numbers irreducible?
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

Write $\rho(t)=\begin{pmatrix}1&\log t\\ 0&1\end{pmatrix}$ for $t>0$, acting on $V=\CC^{2}$.

::: pf

::: {.pf-step #representation}
$\rho$ is a representation of $\RR_{+}$ on $V$.

::: pf-proof
$\log(ts)=\log t+\log s$, so
$$
\rho(t)\rho(s)=\begin{pmatrix}1&\log t\\ 0&1\end{pmatrix}\begin{pmatrix}1&\log s\\ 0&1\end{pmatrix}=\begin{pmatrix}1&\log t+\log s\\ 0&1\end{pmatrix}=\rho(ts),
$$
and $\rho(1)=I$; each $\rho(t)$ is invertible, and $t\mapsto\rho(t)$ is continuous. So $\rho$ is a group homomorphism $\RR_{+}\to\operatorname{GL}_{2}(\CC)$.
:::

:::

::: {.pf-step #reducible}
$V$ is not irreducible: the line $L=\CC e_{1}$ is a submodule.

::: pf-proof
$\rho(t)e_{1}=e_{1}$ for every $t$, so $L$ is invariant, that is, a nonzero proper submodule of $V$; a module is irreducible when its only submodules are $0$ and itself, so $V$ is reducible.
:::

:::

::: {.pf-step #N}
Let $N=\begin{pmatrix}0&1\\ 0&0\end{pmatrix}$. A line $\CC v$ is invariant under $\rho(t)$ for every $t>0$ if and only if $Nv\in\CC v$.

::: pf-proof
$\rho(t)=I+(\log t)N$, so if $Nv=\lambda v$ then $\rho(t)v=(1+\lambda\log t)v$ lies in $\CC v$ for every $t$. Conversely if $\CC v$ is $\rho(t)$-invariant for all $t$, then $v$ and $\rho(e)v=v+Nv$ both lie in $\CC v$, so $Nv=\rho(e)v-v\in\CC v$.
:::

:::

::: {.pf-step #one-line}
The only line invariant under $N$ is $\CC e_{1}$, and it is invariant.

::: pf-proof
$Ne_{1}=0\in\CC e_{1}$. Conversely let $v=ae_{1}+be_{2}$ with $b\neq0$; then $Nv=be_{1}$. If $be_{1}=\lambda v=\lambda ae_{1}+\lambda be_{2}$, comparing the $e_{2}$-coefficient gives $\lambda b=0$, hence $\lambda=0$, hence $b=0$, a contradiction. So no line spanned by a vector with nonzero second coordinate is $N$-invariant.
:::

:::

::: {.pf-step #indecomposable}
$V$ has no decomposition $V=V_{1}\oplus V_{2}$ with both $V_{i}\neq0$ submodules.

::: pf-proof
Such a decomposition of a two-dimensional space gives $\dim V_{1}=\dim V_{2}=1$, so both $V_{i}$ are invariant lines, hence by steps [](#N){.pf-ref} and [](#one-line){.pf-ref} both equal $\CC e_{1}$; but then $V_{1}+V_{2}$ is one-dimensional, contradicting $V_{1}\oplus V_{2}=V$. So $V$ is indecomposable.
:::

:::

::: {.pf-step}
Not every indecomposable $\RR_{+}$-module is irreducible: $V$ is indecomposable and reducible.

::: pf-proof
Steps [](#reducible){.pf-ref} and [](#indecomposable){.pf-ref} give the two properties, and the answer to the question is no.
:::

:::

:::

:::
