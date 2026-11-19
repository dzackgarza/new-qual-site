---
schema: qual/card@1
id: P-CC3DW
kind: problem
title: A square matrix is similar to its transpose
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Canonical Forms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Second provenance recorded: the same question is Problem 8 of the Algebra Preliminary
    Examination of September 8, 2008 (University of Washington), printed p. 2 of the two-page paper
    retained at assets/attachments/UW-Algebra-Qual-2008.pdf, and the 2008 collection's index lists
    this card among its problems. The paragraph at the head of the solution now says so. Checked:
    the statement against the 2008 paper's text layer at the page named, and the matching of the
    wording to Problem 8 there; `qualc.authoring check` on the card, and `tmp/lam.sh` for the
    numbering and the QED. Not checked: the 2008 paper's own statement is not re-proved in this
    pass, the mathematics of the card is unchanged, and no other card of the 2008 collection is
    touched here.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Every step checked: the rational canonical form over an arbitrary field with its uniqueness; the transpose of a conjugate being the conjugate by the transpose; the transpose of a block-diagonal matrix; and the companion matrix's properties, which the prose quoted as standard and which are now proved from the cyclic vector e_1: C^i e_1 = e_{i+1} for i < d, p(C)e_1 = 0 because Ce_d = -(a_0 e_1 + ... + a_{d-1} e_d), hence p(C) = 0 since e_1 is cyclic, hence the minimal polynomial divides p and has degree at least d, hence equals p, hence equals the characteristic polynomial. The step passing from "same minimal polynomial" to "same invariant factors" now says why: min poly of degree equal to the dimension forces a single block. One thing the prose left implicit is now stated: conjugation acts blockwise on a direct sum, so the blockwise similarities assemble into one similarity of the whole direct sum. No statement repair; the proof was already correct over any field, which is what the exercise asks.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repair of the review finding of 16:21Z, which commit 3c891fdd addressed incompletely. The restated definition of a cyclic matrix still quantified over an unnamed vector ("the vectors $v, Cv, \dots, C^{d-1}v$ span $K^d$"), which is the false universal reading the finding objected to; it now says there is a vector $v$ whose iterates form a basis, and records that the iterates are dependent for most $v$. In the companion-matrix step the bound on $\deg\mu$ referred to an undefined symbol $m$ and asserted a dependence without saying where it came from; it now argues that a monic $\mu$ of degree $m<d$ makes $e_1,\dots,C^me_1$ dependent while $C^ie_1=e_{i+1}$ makes them independent, so $\deg\mu\ge d$. No statement repair; nothing else on the card changed.
---

::: {.problem}
Let $M$ be a square matrix over a field $K$.
Use a suitable canonical form to show that $M$ is similar to its transpose $M^T$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own. The same question also stands as Problem 8 of the Algebra Preliminary Examination of September 8, 2008 (University of Washington), printed p. 2 of `assets/attachments/UW-Algebra-Qual-2008.pdf`, which is the paper the 2008 collection retains; that paper prints no solutions either.

Recall that two $n\times n$ matrices are similar when $M'=SMS^{-1}$ for some invertible $S$, that similarity is an equivalence relation, and that a matrix $C\in M_d(K)$ is cyclic when it has a cyclic vector: a vector $v\in K^d$ for which $v,Cv,\dots,C^{d-1}v$ is a basis of $K^d$. The quantifier matters here; a single $v$ is never asked to serve for every vector, and $v,Cv,\dots,C^{d-1}v$ is indeed dependent for most $v$.

::: pf

::: {.pf-step #rcf}
$M$ is similar over $K$ to a direct sum of companion matrices, $M\sim C(p_1)\oplus\cdots\oplus C(p_k)$, with each $p_i\in K[x]$ monic.

::: pf-proof
The rational canonical form (Frobenius normal form) theorem: over any field, every square matrix is similar to a direct sum of companion matrices $C(p_1)\oplus\cdots\oplus C(p_k)$ of monic polynomials with $p_1\mid p_2\mid\cdots\mid p_k$, and the list $p_1,\dots,p_k$ (the invariant factors) is uniquely determined by the similarity class. In particular $\sum_i\deg p_i=n$ if $M$ is $n\times n$.
:::

:::

::: {.pf-step #transpose}
$M^T\sim C(p_1)^T\oplus\cdots\oplus C(p_k)^T$.

::: pf-proof
If $M=SNS^{-1}$ then $M^T=(S^{-1})^TN^TS^T=(S^T)^{-1}N^TS^T$, so $M^T$ is similar to $N^T$. The transpose of a block-diagonal matrix is the block-diagonal matrix of the transposed blocks, because transposition does not mix distinct block rows and columns and reverses the order of the factors inside each block. Applying this to $N=C(p_1)\oplus\cdots\oplus C(p_k)$ from step [](#rcf){.pf-ref} gives the claim.
:::

:::

::: {.pf-step #companion}
For the companion matrix $C=C(p)$ of a monic $p=x^d+a_{d-1}x^{d-1}+\cdots+a_0$, the minimal polynomial and the characteristic polynomial both equal $p$, and $C$ is cyclic.

::: pf-proof
Write $e_1,\dots,e_d$ for the standard basis and let $C$ have columns $e_2,e_3,\dots,e_d,-a_0e_1-\cdots-a_{d-1}e_d$. Then $C^ie_1=e_{i+1}$ for $0\le i\le d-1$, so $e_1,Ce_1,\dots,C^{d-1}e_1$ is the standard basis and $C$ is cyclic with cyclic vector $e_1$. Moreover
$$
p(C)e_1=C^de_1+a_{d-1}C^{d-1}e_1+\cdots+a_0e_1=C e_d+a_{d-1}e_d+\cdots+a_0e_1=0,
$$
the last equality because $Ce_d=-a_0e_1-\cdots-a_{d-1}e_d$; as $K[C]e_1=K^d$, $p(C)=0$, so the minimal polynomial $\mu$ of $C$ divides $p$. If $\mu$ had degree $m<d$, then $\mu(C)e_1=0$ — with $\mu$ monic of degree $m$ — would write $C^me_1$ as a combination of $e_1,\dots,C^{m-1}e_1$, making $e_1,\dots,C^me_1$ dependent; but these are $e_1,\dots,e_{m+1}$, the first $m+1\le d$ vectors of the standard basis, which are independent. Hence $\deg\mu\ge d=\deg p$, and with $\mu\mid p$ this gives $\mu=p$. The characteristic polynomial $\chi_C$ is monic of degree $d$ and $\mu\mid\chi_C$, so $\chi_C=p$ as well.
:::

:::

::: {.pf-step #transposemin}
The minimal polynomial of $C^T$ is $p$, and $C^T$ is cyclic with the single invariant factor $p$.

::: pf-proof
For every $q\in K[x]$ one has $q(C^T)=q(C)^T$: transposition is additive and reverses products, so it carries $\sum c_iC^i$ to $\sum c_i(C^T)^i$. Hence $q(C^T)=0$ if and only if $q(C)=0$, and the annihilator ideals, and therefore the minimal polynomials, of $C^T$ and $C$ coincide; by step [](#companion){.pf-ref} this common minimal polynomial is $p$. Now $C^T$ is $d\times d$, so by step [](#rcf){.pf-ref} it has invariant factors $q_1\mid q_2\mid\cdots\mid q_k$ with $\sum_i\deg q_i=d$; the largest invariant factor is the minimal polynomial (each block $C(q_i)$ has minimal polynomial $q_i$, and since $q_i\mid q_k$ the annihilator of the whole direct sum is the ideal generated by $q_k$), so $q_k=p$ and $\deg q_k=d$, and $\deg q_i\ge1$ for every $i$ then forces $k=1$. So the rational canonical form of $C^T$ is the single block $C(p)$, that is, $C^T$ is cyclic with invariant factor $p$.
:::

:::

::: {.pf-step #blocksimilar}
$C(p)\sim C(p)^T$ over $K$.

::: pf-proof
Steps [](#companion){.pf-ref} and [](#transposemin){.pf-ref} give both matrices the same invariant factor list, namely the single polynomial $p$. By the uniqueness of the rational canonical form (step [](#rcf){.pf-ref}), matrices with equal invariant factor lists are similar.
:::

:::

::: {.pf-step}
$M\sim M^T$ over $K$.

::: pf-proof
Choose isomorphisms $P_i$ with $P_iC(p_i)P_i^{-1}=C(p_i)^T$ (step [](#blocksimilar){.pf-ref}); then $P=\bigoplus_iP_i$ is invertible and conjugates $C(p_1)\oplus\cdots\oplus C(p_k)$ to its transpose, because conjugation acts blockwise on a direct sum. Composing the similarities of steps [](#rcf){.pf-ref} and [](#transpose){.pf-ref} with this one, and using transitivity of similarity, gives $M\sim M^T$. So a suitable canonical form — the rational one — proves the assertion over any field.
:::

:::

:::
:::
