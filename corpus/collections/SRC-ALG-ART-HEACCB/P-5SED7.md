---
schema: qual/card@1
id: P-5SED7
kind: problem
title: Irreducible and indecomposable modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Principal Ideal Domains
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $R$ be a PID.

a. Classify irreducible $R\dash$modules up to isomorphism.

b. Classify indecomposable $R\dash$modules up to isomorphism.
:::

::: solution
\textbf{a) Irreducible modules.}

For a nonzero $R$-module $M$, irreducible means it has no nonzero proper
submodule, so every nonzero element generates all of $M$.
Thus irreducible modules are cyclic modules of the form
\[
M\simeq R/I
\]
with $I$ maximal.
Over a PID, maximal ideals are precisely $(p)$ for irreducible (prime) $p\in R$.
Hence
\[
M\simeq R/(p),\qquad p\ \text{prime}.
\]

\textbf{b) Indecomposable modules.}

Assume $M$ is finitely generated (the standard setting for the classification theorem).
By the structure theorem for finitely generated modules over a PID,
\[
M\simeq R^r\oplus \bigoplus_{i=1}^t R/(p_i^{n_i}),
\]
where $p_i$ are primes in $R$ and $n_i\ge1$.

This decomposition is unique up to order.
An indecomposable summand cannot split further, so the only indecomposable
f.g. modules are:
\[
R \quad\text{and}\quad R/(p^n)\ (p\ \text{prime},\ n\ge1).
\]
Any indecomposable finite direct sum is exactly one of these summands, and every
module above is a direct sum of these indecomposables.
:::
