---
schema: qual/card@1
id: P-HJBTY
kind: problem
title: Rational canonical forms of $3\times 3$ matrices over $\QQ$ annihilated by
  $(x^2+2)(x-1)^3$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What $3 \times 3$ matrices over $\QQ$ (up to similarity) satisfy $f(A) = 0$, where $f(x) = (x^2 + 2)(x - 1)^3$?
List all possible invariant factor lists and rational canonical forms.
:::

::: {.solution}
Write $\mu_A$ and $\chi_A$ for the minimal and characteristic polynomials of $A\in M_3(\QQ)$, and $C(g)$ for the companion matrix of a monic polynomial $g$.

::: pf

::: {.pf-step #char-poly}
$f(A)=0$ if and only if $\mu_A\mid f$, and then $\chi_A$ is $(x^2+2)(x-1)$ or $(x-1)^3$.

::: pf-proof
The polynomials annihilating $A$ are the multiples of $\mu_A$.
The irreducible factors of $f$ over $\QQ$ are $x^2+2$ and $x-1$, and $\chi_A$ has the same irreducible factors as $\mu_A$.
Since $\deg\chi_A=3$, the only monic products of these factors of degree $3$ are $(x^2+2)(x-1)$ and $(x-1)^3$.
:::

:::

::: pf-step
If $\chi_A=(x^2+2)(x-1)$, the invariant-factor list is $[(x^2+2)(x-1)]$ and the rational canonical form is
$$
C(x^3-x^2+2x-2)
=\begin{pmatrix}
0&0&2\\
1&0&-2\\
0&1&1
\end{pmatrix}.
$$

::: pf-proof
Both coprime irreducible factors of $\chi_A$ divide $\mu_A$, so $\mu_A=(x^2+2)(x-1)=\chi_A$, and the only invariant factor is $\chi_A=x^3-x^2+2x-2$.
:::

:::

::: pf-step
If $\chi_A=(x-1)^3$, the invariant-factor lists are $[x-1,x-1,x-1]$, $[x-1,(x-1)^2]$ and $[(x-1)^3]$, with rational canonical forms
$$
I_3,\qquad
\diag\!\left(1,
\begin{pmatrix}0&-1\\1&2\end{pmatrix}\right),\qquad
\begin{pmatrix}
0&0&1\\
1&0&-3\\
0&1&3
\end{pmatrix}.
$$

::: pf-proof
The invariant factors are powers of $x-1$ whose degrees sum to $3$ and form a divisibility chain, which gives exactly the three lists.
The companion matrices of $(x-1)^2=x^2-2x+1$ and $(x-1)^3=x^3-3x^2+3x-1$ are the displayed blocks.
:::

:::

::: pf-step
Exactly $\boxed{4}$ similarity classes of $3\times3$ rational matrices satisfy $f(A)=0$.

::: pf-proof
By step [](#char-poly){.pf-ref}, the two cases above are exhaustive, and they give one and three classes.
:::

:::

:::

:::
