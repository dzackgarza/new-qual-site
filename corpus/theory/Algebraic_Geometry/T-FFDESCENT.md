---
schema: qual/card@1
id: T-FFDESCENT
kind: theorem
title: Faithfully flat descent and the Amitsur complex
classification:
  areas:
  - algebraic-geometry
  topics:
  - Descent
  - Faithfully Flat Modules
  - Amitsur Complex
relations:
- kind: uses
  target: D-DEFFFLAT
- kind: related-to
  target: D-ETFPPF
review: draft
prompts:
- What is the Amitsur complex, and why is it exact for a faithfully flat ring map?
- What is faithfully flat descent?
---

Let $\varphi \colon A \to B$ be a ring map, and write $B^{\otimes n} = B \otimes_A \cdots \otimes_A B$ with $n$ factors.

::: {.definition title="Amitsur complex"}
For an $A$-module $M$, the \dfn{Amitsur complex} of $M$ along $\varphi$ is
$$0 \to M \xrightarrow{d^0} M \otimes_A B \xrightarrow{d^1} M \otimes_A B^{\otimes 2} \xrightarrow{d^2} M \otimes_A B^{\otimes 3} \to \cdots,$$
where $d^0(m) = m \otimes 1$ and, for $n \geq 1$, $d^n = \sum_{i=0}^{n} (-1)^i e_i$ with
$$e_i(m \otimes b_1 \otimes \cdots \otimes b_n) = m \otimes b_1 \otimes \cdots \otimes b_i \otimes 1 \otimes b_{i+1} \otimes \cdots \otimes b_n .$$
:::

::: {.theorem title="Exactness of the Amitsur complex"}
If $\varphi$ is faithfully flat, the Amitsur complex of every $A$-module $M$ is exact.
In particular the sequence $0 \to M \to M \otimes_A B \rightrightarrows M \otimes_A B \otimes_A B$, with the two maps $m \otimes b \mapsto m \otimes b \otimes 1$ and $m \otimes b \mapsto m \otimes 1 \otimes b$, is an equalizer.
:::

::: {.definition title="Descent data"}
A \dfn{descent datum} for $A \to B$ is a $B$-module $N$ with an isomorphism of $B \otimes_A B$-modules $\theta \colon B \otimes_A N \to N \otimes_A B$ satisfying the cocycle condition $\theta_{13} = \theta_{23} \circ \theta_{12}$ as maps $B \otimes_A B \otimes_A N \to N \otimes_A B \otimes_A B$, where $\theta_{ij}$ is $\theta$ acting on the factors in positions $i$ and $j$.
For an $A$-module $M$, the module $M \otimes_A B$ has the canonical descent datum $b \otimes (m \otimes b') \mapsto (m \otimes b) \otimes b'$.
:::

::: {.theorem title="Faithfully flat descent"}
If $A \to B$ is faithfully flat, then $M \mapsto (M \otimes_A B, \text{canonical } \theta)$ is an equivalence from $A$-modules to $B$-modules with descent data.
A quasi-inverse sends $(N, \theta)$ to $\{ n \in N : \theta(1 \otimes n) = n \otimes 1 \}$.
:::

::: {.remark}
Replacing modules by quasicoherent sheaves and $\Spec B \to \Spec A$ by a faithfully flat quasicompact morphism $S' \to S$ gives descent of quasicoherent sheaves; applied to $\Hom$ it shows that morphisms of schemes descend, which is the statement that $h_X$ is an fppf sheaf in [[D-ETFPPF]].
:::
