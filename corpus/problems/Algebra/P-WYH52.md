---
schema: qual/card@1
id: P-WYH52
kind: problem
title: Character table of $S_5$
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (asks
    for the table, no repair needed), and the table itself recomputed entry by entry
    against a fresh derivation — class sizes 1, 10, 15, 20, 20, 30, 24 summing to
    120; the standard character #Fix - 1 = 4, 2, 0, 1, -1, 0, -1; its sign-twist
    4, -2, 0, 1, 1, 0, -1; the symmetric square character (chi^2 + chi(g^2))/2 giving
    10, 4, 2, 1, 1, 0, 0, from which subtracting the trivial and standard rows gives
    5, 1, 1, -1, 1, -1, 0; the exterior square (chi^2 - chi(g^2))/2 giving
    6, 0, -2, 0, 0, 0, 1; and the sign-twist of the former giving 5, -1, 1, -1, -1,
    1, 0. Every row has norm 120 = |S_5|, checked by explicit weighted sums, so each
    is irreducible, and seven irreducibles with seven classes make the table
    complete; the degrees square-sum to 120 as a further check. All correct. What
    was added: the norm computations, which the prose omitted, and the pairwise
    distinctness argument. No source solution is retained for this card, so no
    source comparison was made. What was not checked: any printed source.
---

::: {.problem}
Construct the character table of $S_5$.
:::

::: {.solution}
Let $C(\lambda)$ be the class of permutations of cycle type $\lambda\vdash5$; write $V$ for the standard representation of $S_5$ on $\{(a_1,\ldots,a_5):\sum a_i=0\}$ and $\operatorname{sgn}$ for the sign character.

::: pf

::: {.pf-step #classes}
The conjugacy classes of $S_5$ are the seven cycle types $1^5,2\,1^3,2^21,3\,1^2,3\,2,4\,1,5$, with sizes $1,10,15,20,20,30,24$.

::: pf-proof
Two permutations are conjugate exactly when they have the same cycle type, so the classes are the cycle types and there are as many of them as partitions of $5$, namely seven. The size of a class is the number of permutations of that type, which can be counted directly: $1$ for the identity; $\binom52=10$ transpositions; $\binom52\binom32/2=15$ for type $2^21$; $5\cdot4\cdot3/3=20$ for $3$-cycles; $5\cdot4\cdot3/3\cdot2/2=20$ for type $3\,2$; $5\cdot4\cdot3\cdot2/4=30$ for $4$-cycles; and $5!/5=24$ for $5$-cycles. Their sum is $1+10+15+20+20+30+24=120=\abs{S_5}$.
:::

:::

::: {.pf-step #characters}
The seven rows below are characters of representations of $S_5$:
$$\begin{array}{c|rrrrrrr}
 &1^5&2\,1^3&2^21&3\,1^2&3\,2&4\,1&5\\ \hline
[5]       &1& 1& 1& 1& 1& 1& 1\\
[4,1]     &4& 2& 0& 1&-1& 0&-1\\
[3,2]     &5& 1& 1&-1& 1&-1& 0\\
[3,1,1]   &6& 0&-2& 0& 0& 0& 1\\
[2,2,1]   &5&-1& 1&-1&-1& 1& 0\\
[2,1,1,1] &4&-2& 0& 1& 1& 0&-1\\
[1^5]     &1&-1& 1& 1&-1&-1& 1
\end{array}$$

::: pf-proof
$[5]$ is the trivial character and $[1^5]$ the sign character, whose values are the parities of the cycle types.

$[4,1]$: the permutation character $\pi$ of $S_5$ on $\CC^5$ has $\pi(g)=\#\operatorname{Fix}(g)$, and it contains the trivial character once, so $\chi_V=\pi-1=\#\operatorname{Fix}(g)-1$ is the character of $V$, of dimension $4$. Evaluating: $\#\operatorname{Fix}$ is $5,3,1,2,0,1,0$ on the seven classes, so $\chi_V=4,2,0,1,-1,0,-1$.

$[2,1,1,1]$, $[2,2,1]$: tensoring with the sign character multiplies values by the parity, giving $[2,1,1,1]=\operatorname{sgn}\otimes[4,1]$ and, later, $[2,2,1]=\operatorname{sgn}\otimes[3,2]$.

$[3,2]$ and $[3,1,1]$: for any character $\chi$ of a representation $W$, the symmetric and exterior squares have characters $\chi_{\mathrm{Sym}^2W}(g)=(\chi(g)^2+\chi(g^2))/2$ and $\chi_{\wedge^2W}(g)=(\chi(g)^2-\chi(g^2))/2$, dimensions $\binom{d+1}{2}$ and $\binom d2$ for $d=\dim W$. For $W=V$, $d=4$, so $\dim\operatorname{Sym}^2V=10$ and $\dim\wedge^2V=6$, and $\operatorname{Sym}^2V$ contains the trivial character (the invariant quadratic form $\sum a_i^2$) and, via the map $V\otimes V\to V$, the standard character; subtracting both from $\chi_{\mathrm{Sym}^2V}$ gives $\chi_{\mathrm{Sym}^2V}-1-\chi_V$, of dimension $10-1-4=5$, which is the row $[3,2]$. Computed on the classes, $\chi(g^2)$ is $\chi$ evaluated at the square of the cycle type, and the resulting values are exactly the row displayed. Similarly $\wedge^2V$ has dimension $6$ and its character is the row $[3,1,1]$; both rows were recomputed class by class from the two formulae.
:::

:::

::: {.pf-step #irreducible}
Each of the seven rows is an irreducible character: for every row $\chi$, $\sum_{\lambda}\abs{C(\lambda)}\,\chi(\lambda)^2=120=\abs{S_5}$, so $\langle\chi,\chi\rangle=1$.

::: pf-proof
For $[5]$ and $[1^5]$ the values are $\pm1$, so the sum is $\sum\abs{C(\lambda)}=120$. For $[4,1]$ and $[2,1,1,1]$ the values have equal squares, so both give $1\cdot16+10\cdot4+15\cdot0+20\cdot1+20\cdot1+30\cdot0+24\cdot1=16+40+20+20+24=120$. For $[3,2]$ and $[2,2,1]$: $1\cdot25+10\cdot1+15\cdot1+20\cdot1+20\cdot1+30\cdot1+24\cdot0=25+10+15+20+20+30=120$. For $[3,1,1]$: $1\cdot36+10\cdot0+15\cdot4+20\cdot0+20\cdot0+30\cdot0+24\cdot1=36+60+24=120$. Since a character has $\langle\chi,\chi\rangle$ a positive integer and the norm here is $120/120=1$, each row is irreducible by the character-theoretic criterion.
:::

:::

::: {.pf-step}
The table is the character table of $S_5$: it has one row for each irreducible character and is complete.

::: pf-proof
The seven rows are irreducible characters by step [](#irreducible){.pf-ref}. They are pairwise distinct: the repeated degrees are $1$, $4$ and $5$, and at the column $2\,1^3$ the two rows of degree $1$ take the values $1$ and $-1$, the two of degree $4$ take $2$ and $-2$, and the two of degree $5$ take $1$ and $-1$, so no two rows coincide; the degree-$6$ row is alone. The number of irreducible characters of a finite group equals its number of conjugacy classes, which is seven by step [](#classes){.pf-ref}, so the seven irreducible characters found are all of them. The columns are the classes and the rows the irreducible characters, which is the character table.
:::

:::

:::
:::
