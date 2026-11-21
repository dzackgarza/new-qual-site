---
schema: qual/card@1
id: P-APAS20F
kind: problem
title: Scalar products $\langle e_1^n,e_1^n\rangle$ and $\langle h_3 p_6,s_{5,4}\rangle$
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 6 of the Math 202 Qualifying Exam, Spring 2020 (June 3, 2020), printed
    p. 2 of the paper's own numbered pages, is the statement the card answers, and the head of the
    solution names it; the file retained at assets/attachments/Applied-Algebra-Qual-SP20.pdf puts a
    cover page before those two numbered pages, so paper p. 1 and p. 2 are its second and third pages.
    Checked: the statement against the paper's text layer at the page named; the two scalar-product
    evaluations; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the QED.
    Not checked: no retained solution set exists for this paper to compare the argument with, and no
    other card of the collection in this pass.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the two computations already on the card, with
    the relation between the inner product and the Schur coefficient stated as a step rather
    than used silently, and the Murnaghan-Nakayama statement written out with the cells of the
    skew shape (5,4)/(3) listed so that its height is visible. Not claimed: a retained solution
    set; the provenance names the examination paper only. The two answers, n! and -1, are
    unchanged.
---

::: {.problem}
Let $\langle\,\cdot\,,\,\cdot\,\rangle$ be the scalar product on the ring of symmetric functions.

(a) Evaluate $\langle e_1^n,e_1^n\rangle$.

(b) Evaluate $\langle h_3 p_6,s_{5,4}\rangle$.
:::

::: {.solution}

The problem is Problem 6 of the Math 202 Qualifying Exam, Spring 2020 (June 3, 2020)'s numbered pages — the retained file `assets/attachments/Applied-Algebra-Qual-SP20.pdf` puts a cover page before them.

No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/Applied-Algebra-Qual-SP20.pdf`, the examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout the scalar product is the Hall inner product on symmetric functions, with respect to which the Schur functions are orthonormal and $\langle p_\lambda,p_\mu\rangle=\delta_{\lambda\mu}z_\lambda$, where $z_\lambda=\prod_i i^{m_i(\lambda)}m_i(\lambda)!$ for a partition with $m_i$ parts equal to $i$.

::: pf

::: {.pf-step #part-a}
$\langle e_1^n,e_1^n\rangle=n!$.

::: pf-proof
$e_1=p_1$, the power sum indexed by the one-part partition $(1)$, so $e_1^n=p_1^n=p_{(1^n)}$, the power sum indexed by the partition of $n$ into $n$ parts equal to $1$. That partition has $m_1=n$ and $m_i=0$ for $i>1$, so $z_{(1^n)}=1^n\cdot n!=n!$, and the formula for the inner product on power sums gives $\langle p_{(1^n)},p_{(1^n)}\rangle=z_{(1^n)}=n!$.

:::

:::

::: {.pf-step #part-b-reduction}
$\langle h_3p_6,s_{(5,4)}\rangle$ equals the coefficient $[\,p_6s_{(3)}:s_{(5,4)}\,]$.

::: pf-proof
$h_3=s_{(3)}$ is the complete homogeneous symmetric function of degree $3$, which is the Schur function of the one-row partition $(3)$. Since the Schur functions are orthonormal, $\langle F,s_{(5,4)}\rangle$ is the coefficient of $s_{(5,4)}$ in the expansion of $F$ in Schur functions, and $F=h_3p_6=s_{(3)}p_6$.

:::

:::

::: {.pf-step #border-strip}
The coefficient $[\,p_6\,s_{(3)}:s_{(5,4)}\,]$ is $-1$.

::: pf-proof
By the Murnaghan–Nakayama rule, the coefficient of $s_\lambda$ in $p_6s_\mu$ is the signed sum over border strips $\xi$ of size $6$ with $\lambda/\mu=\xi$ of $(-1)^{\operatorname{ht}\xi}$, where $\operatorname{ht}\xi$ is one less than the number of rows $\xi$ occupies. Here $\mu=(3)$ and $\lambda=(5,4)$, so $\xi=(5,4)/(3)$ consists of the boxes $(1,4),(1,5)$ in the first row and $(2,1),(2,2),(2,3),(2,4)$ in the second: six boxes, connected, occupying two rows and containing no $2\times2$ block, hence a border strip of height $1$. A border strip of size $6$ in $(5,4)$ whose removal leaves $(3)$ is unique, so the signed sum has the single term $(-1)^1=-1$.

:::

:::

::: {.pf-step #conclusion}
$\langle e_1^n,e_1^n\rangle=n!$ and $\langle h_3p_6,s_{5,4}\rangle=-1$.

::: pf-proof
The first is step [](#part-a){.pf-ref}. The second combines steps [](#part-b-reduction){.pf-ref} and [](#border-strip){.pf-ref}.

:::

:::

:::
:::
