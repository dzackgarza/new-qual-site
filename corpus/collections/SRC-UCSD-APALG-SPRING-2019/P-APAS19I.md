---
schema: qual/card@1
id: P-APAS19I
kind: problem
title: Center of a finite-dimensional $\CC$-algebra acts by scalars
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $A$ be a finite-dimensional algebra over $\CC$ with center $Z(A)$, and let $(V,\rho)$ be an irreducible representation of $A$.
Show that $\rho(z)=\chi(z)I_V$ for each $z\in Z(A)$, where $\chi(z)$ is a scalar.
Show that the map $\chi\colon Z(A)\to\CC$ defined by $z\mapsto\chi(z)$ is an algebra homomorphism.
:::

::: {.solution}

The argument is the card's own, by Schur's lemma over $\CC$; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $A$ be a finite-dimensional algebra over $\CC$ with centre $Z(A)$ and let $(V,\rho)$ be an irreducible representation of $A$.

::: pf

::: {.pf-step #commutes}
$\rho(z)\rho(a)=\rho(a)\rho(z)$ for every $z\in Z(A)$ and $a\in A$.

::: pf-proof
$\rho$ is an algebra homomorphism, so $\rho(z)\rho(a)=\rho(za)$ and $\rho(a)\rho(z)=\rho(az)$; and $za=az$ because $z$ lies in the centre. Hence the two products are equal.
:::

:::

::: {.pf-step #scalar}
For each $z\in Z(A)$ there is a unique $\chi(z)\in\CC$ with $\rho(z)=\chi(z)I_{V}$.

::: pf-proof
By step [](#commutes){.pf-ref}, $\rho(z)$ is an $A$-equivariant endomorphism of the irreducible complex module $V$, so Schur's lemma gives $\rho(z)=\lambda I_{V}$ for some $\lambda\in\CC$. The scalar is unique when $V\ne0$: the identity endomorphism of a nonzero space is not also a different scalar multiple of itself. And $V\ne0$, since the zero module is not irreducible.
:::

:::

::: {.pf-step #homomorphism}
The map $\chi:Z(A)\to\CC$, $z\mapsto\chi(z)$, is a unital $\CC$-algebra homomorphism.

::: pf-proof
For $z,w\in Z(A)$ and $c\in\CC$, additivity of $\rho$ and step [](#scalar){.pf-ref} give
$$
\rho(z+w)=\rho(z)+\rho(w)=\big(\chi(z)+\chi(w)\big)I_{V},
$$
and the scalar in step [](#scalar){.pf-ref} is unique, so $\chi(z+w)=\chi(z)+\chi(w)$. Multiplicativity of $\rho$ gives
$$
\rho(zw)=\rho(z)\rho(w)=\chi(z)\chi(w)I_{V},
$$
so $\chi(zw)=\chi(z)\chi(w)$; likewise $\rho(cz)=c\rho(z)=c\chi(z)I_{V}$ gives $\chi(cz)=c\chi(z)$; and $\rho(1_{A})=I_{V}$ gives $\chi(1_{A})=1$. So $\chi$ preserves addition, multiplication, scalars and the unit.
:::

:::

:::
:::
