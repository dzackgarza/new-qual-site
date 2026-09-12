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

::: problem
Let $R$ be a one-dimensional Noetherian domain.
What can be said about its integral closure $\widetilde R$?
:::

::: solution
Let $K=\operatorname{Frac}(R)$, and let $\widetilde R$ be the integral closure
of $R$ in $K$. Then $\widetilde R$ is a Dedekind domain. In particular, it is
Noetherian, integrally closed, and one-dimensional.

<1>1. The ring $\widetilde R$ is integrally closed in $K$.
::: proof
Let $x\in K$ be integral over $\widetilde R$. Since every element of
$\widetilde R$ is integral over $R$, transitivity of integral dependence shows
that $x$ is integral over $R$. By definition of the integral closure,
$x\in\widetilde R$.
:::

<1>2. The ring $\widetilde R$ is Noetherian.
::: proof
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

<1>3. The ring $\widetilde R$ has dimension $1$.
::: proof
The extension $R\subseteq\widetilde R$ is integral. By lying over and going up,
chains of prime ideals in $R$ lift to chains in $\widetilde R$, while contraction
of a strict chain of primes in an integral extension remains strict. Hence
\[
\dim\widetilde R=\dim R=1.
\]
:::

<1>4. Therefore $\widetilde R$ is Dedekind.
::: proof
A Noetherian, integrally closed domain of dimension $1$ is a Dedekind domain.
Apply <1>1--<1>3.
:::

<1>5. The conclusion does not assert that $\widetilde R$ is finite as an
$R$-module.
::: proof
Krull--Akizuki proves Noetherianity of the intermediate ring; module-finiteness
of normalization requires additional hypotheses and can fail for
one-dimensional Noetherian domains. Thus Noetherianity and module-finiteness
must not be conflated here.
:::
:::
