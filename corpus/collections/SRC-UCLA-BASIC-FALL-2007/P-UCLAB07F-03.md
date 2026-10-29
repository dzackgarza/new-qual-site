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

::: pf

::: {.pf-step #s1-1}

Every nonzero vector of $V$ is an eigenvector of $T$.


::: pf-proof

Let $v\ne0$. By hypothesis, $Tv$ and $v$ are linearly dependent. Hence there are scalars $a,b$, not both zero, such that
$$
aTv+bv=0.
$$
If $a=0$, then $bv=0$ forces $b=0$, a contradiction. Thus $a\ne0$, and
$$
Tv=-\frac ba\,v.
$$
So $v$ is an eigenvector.

:::

:::

::: pf-step

Fix a nonzero vector $u\in V$ and write
$$
Tu=\lambda u
$$
for some scalar $\lambda$.


::: pf-proof

This is possible by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

If $v\in V$ is linearly independent of $u$, then
$$
Tv=\lambda v.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, there are scalars $\mu,\nu$ such that
$$
Tv=\mu v
$$
and
$$
T(u+v)=\nu(u+v).
$$
Linearity gives
$$
\lambda u+\mu v
=
Tu+Tv
=
T(u+v)
=
\nu u+\nu v.
$$
Therefore
$$
(\lambda-\nu)u+(\mu-\nu)v=0.
$$
Since $u$ and $v$ are linearly independent,
$$
\lambda=\nu=\mu.
$$
Hence $Tv=\lambda v$.

:::

:::

::: {.pf-step #s1-4}

For every $v\in V$,
$$
Tv=\lambda v.
$$


::: pf-proof

If $v$ is linearly independent of $u$, apply step [](#s1-3){.pf-ref}. If $v$ is linearly dependent on $u$, write
$$
v=cu
$$
for some scalar $c$. Then
$$
Tv=cTu=c\lambda u=\lambda v.
$$
The zero vector also satisfies the equality.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{T=\lambda I}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} says that $T$ and $\lambda I$ agree on every vector in $V$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
