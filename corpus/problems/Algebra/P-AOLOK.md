---
schema: qual/card@1
id: P-AOLOK
kind: problem
title: Irreducible minimal polynomial implies every invariant subspace has an invariant
  complement
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Show that if the minimal polynomial of a linear map $T$ is irreducible, then every $T\dash$invariant subspace has a $T\dash$invariant complement.
:::


::: {.solution}
Let $V$ be a finite-dimensional vector space over a field $F$, let $T\in\operatorname{End}_F(V)$, and suppose its minimal polynomial $m_T(x)$ is irreducible.

<1>1. The algebra
\[
K=F[x]/(m_T)
\]
is a field, and $V$ is naturally a vector space over $K$.
::: {.proof}
Because $m_T$ is irreducible, the ideal $(m_T)$ is maximal in the PID $F[x]$, so $K$ is a field. Define
\[
[f(x)]\cdot v=f(T)v.
\]
This is well defined because $m_T(T)=0$, so two polynomials congruent modulo $m_T$ induce the same endomorphism of $V$. Thus the $F[x]$-module structure defined by $x\cdot v=T(v)$ factors through the field $K$.
:::

<1>2. A subspace $W\subseteq V$ is $T$-invariant if and only if it is a $K$-linear subspace.
::: {.proof}
If $W$ is $K$-linear, it is stable under the class of $x$, hence under $T$.

Conversely, if $W$ is $T$-invariant, then it is stable under every polynomial in $T$, so it is stable under the action of every class $[f(x)]\in K$. Hence $W$ is a $K$-subspace.
:::

<1>3. Every $T$-invariant subspace has a $T$-invariant complement.
::: {.proof}
Let $W\subseteq V$ be $T$-invariant. By <1>2, $W$ is a $K$-subspace of the $K$-vector space $V$. Extend a $K$-basis of $W$ to a $K$-basis of $V$, and let $U$ be the $K$-span of the added basis vectors. Then
\[
V=W\oplus U
\]
as $K$-vector spaces. Since $U$ is a $K$-subspace, <1>2 shows that $U$ is $T$-invariant. Thus $U$ is the required invariant complement.
:::
:::
