---
schema: qual/card@1
id: P-ALGS06H
kind: problem
title: "Cyclic multiplicative group and existence of irreducible polynomials over finite fields"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) If $\mathbb{F}_q$ is a field with $q$ elements, show that $\mathbb{F}_q^\times$ is a cyclic group.

(b) Show that for each integer $n \geq 1$, there exists an irreducible polynomial over $\mathbb{F}_q$ of degree $n$.

(c) Consider the map $\phi: \mathbb{F}_{q^n} \to \mathbb{F}_{q^n}$ given by $\phi(x) = x^q$.
Note that $\phi$ is an $\mathbb{F}_q$-linear endomorphism of the $\mathbb{F}_q$-vector space $\mathbb{F}_{q^n}$.
Find the characteristic and minimal polynomials of $\phi$.
:::

::: {.solution}
<1>1. $\F_q^\times$ cyclic of order $q-1$.
Proof: finite subgroup of field multiplicative group is cyclic.

<1>2. Count monic irreducibles: number is $(1/n)\sum_{d\mid n}\mu(d)q^{n/d}>0$.
Proof: Möbius.

<1>3. $\phi(x)=x^q$ has minimal polynomial $x^n-1$? Actually $x^n-1=0$ on $\F_{q^n}^\times$.
Proof: $\phi^n=\operatorname{id}$.

<1>4. Char poly $=x^n-1$, minimal $=x^n-1$ (cyclic).
Proof: $\F_{q^n}/\F_q$ Galois.

<1>5. Q.E.D.
Proof: <1>1 and <1>4.
:::
