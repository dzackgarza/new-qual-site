---
schema: qual/card@1
id: P-APAS19H
kind: problem
title: Character table of $S_3\times S_2$ and restriction of $S^{(3,2)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Part (a): the six irreducible
    characters are the external tensor products, and the table was recomputed row by row from the
    S3 and S2 tables, with the sum of squares of the degrees 1+1+4+1+1+4 = 12 = |S3 x S2| as the
    check. Part (b): the Littlewood-Richardson rule for the Young subgroup is stated once and the
    three coefficients are computed from lattice words rather than asserted; the words for the
    skew shapes (3,2)/(2) and (3,2)/(1,1) are written out, including the two contents that fail
    the lattice condition (1,3,2 and 2,1,1), so the vanishing cases are accounted for. The
    decomposition has dimension 1 + 2 + 2 = 5, and dim S^(3,2) = 5 is recomputed by the hook length
    formula with hooks 4,3,1,2,1. The card's answer is correct as it stood; the statement is
    unchanged and the card says the argument is its own.
---

::: {.problem}
Let $S_n$ be the symmetric group on $n$ letters.

(a) Calculate the character table of the product group $S_3\times S_2$.

(b) Let $\lambda=(3,2)\vdash 5$ and let $S^\lambda$ be the associated irreducible representation of $S_5$.
Calculate the decomposition of the restricted module $S^\lambda\downarrow_{S_3\times S_2}^{S_5}$ into irreducibles.
:::

::: {.solution}
Part (a) is the fact that the irreducible characters of a direct product are the external tensor products of those of the factors, applied to the three irreducible characters of $S_3$ and the two of $S_2$; part (b) is the Littlewood--Richardson branching rule for the subgroup $S_3\times S_2$ of $S_5$, whose three nonzero coefficients are computed from lattice words and checked against the dimension $\dim S^{(3,2)}=5$. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #product}
The irreducible characters of $G\times H$ over $\CC$ are exactly the functions $(g,h)\mapsto\varphi(g)\psi(h)$ with $\varphi,\psi$ irreducible characters of the factors, and the conjugacy classes of $G\times H$ are the products of conjugacy classes.

::: pf-proof
$(g,h)$ and $(g',h')$ are conjugate in $G\times H$ exactly when $g\sim g'$ in $G$ and $h\sim h'$ in $H$, since conjugation acts coordinatewise; so the classes are the products $C\times D$. For characters: the tensor product $V\otimes W$ of an irreducible $G$-module with an irreducible $H$-module, with $(g,h)$ acting as $g\otimes h$, is irreducible under $G\times H$ (a standard result, from the density of the image of $\CC[G]\otimes\CC[H]$ in $\operatorname{End}(V\otimes W)$); these give $\abs{\operatorname{Irr}G}\abs{\operatorname{Irr}H}$ distinct irreducible characters, which is the number of classes of the product, so they are all of them.
:::

:::


::: {.pf-step #s3}
The character table of $S_3$ on the classes $1$, $(12)$, $(123)$ is
$$
\begin{array}{c|ccc}
&1&(12)&(123)\\ \hline
\mathbf 1&1&1&1\\
\mathrm{sgn}&1&-1&1\\
\mathrm{std}&2&0&-1
\end{array}
$$
and the character table of $S_2$ on $1$, $\tau$ is $\mathbf 1=(1,1)$, $\mathrm{sgn}=(1,-1)$.

::: pf-proof
$S_3$ has three classes, hence three irreducible characters, of degrees $1,1,2$ summing in squares to $1+1+4=6=\abs{S_3}$. The trivial character and the sign character are the two linear ones; the standard character is the permutation character on $\CC^3$ minus the trivial summand, of degree $2$, taking the value $2$ at the identity, $0$ at a transposition (a transposition fixes one point and swaps two, so the permutation character is $1$ and subtracting the trivial gives $0$) and $-1$ at a $3$-cycle (the permutation character is $0$, minus $1$). $S_2$ has two classes and two linear characters.
:::

:::


::: {.pf-step #table}
(a) The character table of $S_3\times S_2$ on the six classes $(1,1)$, $((12),1)$, $((123),1)$, $(1,\tau)$, $((12),\tau)$, $((123),\tau)$ is the array displayed in the statement.

::: pf-proof
By steps [](#product){.pf-ref} and [](#s3){.pf-ref} the six irreducible characters are $\varphi\boxtimes\psi$ with $\varphi\in\{\mathbf1,\mathrm{sgn},\mathrm{std}\}$ and $\psi\in\{\mathbf1,\mathrm{sgn}\}$, and the value at $(g,h)$ is $\varphi(g)\psi(h)$. Evaluating: $\mathbf1\boxtimes\mathbf1$ is $1$ everywhere; a character of the form $\varphi\boxtimes\mathbf1$ takes the value $\varphi(g)$ at $(g,h)$ for either $h$, so its row is the $S_3$ row repeated on the two blocks, giving $1,-1,1,1,-1,1$ for $\mathrm{sgn}$ and $2,0,-1,2,0,-1$ for $\mathrm{std}$; $\mathbf1\boxtimes\mathrm{sgn}$ is $1$ on the first block and $-1$ on the second; $\mathrm{sgn}\boxtimes\mathrm{sgn}$ is $-\mathrm{sgn}$ on the first block and $+\mathrm{sgn}$ on the second, that is $1,-1,1,-1,1,-1$; and $\mathrm{std}\boxtimes\mathrm{sgn}$ is $2,0,-1,-2,0,1$. That is the displayed table, and the degrees satisfy $1+1+4+1+1+4=12=\abs{S_3\times S_2}$, as the sum of squares of the degrees of an irreducibles list must.
:::

:::


::: {.pf-step #lr}
(b) Littlewood--Richardson branching: for $S_k\times S_{n-k}\le S_n$,
$$
\operatorname{Res}^{S_n}_{S_k\times S_{n-k}}S^\lambda\cong\bigoplus_{\alpha\vdash k,\ \beta\vdash n-k}c^\lambda_{\alpha,\beta}\,S^\alpha\boxtimes S^\beta ,
$$
where $c^\lambda_{\alpha,\beta}$ is the number of Littlewood--Richardson tableaux of shape $\lambda/\beta$ and content $\alpha$.

::: pf-proof
This is the Littlewood--Richardson rule in the form for a Young subgroup, and it is the standard input here; the coefficients are the same ones that appear in the decomposition of a product of Schur functions, $s_\alpha s_\beta=\sum_\lambda c^\lambda_{\alpha,\beta}s_\lambda$. For $n=5$, $k=3$ the sum runs over $\alpha\vdash3$ and $\beta\vdash2$.
:::

:::


::: {.pf-step #coeffs}
For $\lambda=(3,2)$ the only nonzero coefficients are $c^{(3,2)}_{(3),(2)}=c^{(3,2)}_{(2,1),(2)}=c^{(3,2)}_{(2,1),(1,1)}=1$, all others vanishing.

::: pf-proof
Compute the lattice words. For $\beta=(2)$ the skew shape $\lambda/\beta$ has cells $(1,3)$, $(2,1)$, $(2,2)$, with no two cells in a column. Content $(3)$: all entries $1$, weakly increasing in row $2$, word $1,1,1$ lattice — one tableau. Content $(2,1)$: row $2$ weakly increasing and the word read right to left in each row, top row first, must be lattice; the fillings $((1,3),(2,1),(2,2))=(2,1,1)$ and $(1,2,2)$ give words $2,1,1$ and $1,2,2$, failing lattice, while $(1,1,2)$ gives $1,2,1$, which is lattice — one tableau. Content $(1,1,1)$: the word must begin with $1$, so $(1,3)=1$, and row $2$ weakly increasing forces $(2,1)=2$, $(2,2)=3$; the word is read right to left within each row, so it is $1,3,2$, whose prefix $1,3$ has more $3$'s than $1$'s, so it is not lattice and this content contributes nothing. For $\beta=(1,1)$ the skew cells are $(1,2)$, $(1,3)$, $(2,2)$, with $(1,2)$ and $(2,2)$ in one column. Content $(3)$: all $1$'s violate strict increase down column $2$ — nothing. Content $(2,1)$: $(1,2)=1$, $(1,3)=1$, $(2,2)=2$ is weakly increasing in row $1$, strictly increasing down column $2$, with word $1,1,2$ — one tableau. Content $(1,1,1)$: the lattice condition puts $1$ at $(1,3)$, and then weak increase in row $1$ forces $(1,2)=1$, using two $1$'s, which the content does not allow — nothing. So the three coefficients displayed are $1$ and the rest are $0$.
:::

:::


::: {.pf-step #decomp}
(b) $S^{(3,2)}\downarrow_{S_3\times S_2}\cong S^{(3)}\boxtimes S^{(2)}\oplus S^{(2,1)}\boxtimes S^{(2)}\oplus S^{(2,1)}\boxtimes S^{(1,1)}$.

::: pf-proof
Substituting the coefficients of step [](#coeffs){.pf-ref} into the rule of step [](#lr){.pf-ref}: the nonzero terms are $\alpha=(3),\beta=(2)$; $\alpha=(2,1),\beta=(2)$; and $\alpha=(2,1),\beta=(1,1)$, each with multiplicity $1$. Dimension check: $\dim S^{(3)}=1$, $\dim S^{(2,1)}=2$, $\dim S^{(2)}=1$, $\dim S^{(1,1)}=1$, so the right side has dimension $1\cdot1+2\cdot1+2\cdot1=5$; and $\dim S^{(3,2)}=5$ by the hook length formula, the hooks of $(3,2)$ being $4,3,1,2,1$ with product $24$ and $5!/24=5$. The dimensions agree, as they must for a restriction.
:::

:::


::: {.pf-step #conclusion}
Parts (a) and (b) hold as displayed.

::: pf-proof
Step [](#table){.pf-ref} gives the character table and step [](#decomp){.pf-ref} the decomposition, with step [](#coeffs){.pf-ref} the coefficient computation and the dimension check confirming it.
:::

:::

:::
:::
