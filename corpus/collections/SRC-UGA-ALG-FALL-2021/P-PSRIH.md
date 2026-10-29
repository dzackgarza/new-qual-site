---
schema: qual/card@1
id: P-PSRIH
kind: problem
title: Presentation of the nonabelian group of order $63$ with an element of order
  $9$
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Semidirect Products
  - Classification
relations: []
review: draft
---
::: {.problem}
Give generators and relations (a presentation) for a non-abelian group $G$ of order $63$ containing an element of order $9$.
:::

::: {.solution}

::: pf

::: pf-step

The cyclic group $C_9$ acts nontrivially on $C_7$ by sending a generator to its square.

::: pf-proof

Let $x$ generate $C_7$. The assignment $x\mapsto x^2$ is an automorphism because $2$ is invertible modulo $7$. Its order is three: $2^3\equiv1\pmod7$, whereas $2\not\equiv1\pmod7$. Thus mapping a generator $y$ of $C_9$ to this automorphism respects $y^9=1$, giving a nontrivial homomorphism $\theta:C_9\to\operatorname{Aut}(C_7)$.

:::

:::

::: {.pf-step #s2}

The semidirect product $G=C_7\rtimes_\theta C_9$ has order $63$, contains an element of order nine, and is nonabelian.

::: pf-proof

As a set, the semidirect product consists of pairs from $C_7\times C_9$, so it has $7\cdot9=63$ elements. Its embedded subgroup $\{1\}\rtimes C_9$ contains an element $y$ of order nine. If $x$ generates the embedded $C_7$, then $yxy^{-1}=x^2\neq x$; hence $G$ is nonabelian.

:::

:::

::: {.pf-step #s3}

A presentation for the required group is
$$
\boxed{G=\langle x,y\mid x^7=1,\ y^9=1,\ yxy^{-1}=x^2\rangle}.
$$

::: pf-proof

The semidirect product constructed in step [](#s2){.pf-ref} satisfies the three displayed relations, giving a surjective homomorphism from the presented group onto $G$. Conversely, the relation $yx=x^2y$ allows every word in the presented group to be written as $x^ay^b$ with $0\leq a<7$ and $0\leq b<9$. Thus the presented group has at most $63$ elements. Its quotient $G$ has exactly $63$ elements by step [](#s2){.pf-ref}, forcing the homomorphism to be an isomorphism.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the presentation, and step [](#s2){.pf-ref} verifies the required properties.

:::

:::

:::
