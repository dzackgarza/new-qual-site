---
schema: qual/card@1
id: P-QX43E
kind: problem
title: Solving $\exp(A)=B$ over $\CC$ and over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Jordan Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
When and how can we solve the matrix equation $\exp(A) = B$?
Do it over the complex numbers and over the real numbers.
Give a counterexample with real entries.
:::

::: {.solution}
::: pf

::: {.pf-step #complex}
Over $\CC$, $e^A=B$ has a solution $A$ if and only if $B$ is invertible.

::: pf-proof

::: pf-step
If $e^A=B$, then $B$ is invertible.

::: pf-proof
$\det(e^A)=e^{\operatorname{tr}A}\ne0$.
:::

:::

::: pf-step
If $B$ is invertible, then $B=e^A$ for some complex matrix $A$.

::: pf-proof
Write $B=SJS^{-1}$ with $J$ in Jordan form. Each Jordan block has the form $\lambda(I+N)$ with $\lambda\ne0$ and $N^m=0$. Choose a complex logarithm $\ell$ of $\lambda$ and set
$$
L\coloneqq\ell I+\sum_{r=1}^{m-1}\frac{(-1)^{r+1}}{r}N^r .
$$
The two summands commute, and $\exp\bigl(\sum_{r\ge1}(-1)^{r+1}N^r/r\bigr)=I+N$ by the formal power series identity $\exp(\log(1+t))=1+t$, which is valid for the nilpotent $N$ because all sums are finite. Hence $e^L=\lambda(I+N)$. With $L_J$ the block diagonal matrix of these logarithms, $A\coloneqq SL_JS^{-1}$ satisfies $e^A=Se^{L_J}S^{-1}=B$.
:::

:::

:::

:::

::: pf-step
Over $\RR$, a real $B$ is $e^A$ for a real matrix $A$ if and only if $B$ is invertible and, for each negative eigenvalue of $B$, the Jordan blocks of each size occur an even number of times. In particular $\det B>0$ is necessary but not sufficient.

::: pf-proof
The equivalence is Culver's theorem on real logarithms [@Cul66]. Positive eigenvalues use the logarithm of step [](#complex){.pf-ref} with the real choice of $\ell$; a pair of conjugate nonreal blocks, or a pair of equal negative blocks, has a real logarithm block. Necessity of $\det B>0$ follows from $\det e^A=e^{\operatorname{tr}A}>0$ for real $A$.
:::

:::

::: pf-step
The real matrix $\boxed{B=\begin{pmatrix}-1&0\\0&-2\end{pmatrix}}$ has $\det B=2>0$ and is not $e^A$ for any real $A$.

::: pf-proof
Suppose $A$ is real and $e^A=B$. If $\mu$ is an eigenvalue of $A$, then $e^\mu$ is an eigenvalue of $B$, hence negative, so $\mu\notin\RR$. A real $2\times2$ matrix with a nonreal eigenvalue $\mu$ has eigenvalues $\mu,\bar\mu$, so $B$ has eigenvalues $e^\mu$ and $e^{\bar\mu}=\overline{e^\mu}=e^\mu$, because $e^\mu$ is real. This contradicts the eigenvalues $-1\ne-2$ of $B$.
:::

:::

:::
:::
