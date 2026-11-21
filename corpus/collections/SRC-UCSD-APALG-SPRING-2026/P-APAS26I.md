---
schema: qual/card@1
id: P-APAS26I
kind: problem
title: Irreducible decomposition of the permutation representation of $S_n$; character table of $S_3$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
  - Character Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 9 of the Spring 2026 Applied Algebra Qualifying Exam (Math 202 A/B/C),
    printed p. 18, is the statement the card answers, and the head of the solution names it; the
    retained file assets/attachments/SP26_202_Applied_Algebra_Qual.pdf numbers every page including the
    blank versos, so Problem 9 stands on its page 18. Checked: the statement against the paper's text
    layer at the page named; the two summands of $V$ and the character table of $S_3$; `qualc.authoring
    check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained
    solution set exists for this paper to compare the argument with, and no other card of the collection
    in this pass.
---

::: {.problem}
Let $n \ge 2$.
Let $S_n = \operatorname{Aut}\{1, \ldots, n\}$ be the symmetric group, and consider the unitary representation $(V, \varphi)$ of $S_n$ in which
$$
V = \bigoplus_{i=1}^{n} \CC\diracbar i\rangle, \qquad \varphi(\pi)\diracbar i\rangle = \diracbar\pi(i)\rangle.
$$
Decompose $(V, \varphi)$ into irreducible unitary representations of $S_n$, with proof.
Write out the character table of $S_3$.
:::

::: {.solution}

The problem is Problem 9 of the Spring 2026 Applied Algebra Qualifying Exam (Math 202 A/B/C), the retained file `assets/attachments/SP26_202_Applied_Algebra_Qual.pdf` numbers the blank versos too, so the problems stand on its even pages.

No retained solution set covers this exercise: the card's own argument follows, with the two summands, the irreducibility of the standard piece and the character table as separate steps.

Let $V=\bigoplus_{i}\CC\ket{i}$ with $\varphi(\pi)\ket{i}=\ket{\pi(i)}$, and $n\ge2$.

::: pf

::: {.pf-step #trivial}
The line $U=\CC u$ spanned by $u=\ket1+\cdots+\ket n$ is an $S_{n}$-stable subspace on which $S_{n}$ acts trivially.

::: pf-proof
$\varphi(\pi)u=\sum_{i}\ket{\pi(i)}=\sum_{j}\ket{j}=u$, since $\pi$ is a bijection of $\theset{1,\dots,n}$.
:::

:::

::: {.pf-step #standard}
$W=\theset{\sum c_{i}\ket i\mid\sum c_{i}=0}$ is $S_{n}$-stable, $V=U\oplus W$, and $\dim W=n-1$.

::: pf-proof
If $\sum c_{i}=0$ then $\sum_{i}c_{i}\ket{\pi(i)}=\sum_{j}c_{\pi^{-1}(j)}\ket j$ also has coefficient sum $0$, so $W$ is stable. $U\cap W=\{0\}$ because a multiple $\lambda u$ has coefficient sum $n\lambda$, which vanishes only if $\lambda=0$; and $\dim U+\dim W=1+(n-1)=n=\dim V$, so $V=U\oplus W$.
:::

:::

::: {.pf-step #irreducible}
$W$ is irreducible.

::: pf-proof
Let $W'\ne0$ be an $S_{n}$-stable subspace of $W$ and pick $0\ne w=\sum c_{i}\ket i\in W'$. Since $\sum c_{i}=0$ and $w\ne0$, not all $c_{i}$ are equal, so there are $i\ne j$ with $c_{i}\ne c_{j}$. Then $\varphi((ij))w-w=\sum_{k}(c_{(ij)(k)}-c_{k})\ket k=(c_{j}-c_{i})\big(\ket i-\ket j\big)\in W'$, so $\ket i-\ket j\in W'$ because $c_j-c_i\ne0$. For any $k\notin\{i,j\}$ take $\pi$ with $\pi(i)=i$ and $\pi(j)=k$; then $\varphi(\pi)(\ket i-\ket j)=\ket i-\ket k\in W'$. So $W'$ contains $\ket i-\ket k$ for every $k\ne i$, and those $n-1$ vectors are independent and span $W$; hence $W'=W$.
:::

:::

::: {.pf-step #s3}
The character table of $S_{3}$ (classes: $1$; the three transpositions; the two 3-cycles):
$$\begin{array}{c|ccc} & 1 & (12) & (123)\\ \hline \text{trivial} & 1 & 1 & 1\\ \text{sign} & 1 & -1 & 1\\ \text{standard} & 2 & 0 & -1 \end{array}$$

::: pf-proof
The trivial and sign characters are clear. The permutation character of $V$ is $\chi_{V}(\pi)=\abs{\mathrm{Fix}(\pi)}$, namely $3,1,0$ on the three classes, and $\chi_{V}=\chi_{\text{triv}}+\chi_{\text{std}}$ by steps [](#trivial){.pf-ref} and [](#standard){.pf-ref}, so $\chi_{\text{std}}=(3,1,0)-(1,1,1)=(2,0,-1)$; its dimension is $n-1=2$, and $\langle\chi_{\text{std}},\chi_{\text{std}}\rangle=\frac16\big(4+3\cdot0+2\cdot1\big)=1$, confirming irreducibility by step [](#irreducible){.pf-ref}. Completeness follows from $\sum d_{i}^{2}=1+1+4=6=\abs{S_{3}}$.
:::

:::

::: {.pf-qed}
$V=U\oplus W$ with $U$ trivial, $W$ irreducible of dimension $n-1$ (steps [](#trivial){.pf-ref}, [](#standard){.pf-ref}, [](#irreducible){.pf-ref}), and the character table of $S_{3}$ is step [](#s3){.pf-ref}.
:::

:::

:::
