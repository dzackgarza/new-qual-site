---
schema: qual/card@1
id: P-APAS24D
kind: problem
title: Diagonal similarity making a matrix norm close to the spectral radius
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 4 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p.
    4 of the paper's own numbered pages, is the statement the card answers, and the head of the solution
    names it; the file retained at assets/attachments/SP24_math_202_exam.pdf puts a cover page before
    those pages, so paper p. 4 is its page 5. Checked: the statement against the paper's text layer at
    the page named; the weighted 1-norm estimate under conjugation by
    $D=\operatorname{diag}(\eta^{j-1})$; `qualc.authoring check` on the card; the card carries no `pf`
    block, so `tmp/lam.sh` does not apply and was not run. Not checked: no retained solution set exists
    for this paper to compare the argument with, and no other card of the collection in this pass.
---

::: {.problem}
Given an upper triangular matrix $A\in M_n(\CC)=\CC^{n\times n}$ and $\varepsilon\in\RR$, $\varepsilon>0$, prove there exists $\eta\in\RR$, $\eta>0$, such that the diagonal matrix $D=(d_{ij})\in M_n(\RR)=\RR^{n\times n}$ with entries
$$
d_{jj}=\eta^{j-1},
$$
for $1\le j\le n$, satisfies
$$
\norm{A}\le\rho(A)+\varepsilon,
$$
where the matrix norm $\norm{\cdot}$ is defined by
$$
\norm{B}=\norm{D^{-1}BD}_1
$$
for all $B\in M_n(\CC)=\CC^{n\times n}$.
:::

::: {.solution}

The problem is Problem 4 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p. 4 of the paper's numbered pages — the retained file `assets/attachments/SP24_math_202_exam.pdf` puts a cover page before them. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own.

Let
$$
D=\operatorname{diag}(1,\eta,\eta^2,\ldots,\eta^{n-1}).
$$
Since $A$ is upper triangular, so is $D^{-1}AD$, and its entries are
$$
(D^{-1}AD)_{ij}=\eta^{\,j-i}a_{ij}
\qquad(i\le j).
$$
In particular, the diagonal entries are unchanged. Since the eigenvalues of an upper-triangular matrix are its diagonal entries,
$$
\rho(A)=\max_j\abs{a_{jj}}.
$$

Let
$$
C=\sum_{1\le i<j\le n}\abs{a_{ij}}.
$$
If $C=0$, then $A$ is diagonal and for every $\eta>0$,
$$
\norm{A}=\norm{A}_1=\rho(A).
$$
Assume $C>0$. Choose
$$
0<\eta\le1
\qquad\text{with}\qquad
\eta C<\varepsilon.
$$
For each column $j$,
$$
\sum_{i=1}^n \abs{(D^{-1}AD)_{ij}}
=
\abs{a_{jj}}+\sum_{i<j}\eta^{j-i}\abs{a_{ij}}.
$$
Because $j-i\ge1$ and $0<\eta\le1$,
$$
\eta^{j-i}\le\eta.
$$
Hence
$$
\sum_i \abs{(D^{-1}AD)_{ij}}
\le
\abs{a_{jj}}+\eta C
<
\rho(A)+\varepsilon.
$$
Taking the maximum over columns gives
$$
\norm{A}
=\norm{D^{-1}AD}_1
\le\rho(A)+\varepsilon.
$$
Thus such an $\eta>0$ exists.
:::
