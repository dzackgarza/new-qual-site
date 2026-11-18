---
schema: qual/card@1
id: P-APA17E
kind: problem
title: Irreducible decomposition of cubic forms under $S_4$ and $\operatorname{End}_{S_4}(V)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
Consider the action of the symmetric group $S_4$ on the vector space $V = \CC[x_1, x_2, x_3, x_4]_3$ of homogeneous cubic polynomials in the variables $x_1, x_2, x_3,$ and $x_4$ given by subscript permutation:
$$
\sigma \cdot f(x_1, x_2, x_3, x_4) := f(x_{\sigma(1)}, x_{\sigma(2)}, x_{\sigma(3)}, x_{\sigma(4)})
$$
for $\sigma \in S_4$ and $f \in \CC[x_1, x_2, x_3, x_4]$.
Calculate the decomposition of $V$ into a direct sum of irreducible $S_4$-modules and determine the structure (as a product of matrix rings over $\CC$) of the endomorphism algebra $\operatorname{End}_{S_4}(V)$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own character computation is completed here, with the symmetric-cube character, its pairings and the endomorphism algebra as separate steps.

Let $W=\CC^{4}$ be the permutation representation of $S_{4}$, so $V=\CC[x_{1},\dots,x_{4}]_{3}\cong\operatorname{Sym}^{3}W$.

::: pf

::: {.pf-step #character}
$\chi_{\operatorname{Sym}^{3}}(g)=\frac{1}{6}\big(\chi(g)^{3}+3\chi(g)\chi(g^{2})+2\chi(g^{3})\big)$, and on the classes $1,(12),(12)(34),(123),(1234)$ of $S_{4}$ the values are $20,6,0,2,0$.

::: pf-proof
The cycle-index formula for $\operatorname{Sym}^{3}$ is $\frac16\big(p_{1}^{3}+3p_{1}p_{2}+2p_{3}\big)$ evaluated on the eigenvalues, which gives the displayed expression in terms of the character of $W$. The permutation character is $\chi(g)=\#\mathrm{Fix}(g)$, equal to $4,2,0,1,0$ on the five classes; with $g^{2}$ and $g^{3}$ giving $(4,4,4,1,0)$ and $(4,2,0,4,0)$ respectively, the formula yields $20,6,0,2,0$. Also $\chi(1)=20=\dim\operatorname{Sym}^{3}\CC^{4}=\binom{6}{3}$.
:::

:::

::: {.pf-step #multiplicities}
With the irreducible characters of $S_{4}$ — trivial $(1,1,1,1,1)$, sign $(1,-1,1,1,-1)$, standard $\chi_{3}=(3,1,-1,0,-1)$, $\chi_{3'}=(3,-1,-1,0,1)$, and $\chi_{2}=(2,0,2,-1,0)$ — the multiplicities are $3,0,4,1,1$.

::: pf-proof
Each multiplicity is $\langle\chi_{\operatorname{Sym}^{3}},\chi_{\alpha}\rangle=\frac{1}{24}\sum_{\text{classes}}\abs{C}\chi_{\operatorname{Sym}^{3}}\chi_{\alpha}$ with class sizes $1,6,3,8,6$: for the trivial character this is $\frac1{24}(20+36+0+16+0)=3$; for the sign character $\frac1{24}(20-36+0+16+0)=0$; for $\chi_{3}$, $\frac1{24}(60+36+0+0+0)=4$; for $\chi_{3'}$, $\frac1{24}(60-36+0+0+0)=1$; for $\chi_{2}$, $\frac1{24}(40+0+0-16+0)=1$. The dimensions add up: $3\cdot1+4\cdot3+1\cdot3+1\cdot2=20=\dim V$.
:::

:::

::: {.pf-step #decomposition}
$V\cong 3\cdot\mathbf{1}\oplus 4\cdot\chi_{3}\oplus\chi_{3'}\oplus\chi_{2}$ as $S_{4}$-modules.

::: pf-proof
Complete reducibility of finite-dimensional complex representations of a finite group and the multiplicities of step [](#multiplicities){.pf-ref} determine the isotypic decomposition; the dimension check in that step confirms no irreducible was missed.
:::

:::

::: {.pf-step #endomorphism}
$\operatorname{End}_{S_{4}}(V)\cong M_{3}(\CC)\times M_{4}(\CC)\times\CC\times\CC$.

::: pf-proof
By Schur's lemma and complete reducibility, the endomorphism algebra of a direct sum $\bigoplus_{i}V_{i}^{\oplus m_{i}}$ with $V_{i}$ pairwise non-isomorphic irreducible is $\prod_{i}M_{m_{i}}(\CC)$: an intertwiner preserves each isotypic component and acts there as a $m_{i}\times m_{i}$ matrix of scalars on the irreducible factor. With multiplicities $3,4,1,1$ from step [](#multiplicities){.pf-ref} this gives $M_{3}(\CC)\times M_{4}(\CC)\times M_{1}(\CC)\times M_{1}(\CC)$, of dimension $9+16+1+1=27$.
:::

:::

::: {.pf-qed}
$V=3\cdot\mathbf{1}\oplus4\cdot\chi_{3}\oplus\chi_{3'}\oplus\chi_{2}$ by step [](#decomposition){.pf-ref}, and $\operatorname{End}_{S_{4}}(V)\cong M_{3}(\CC)\times M_{4}(\CC)\times\CC^{2}$ by step [](#endomorphism){.pf-ref}.
:::

:::

:::
