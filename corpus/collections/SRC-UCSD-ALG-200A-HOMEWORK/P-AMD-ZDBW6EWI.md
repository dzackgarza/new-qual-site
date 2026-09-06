---
schema: qual/card@1
id: P-AMD-ZDBW6EWI
kind: problem
title: Automorphisms of finite cyclic groups are abelian and counted by Euler's totient
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against the concluding sentence of UCSD Math 200A Fall 2016
    Homework 2, Exercise 6. Restored the omitted hypothesis that G has order n,
    which is necessary for the stated order phi(n).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Identified Aut(G) with the unit group (Z/nZ)^x via power maps. The latter is
    abelian because multiplication modulo n is commutative and has phi(n)
    elements by the definition of Euler's totient.
---

::: {.problem}
Let $G$ be a cyclic group of order $n$.

Show that $\operatorname{Aut}(G)$ is abelian and
\[
|\operatorname{Aut}(G)|=\varphi(n).
\]
:::

::: {.solution}
Fix a generator $g$ of $G$.

<1>1. There is a group isomorphism
\[
(\mathbb Z/n\mathbb Z)^\times\cong\operatorname{Aut}(G).
\]
::: {.proof}
For an integer $a$ with $\gcd(a,n)=1$, define
\[
\sigma_a(x)=x^a.
\]
The element $g^a$ is a generator of $G$ exactly when $\gcd(a,n)=1$, so these power maps are precisely the automorphisms of $G$: an automorphism is determined by the image of $g$, and that image must be a generator.
Moreover,
\[
\sigma_a=\sigma_b\iff a\equiv b\pmod n,
\qquad
\sigma_a\circ\sigma_b=\sigma_{ab}.
\]
Hence
\[
[a]\longmapsto\sigma_a
\]
is a well-defined bijective homomorphism $(\mathbb Z/n\mathbb Z)^\times\to\operatorname{Aut}(G)$.
:::

<1>2. The group $\operatorname{Aut}(G)$ is abelian.
::: {.proof}
The ring $\mathbb Z/n\mathbb Z$ is commutative, so its group of units $(\mathbb Z/n\mathbb Z)^\times$ is abelian under multiplication.
By <1>1, $\operatorname{Aut}(G)$ is isomorphic to this abelian group, hence is abelian.
:::

<1>3. The group $\operatorname{Aut}(G)$ has order $\varphi(n)$.
::: {.proof}
The units in $\mathbb Z/n\mathbb Z$ are exactly the residue classes $[a]$ with
\[
\gcd(a,n)=1.
\]
By definition, Euler's totient $\varphi(n)$ is the number of residue classes modulo $n$ represented by integers coprime to $n$.
Therefore
\[
|(\mathbb Z/n\mathbb Z)^\times|=\varphi(n).
\]
Using <1>1,
\[
|\operatorname{Aut}(G)|=\varphi(n).
\]
:::
:::
