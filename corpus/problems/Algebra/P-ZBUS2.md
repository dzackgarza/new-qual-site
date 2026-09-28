---
schema: qual/card@1
id: P-ZBUS2
kind: problem
title: Character table of $A_4$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Do you know any representation theory?
What about representations of \(A_4\)?

Give a nontrivial one.
What else is there?
How many irreducible representations do we have?
What are their degrees?
Write the character table of \(A_4\).
:::

::: {.solution}
The conjugacy classes of $A_4$ are
\[
\{1\},\qquad
\{(12)(34),(13)(24),(14)(23)\},
\]
and two conjugacy classes of $3$-cycles, each of size $4$. Hence $A_4$ has four irreducible complex characters.

Let
\[
V_4=\{1,(12)(34),(13)(24),(14)(23)\}\trianglelefteq A_4.
\]
Since
\[
A_4/V_4\cong C_3,
\]
there are three one-dimensional characters. If $\omega=e^{2\pi i/3}$, they are the trivial character and the two characters taking values $\omega,\omega^2$ on the two classes of $3$-cycles.

The remaining irreducible has degree $3$, because
\[
12=1^2+1^2+1^2+d^2
\]
forces $d=3$. It is the standard representation obtained from the permutation representation on four letters by removing the trivial summand. Its character is
\[
(3,-1,0,0)
\]
on the four classes above.

Thus, choosing representatives $1,(12)(34),(123),(132)$ for the four classes,
\[
\begin{array}{c|cccc}
&1&(12)(34)&(123)&(132)\\\hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega\\
\chi_4&3&-1&0&0
\end{array}
\]
is the character table of $A_4$.
:::
