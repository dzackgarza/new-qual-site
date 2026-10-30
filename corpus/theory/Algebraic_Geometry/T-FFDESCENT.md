---
schema: qual/card@1
id: T-FFDESCENT
kind: definition
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

Faithful flatness makes base change reversible: the Amitsur complex is exact, and $A$-modules are exactly $B$-modules with descent data.

Let $\varphi \colon A \to B$ be a ring map, and write $B^{\otimes n} = B \otimes_A \cdots \otimes_A B$ with $n$ factors.

::: {.definition title="Amitsur complex"}
For an $A$-module $M$, the \dfn{Amitsur complex} of $M$ along $\varphi$ is
$$
0 \to M \xrightarrow{d^0} M \otimes_A B
\xrightarrow{d^1} M \otimes_A B^{\otimes 2}
\xrightarrow{d^2} M \otimes_A B^{\otimes 3} \to \cdots,
$$
where $d^0(m)=m\otimes1$ and, for $n\geq1$,
$$
d^n=\sum_{i=0}^{n}(-1)^i e_i,
$$
with
$$
e_i(m\otimes b_1\otimes\cdots\otimes b_n)
=m\otimes b_1\otimes\cdots\otimes b_i\otimes1\otimes b_{i+1}\otimes\cdots\otimes b_n.
$$
:::

::: {.theorem title="Exactness of the Amitsur complex"}
If $\varphi$ is faithfully flat, the Amitsur complex of every $A$-module $M$ is exact.
In particular the sequence $0 \to M \to M \otimes_A B \rightrightarrows M \otimes_A B \otimes_A B$, with the two maps $m \otimes b \mapsto m \otimes b \otimes 1$ and $m \otimes b \mapsto m \otimes 1 \otimes b$, is an equalizer.
:::

::: {.definition title="Descent data"}
Put $C=B\otimes_AB$, with structure maps
$$
p_1,p_2\colon B\longrightarrow C,
\qquad
p_1(b)=b\otimes1,\quad p_2(b)=1\otimes b.
$$
A \dfn{descent datum} on a $B$-module $N$ is an isomorphism of $C$-modules
$$
\theta\colon C\otimes_{B,p_1}N\xrightarrow{\sim}C\otimes_{B,p_2}N
$$
such that after pullback to $B\otimes_AB\otimes_AB$ one has the cocycle identity
$$
p_{23}^*\theta\circ p_{12}^*\theta=p_{13}^*\theta.
$$
For an $A$-module $M$, the $B$-module $M\otimes_AB$ has the canonical descent datum induced by the tautological identification of its two pullbacks to $B\otimes_AB$.
:::

::: {.theorem title="Faithfully flat descent"}
If $A \to B$ is faithfully flat, then $M \mapsto (M \otimes_A B, \text{canonical } \theta)$ is an equivalence from $A$-modules to $B$-modules with descent data.
A quasi-inverse sends $(N, \theta)$ to $\{ n \in N : \theta(1 \otimes n) = n \otimes 1 \}$.
:::

::: {.remark}
Replacing modules by quasicoherent sheaves and $\Spec B\to\Spec A$ by a faithfully flat quasicompact morphism $S'\to S$ gives fpqc descent of quasicoherent sheaves.
Representable functors are fpqc sheaves, hence in particular sheaves for the [[D-ETFPPF|fppf topology]].
:::
