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
If $\varphi$ is faithfully flat, the Amitsur complex of every $A$-module $M$ is exact (Stacks Project, Lemma 35.3.6, tag 023M).
In particular the sequence $0 \to M \to M \otimes_A B \rightrightarrows M \otimes_A B \otimes_A B$ is an equalizer, the two parallel maps being $e_0$ and $e_1$ of $d^1=e_0-e_1$, that is $m \otimes b \mapsto m \otimes 1 \otimes b$ and $m \otimes b \mapsto m \otimes b \otimes 1$; both have source $M\otimes_AB$ and target $M\otimes_AB\otimes_AB$.
:::

::: {.definition title="Descent data"}
Put $C=B\otimes_AB$, with structure maps
$$
p_1,p_2\colon B\longrightarrow C,
\qquad
p_1(b)=b\otimes1,\quad p_2(b)=1\otimes b.
$$
For a $B$-module $N$ the two pullbacks to $C$ are $p_1^*N=C\otimes_{B,p_1}N\cong N\otimes_AB$ and $p_2^*N=C\otimes_{B,p_2}N\cong B\otimes_AN$, with the $B\otimes_AB$-actions $(b_1\otimes b_2)(n\otimes b)=b_1n\otimes b_2b$ and $(b_1\otimes b_2)(b\otimes n)=b_1b\otimes b_2n$.
A \dfn{descent datum} on a $B$-module $N$ is an isomorphism of $B\otimes_AB$-modules
$$
\theta\colon p_1^*N=N\otimes_AB\xrightarrow{\sim}B\otimes_AN=p_2^*N ,
$$
so the tensor order is fixed by the convention: $\theta$ goes from the first pullback to the second, and after pullback to $B\otimes_AB\otimes_AB$ it is required that the cocycle identity holds:
$$
\theta_{01}=\theta\otimes\id_B\colon N\otimes_AB\otimes_AB\longrightarrow B\otimes_AN\otimes_AB,
\qquad
\theta_{12}=\id_B\otimes\theta\colon B\otimes_AN\otimes_AB\longrightarrow B\otimes_AB\otimes_AN,
$$
with $\theta_{02}=\theta_{12}\circ\theta_{01}$, where $\theta_{01}$ is the pullback along $b\otimes b'\mapsto b\otimes b'\otimes1$, $\theta_{12}$ the pullback along $b\otimes b'\mapsto1\otimes b\otimes b'$, and $\theta_{02}\colon N\otimes_AB\otimes_AB\to B\otimes_AB\otimes_AN$ the pullback along the middle insertion $b\otimes b'\mapsto b\otimes1\otimes b'$, determined by $\theta_{02}(n\otimes1\otimes1)=\sum_ia_i\otimes1\otimes n_i$ if $\theta(n\otimes1)=\sum_ia_i\otimes n_i$ (Stacks Project, Definition 35.3.1, tag 023G).
A datum written in the opposite tensor order is $\psi=\theta^{-1}\colon p_2^*N=B\otimes_AN\to N\otimes_AB=p_1^*N$, and the two conventions are compared by the flip $\tau\colon B\otimes_AB\to B\otimes_AB$, $b\otimes b'\mapsto b'\otimes b$, together with the swap $s\colon N\otimes_AB\to B\otimes_AN$, $n\otimes b\mapsto b\otimes n$, which satisfies $s(c\cdot x)=\tau(c)\cdot s(x)$ and is therefore a map of $B\otimes_AB$-modules only after the twist by $\tau$.
The pullbacks of $\psi$ are the inverses of those of $\theta$ along the same three insertions, $\psi_{01}=\theta_{01}^{-1}\colon B\otimes_AN\otimes_AB\to N\otimes_AB\otimes_AB$, $\psi_{12}=\theta_{12}^{-1}\colon B\otimes_AB\otimes_AN\to B\otimes_AN\otimes_AB$ and $\psi_{02}=\theta_{02}^{-1}\colon B\otimes_AB\otimes_AN\to N\otimes_AB\otimes_AB$, so inverting $\theta_{02}=\theta_{12}\circ\theta_{01}$ gives $\psi_{02}=\psi_{01}\circ\psi_{12}$, the order in which $\psi_{12}$ ends where $\psi_{01}$ begins.
For an $A$-module $M$, the $B$-module $M\otimes_AB$ carries the canonical descent datum
$$
\operatorname{can}\colon (M\otimes_AB)\otimes_AB\longrightarrow B\otimes_A(M\otimes_AB),
\qquad
(m\otimes b)\otimes b'\longmapsto b\otimes(m\otimes b'),
$$
the identification of its two pullbacks to $C$ (Stacks Project, Section 35.3, tag 023F).
:::

::: {.theorem title="Faithfully flat descent"}
If $A \to B$ is faithfully flat, then $M \mapsto (M \otimes_A B, \operatorname{can})$ is an equivalence from $A$-modules to $B$-modules with descent data, and a quasi-inverse sends $(N,\theta)$ to the $A$-module
$$
\theset{n\in N:\theta(n\otimes1)=1\otimes n}
=\ker(n\mapsto 1\otimes n-\theta(n\otimes1))\subseteq N ,
$$
where $n\otimes1\in N\otimes_AB$ with the $1$ the second factor, in $B$, and where $\theta(n\otimes1)$ and $1\otimes n$ both lie in $B\otimes_AN$ with the $1$ the first factor, in $B$ (Stacks Project, Proposition 35.3.9, tag 023N, Lemma 35.3.7, tag 039W, and Remarks 59.16.8, tag 03OE).
:::

::: {.remark}
Replacing modules by quasicoherent sheaves and $\Spec B\to\Spec A$ by a faithfully flat quasicompact morphism $S'\to S$ gives fpqc descent of quasicoherent sheaves: any descent datum is effective (Stacks Project, Proposition 35.5.2, tag 023T).
Representable functors are fpqc sheaves, hence in particular sheaves for the [[D-ETFPPF|fppf topology]] (Stacks Project, Lemma 59.15.8, tag 03O3).
:::
