---
schema: qual/card@1
id: E-AMD-4WD576RU
kind: problem
title: An operator with irreducible minimal polynomial is semisimple
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Semisimplicity
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if the minimal polynomial of a linear operator $T: V \to V$ on a finite-dimensional vector space $V$ over a field $F$ is irreducible, then every $T$-invariant subspace has a $T$-invariant complement (i.e. $V$ is a semisimple $F[T]$-module).
:::

::: {.solution}
Let \(m_T(x)=p(x)\) be irreducible. Regard \(V\) as an \(F[x]\)-module by letting \(x\) act as \(T\). Since \(p(T)=0\), the action factors through
\[
K:=F[x]/(p),
\]
which is a field. Hence \(V\) is naturally a vector space over \(K\).

A subspace \(W\subseteq V\) is \(T\)-invariant exactly when it is an \(F[x]\)-submodule. Because the \(F[x]\)-action factors through \(K\), such a \(W\) is a \(K\)-subspace. Choose a \(K\)-linear complement \(W'\) so that
\[
V=W\oplus W'.
\]
Since \(W'\) is a \(K\)-subspace, it is stable under the class of \(x\), hence under \(T\). Thus every \(T\)-invariant subspace has a \(T\)-invariant complement.
:::
