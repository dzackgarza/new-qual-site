---
schema: qual/card@1
id: P-APASP08F
kind: problem
title: "Scalar products of characters via the SF package and their interpretation"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Read against the UCSD Applied Algebra Qualifying Exam, Spring 2008, Part II ST.1,
    printed p. 2. The two scalar products and both follow-up questions match the printed
    statement.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own
    character-table computation, with every conjugacy class included in each sum, and
    the sign-twisting explanation of why (b) follows from (a). Checked the $S_5$
    character values used and both sums term by term.
---

::: {.problem}
Use the SF package to compute the two scalar products:

**(a)**
$$
\frac{1}{5!}\sum_{\sigma \in S_5} \chi^{(2,2,1)}(\sigma)\,\chi^{(3,2)}(\sigma)\,\chi^{(3,1,1)}(\sigma).
$$

**(b)**
$$
\frac{1}{5!}\sum_{\sigma \in S_5} \bigl(\chi^{(3,2)}(\sigma)\bigr)^2 \chi^{(3,1,1)}(\sigma).
$$

1. Give a representation-theoretic interpretation of the resulting integers.

2. Could you have predicted the answer for (b) given the answer for (a)?
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #multiplicity-form}
For real-valued characters of a finite group $G$,
$$
\frac1{\cardinality{G}}\sum_{g\in G}\alpha(g)\beta(g)\gamma(g)
=\left\langle\alpha\beta,\gamma\right\rangle.
$$
In particular the two requested integers are
$$
\left\langle\chi^{(2,2,1)}\chi^{(3,2)},\chi^{(3,1,1)}\right\rangle
\quad\text{and}\quad
\left\langle(\chi^{(3,2)})^2,\chi^{(3,1,1)}\right\rangle.
$$

::: pf-proof
The scalar product is $\langle\alpha,\beta\rangle=\frac1{\cardinality{G}}\sum_g\alpha(g)\overline{\beta(g)}$. All characters of $S_5$ are real-valued, so the conjugates may be omitted and the two products have the displayed forms.
:::
:::

::: {.pf-step #character-table}
On cycle types $1^5,2\,1^3,2^2 1,3\,1^2,3\,2,4\,1,5$, of class sizes
$$
1,10,15,20,20,30,24,
$$
the three characters are
$$
\begin{array}{c|rrrrrrr}
&1^5&2\,1^3&2^2 1&3\,1^2&3\,2&4\,1&5\\ \hline
\chi^{(2,2,1)}&5&-1&1&-1&-1&1&0\\
\chi^{(3,2)}&5&1&1&-1&1&-1&0\\
\chi^{(3,1,1)}&6&0&-2&0&0&0&1
\end{array}.
$$

::: pf-proof
These are the standard irreducible characters of $S_5$ obtained from the character table (for instance by the Murnaghan--Nakayama rule). Their squared norms with the displayed class sizes are all $1$, and distinct rows are orthogonal, so they are precisely the three irreducible characters named by the partitions.
:::
:::

::: {.pf-step #part-a}
$$
\frac1{5!}\sum_{\sigma\in S_5}\chi^{(2,2,1)}(\sigma)\chi^{(3,2)}(\sigma)\chi^{(3,1,1)}(\sigma)=1.
$$

::: pf-proof
Multiplying the three rows of step [](#character-table){.pf-ref} and weighting by the class sizes gives
$$
\frac1{120}\left(1\cdot5\cdot5\cdot6
+15\cdot1\cdot1\cdot(-2)\right)
=\frac{120-30}{120}=1.
$$
The five omitted terms contain the factor $0$ from the middle row or $0$ in the last row on the class $5$.
:::
:::

::: {.pf-step #part-b}
$$
\frac1{5!}\sum_{\sigma\in S_5}\bigl(\chi^{(3,2)}(\sigma)\bigr)^2\chi^{(3,1,1)}(\sigma)=1.
$$

::: pf-proof
Squaring the second row of step [](#character-table){.pf-ref} gives
$$
\frac1{120}\left(1\cdot5^2\cdot6
+15\cdot1^2\cdot(-2)\right)
=\frac{150-30}{120}=1.
$$
Again the remaining classes contribute zero.
:::
:::

::: {.pf-step #interpretation}
Both integers are multiplicities:
$$
[V_{(2,2,1)}\otimes V_{(3,2)}:V_{(3,1,1)}]=1,
\qquad
[V_{(3,2)}\otimes V_{(3,2)}:V_{(3,1,1)}]=1.
$$
Equivalently they are the dimensions of the corresponding $S_5$-equivariant Hom spaces.

::: pf-proof
For finite-dimensional complex representations, $\langle\chi_U,\chi_W\rangle=\dim\operatorname{Hom}_G(U,W)$. Applying this to the characters $\chi^{(2,2,1)}\chi^{(3,2)}$ and $(\chi^{(3,2)})^2$ with target $V_{(3,1,1)}$ gives the two multiplicities.
:::
:::

::: {.pf-step #prediction}
The answer to (b) is forced by the answer to (a), without a second character-table calculation.

::: pf-proof
Transposition of Young diagrams tensors an irreducible by the sign character, and $(3,2)'=(2,2,1)$ while $(3,1,1)'=(3,1,1)$. Hence $V_{(2,2,1)}\cong V_{(3,2)}\otimes\operatorname{sgn}$ and $V_{(3,1,1)}\cong V_{(3,1,1)}\otimes\operatorname{sgn}$. Therefore
$$
\operatorname{Hom}_{S_5}(V_{(3,1,1)},V_{(2,2,1)}\otimes V_{(3,2)})
\cong
\operatorname{Hom}_{S_5}(V_{(3,1,1)}\otimes\operatorname{sgn},V_{(3,2)}^{\otimes2})
\cong
\operatorname{Hom}_{S_5}(V_{(3,1,1)},V_{(3,2)}^{\otimes2}),
$$
so the two multiplicities are equal. This answers the final question.
:::
:::

:::
:::
