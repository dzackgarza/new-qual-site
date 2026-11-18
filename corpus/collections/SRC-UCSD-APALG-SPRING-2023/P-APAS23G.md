---
schema: qual/card@1
id: P-APAS23G
kind: problem
title: $S_5$ on ordered pairs; irreducible decomposition and $\dim \operatorname{End}_{S_5}(\CC[X])$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the answer re-derived twice. The card decomposes $\CC[X]$ via the two orbits of $S_5$ on $X$; the stabiliser of an ordered off-diagonal pair is the Young subgroup $(3,1,1)$, so that piece is $\operatorname{Ind}\mathbf 1$ with characteristic $h_3h_1^2$, and two applications of Pieri give $s_{(5)}+2s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)}$; with the diagonal piece $S^{(5)}+S^{(4,1)}$ the multiplicities are $2,3,1,1$ and $\dim\operatorname{End}=4+9+1+1=15$. Every number on the card was checked independently: (i) the tensor route, $\CC[X]=\CC^A\otimes\CC^A=(\text{triv}\oplus V)^{\otimes2}$ with $V^{\otimes2}=\operatorname{Sym}^2V\oplus\Lambda^2V=S^{(5)}\oplus S^{(4,1)}\oplus S^{(3,2)}\oplus S^{(3,1,1)}$ (verified by inner products of the symmetric and exterior square characters with the character table of $S_5$), which reproduces the same multiplicities; and (ii) the orbital count $\dim\operatorname{End}=$ number of orbits of $S_5$ on $X\times X= B_4=15$, which agrees with $15$. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
The symmetric group $S_5$ acts on the set $X$ of ordered pairs $(i, j)$ of (not necessarily distinct!)
elements of $\{1, 2, 3, 4, 5\}$.
Let $\CC[X]$ be the associated permutation representation.

(1) Find the decomposition of $\CC[X]$ into irreducible $S_5$-modules.

(2) Find the dimension of the endomorphism algebra $\operatorname{End}_{S_5}(\CC[X])$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $A=\{1,2,3,4,5\}$, $X=A\times A$ and $S^\lambda$ for the irreducible $S_5$-module indexed by the partition $\lambda$ of $5$. Maschke's theorem applies, so every $S_5$-module over $\CC$ is semisimple.

::: pf

::: {.pf-step #orbits}
$X$ has the two orbits $X_= =\{(i,i)\}$, of size $5$, and $X_\ne=\{(i,j):i\ne j\}$, of size $20$, so $\CC[X]\cong\CC[X_=]\oplus\CC[X_\ne]$.

::: pf-proof
$S_5$ carries a diagonal pair $(i,i)$ to a diagonal pair and two distinct indices to two distinct indices, so both subsets are invariant. Given $(i,i)$ and $(j,j)$ there is a permutation taking $i$ to $j$; given $(i,j)$ and $(k,l)$ with $i\ne j$, $k\ne l$, extend the map $i\mapsto k$, $j\mapsto l$ to a permutation of the five letters. So each subset is a single orbit. A $G$-invariant decomposition $X=X_1\sqcup X_2$ of a $G$-set gives $\CC[X]=\CC[X_1]\oplus\CC[X_2]$.
:::

:::

::: {.pf-step #diagonal}
$\CC[X_=]\cong S^{(5)}\oplus S^{(4,1)}$.

::: pf-proof
$\CC[X_=]$ is the permutation representation of $S_5$ on five points, i.e. the natural module $\CC^A$. The constant vectors $\CC\cdot(1,\dots,1)$ form a trivial invariant subspace $S^{(5)}$, and its complement $\{x:\sum_ix_i=0\}$ is invariant of dimension $4$; that complement is irreducible, being the standard representation $S^{(4,1)}$. Hence $\CC[X_=]\cong S^{(5)}\oplus S^{(4,1)}$.
:::

:::

::: {.pf-step #stabiliser}
$\CC[X_\ne]\cong\operatorname{Ind}_{S_3\times S_1\times S_1}^{S_5}\mathbf 1$, whose Frobenius characteristic is $h_3h_1^2$.

::: pf-proof
$X_\ne$ is a single orbit, so $\CC[X_\ne]$ is the permutation module of the transitive $S_5$-set $S_5/H$ with $H$ the stabiliser of $(1,2)$; that module is $\operatorname{Ind}_H^{S_5}\mathbf 1$. Now $g$ fixes $(1,2)$ exactly when $g(1)=1$ and $g(2)=2$, so $H$ is the group of permutations of $\{3,4,5\}$, the Young subgroup $S_3\times S_1\times S_1$ for the composition $(3,1,1)$. The characteristic of $\operatorname{Ind}_{S_\mu}^{S_n}\mathbf 1$ for a Young subgroup $S_\mu$ is the complete homogeneous symmetric function $h_\mu$; here $h_{(3,1,1)}=h_3h_1^2$.
:::

:::

::: {.pf-step #pieri}
$h_3h_1^2=s_{(5)}+2s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)}$.

::: pf-proof
The Pieri rule says $s_\lambda h_1=\sum_{\mu}s_\mu$ over the partitions $\mu$ obtained from $\lambda$ by adding one box. So $s_{(3)}h_1=s_{(4)}+s_{(3,1)}$ (adding a box to $(3)$ gives $(4)$ or $(3,1)$), and applying it again,
$$
(s_{(4)}+s_{(3,1)})h_1=(s_{(5)}+s_{(4,1)})+(s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)})=s_{(5)}+2s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)},
$$
adding a box to $(4)$ and to $(3,1)$ in all ways. Finally $h_3=s_{(3)}$.
:::

:::

::: {.pf-step #decomposition}
$\CC[X]\cong 2S^{(5)}\oplus3S^{(4,1)}\oplus S^{(3,2)}\oplus S^{(3,1,1)}$.

::: pf-proof
Adding steps [](#diagonal){.pf-ref} and [](#pieri){.pf-ref} (with [](#stabiliser){.pf-ref}),
$$
\CC[X]\cong\bigl(S^{(5)}+S^{(4,1)}\bigr)+\bigl(s_{(5)}+2s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)}\bigr)=2S^{(5)}+3S^{(4,1)}+S^{(3,2)}+S^{(3,1,1)},
$$
where the Frobenius characteristic determines the module up to isomorphism (the Schur functions $s_\lambda$ are the characters, so a positive integral expansion is the multiplicity decomposition). As a check of dimensions, $2\cdot1+3\cdot4+5+6=25=\cardinality{X}$.
:::

:::

::: {.pf-step #end}
$\dim\operatorname{End}_{S_5}(\CC[X])=2^2+3^2+1^2+1^2=15$.

::: pf-proof
$\CC$ is a splitting field and the group is finite, so $\CC[S_5]$ is semisimple and the $S^\lambda$ are pairwise nonisomorphic simple modules. For such a module $M=\bigoplus_im_iV_i$, Schur's lemma gives $\operatorname{Hom}(m_iV_i,m_jV_j)=0$ for $i\ne j$ and $\operatorname{Hom}(m_iV_i,m_iV_i)\cong M_{m_i}(\CC)$, so $\operatorname{End}_{S_5}(M)\cong\prod_iM_{m_i}(\CC)$ and its dimension is $\sum_im_i^2$; with multiplicities $2,3,1,1$ by step [](#decomposition){.pf-ref} this is $4+9+1+1=15$.
:::

:::

::: {.pf-step #orbitalcheck}
The same number, independently: $\dim\operatorname{End}_{S_5}(\CC[X])$ equals the number of orbits of $S_5$ on $X\times X$, which is $15$.

::: pf-proof
For a finite group acting on a finite set, $\dim\operatorname{End}_G(\CC[X])$ is the number of orbits of $G$ on $X\times X$: the matrices constant on each orbit form a basis of the endomorphism algebra. Here an element of $X\times X$ is a $4$-tuple $(i,j,k,l)\in A^4$, and two such tuples are in the same $S_5$-orbit exactly when they have the same equality pattern, i.e. when they induce the same partition of the four positions; every partition of a four-element set is realisable because at most four distinct letters are needed and five are available. The number of such partitions is $1+6+3+4+1=15$ (the Bell number $B_4$), matching step [](#end){.pf-ref}.
:::

:::

:::
:::
