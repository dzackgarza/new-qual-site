---
schema: qual/card@1
id: P-HCAO35
kind: problem
title: A one-dimensional normal domain which is not Noetherian
classification:
  areas:
  - algebra
  topics:
  - Integral Closure
  - Krull Dimension
  - Noetherian Rings
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained sheet `assets/attachments/MGSA_Commutative_Algebra_Oral_Questions.pdf`: the statement is the item "An example of a domain which is integrally closed, one-dimensional, and not noetherian",
    and its printed words are the card's. The sheet numbers nothing and prints no folios, so the
    item is identified by its position and its opening words rather than by a number. Both are now
    named in the solution's opening sentence. Not checked in this pass: the argument, which the
    edit does not touch.
---

::: {.problem}
Give an example of a one-dimensional integrally closed domain which is not Noetherian.
:::

::: {.solution}
This is the sheet `assets/attachments/MGSA_Commutative_Algebra_Oral_Questions.pdf`, Commutative Algebra section, item "An example of a domain which is integrally closed, one-dimensional, and not noetherian"; the statement below is its wording.
Let $R=\overline{\ZZ}$ be the ring of algebraic integers, the integral closure
of $\ZZ$ in $\overline{\QQ}$.

::: pf

::: pf-step
$R$ is an integrally closed domain.

::: pf-proof
As a subring of the field $\overline{\QQ}$, $R$ is a domain. Every
$\alpha\in\overline{\QQ}$ has a nonzero integer multiple in $R$, so
$\operatorname{Frac}(R)=\overline{\QQ}$. If $\alpha\in\overline{\QQ}$ is
integral over $R$, then by transitivity of integrality it is integral over
$\ZZ$, so $\alpha\in R$.
:::

:::

::: pf-step
$\dim R=1$.

::: pf-proof
The extension $\ZZ\subseteq R$ is integral. By going up and incomparability,
an integral extension preserves Krull dimension, so
$\dim R=\dim\ZZ=1$.
:::

:::

::: pf-step
$R$ is not Noetherian.

::: pf-proof
For $n\ge1$ let $I_n=\bigl(2^{1/2^n}\bigr)\subseteq R$. Since
$2^{1/2^n}=\bigl(2^{1/2^{n+1}}\bigr)^2$, we have $I_n\subseteq I_{n+1}$. The
inclusion is strict: equality would make
$$
\frac{2^{1/2^{n+1}}}{2^{1/2^n}}=2^{-1/2^{n+1}}
$$
an element of $R$, but its minimal polynomial over $\QQ$ is
$x^{2^{n+1}}-\tfrac12$, which does not have integer coefficients. The chain
$I_1\subsetneq I_2\subsetneq\cdots$ does not stabilize.
:::

:::

:::
:::
