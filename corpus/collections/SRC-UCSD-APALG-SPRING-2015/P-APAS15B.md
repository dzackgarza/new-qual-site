---
schema: qual/card@1
id: P-APAS15B
kind: problem
title: Character table of $S_3 \times S_2$ and restriction of $S^{(2,2,1)}$
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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card. The three
    Littlewood-Richardson coefficients are now computed from the skew tableaux rather than
    quoted: for mu = (3) the skew shape does not exist; for mu = (1,1,1) the shape is a column,
    so a semistandard filling needs content (1,1) and not (2); for mu = (2,1) the shape has two
    boxes in distinct rows and columns and admits content (2) and (1,1), each with row word a
    lattice permutation. Also added: completeness of the product character table from the sum
    of squared degrees 1+1+4+1+1+4 = 12 = |S_3 x S_2|, an explicit entry computed in both
    factors, and the hook-length computation of dim S^{(2,2,1)} = 5 that the dimension check
    uses. Not claimed: a retained solution set; the provenance names the examination paper.
    Statement, the character table and the decomposition are unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card. The three
    Littlewood-Richardson coefficients are now computed from the skew tableaux rather than
    quoted: for mu = (3) the skew shape does not exist; for mu = (1,1,1) the shape is a column,
    so a semistandard filling needs content (1,1) and not (2); for mu = (2,1) the shape has two
    boxes in distinct rows and columns and admits content (2) and (1,1), each with row word a
    lattice permutation. Also added: completeness of the product character table from the sum
    of squared degrees 1+1+4+1+1+4 = 12 = |S_3 x S_2|, an explicit entry computed in both
    factors, and the hook-length computation of dim S^{(2,2,1)} = 5 that the dimension check
    uses. Not claimed: a retained solution set; the provenance names the examination paper.
    Statement, the character table and the decomposition are unchanged.
---

::: {.problem}
(1) Write down the character table of the product of symmetric groups $S_3 \times S_2$.

(2) Let $S^{(2,2,1)}$ be the irreducible representation of $S_5$ indexed by the partition $(2,2,1) \vdash 5$.
Determine the decomposition of the restriction $S^{(2,2,1)} \downarrow_{S_3 \times S_2}$ into irreducible $S_3 \times S_2$-representations.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2015 applied-algebra examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose; the Littlewood–Richardson coefficients in (2) are recomputed here from the tableaux rather than quoted.

Throughout, $\mathbf1$, $\varepsilon$, $\rho$ are the trivial, sign and standard (two-dimensional) characters of $S_3$, and $\mathbf1$, $\delta$ those of $S_2$.

::: pf

::: {.pf-step #product}
The irreducible characters of $G\times H$ are the external products $\chi\boxtimes\psi$ with $(\chi\boxtimes\psi)(g,h)=\chi(g)\psi(h)$, and the conjugacy classes of $G\times H$ are the products of classes.

::: pf-proof
$(g,h)$ and $(g',h')$ are conjugate iff both coordinates are, so classes are products and there are as many as the product of the numbers of classes; the external products are characters of irreducible representations, being the characters of the tensor products of the pulled-back representations along the two projections, and they are distinct and orthogonal, with $\langle\chi\boxtimes\psi,\chi'\boxtimes\psi'\rangle=\langle\chi,\chi'\rangle\langle\psi,\psi'\rangle$. Their number is the product of the numbers of irreducible characters of the factors, which is the number of classes of $G\times H$; so they are all of them.

:::

:::

::: {.pf-step #s3-table}
The character table of $S_3$ on the classes $1,(12),(123)$ is
$$
\begin{array}{c|rrr} &1&(12)&(123)\\\hline \mathbf1&1&1&1\\ \varepsilon&1&-1&1\\ \rho&2&0&-1\end{array}
$$
and that of $S_2$ on $1,(12)$ is
$$
\begin{array}{c|rr} &1&(12)\\\hline \mathbf1&1&1\\ \delta&1&-1\end{array}.
$$

::: pf-proof
These are the classical tables: $S_3$ has three classes, hence three irreducible characters of degrees $1,1,2$ with $1^2+1^2+2^2=6=\abs{S_3}$; $\rho$ is the standard representation on $\theset{\sum x_i=0}$, on which a transposition acts with trace $0$ and a $3$-cycle with trace $-1$. $S_2$ has two characters, trivial and sign.

:::

:::

::: {.pf-step #table}
The character table of $S_3\times S_2$ is the six-row table displayed on the card, with rows $\chi\boxtimes\psi$ and columns the products of classes in the order $\bigl(1,1\bigr)$, $\bigl((12),1\bigr)$, $\bigl((123),1\bigr)$, $\bigl(1,(12)\bigr)$, $\bigl((12),(12)\bigr)$, $\bigl((123),(12)\bigr)$.

::: pf-proof
Each entry is $\chi(g)\psi(h)$ by step [](#product){.pf-ref}, multiplying the tables of step [](#s3-table){.pf-ref}; for example $\rho\boxtimes\delta$ at $\bigl((12),(12)\bigr)$ is $0\cdot(-1)=0$ and at $\bigl((123),(12)\bigr)$ is $(-1)\cdot(-1)=1$. The six rows are distinct, mutually orthogonal under $\langle\cdot,\cdot\rangle=\frac{1}{12}\sum_{\text{classes}}\abs{\text{class}}\cdot\text{product}$ and their squared degrees $1,1,4,1,1,4$ sum to $12=\abs{S_3\times S_2}$, so the table is complete.

:::

:::

::: {.pf-step #lr}
$\operatorname{Res}^{S_5}_{S_3\times S_2}S^\lambda\cong\bigoplus_{\mu\vdash3,\ \nu\vdash2}c^\lambda_{\mu,\nu}\,S^\mu\boxtimes S^\nu$, where $c^\lambda_{\mu,\nu}$ is the number of Littlewood–Richardson tableaux of shape $\lambda/\mu$ and content $\nu$.

::: pf-proof
This is the Littlewood–Richardson rule in the form that computes the restriction to a Young subgroup $S_3\times S_2$: the multiplicity of $S^\mu\boxtimes S^\nu$ in the restriction is $c^\lambda_{\mu,\nu}$, the number of semistandard skew tableaux of shape $\lambda/\mu$ with content $\nu$ whose row word is a lattice permutation.

:::

:::

::: {.pf-step #coefficients}
For $\lambda=(2,2,1)$ the nonzero coefficients with $\multiindexsize{\mu}=3$, $\multiindexsize{\nu}=2$ are
$$
c^{(2,2,1)}_{(1,1,1),(1,1)}=c^{(2,2,1)}_{(2,1),(1,1)}=c^{(2,2,1)}_{(2,1),(2)}=1,
$$
and all others are zero.

::: pf-proof
The possible $\mu$ are $(3)$, $(2,1)$, $(1,1,1)$. For $\mu=(3)$ the skew shape $(2,2,1)/(3)$ does not exist, since $\mu_1=3>2=\lambda_1$, so both coefficients vanish there. For $\mu=(1,1,1)$ the skew shape is the column $\theset{(1,2),(2,2)}$: a semistandard filling is strictly increasing down the column, so it reads $1$ over $2$, with content $(1,1)$ and row word $12$, a lattice permutation; the content $(2)$ is impossible in a single column. Hence $c_{(1,1,1),(1,1)}=1$ and $c_{(1,1,1),(2)}=0$. For $\mu=(2,1)$ the skew shape is $\theset{(2,2),(3,1)}$, two boxes in distinct columns and rows: with entries both $1$ it has content $(2)$ and row word $11$, and with entries $1$ at $(2,2)$ and $2$ at $(3,1)$ it has content $(1,1)$ and row word $12$, both lattice; so $c_{(2,1),(2)}=c_{(2,1),(1,1)}=1$.

:::

:::

::: {.pf-step #conclusion}
$\operatorname{Res}^{S_5}_{S_3\times S_2}S^{(2,2,1)}\cong S^{(1,1,1)}\boxtimes S^{(1,1)}\oplus S^{(2,1)}\boxtimes S^{(1,1)}\oplus S^{(2,1)}\boxtimes S^{(2)}$.

::: pf-proof
Substituting the coefficients of step [](#coefficients){.pf-ref} into the rule of step [](#lr){.pf-ref} gives the displayed decomposition. Its dimension is $1\cdot1+2\cdot1+2\cdot1=5$, which agrees with $\dim S^{(2,2,1)}=5$ computed by the hook length formula: the hooks of $(2,2,1)$ are $4,2,3,1,1$, with product $24$, and $5!/24=5$.

:::

:::

:::
:::
