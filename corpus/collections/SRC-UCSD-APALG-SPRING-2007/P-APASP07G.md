---
schema: qual/card@1
id: P-APASP07G
kind: problem
title: "Decomposition of an induced symmetric group module into irreducibles"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, with both Pieri applications enumerated rather than quoted. Every number was checked: the three horizontal 2-strips on (3,3) are (5,3), (4,3,1) and (3,3,2) (a box in row 1 with one in row 2 would share column 4, and rows 4 and below would put two boxes in column 1); the nine additions of a single box to those three give the eight-term product with the multiplicities 2 for (5,3,1) and 2 for (4,3,2); the four horizontal 3-strips on (3,3) are (6,3), (5,3,1), (4,3,2) and (3,3,3); and the cancellation leaves six constituents of multiplicity one. The six hook-length dimensions 42, 162, 84, 168, 216, 168 sum to 840 = 84 * 5 * 2 = [S9:S6xS3] dim V(3,3) dim V(2,1), and the two intermediate products were checked the same way (48 + 42 + 324 + 84 + 336 + 216 + 42 + 168 = 1260 = 252 * 5 for the S6 x S2 x S1 induction, and 48 + 162 + 168 + 42 = 420 = 84 * 5 for s(3,3) s(3)), all computed by hook-length formula rather than taken from the card. No retained solution set covers the exercise; the card says the argument is its own. No statement repair: the decomposition and all dimensions on the card are correct.
---

::: {.problem}
Let $W$ be the $S_9$-module obtained by inducing up from the $S_6 \times S_3$-module $V_{(3,3)} \otimes V_{(2,1)}$; here $V_\lambda$ denotes the simple $S_n$-module labeled by the Young diagram $\lambda$.
Determine the decomposition of $W$ into a direct sum of irreducible $S_9$-modules.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $\operatorname{ch}$ for the Frobenius characteristic, which sends a virtual representation of $S_n$ to a symmetric function of degree $n$ and satisfies $\operatorname{ch}(U\otimes V)=\operatorname{ch}(U)\operatorname{ch}(V)$ for $U$ an $S_m$-module and $V$ an $S_n$-module, and $\operatorname{ch}\big(\operatorname{Ind}_{S_m\times S_n}^{S_{m+n}}(U\boxtimes V)\big)=\operatorname{ch}(U)\operatorname{ch}(V)$; in particular $\operatorname{ch}V_\lambda=s_\lambda$.

::: pf

::: {.pf-step #characteristic}
$W$ has Frobenius characteristic $s_{(3,3)}s_{(2,1)}$, so its decomposition is that of this product.

::: pf-proof
$W=\operatorname{Ind}_{S_6\times S_3}^{S_9}\big(V_{(3,3)}\boxtimes V_{(2,1)}\big)$, so by the two properties above $\operatorname{ch}W=s_{(3,3)}s_{(2,1)}$. The Schur functions $s_\nu$ with $\nu$ a partition of $9$ are the characters of the pairwise nonisomorphic simple $S_9$-modules, so expanding the product in Schur functions gives the multiplicities.
:::

:::

::: {.pf-step #threeterm}
$s_{(2,1)}=s_{(2)}s_{(1)}-s_{(3)}$.

::: pf-proof
The Pieri rule for multiplying by $s_{(1)}$ says $s_{(2)}s_{(1)}=\sum_\nu s_\nu$ over the partitions $\nu$ obtained by adding one box to $(2)$, namely $(3)$ and $(2,1)$. So $s_{(2)}s_{(1)}=s_{(3)}+s_{(2,1)}$, which is the displayed identity after rearrangement.
:::

:::

::: {.pf-step #first}
$s_{(3,3)}s_{(2)}=s_{(5,3)}+s_{(4,3,1)}+s_{(3,3,2)}$.

::: pf-proof
By the Pieri rule for $s_{(2)}$, the multiplicity of $s_\nu$ is the number of ways to write $\nu/(3,3)$ as a horizontal $2$-strip, i.e. to add two boxes to $(3,3)$ with no two in the same column. A box added to row $1$ or row $2$ of $(3,3)$ occupies column $4$ or beyond, and one added to row $3$ occupies column $1$ or beyond, since row $3$ was empty; two boxes added to the same row occupy different columns. So the possibilities are: both boxes in row $1$, giving $(5,3)$; one in row $1$ and one in row $3$, giving $(4,3,1)$; both in row $3$, giving $(3,3,2)$. A box in row $1$ together with one in row $2$ would put both in column $4$, which is excluded; rows $4$ and below cannot receive two boxes without two in column $1$. So there are exactly three, each with multiplicity one.
:::

:::

::: {.pf-step #second}
$$
s_{(3,3)}s_{(2)}s_{(1)}
=s_{(6,3)}+s_{(5,4)}+2s_{(5,3,1)}+s_{(4,4,1)}+2s_{(4,3,2)}+s_{(4,3,1,1)}+s_{(3,3,3)}+s_{(3,3,2,1)} .
$$

::: pf-proof
Apply Pieri to each term of step [](#first){.pf-ref}, summing the resulting Schur functions. From $s_{(5,3)}$, adding one box gives $s_{(6,3)},s_{(5,4)},s_{(5,3,1)}$; from $s_{(4,3,1)}$ it gives $s_{(5,3,1)},s_{(4,4,1)},s_{(4,3,2)},s_{(4,3,1,1)}$; from $s_{(3,3,2)}$ it gives $s_{(4,3,2)},s_{(3,3,3)},s_{(3,3,2,1)}$. Collecting equal terms gives the displayed coefficients, two for $(5,3,1)$ and two for $(4,3,2)$ (each arises from two different summands) and one for each of the other six.
:::

:::

::: {.pf-step #third}
$s_{(3,3)}s_{(3)}=s_{(6,3)}+s_{(5,3,1)}+s_{(4,3,2)}+s_{(3,3,3)}$.

::: pf-proof
By Pieri for $s_{(3)}$, the multiplicity of $s_\nu$ is the number of ways to write $\nu/(3,3)$ as a horizontal $3$-strip. Three boxes in row $1$ give $(6,3)$; two in row $1$ (columns $4,5$) and one in row $3$ (column $1$) give $(5,3,1)$; one in row $1$ (column $4$) and two in row $3$ (columns $1,2$) give $(4,3,2)$; three in row $3$ (columns $1,2,3$) give $(3,3,3)$. Any box in row $2$ would share column $4$ with the box in row $1$ or leave a column gap, and rows $4$ and below would give two boxes in column $1$; so these four are all, each with multiplicity one.
:::

:::

::: {.pf-step #decomposition}
$s_{(3,3)}s_{(2,1)}=s_{(5,4)}+s_{(5,3,1)}+s_{(4,4,1)}+s_{(4,3,2)}+s_{(4,3,1,1)}+s_{(3,3,2,1)}$, so
$$
W\cong V_{(5,4)}\oplus V_{(5,3,1)}\oplus V_{(4,4,1)}\oplus V_{(4,3,2)}\oplus V_{(4,3,1,1)}\oplus V_{(3,3,2,1)}
$$
with every constituent of multiplicity one.

::: pf-proof
By steps [](#threeterm){.pf-ref}, [](#second){.pf-ref} and [](#third){.pf-ref},
$$
s_{(3,3)}s_{(2,1)}=s_{(3,3)}s_{(2)}s_{(1)}-s_{(3,3)}s_{(3)}
=\bigl[s_{(6,3)}+s_{(5,4)}+2s_{(5,3,1)}+s_{(4,4,1)}+2s_{(4,3,2)}+s_{(4,3,1,1)}+s_{(3,3,3)}+s_{(3,3,2,1)}\bigr]
-\bigl[s_{(6,3)}+s_{(5,3,1)}+s_{(4,3,2)}+s_{(3,3,3)}\bigr],
$$
in which $s_{(6,3)}$, $s_{(3,3,3)}$ and one copy each of $s_{(5,3,1)}$ and $s_{(4,3,2)}$ cancel; the six remaining terms have coefficient one. By step [](#characteristic){.pf-ref} the decomposition of $W$ is the same expansion.
:::

:::

::: {.pf-step #dimensions}
The six constituents have dimensions $42$, $162$, $84$, $168$, $216$, $168$, summing to $840=\dim W$.

::: pf-proof
The hook-length formula $\dim V_\lambda=9!/\prod_{c\in\lambda}h(c)$ gives
$$
\dim V_{(5,4)}=42,\quad \dim V_{(5,3,1)}=162,\quad \dim V_{(4,4,1)}=84,\quad \dim V_{(4,3,2)}=168,\quad \dim V_{(4,3,1,1)}=216,\quad \dim V_{(3,3,2,1)}=168,
$$
and $42+162+84+168+216+168=840$. On the other side, $\dim W=[S_9:S_6\times S_3]\dim V_{(3,3)}\dim V_{(2,1)}$, and $[S_9:S_6\times S_3]=9!/(6!\,3!)=84$ while $\dim V_{(3,3)}=6!/(4\cdot3\cdot2\cdot3\cdot2\cdot1)=5$ and $\dim V_{(2,1)}=2$, so $\dim W=84\cdot5\cdot2=840$; the two agree.
:::

:::

::: {.pf-step #checks}
The intermediate products have the correct total dimensions as well.

::: pf-proof
Step [](#second){.pf-ref} should have total dimension $[S_9:S_6\times S_2\times S_1]\dim V_{(3,3)}\dim V_{(2)}\dim V_{(1)}=252\cdot5=1260$, and its terms give $48+42+2\cdot162+84+2\cdot168+216+42+168=1260$. Step [](#third){.pf-ref} should have total dimension $[S_9:S_6\times S_3]\cdot5\cdot1=420$, and its terms give $48+162+168+42=420$. So each step of the computation is consistent with the dimensions of the induced modules.
:::

:::

:::
:::
