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

::: {.proof}
1. Since $B$ is faithfully flat over $A$, a complex of $A$-modules is exact if and only if it is exact after applying $- \otimes_A B$ ([[D-DEFFFLAT]]).
   So it suffices to prove exactness of $C^\bullet \otimes_A B$, where $C^\bullet$ is the Amitsur complex.

2. Index the complex by $C^{n} = M \otimes_A B^{\otimes (n+1)}$ for $n \geq -1$, and write $D^n = B \otimes_A C^n$, placing the new factor first.
   Define $h \colon D^{n+1} \to D^{n}$ for $n \geq -1$ by multiplying the new factor into the first factor of $B^{\otimes (n+2)}$:
   $$h(c \otimes m \otimes b_1 \otimes b_2 \otimes \cdots \otimes b_{n+2}) = c\, b_1 \otimes m \otimes b_2 \otimes \cdots \otimes b_{n+2} .$$

3. Write $e_i$ also for $\id_B \otimes e_i$.
   On elementary tensors, $h \circ e_0 = \id$, since $e_0$ inserts $1$ in the first position, and $h \circ e_i = e_{i-1} \circ h$ for $i \geq 1$.
   Hence
   $$h \circ d^{n+1} = \sum_{i=0}^{n+1} (-1)^i h e_i = \id - \sum_{j=0}^{n} (-1)^j e_j h = \id - d^{n} \circ h$$
   on $D^{n}$ for $n \geq 0$, and $h \circ d^0 = \id$ on $D^{-1} = B \otimes_A M$.
   So $h$ is a contracting homotopy, $D^\bullet$ is exact, and step 1 gives exactness of $C^\bullet$.
:::

::: {.definition title="Descent data"}
A \dfn{descent datum} for $A \to B$ is a $B$-module $N$ with an isomorphism of $B \otimes_A B$-modules $\theta \colon B \otimes_A N \to N \otimes_A B$ satisfying the cocycle condition $\theta_{13} = \theta_{23} \circ \theta_{12}$ as maps $B \otimes_A B \otimes_A N \to N \otimes_A B \otimes_A B$, where $\theta_{ij}$ is $\theta$ acting on the factors in positions $i$ and $j$.
For an $A$-module $M$, the module $M \otimes_A B$ has the canonical descent datum $b \otimes (m \otimes b') \mapsto (m \otimes b) \otimes b'$.
:::

::: {.theorem title="Faithfully flat descent"}
If $A \to B$ is faithfully flat, then $M \mapsto (M \otimes_A B, \text{canonical } \theta)$ is an equivalence from $A$-modules to $B$-modules with descent data.
A quasi-inverse sends $(N, \theta)$ to $\{ n \in N : \theta(1 \otimes n) = n \otimes 1 \}$.
:::

::: {.proof}
1. For $M$ an $A$-module, the submodule of $M \otimes_A B$ of elements $x$ with $\theta(1 \otimes x) = x \otimes 1$ is the equalizer of the two maps $M \otimes_A B \rightrightarrows M \otimes_A B \otimes_A B$, which is $M$ by exactness of the Amitsur complex. So the composite starting from $A$-modules is the identity.

2. For $(N, \theta)$ with $N_0 = \{ n : \theta(1 \otimes n) = n \otimes 1 \}$, consider the natural map $N_0 \otimes_A B \to N$.
   After base change along the faithfully flat map $A \to B$ and using $\theta$ to identify $B \otimes_A N$ with $N \otimes_A B$, the cocycle condition turns $N_0 \otimes_A B$ into the equalizer computed by the Amitsur complex of the $B$-module $N$ along $B \to B \otimes_A B$, which has a section and so is exact; hence the base-changed map is an isomorphism, and by faithful flatness so is $N_0 \otimes_A B \to N$.
:::

::: {.remark}
Replacing modules by quasicoherent sheaves and $\Spec B \to \Spec A$ by a faithfully flat quasicompact morphism $S' \to S$ gives descent of quasicoherent sheaves; applied to $\Hom$ it shows that morphisms of schemes descend, which is the statement that $h_X$ is an fppf sheaf in [[D-ETFPPF]].
:::
