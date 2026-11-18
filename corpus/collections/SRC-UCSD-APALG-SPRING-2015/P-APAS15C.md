---
schema: qual/card@1
id: P-APAS15C
kind: problem
title: Character table of $S_4$, Kronecker product of Specht modules, and its endomorphism algebra
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
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; re-checked the character table of S_4 (five classes
    with sizes summing to 24, the trivial and sign rows, chi^(3,1) as fixed points minus
    one, chi^(2,1,1) as chi^(3,1) times sign, and column orthogonality giving 24 at the
    identity), the tensor character as the pointwise product with values 18, 0, 2, 0, 0, the
    five multiplicities by the inner product, the decomposition with the dimension check 1 +
    6 + 4 + 6 + 1 = 18, and the endomorphism algebra as the product of matrix algebras of
    the multiplicities by Schur's lemma. The argument is the card's own; no retained set is
    cited. No repair needed to the answers.
---

::: {.problem}
(1) Write down the character table of the symmetric group $S_4$.

(2) For $\lambda \vdash 4$, let $S^\lambda$ denote the corresponding irreducible representation of $S_4$.
Endow the tensor product $S^{(3,1)} \otimes S^{(2,2)} \otimes S^{(2,1,1)}$ with a $S_4$-module structure by
$$
\sigma.(u \otimes v \otimes w) := (\sigma.u) \otimes (\sigma.v) \otimes (\sigma.w)
$$
for $\sigma \in S_4$, $u \in S^{(3,1)}$, $v \in S^{(2,2)}$, and $w \in S^{(2,1,1)}$.
(This is the Kronecker product.)
Find the decomposition of $S^{(3,1)} \otimes S^{(2,2)} \otimes S^{(2,1,1)}$ into irreducible $S_4$-modules.

(3) Describe the structure (as a product of matrix algebras over $\CC$) of the algebra of $S_4$-endomorphisms $\operatorname{End}_{S_4}(S^{(3,1)} \otimes S^{(2,2)} \otimes S^{(2,1,1)})$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. All computations are over $\CC$, where $\CC[S_{4}]$ is semisimple by Maschke's theorem.

::: pf

::: {.pf-step #classes}
$S_{4}$ has five conjugacy classes, indexed by the partitions of $4$, with sizes $1,6,3,8,6$.

::: pf-proof
The cycle type of a permutation determines and is determined by its conjugacy class. For the five types: $1$ identity; transpositions, of which there are $\binom{4}{2}=6$; double transpositions, of which there are $3$; $3$-cycles, $2\binom{4}{3}=8$; and $4$-cycles, $3!=6$. Their sum is $1+6+3+8+6=24=\abs{S_{4}}$.
:::

:::

::: {.pf-step #table}
The character table of $S_{4}$ is the following, rows indexed by $\lambda\vdash4$ in the order $(4),(3,1),(2,2),(2,1,1),(1^{4})$ and columns as displayed.

|  | $(1^{4})$ | $(2,1,1)$ | $(2,2)$ | $(3,1)$ | $(4)$ |
|---|---|---|---|---|---|
| $\chi^{(4)}$ | $1$ | $1$ | $1$ | $1$ | $1$ |
| $\chi^{(3,1)}$ | $3$ | $1$ | $-1$ | $0$ | $-1$ |
| $\chi^{(2,2)}$ | $2$ | $0$ | $2$ | $-1$ | $0$ |
| $\chi^{(2,1,1)}$ | $3$ | $-1$ | $-1$ | $0$ | $1$ |
| $\chi^{(1^{4})}$ | $1$ | $-1$ | $1$ | $1$ | $-1$ |

::: pf-proof
There are five irreducible characters, as many as conjugacy classes, indexed by the partitions. The first row is the trivial character; the last is the sign character, which is $+1$ on even and $-1$ on odd permutations, that is on $1^{4}$, $(2,2)$, $(3,1)$ and on $(2,1,1)$, $(4)$ respectively. The row $\chi^{(3,1)}$ is $\#$fixed points $-1$, since $S^{(3,1)}$ is the standard representation on $\{x:\sum x_{i}=0\}$; it gives $3$ at $1^{4}$, $1$ at a transposition, $-1$ at a double transposition, $0$ at a $3$-cycle and $-1$ at a $4$-cycle. The row $\chi^{(2,1,1)}$ is $\chi^{(3,1)}\otimes\chi^{(1^{4})}$, the product of those two rows, and the row $\chi^{(2,2)}$ is determined by column orthogonality, which the completed table satisfies: the sums $\sum_{\lambda}\abs{\chi^{\lambda}(C)}^{2}$ are $24$ on the identity class and $0$ on the others.
:::

:::

::: {.pf-step #tensor-character}
For the diagonal action on $V=S^{(3,1)}\otimes S^{(2,2)}\otimes S^{(2,1,1)}$ the character is the pointwise product, $\chi_{V}=\chi^{(3,1)}\chi^{(2,2)}\chi^{(2,1,1)}=(18,\,0,\,2,\,0,\,0)$, and $\dim V=18$.

::: pf-proof
On the tensor product of three modules the trace of $\sigma$ is the product of the traces, since the matrix of $\sigma$ on a tensor product is the Kronecker product of the three matrices and the trace of a Kronecker product is the product of the traces. Multiplying the rows of the table entrywise gives $3\cdot2\cdot3=18$, $1\cdot0\cdot(-1)=0$, $(-1)\cdot2\cdot(-1)=2$, $0\cdot(-1)\cdot0=0$ and $(-1)\cdot0\cdot1=0$. The dimension is the value at the identity, $18=3\cdot2\cdot3$.
:::

:::

::: {.pf-step #multiplicities}
$m_{\lambda}=\langle\chi_{V},\chi^{\lambda}\rangle=\frac{1}{24}\sum_{C}\abs{C}\chi_{V}(C)\chi^{\lambda}(C)$ takes the values $1,2,2,2,1$ for $\lambda=(4),(3,1),(2,2),(2,1,1),(1^{4})$.

::: pf-proof
The multiplicity of an irreducible in a representation is the inner product of the characters, the characters being real-valued here so that no conjugation is needed. Computing with the class sizes and the two displays:
$$
m_{(4)}=\tfrac{1}{24}\big(18+3\cdot2\big)=1,\quad
m_{(3,1)}=\tfrac{1}{24}\big(18\cdot3+3\cdot2\cdot(-1)\big)=2,\quad
m_{(2,2)}=\tfrac{1}{24}\big(18\cdot2+3\cdot2\cdot2\big)=2,
$$
$$
m_{(2,1,1)}=\tfrac{1}{24}\big(18\cdot3+3\cdot2\cdot(-1)\big)=2,\quad
m_{(1^{4})}=\tfrac{1}{24}\big(18+3\cdot2\big)=1,
$$
the classes $(2,1,1)$ and $(3,1)$ and $(4)$ contributing nothing because $\chi_{V}$ vanishes there.
:::

:::

::: {.pf-step #decomposition}
$V\cong S^{(4)}\oplus2S^{(3,1)}\oplus2S^{(2,2)}\oplus2S^{(2,1,1)}\oplus S^{(1^{4})}$.

::: pf-proof
A semisimple module is the direct sum of its isotypic components with the computed multiplicities. As a check, the dimensions agree: $1+2\cdot3+2\cdot2+2\cdot3+1=18=\dim V$.
:::

:::

::: {.pf-step #endomorphism}
$\operatorname{End}_{S_{4}}(V)\cong\CC\times M_{2}(\CC)\times M_{2}(\CC)\times M_{2}(\CC)\times\CC\cong\CC^{2}\times M_{2}(\CC)^{3}$.

::: pf-proof
For a semisimple $G$-module $V\cong\bigoplus_{i}m_{i}V_{i}$ with the $V_{i}$ pairwise nonisomorphic irreducibles, Schur's lemma gives $\operatorname{End}_{G}(V)\cong\prod_{i}M_{m_{i}}(\CC)$: a $G$-endomorphism preserves each isotypic component, and on $m_{i}$ copies of $V_{i}$ its endomorphisms are arbitrary $m_{i}\times m_{i}$ matrices, while $\operatorname{Hom}_{G}(V_{i},V_{j})=0$ for $i\ne j$. With the multiplicities of step [](#multiplicities){.pf-ref}, the three factors of multiplicity two give $M_{2}(\CC)$ and the two of multiplicity one give $\CC$.
:::

:::

::: {.pf-step}
All three parts hold.

::: pf-proof
Step [](#table){.pf-ref} is (1), step [](#decomposition){.pf-ref} is (2) and step [](#endomorphism){.pf-ref} is (3).
:::

:::

:::
:::
