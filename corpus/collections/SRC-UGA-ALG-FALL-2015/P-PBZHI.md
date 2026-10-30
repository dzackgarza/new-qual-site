---
schema: qual/card@1
id: P-PBZHI
kind: problem
title: Every finite group is a Galois group, and intermediate fields of degrees $3$
  and $2$ in a Galois extension of degree $12$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Permutations
relations: []
review: draft
---

::: {.problem}
a.
Let $G$ be a finite group.
Show that there exists a field extension $K/F$ with $\gal(K/F) = G$.

  > You may assume that for any natural number $n$ there is a field extension with Galois group $S_n$.

b.
Let $K$ be a Galois extension of $F$ with $\abs{\gal(K/F)} = 12$.
Prove that there exists an intermediate field $E$ of $K/F$ with $[E: F] = 3$.

c.
With $K/F$ as in (b), does an intermediate field $L$ necessarily exist satisfying $[L: F] = 2$?
Give a proof or counterexample.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every finite group $G$ occurs as a Galois group of a field extension.


::: pf-proof

Let $n=\cardinality{G}$. Cayley's theorem embeds $G$ into $S_n$ by its left regular action. By the stated assumption choose a finite Galois extension $M/F$ with $\operatorname{Gal}(M/F)\cong S_n$ and identify $G$ with the corresponding subgroup. Set $E=M^G$. The fundamental theorem of Galois theory gives $M/E$ finite Galois with
$$
\boxed{\operatorname{Gal}(M/E)\cong G}.
$$
Thus taking $K=M$ and the base field to be $E$ realizes $G$.

:::

:::

::: {.pf-step #s1-2}

Every Galois extension $K/F$ of degree $12$ contains an intermediate field of degree $3$.


::: pf-proof

Put $\Gamma=\operatorname{Gal}(K/F)$, of order $12$. By Sylow's theorem $\Gamma$ contains a subgroup $H$ of order $4$. The fixed field $E=K^H$ is intermediate, and the fundamental theorem of Galois theory gives
$$
\boxed{[E:F]=[\Gamma:H]=12/4=3}.
$$

:::

:::

::: {.pf-step #s1-3}

An intermediate field of degree $2$ need not exist.


::: pf-proof

By step [](#s1-1){.pf-ref} there exists a finite Galois extension $K/F$ with $\operatorname{Gal}(K/F)\cong A_4$, of order $12$. Were there an intermediate field $L$ with $[L:F]=2$, the corresponding subgroup $\operatorname{Gal}(K/L)$ would have index $2$ and hence be normal, giving a surjective homomorphism $A_4\to C_2$. Every $3$-cycle maps to the identity because $C_2$ has no nonidentity element of order dividing $3$. But $3$-cycles generate $A_4$, so this homomorphism would be trivial, a contradiction.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, and [](#s1-3){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
