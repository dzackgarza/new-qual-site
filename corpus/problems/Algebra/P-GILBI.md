---
schema: qual/card@1
id: P-GILBI
kind: problem
title: Cayley–Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
State/prove the Cayley–Hamilton theorem.
:::

::: {.solution}
**Cayley–Hamilton.** If $A\in M_n(F)$ and
\[
\chi_A(t)=\det(tI-A),
\]
then
\[
\chi_A(A)=0.
\]

::: pf

::: {.pf-step #s1}

It suffices to prove the theorem after extending scalars to an algebraic closure $\overline F$.

::: pf-proof

The matrix $\chi_A(A)$ has entries in $F$. If it becomes the zero matrix after applying the injective map $F\hookrightarrow\overline F$, then it was already zero over $F$.

:::

:::

::: pf-step

Over $\overline F$, choose a basis in which $A$ is upper triangular with diagonal entries $\lambda_1,\dots,\lambda_n$.

::: pf-proof

Over an algebraically closed field, every linear operator admits a complete invariant flag, equivalently an upper-triangular matrix form.

:::

:::

::: {.pf-step #s3}

Let $F_i$ be the span of the first $i$ basis vectors. Then
\[
(A-\lambda_iI)F_i\subseteq F_{i-1}.
\]

::: pf-proof

Upper triangularity gives $AF_i\subseteq F_i$, and on the one-dimensional quotient $F_i/F_{i-1}$ the induced map is multiplication by the $i$th diagonal entry $\lambda_i$.

:::

:::

::: {.pf-step #s4}

Therefore
\[
(A-\lambda_1I)\cdots(A-\lambda_nI)=0.
\]

::: pf-proof

Apply the factors from right to left. By step [](#s3){.pf-ref}, the factor $A-\lambda_nI$ sends $F_n$ into $F_{n-1}$, then $A-\lambda_{n-1}I$ sends that into $F_{n-2}$, and so on, eventually into $F_0=0$.

:::

:::

::: pf-step

Since
\[
\chi_A(t)=\prod_{i=1}^n(t-\lambda_i),
\]
we obtain $\chi_A(A)=0$.

::: pf-proof

For an upper-triangular matrix the characteristic polynomial is the product of $t$ minus the diagonal entries. Combine this with step [](#s4){.pf-ref} and then descend using step [](#s1){.pf-ref}.

:::

:::

:::

:::
