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
Let $m_T=p$ be irreducible, and regard $V$ as an $F[x]$-module with $x$ acting as $T$.

::: pf

::: {.pf-step #field-action}
$V$ is a vector space over the field $K\coloneqq F[x]/(p)$, and its $K$-subspaces are exactly its $T$-invariant $F$-subspaces.

::: pf-proof
Since $p(T)=0$, the $F[x]$-action factors through $F[x]/(p)$, which is a field because $p$ is irreducible. A subspace is $T$-invariant exactly when it is an $F[x]$-submodule, and the $F[x]$-submodules are exactly the $K$-submodules because the action factors through $K$.
:::

:::

::: pf-step
Every $T$-invariant subspace $W$ has a $T$-invariant complement.

::: pf-proof
By step [](#field-action){.pf-ref}, $W$ is a $K$-subspace, so it has a $K$-linear complement $W'$ with $V=W\oplus W'$. By step [](#field-action){.pf-ref} again, $W'$ is $T$-invariant.
:::

:::

:::

:::
