---
schema: qual/card@1
id: P-AGH2319CHEVALLEY
kind: problem
title: Images of constructible sets under a finite type morphism are constructible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Constructible Sets
  - Finite Type
  - Noetherian Induction
relations: []
review: draft
---

::: {.problem}
Let $f: X \to Y$ be a morphism of finite type of noetherian schemes.
Then the image of any constructible subset of $X$ is a constructible subset of $Y$.
In particular $f(X)$, which need not be either open or closed, is a constructible subset of $Y$.

Prove this theorem in the following steps.

a. Reduce to showing that $f(X)$ itself is constructible, in the case where $X$ and $Y$ are affine, integral, noetherian schemes and $f$ is a dominant morphism.

b. In that case, show that $f(X)$ contains a nonempty open subset of $Y$ using the following result from commutative algebra.
Let $A \subseteq B$ be an inclusion of noetherian integral domains such that $B$ is a finitely generated $A$-algebra.
Then given a nonzero element $b \in B$, there is a nonzero element $a \in A$ with the following property: if $\phi: A \to K$ is any homomorphism of $A$ into an algebraically closed field $K$ with $\phi(a) \neq 0$, then $\phi$ extends to a homomorphism $\phi'$ of $B$ into $K$ with $\phi'(b) \neq 0$.

c. Now use noetherian induction on $Y$ to complete the proof.

d. Give some examples of morphisms $f: X \to Y$ of varieties over an algebraically closed field $k$ showing that $f(X)$ need not be either open or closed.
:::

::: {.remark}
Prove the algebraic result of (b) by induction on the number of generators of $B$ over $A$; for one generator prove it directly.
In the application, take $b = 1$.
This statement is Chevalley's theorem; see Cartan and Chevalley, exposé 7, and Matsumura.
:::
