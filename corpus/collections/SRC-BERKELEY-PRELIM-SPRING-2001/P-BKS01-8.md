---
schema: qual/card@1
id: P-BKS01-8
kind: problem
title: Are the squares in a finite group always a subgroup?
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Used G=A_4. Its order-two elements square to the identity, while
    squaring permutes the eight 3-cycles. Thus the set of squares has
    9 elements, which cannot be the order of a subgroup of A_4.
---

::: {.problem}
If $G$ is a finite group, must
\[
S=\{g^2:g\in G\}
\]
be a subgroup?
Give a proof or a counterexample.
:::

::: {.solution}
The answer is no.

<1>1. Take
$$
G=A_4.
$$
Its elements consist of the identity, three double transpositions, and
eight $3$-cycles.

::: {.proof}
The even permutations in $S_4$ have cycle types
$$
1^4,
\qquad
2^2,
\qquad
3\,1.
$$
There is one identity, three products of two disjoint transpositions,
and
$$
\binom43(3-1)!
=
4\cdot2
=8
$$
$3$-cycles, accounting for all $12$ elements of $A_4$.
:::

<1>2. The set of squares in $A_4$ is exactly
$$
S
=
\{e\}
\cup
\{\text{all $3$-cycles in }A_4\}.
$$

::: {.proof}
The identity squares to itself. Every double transposition has order
$2$, so its square is $e$.

If $\sigma$ is a $3$-cycle, then $\sigma^2=\sigma^{-1}$ is again a
$3$-cycle. Conversely, every $3$-cycle $\tau$ is a square, since
$$
(\tau^{-1})^2
=
\tau
$$
for an element of order $3$.
Thus the displayed set is precisely the set of all squares.
:::

<1>3. The set $S$ has cardinality
$$
\abs{S}=9.
$$

::: {.proof}
By step <1>2, it contains the identity and the eight $3$-cycles.
:::

<1>4. The set $S$ is not a subgroup of $A_4$.

::: {.proof}
If $S\leq A_4$, Lagrange's theorem would imply
$$
\abs{S}\mid\abs{A_4}.
$$
But
$$
9\nmid12,
$$
contradicting step <1>3.
:::

<1>5. Therefore the set of squares in a finite group need not be a
subgroup.

::: {.proof}
The finite group $A_4$ constructed above is a counterexample by step
<1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers the question.
:::
:::
