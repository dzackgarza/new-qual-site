---
schema: qual/card@1
id: P-UCLAB07F-03
kind: problem
title: A linear map whose every vector is an eigenvector is scalar
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $T:V\to V$ be linear.
If $Tv$ and $v$ are linearly dependent for every $v\in V$, show that $T$ is a scalar multiple of the identity.
:::

::: {.solution}
If $V=\{0\}$, then $T=0$ and the conclusion is immediate. Assume $V\ne\{0\}$.

<1>1. Every nonzero vector of $V$ is an eigenvector of $T$.

::: {.proof}
Let $v\ne0$. By hypothesis, $Tv$ and $v$ are linearly dependent. Hence there are scalars $a,b$, not both zero, such that
\[
aTv+bv=0.
\]
If $a=0$, then $bv=0$ forces $b=0$, a contradiction. Thus $a\ne0$, and
\[
Tv=-\frac ba\,v.
\]
So $v$ is an eigenvector.
:::

<1>2. Fix a nonzero vector $u\in V$ and write
\[
Tu=\lambda u
\]
for some scalar $\lambda$.

::: {.proof}
This is possible by step <1>1.
:::

<1>3. If $v\in V$ is linearly independent of $u$, then
\[
Tv=\lambda v.
\]

::: {.proof}
By step <1>1, there are scalars $\mu,\nu$ such that
\[
Tv=\mu v
\]
and
\[
T(u+v)=\nu(u+v).
\]
Linearity gives
\[
\lambda u+\mu v
=
Tu+Tv
=
T(u+v)
=
\nu u+\nu v.
\]
Therefore
\[
(\lambda-\nu)u+(\mu-\nu)v=0.
\]
Since $u$ and $v$ are linearly independent,
\[
\lambda=\nu=\mu.
\]
Hence $Tv=\lambda v$.
:::

<1>4. For every $v\in V$,
\[
Tv=\lambda v.
\]

::: {.proof}
If $v$ is linearly independent of $u$, apply step <1>3. If $v$ is linearly dependent on $u$, write
\[
v=cu
\]
for some scalar $c$. Then
\[
Tv=cTu=c\lambda u=\lambda v.
\]
The zero vector also satisfies the equality.
:::

<1>5. One has
\[
\boxed{T=\lambda I}.
\]

::: {.proof}
Step <1>4 says that $T$ and $\lambda I$ agree on every vector in $V$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
