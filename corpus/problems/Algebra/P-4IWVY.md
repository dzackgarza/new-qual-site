---
schema: qual/card@1
id: P-4IWVY
kind: problem
title: Irreducible modules over a PID are $R/(p)$ and indecomposable modules are $R/(p^n)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a Principal Ideal Domain (PID).
(1) If $R$ is not a field, prove that the irreducible (simple) $R$-modules are precisely $R/(p)$ where $p\in R$ is irreducible. If $R$ is a field, show that the only simple $R$-module up to isomorphism is $R$.
(2) Prove that the finitely generated indecomposable $R$-modules are precisely $R$ and $R/(p^n)$ where $p\in R$ is irreducible and $n\ge1$.
:::

::: {.solution}
Let $M$ be a nonzero simple $R$-module and choose $0\ne m\in M$. Then $Rm=M$, so
\[
M\cong R/\operatorname{Ann}(m).
\]
Simplicity says that $\operatorname{Ann}(m)$ is maximal. If $R$ is not a field, every maximal ideal of the PID $R$ is nonzero and therefore has the form $(p)$ with $p$ irreducible. Thus $M\cong R/(p)$. Conversely, $(p)$ is maximal for irreducible $p$, so $R/(p)$ is simple. If $R$ is a field, its only maximal ideal is $(0)$, and the only simple module up to isomorphism is $R$ itself.

For part (2), the structure theorem gives every finitely generated $R$-module in the form
\[
R^r\oplus\bigoplus_i R/(p_i^{n_i}).
\]
If such a module is indecomposable, at most one nonzero summand can occur. Hence an indecomposable module must be either $R$ or $R/(p^n)$.

The module $R$ is indecomposable: a decomposition $R=I\oplus J$ would give $1=e+(1-e)$ with $e^2=e$; a domain has only the idempotents $0,1$, so one summand is zero.

Finally, the submodules of $R/(p^n)$ are exactly
\[
(p^j)/(p^n),\qquad 0\le j\le n,
\]
which form a chain. Hence two nonzero submodules cannot have zero intersection, so $R/(p^n)$ cannot decompose as a direct sum of two nonzero submodules. Therefore the finitely generated indecomposable modules are exactly $R$ and the $R/(p^n)$.
:::
