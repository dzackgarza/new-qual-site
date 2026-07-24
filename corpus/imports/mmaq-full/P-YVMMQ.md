---
schema: qual/card@1
id: P-YVMMQ
kind: problem
title: "Let $K/F$ be a finite Galois extension and let $n=[K:F]$. There is a t…"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
Let $K/F$ be a finite Galois extension and let $n=[K:F]$. There is a theorem
(often referred to as the "normal basis theorem") which states that there
exists an irreducible polynomial $f(x)\in F[x]$ whose
roots form a basis for $K$ as a vector space over $F$. You may assume
that theorem in this problem.

- Let $G=\Gal(K/F)$. The action of $G$ on $K$ makes $K$ into
  a finite-dimensional representation space for $G$ over $F$.
  Prove that $K$ is isomorphic to the regular representation
  for $G$ over $F$.

  > The regular representation is defined by letting $G$ act
  on the group algebra $F[G]$ by multiplication on
  the left.

- Suppose that the Galois group $G$ is cyclic and that $F$
  contains a primitive $n^{\text{th}}$ root of unity. Show that
  there exists an injective homomorphism $\chi:G\rightarrow
  F^{\times}$.

- Show that $K$ contains a non-zero element $a$ with the
  following property:
  \begin{align*}
  g(a)=\chi(g)\cdot a
  .\end{align*}
  
  for all $g\in G$.

- If $a$ has the property stated in (c), show that $K=F(a)$ and
  that $a^n\in F^{\times}$.
:::
