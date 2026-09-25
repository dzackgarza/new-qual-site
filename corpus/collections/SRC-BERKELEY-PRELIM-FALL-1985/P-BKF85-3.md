---
schema: qual/card@1
id: P-BKF85-3
kind: problem
title: Count irreducible quadratics and cubics over $\mathbb F_5$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md; Flash appends stray glyphs after the field name, which the card restores as the explicitly named field $\mathbb Z_5=\mathbb F_5$.
---

::: {.problem}
1. How many distinct monic irreducible polynomials of degree $2$ are there over $\mathbb F_5$?

2. How many distinct monic irreducible polynomials of degree $3$ are there over $\mathbb F_5$?
:::

::: {.solution}
<1>1. A polynomial of degree $2$ or $3$ over a field is reducible if and only if it has a root in that field.

::: {.proof}
If such a polynomial has a root $a$, then it is divisible by $x-a$ and is reducible. Conversely, any nontrivial factorization of a polynomial of degree $2$ or $3$ has a factor of degree $1$, and a degree-$1$ factor supplies a root in the field.
:::

<1>2. There are exactly $15$ reducible monic quadratic polynomials over $\FF_5$.

::: {.proof}
For each $a\in\FF_5$, let $A_a$ be the set of monic quadratic polynomials having $a$ as a root. Every element of $A_a$ has the form
$$
(x-a)(x-b),
\qquad
b\in\FF_5,
$$
so
$$
\abs{A_a}=5.
$$
If $a\neq b$, then
$$
A_a\cap A_b
=
\{(x-a)(x-b)\},
$$
so every pairwise intersection has size $1$. No quadratic has three distinct roots. Hence inclusion--exclusion gives
$$
\abs{\bigcup_{a\in\FF_5}A_a}
=
5\cdot5-\binom52
=
25-10
=
15.
$$
By step <1>1, this union is exactly the set of reducible monic quadratics.
:::

<1>3. There are exactly
$$
25-15=10
$$
monic irreducible quadratic polynomials over $\FF_5$.

::: {.proof}
A monic quadratic is determined by its two nonleading coefficients, so there are
$$
5^2=25
$$
monic quadratics in total. Subtract the $15$ reducible ones counted in step <1>2.
:::

<1>4. There are exactly $85$ reducible monic cubic polynomials over $\FF_5$.

::: {.proof}
For each $a\in\FF_5$, let $B_a$ be the set of monic cubic polynomials having $a$ as a root. Such a polynomial is
$$
(x-a)q(x),
$$
where $q$ is an arbitrary monic quadratic, so
$$
\abs{B_a}=5^2=25.
$$

If $a\neq b$, then a polynomial in $B_a\cap B_b$ has the form
$$
(x-a)(x-b)(x-c),
\qquad
c\in\FF_5,
$$
and therefore
$$
\abs{B_a\cap B_b}=5.
$$
If $a,b,c$ are three distinct field elements, then
$$
B_a\cap B_b\cap B_c
=
\{(x-a)(x-b)(x-c)\},
$$
so every triple intersection has size $1$. No cubic has four distinct roots. Inclusion--exclusion gives
$$
\begin{aligned}
\abs{\bigcup_{a\in\FF_5}B_a}
&=
5\cdot25
-\binom52\cdot5
+\binom53\\
&=
125-50+10\\
&=
85.
\end{aligned}
$$
By step <1>1, these are precisely the reducible monic cubics.
:::

<1>5. There are exactly
$$
125-85=40
$$
monic irreducible cubic polynomials over $\FF_5$.

::: {.proof}
A monic cubic is determined by its three nonleading coefficients, so there are
$$
5^3=125
$$
monic cubics in total. Subtract the $85$ reducible ones counted in step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3 and <1>5 give the answers $10$ and $40$, respectively.
:::
:::
