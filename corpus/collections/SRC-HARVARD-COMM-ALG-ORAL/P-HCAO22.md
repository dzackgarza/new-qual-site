---
schema: qual/card@1
id: P-HCAO22
kind: problem
title: Integral closure of a one-dimensional Noetherian domain
classification:
  areas:
  - algebra
  topics:
  - Integral Closure
  - Dedekind Domains
  - Noetherian Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a one-dimensional Noetherian domain.
What can be said about its integral closure $\widetilde R$?
:::

::: {.solution}
Let $K=\operatorname{Frac}(R)$, and let $\widetilde R$ be the integral closure
of $R$ in $K$. Then $\widetilde R$ is a Dedekind domain. In particular, it is
Noetherian, integrally closed, and one-dimensional.

::: pf

::: {.pf-step #r-tilde-integrally-closed}
The ring $\widetilde R$ is integrally closed in $K$.

::: pf-proof
Let $x\in K$ be integral over $\widetilde R$. Since every element of
$\widetilde R$ is integral over $R$, transitivity of integral dependence shows
that $x$ is integral over $R$. By definition of the integral closure,
$x\in\widetilde R$.
:::

:::

::: {.pf-step #r-tilde-noetherian}
The ring $\widetilde R$ is Noetherian.

::: pf-proof
Apply the Krull--Akizuki theorem to the one-dimensional Noetherian domain $R$
and the finite field extension
\[
K/K.
\]
It states that every intermediate ring
\[
R\subseteq A\subseteq K
\]
is Noetherian. Taking $A=\widetilde R$ gives the claim.
:::

:::

::: {.pf-step #r-tilde-dimension-one}
The ring $\widetilde R$ has dimension $1$.

::: pf-proof
The extension $R\subseteq\widetilde R$ is integral. By lying over and going up,
chains of prime ideals in $R$ lift to chains in $\widetilde R$, while contraction
of a strict chain of primes in an integral extension remains strict. Hence
\[
\dim\widetilde R=\dim R=1.
\]
:::

:::

::: pf-step
Therefore $\widetilde R$ is Dedekind.

::: pf-proof
A Noetherian, integrally closed domain of dimension $1$ is a Dedekind domain.
Apply steps [](#r-tilde-integrally-closed){.pf-ref}, [](#r-tilde-noetherian){.pf-ref} and [](#r-tilde-dimension-one){.pf-ref}.
:::

:::

:::
:::

::: {.remark}
The ring $\widetilde R$ need not be a finite $R$-module: there are
one-dimensional Noetherian local domains whose integral closure is not
module-finite over them. If $R$ is a finitely generated algebra over a field,
then $\widetilde R$ is a finite $R$-module.
:::
