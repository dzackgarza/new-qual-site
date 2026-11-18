---
schema: qual/card@1
id: P-APAS20E
kind: problem
title: Permutation representations of $S_7$ on $4$-subsets and ordered complements
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
(a) Let $X$ be the set of $4$-element subsets of $\{1,\ldots,7\}$ with the action of the symmetric group $S_7$ via permuting values.
What is the decomposition of the permutation representation $\CC[X]$ into irreducible representations?

(b) Let $Y$ be the set of pairs $(S,\sigma)$ where $S$ is a $4$-element subset of $\{1,\ldots,7\}$ and $\sigma$ is an ordering of $\{1,\ldots,7\}\setminus S$, again with the action of the symmetric group $S_7$ via permuting values.
What is the decomposition of the permutation representation $\CC[Y]$ into irreducible representations?

(c) Explain what computation regarding polynomial functors the above two problems can be used to solve.
:::

::: {.solution}

The argument is the card's own: the two permutation modules are induced from Young subgroups, so both decompositions are Pieri's rule applied to a product of complete symmetric functions; part (c) states what that product computes for polynomial functors. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Write $h_{k}$ and $s_{\lambda}$ for the complete symmetric function and the Schur function, and $S^{\lambda}$ for the irreducible representation of a symmetric group indexed by $\lambda$; the Frobenius characteristic of the permutation module on a transitive $S_{n}$-set with point stabiliser $H$ is $\operatorname{ch}\CC[S_{n}/H]=\operatorname{ch}\big(\operatorname{Ind}_{H}^{S_{n}}\mathbf 1\big)$, and for a Young subgroup $S_{\mu}$ that characteristic is $h_{\mu}$.

::: pf

::: {.pf-step #a-induced}
(a) $\CC[X]\cong\operatorname{Ind}_{S_{4}\times S_{3}}^{S_{7}}\mathbf 1$, so $\operatorname{ch}\CC[X]=h_{4}h_{3}$.

::: pf-proof
$S_{7}$ acts transitively on the $4$-element subsets of $\{1,\ldots,7\}$: any two such subsets are carried to one another by a permutation. The stabiliser of $S_{0}=\{1,2,3,4\}$ consists of the permutations preserving $S_{0}$, that is the Young subgroup $S_{4}\times S_{3}$ acting on $S_{0}$ and on its complement. A transitive $G$-set is isomorphic to $G/H$ for a point stabiliser $H$, and $\CC[G/H]\cong\operatorname{Ind}_{H}^{G}\mathbf 1$; the Frobenius characteristic of the latter is the complete symmetric function on the parts of $\mu$ when $H=S_{\mu}$, which is $h_{4}h_{3}$ here.
:::

:::

::: {.pf-step #a-pieri}
(a) $h_{4}h_{3}=s_{(7)}+s_{(6,1)}+s_{(5,2)}+s_{(4,3)}$, hence $\CC[X]\cong S^{(7)}\oplus S^{(6,1)}\oplus S^{(5,2)}\oplus S^{(4,3)}$.

::: pf-proof
Pieri's rule in the form $h_{b}s_{\lambda}=\sum_{\mu}s_{\mu}$, the sum over partitions $\mu$ of $\abs{\lambda}+b$ containing $\lambda$ with $\mu/\lambda$ a horizontal strip, applies with $b=3$ and $\lambda=(4)$, since $h_{3}=s_{(3)}$ and $h_{4}=s_{(4)}$. The partitions of $7$ containing $(4)$ are $(7)$, $(6,1)$, $(5,2)$, $(5,1,1)$, $(4,3)$, $(4,2,1)$, $(4,1,1,1)$; the three added boxes occupy distinct columns only for $(7)$ (columns $5,6,7$), $(6,1)$ (columns $5,6$ and $1$), $(5,2)$ (column $5$ and columns $1,2$) and $(4,3)$ (columns $1,2,3$), while in $(5,1,1)$, $(4,2,1)$ and $(4,1,1,1)$ two boxes share column $1$. So the four terms displayed are exactly the horizontal-strip cases, and $S^{\lambda}$ occurs in $\CC[X]$ with the multiplicity of $s_{\lambda}$ in that product. As a check, $\dim S^{(7)}=1$, $\dim S^{(6,1)}=6$, $\dim S^{(5,2)}=\dim S^{(4,3)}=14$, and $1+6+14+14=35=\binom{7}{4}=\cardinality{X}$.
:::

:::

::: {.pf-step #b-induced}
(b) $\CC[Y]\cong\operatorname{Ind}_{S_{4}\times S_{1}^{3}}^{S_{7}}\mathbf 1$, so $\operatorname{ch}\CC[Y]=h_{4}h_{1}^{3}$.

::: pf-proof
$S_{7}$ acts transitively on the pairs $(S,\sigma)$: a permutation carries $(S,\sigma)$ to $(gS,g\sigma)$. The pair is fixed by $g$ exactly when $gS=S$ and $g$ fixes the ordered tuple $\sigma$ entry by entry, that is $g$ fixes each of the three elements of the complement; so the stabiliser is $S_{4}$ on $S$ times three trivial factors, the Young subgroup $S_{4}\times S_{1}\times S_{1}\times S_{1}$. As in step [](#a-induced){.pf-ref} the characteristic is $h_{4}h_{1}^{3}$, and $h_{1}=s_{(1)}$.
:::

:::

::: {.pf-step #b-pieri}
(b) $h_{4}h_{1}^{3}=s_{(7)}+3s_{(6,1)}+3s_{(5,2)}+3s_{(5,1,1)}+s_{(4,3)}+2s_{(4,2,1)}+s_{(4,1,1,1)}$.

::: pf-proof
Apply Pieri's rule three times with $b=1$. First $h_{4}h_{1}=s_{(5)}+s_{(4,1)}$, the two partitions obtained by adding one box. Then
$$
h_{4}h_{1}^{2}=(s_{(5)}+s_{(4,1)})s_{(1)}=\big(s_{(6)}+s_{(5,1)}\big)+\big(s_{(5,1)}+s_{(4,2)}+s_{(4,1,1)}\big)=s_{(6)}+2s_{(5,1)}+s_{(4,2)}+s_{(4,1,1)},
$$
and one more multiplication by $s_{(1)}$ multiplies each term:
$$
\begin{aligned}
s_{(6)}s_{(1)}&=s_{(7)}+s_{(6,1)},\\
2s_{(5,1)}s_{(1)}&=2\big(s_{(6,1)}+s_{(5,2)}+s_{(5,1,1)}\big),\\
s_{(4,2)}s_{(1)}&=s_{(5,2)}+s_{(4,3)}+s_{(4,2,1)},\\
s_{(4,1,1)}s_{(1)}&=s_{(5,1,1)}+s_{(4,2,1)}+s_{(4,1,1,1)},
\end{aligned}
$$
and collecting the coefficients gives the displayed expansion.
:::

:::

::: {.pf-step #b-decomposition}
(b) $\CC[Y]\cong S^{(7)}\oplus3S^{(6,1)}\oplus3S^{(5,2)}\oplus3S^{(5,1,1)}\oplus S^{(4,3)}\oplus2S^{(4,2,1)}\oplus S^{(4,1,1,1)}$.

::: pf-proof
The multiplicity of $S^{\lambda}$ in $\CC[Y]$ is the coefficient of $s_{\lambda}$ in $\operatorname{ch}\CC[Y]$, which is step [](#b-pieri){.pf-ref}. As a check on the coefficients, the dimensions are $1,6,14,15,14,35,20$ for $(7),(6,1),(5,2),(5,1,1),(4,3),(4,2,1),(4,1,1,1)$, so the total is
$$
1+3\cdot6+3\cdot14+3\cdot15+14+2\cdot35+20=210=35\cdot6=\cardinality{Y},
$$
as it must be, since $Y$ consists of a $4$-subset together with one of the $3!=6$ orderings of its complement.
:::

:::

::: {.pf-step #c}
(c) The two expansions are the decompositions of the polynomial functors $\operatorname{Sym}^{4}\otimes\operatorname{Sym}^{3}$ and $\operatorname{Sym}^{4}\otimes(\mathrm{Id})^{\otimes3}$ into Schur functors.

::: pf-proof
The Frobenius characteristic is multiplicative under tensor products of homogeneous polynomial functors: for functors $F$ of degree $a$ and $G$ of degree $b$, the character of $F\otimes G$ at a permutation $\sigma\in S_{a+b}$ is the product of the characters of $F$ and $G$ at the induced permutations, so $\operatorname{ch}(F\otimes G)=\operatorname{ch}(F)\operatorname{ch}(G)$, and $\operatorname{ch}$ of the Schur functor $\schur_{\lambda}$ is $s_{\lambda}$. The functor $\operatorname{Sym}^{k}$ has characteristic $h_{k}$ and the identity functor has characteristic $h_{1}$. Hence
$$
\operatorname{ch}\big(\operatorname{Sym}^{4}\otimes\operatorname{Sym}^{3}\big)=h_{4}h_{3},\qquad \operatorname{ch}\big(\operatorname{Sym}^{4}\otimes(\mathrm{Id})^{\otimes3}\big)=h_{4}h_{1}^{3},
$$
and expanding these products in Schur functions — steps [](#a-pieri){.pf-ref} and [](#b-pieri){.pf-ref} — gives the decomposition into Schur functors displayed in (a) and (b), in every vector space of dimension at least the number of boxes.
:::

:::

:::
:::
