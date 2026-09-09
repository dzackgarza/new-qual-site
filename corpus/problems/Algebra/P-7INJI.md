---
schema: qual/card@1
id: P-7INJI
kind: problem
title: Representations and the group algebra of $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Group Rings
  - Cyclic Groups
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
Let $k$ be a field. Discuss representations of the infinite cyclic group $\ZZ$ over $k$, and identify the group algebra $k[\ZZ]$.
:::

::: {.solution}
Write
\[
\ZZ=\langle t\rangle.
\]

<1>1. The group algebra is the Laurent polynomial ring
\[
k[\ZZ]\cong k[t,t^{-1}].
\]
::: {.proof}
An element of the group algebra is a finite sum
\[
\sum_{n\in\ZZ} a_n t^n,
\qquad a_n\in k,
\]
with multiplication induced by $t^m t^n=t^{m+n}$. This is exactly the ring of Laurent polynomials in one invertible indeterminate.
:::

<1>2. A representation
\[
\rho:\ZZ\to\operatorname{GL}(V)
\]
is determined uniquely by the single invertible operator
\[
T=\rho(1).
\]
::: {.proof}
For every $n\in\ZZ$,
\[
\rho(n)=\rho(1)^n=T^n.
\]
Conversely, any $T\in\operatorname{GL}(V)$ defines a representation by $n\mapsto T^n$.
:::

<1>3. Equivalently, representations of $\ZZ$ over $k$ are precisely modules over $k[t,t^{-1}]$.
::: {.proof}
Given a representation, let $t$ act as $T=\rho(1)$ and $t^{-1}$ as $T^{-1}$; this extends uniquely to an action of $k[t,t^{-1}]$. Conversely, restricting a $k[t,t^{-1}]$-module to the units $t^n$ gives a representation of $\ZZ$. These constructions are inverse.
:::

<1>4. Finite-dimensional representations are therefore classified by invertible linear operators up to similarity.
::: {.proof}
A change of basis conjugates $T$. Two representations are isomorphic exactly when their defining operators are conjugate in $\operatorname{GL}(V)$. Thus rational canonical form, or Jordan form over a splitting field, gives the usual classification.
:::

<1>5. If $k$ is algebraically closed, every finite-dimensional irreducible representation of $\ZZ$ is one-dimensional.
::: {.proof}
Let $V$ be a nonzero finite-dimensional irreducible representation and let $T=\rho(1)$. Since $k$ is algebraically closed, $T$ has an eigenvector $0\ne v\in V$ with
\[
Tv=\lambda v,
\qquad \lambda\ne0
\]
because $T$ is invertible. The line $kv$ is invariant under both $T$ and $T^{-1}$, hence under all of $\ZZ$. Irreducibility forces $V=kv$.
:::

<1>6. Thus, over algebraically closed $k$, irreducible representations are indexed by scalars $\lambda\in k^\times$, with
\[
1\in\ZZ
\]
acting as multiplication by $\lambda$.
::: {.proof}
Every one-dimensional representation has this form, and <1>5 shows there are no other finite-dimensional irreducibles.
:::
:::
