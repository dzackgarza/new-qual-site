---
schema: qual/card@1
id: P-APAS20H
kind: problem
title: Haar integrals of $\Tr U$ and $\abs{u_{11}}^2$ over $\U(2)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the character of the defining
    representation averages to the dimension of its invariant space, which is $0$ because $-I$ sends
    $v\ne0$ to $-v$; a unitary matrix has orthonormal rows, so
    $\abs{u_{11}}^2+\abs{u_{12}}^2=1$ and the two integrals sum to $1$ against the normalised
    measure; and right multiplication by $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ interchanges the
    columns, so right invariance of Haar measure makes the two integrals equal and each is
    $\tfrac12$. Added: the trace-of-the-projector justification for averaging a character, the
    normalisation of the measure as a step, and the computation of $(UP)_{11}=u_{12}$, which the
    prose asserted. Presentation repairs: `\operatorname{Tr}` and `U(2)` are written `\Tr` and
    `\U(2)`, the vocabulary macros (STYLE-03/04), in the statement and in the proof. The collection's
    provenance is the Spring 2020 examination paper, so no retained solution set covers it.
---

::: {.problem}
Compute the integrals
$$
\int_{\U(2)}\Tr U\,dU
\qquad\text{and}\qquad
\int_{\U(2)}\abs{u_{11}}^2\,dU,
$$
where the integration is over the group of $2\times 2$ unitary matrices
$$
U=\begin{bmatrix}u_{11}&u_{12}\\ u_{21}&u_{22}\end{bmatrix}
$$
against Haar measure.
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own. Normalise Haar measure on the compact group $\U(2)$ to have total mass $1$.

::: pf

::: {.pf-step #character}
$\int_{\U(2)}\Tr U\,dU=0$.

:::: pf-proof

::: {.pf-step #no-invariant-vector}
The defining two-dimensional representation of $\U(2)$ has no nonzero invariant vector.

::: pf-proof
Let $v\ne0$ in $\CC^2$. The scalar matrix $-I$ is unitary and sends $v$ to $-v\ne v$, so $v$ is not fixed by every element of $\U(2)$; hence the space of invariant vectors is $\{0\}$.
:::

:::

::: {.pf-step}
$\int_{\U(2)}\Tr U\,dU=0$.

::: pf-proof
$U\mapsto\Tr U$ is the character of the defining representation $\rho$. Let $A=\int_{\U(2)}\rho(g)\,dg$ be the average of $\rho$ over the group; right invariance of the measure gives $\rho(h)A=A$ for every $h$, so the image of $A$ consists of invariant vectors, while $A$ fixes each invariant vector because $\rho(g)v=v$ makes the integrand constant $v$ of total mass $1$. Hence $A$ is a projection onto the space of invariant vectors, and $\Tr A$ is the dimension of that space. By step [](#no-invariant-vector){.pf-ref} that dimension is $0$, and $\Tr A=\int\Tr\rho(g)\,dg$ because the trace is linear and continuous.
:::

:::

:::

:::

::: {.pf-step #row-norm}
$\int_{\U(2)}\abs{u_{11}}^2\,dU+\int_{\U(2)}\abs{u_{12}}^2\,dU=1$.

::: pf-proof
The rows of a unitary matrix are orthonormal, so $\abs{u_{11}}^2+\abs{u_{12}}^2=1$ for every $U\in\U(2)$. Integrating this constant identity against the normalised Haar measure, the integral of $1$ being the total mass $1$, gives the displayed sum.
:::

:::

::: {.pf-step #columns}
$\int_{\U(2)}\abs{u_{11}}^2\,dU=\int_{\U(2)}\abs{u_{12}}^2\,dU$.

::: pf-proof
Let $P=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which is unitary, and note $(UP)_{11}=u_{12}$ and $(UP)_{12}=u_{11}$, since right multiplication by $P$ interchanges the columns. Right invariance of Haar measure gives
$$
\int_{\U(2)}\abs{u_{11}}^2\,dU=\int_{\U(2)}\abs{(UP)_{11}}^2\,dU=\int_{\U(2)}\abs{u_{12}}^2\,dU.
$$
:::

:::

::: {.pf-step}
$\boxed{\int_{\U(2)}\Tr U\,dU=0,\qquad \int_{\U(2)}\abs{u_{11}}^2\,dU=\tfrac12}$.

::: pf-proof
The first value is step [](#character){.pf-ref}. For the second, the two integrals of step [](#columns){.pf-ref} are equal and their sum is $1$ by step [](#row-norm){.pf-ref}, so each is $\tfrac12$; the second integral asked for is the first of the two.
:::

:::

:::
:::
