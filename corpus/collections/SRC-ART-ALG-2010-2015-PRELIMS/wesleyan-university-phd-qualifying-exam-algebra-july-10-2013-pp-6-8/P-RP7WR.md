---
schema: qual/card@1
id: P-RP7WR
kind: problem
title: Finite subgroups of field automorphism groups, and of finite-field automorphism
  groups
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Automorphisms
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked both automorphism-group realization questions in July 2013 Fields 2 on PDF page 8, distinguishing arbitrary fields from finite fields."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked faithfulness and composition of the variable-permutation action, the exact Frobenius order and automorphism bound, and existence of finite fields realizing every cyclic order."
---

::: {.problem}
a. What finite groups $G$ can occur as collections of automorphisms of some field $F$?
More precisely, for which $G$ does there exist a field $F$ such that $G$ is a subgroup of the automorphism group of $F$?
Explain.

b. What finite groups $G$ can occur as collections of automorphisms of some finite field $F$?
Explain.
:::

::: solution
In part (a), every finite group occurs. In part (b), exactly
the finite cyclic groups occur, including the trivial group.

<1>1. Every finite group embeds in the automorphism group of
a field.

::: proof
Given a finite group $G$, take algebraically independent
indeterminates $X_h$ indexed by $h\in G$, and put
$F=\mathbb Q(X_h:h\in G)$. For $g\in G$, the permutation
of the indeterminates given by
$$
\sigma_g(X_h)=X_{gh}
$$
extends to a polynomial-ring automorphism fixing $\mathbb Q$,
with inverse $\sigma_{g^{-1}}$. It extends further to the
fraction field by $\sigma_g(A/B)=\sigma_g(A)/\sigma_g(B)$:
the denominator remains nonzero, and equal fractions remain
equal after applying a ring automorphism.

On every variable one has
$\sigma_g\sigma_k(X_h)=X_{gkh}=\sigma_{gk}(X_h)$.
Thus $g\mapsto\sigma_g$ is a homomorphism to
$\operatorname{Aut}(F)$. If $g\ne1$, then
$\sigma_g(X_1)=X_g\ne X_1$, so it is not the identity.
This proves injectivity and realizes $G$ as a subgroup.
:::

<1>2. The full automorphism group of any finite field is cyclic.

::: proof
Let $F$ be finite. Its characteristic is a prime $p$: the
additive order of $1$ is finite and exceeds one, and a
composite order would give zero divisors by factoring it.
The prime subfield is therefore $\mathbb F_p$. If
$[F:\mathbb F_p]=n$, then counting coordinates in a basis
gives $|F|=p^n$, with $n\geq1$.

The Frobenius map $\varphi(a)=a^p$ is a field homomorphism:
the binomial theorem in characteristic $p$ gives additivity,
and multiplication is preserved. It is injective and hence
surjective on the finite field, so is an automorphism.
Since $F^\times$ has order $p^n-1$, Lagrange's theorem gives
$a^{p^n}=a$ for every $a\in F$, including zero [@DF04].
Thus $\varphi^n=1$. If $0<d<n$ and $\varphi^d=1$, all
$p^n$ elements would be roots of the nonzero polynomial
$T^{p^d}-T$ of degree $p^d<p^n$. This contradicts the
root bound. Hence $\varphi$ has order exactly $n$.

Every automorphism of $F$ fixes $1$, and consequently fixes
the prime subfield. There are at most $n$ embeddings of
$F$ over $\mathbb F_p$ into an algebraic closure. Indeed,
adjoin a finite set of generators successively. At a step
of degree $d$, an extension of a given embedding is determined
by the image of the adjoined element, and that image must be
a root of its transformed minimal polynomial. There are at
most $d$ choices. Multiplying these bounds along the tower
gives at most the total degree $n$.

The $n$ powers of $\varphi$ are already distinct automorphisms,
so they exhaust $\operatorname{Aut}(F)$. It is therefore
$\langle\varphi\rangle\cong C_n$.
:::

<1>3. Exactly the finite cyclic groups are realized in part (b).

::: proof
Every subgroup of a cyclic group is cyclic [@DF04], so
step <1>2 proves necessity. To prove existence for every
order $n\geq1$, fix a prime $p$ and work in an algebraic
closure of $\mathbb F_p$. The polynomial $T^{p^n}-T$ has
derivative $-1$, so it has exactly $p^n$ distinct roots there.
Their set $F_n$ is a field: it contains $0,1$, and for
roots $a,b$,
$$
(a-b)^{p^n}=a-b,\qquad (ab)^{p^n}=ab,
\qquad (a^{-1})^{p^n}=a^{-1}\quad(a\ne0).
$$
The first identity follows by iterating the characteristic-$p$
binomial identity, and the other two by multiplicativity.
Thus $F_n$ is a field of cardinality $p^n$. Step <1>2 gives
$\operatorname{Aut}(F_n)\cong C_n$, realizing the prescribed
cyclic group. For $n=1$ the group is trivial.
:::
:::
