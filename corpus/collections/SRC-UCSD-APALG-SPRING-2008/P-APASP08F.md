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
For complex characters of a finite group, the scalar product
\[
\langle \alpha,\beta\rangle
=\frac1{|G|}\sum_{g\in G}\alpha(g)\overline{\beta(g)}
\]
computes multiplicity. The irreducible characters of $S_5$ are real-valued, so the two quantities in the problem are
\[
\left\langle
\chi^{(2,2,1)}\chi^{(3,2)},\chi^{(3,1,1)}
\right\rangle
\]
and
\[
\left\langle
\chi^{(3,2)}\chi^{(3,2)},\chi^{(3,1,1)}
\right\rangle.
\]
An exact character-table computation gives
\[
\boxed{1}
\qquad\text{and}\qquad
\boxed{1}.
\]

For example, using the conjugacy classes in cycle types
\[
1^5,\quad 2\,1^3,\quad 2^2 1,\quad 3\,1^2,\quad 3\,2,\quad 4\,1,\quad 5,
\]
whose sizes are
\[
1,10,15,20,20,30,24,
\]
the three relevant irreducible characters are
\[
\begin{array}{c|rrrrrrr}
&1^5&2\,1^3&2^2 1&3\,1^2&3\,2&4\,1&5\\ \hline
\chi^{(2,2,1)}&5&-1&1&-1&-1&1&0\\
\chi^{(3,2)}&5&1&1&-1&1&-1&0\\
\chi^{(3,1,1)}&6&0&-2&0&0&0&1
\end{array}
\]
so direct substitution gives
\[
\frac1{120}
\left(1\cdot5\cdot5\cdot6
+15\cdot1\cdot1\cdot(-2)
\right)
=1
\]
for (a), and
\[
\frac1{120}
\left(1\cdot5^2\cdot6
+15\cdot1^2\cdot(-2)
\right)
=1
\]
for (b).

Representation-theoretically, therefore,
\[
\boxed{
[V_{(2,2,1)}\otimes V_{(3,2)}:V_{(3,1,1)}]=1
}
\]
and
\[
\boxed{
[V_{(3,2)}\otimes V_{(3,2)}:V_{(3,1,1)}]=1.
}
\]
Equivalently, the two integers are the dimensions of the corresponding $S_5$-equivariant Hom spaces.

The answer to the final question is yes. Transposing a Young diagram corresponds to tensoring the associated irreducible representation by the sign representation. Since
\[
(3,2)'=(2,2,1),
\qquad
(3,1,1)'=(3,1,1),
\]
we have
\[
V_{(2,2,1)}\cong V_{(3,2)}\otimes\operatorname{sgn}
\]
and
\[
V_{(3,1,1)}\cong V_{(3,1,1)}\otimes\operatorname{sgn}.
\]
Hence
\[
\begin{aligned}
\operatorname{Hom}_{S_5}
\bigl(V_{(3,1,1)},V_{(2,2,1)}\otimes V_{(3,2)}\bigr)
&\cong
\operatorname{Hom}_{S_5}
\bigl(V_{(3,1,1)},V_{(3,2)}^{\otimes2}\otimes\operatorname{sgn}\bigr)\\
&\cong
\operatorname{Hom}_{S_5}
\bigl(V_{(3,1,1)}\otimes\operatorname{sgn},V_{(3,2)}^{\otimes2}\bigr)\\
&\cong
\operatorname{Hom}_{S_5}
\bigl(V_{(3,1,1)},V_{(3,2)}^{\otimes2}\bigr).
\end{aligned}
\]
Thus the two scalar products are necessarily equal even before performing the second character-table calculation.
:::
