---
schema: qual/card@1
id: P-APAS20D
kind: problem
title: Conjugacy class sizes from a character table of a group of order $360$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 4 of the Math 202 Qualifying Exam, Spring 2020 (June 3, 2020), printed
    p. 2 of the paper's own numbered pages, is the statement the card answers, and the head of the
    solution names it; the file retained at assets/attachments/Applied-Algebra-Qual-SP20.pdf puts a
    cover page before those two numbered pages, so paper p. 1 and p. 2 are its second and third pages.
    Checked: the statement against the paper's text layer at the page named; the class sizes computed
    from column orthogonality; `qualc.authoring check` on the card; the card carries no `pf` block, so
    `tmp/lam.sh` does not apply and was not run. Not checked: no retained solution set exists for this
    paper to compare the argument with, and no other card of the collection in this pass.
---

::: {.problem}
Here is the character table for some group of size $360$ (rows are characters, the columns are conjugacy classes):
$$
\begin{array}{c|ccccccc}
 & \gamma_1 & \gamma_2 & \gamma_3 & \gamma_4 & \gamma_5 & \gamma_6 & \gamma_7 \\
\hline
\chi_1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\chi_2 & 5 & -1 & 2 & -1 & 1 & 0 & 0 \\
\chi_3 & 5 & 2 & -1 & -1 & 1 & 0 & 0 \\
\chi_4 & 8 & -1 & -1 & 0 & 0 & \dfrac{1+\sqrt{5}}{2} & \dfrac{1-\sqrt{5}}{2} \\
\chi_5 & 8 & -1 & -1 & 0 & 0 & \dfrac{1-\sqrt{5}}{2} & \dfrac{1+\sqrt{5}}{2} \\
\chi_6 & 9 & 0 & 0 & 1 & 1 & -1 & -1 \\
\chi_7 & 10 & 1 & 1 & 0 & -2 & 0 & 0
\end{array}
$$
Determine the sizes of its conjugacy classes.
For your convenience, the divisors of $360$ are:
$$
1,2,3,4,5,6,8,9,10,12,15,18,20,24,30,36,40,45,60,72,90,120,180,360.
$$
:::

::: {.solution}

The problem is Problem 4 of the Math 202 Qualifying Exam, Spring 2020 (June 3, 2020), printed p. 2 of the paper's numbered pages — the retained file `assets/attachments/Applied-Algebra-Qual-SP20.pdf` puts a cover page before them. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the class sizes from column orthogonality, $\cardinality{C_j}=\cardinality{G}/\sum_i\abs{\chi_i(g_j)}^2$

If $g\in G$, column orthogonality for the irreducible character table gives
$$
\sum_{\chi\in\operatorname{Irr}(G)} \abs{\chi(g)}^2=\cardinality{C_G(g)}.
$$
If $K_g$ is the conjugacy class of $g$, then
$$
\cardinality{K_g}=\frac{\cardinality{G}}{\cardinality{C_G(g)}}.
$$
We therefore compute the squared column norms.

For $\gamma_1$,
$$
1^2+5^2+5^2+8^2+8^2+9^2+10^2=360,
$$
so $\cardinality{\gamma_1}=360/360=1$.

For $\gamma_2$,
$$
1^2+(-1)^2+2^2+(-1)^2+(-1)^2+0^2+1^2=9,
$$
so $\cardinality{\gamma_2}=360/9=40$. The same computation for $\gamma_3$ gives $\cardinality{\gamma_3}=40$.

For $\gamma_4$,
$$
1^2+(-1)^2+(-1)^2+0+0+1^2+0=4,
$$
so $\cardinality{\gamma_4}=90$.

For $\gamma_5$,
$$
1^2+1^2+1^2+0+0+1^2+(-2)^2=8,
$$
so $\cardinality{\gamma_5}=45$.

For $\gamma_6$, let
$$
\alpha=\frac{1+\sqrt5}{2},\qquad \beta=\frac{1-\sqrt5}{2}.
$$
Since $\alpha+\beta=1$ and $\alpha\beta=-1$,
$$
\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=3.
$$
Hence the squared column norm is
$$
1+\alpha^2+\beta^2+1=5,
$$
so $\cardinality{\gamma_6}=72$. The same holds for $\gamma_7$.

Thus the conjugacy-class sizes, in the order displayed in the table, are
$$
\boxed{1,40,40,90,45,72,72}.
$$
Their sum is $360$, as required.
:::
