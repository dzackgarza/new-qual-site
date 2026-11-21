---
schema: qual/card@1
id: P-F07EX
kind: problem
title: 'Examples: an integral with a corner, a series with divergent squares, and
  a basis of a subspace of $\mathcal{P}_3$'
classification:
  areas:
  - prelim
  topics:
  - Counterexamples
  - Series of Numbers
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the three examples into Lamport steps and checked each: the step function has
    one-sided difference quotients 0 and 1 at x = 1; the alternating sequence has convergent
    series and harmonic squares; and for part (c) the coefficient columns were computed, p_3 =
    p_1 + p_2 was verified (so the third polynomial is redundant), and the independence of
    p_1, p_2, p_4 was verified by an explicit 3x3 minor equal to 2. All three claims were
    additionally checked by exact rational rank computation (rank 3 for the four columns, rank 3
    for p_1, p_2, p_4). The card's stated basis is correct.
---

::: {.problem}
Give an example (without proof) of each of the following:

(a) An integrable function $f: \RR \to \RR$ so that the function $F(x) = \int_0^x f(t)\,dt$ is differentiable everywhere but at $x = 1$.

(b) A sequence $\{a_n\}$ of real numbers such that $\sum_{n=1}^{\infty} a_n$ converges and $\sum_{n=1}^{\infty} a_n^2$ diverges.

(c) A basis for the subspace of $\mathcal{P}_3$ spanned by $x^2 + x + 1$, $x^3 - x + 2$, $x^3 + x^2 + 3$, and $-x^3 + x^2 + 2x + 1$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
The problem asks only for examples; what follows checks that each example has the required property.

::: pf

::: {.pf-step #part-a}
With $f(t)=0$ for $t<1$ and $f(t)=1$ for $t\ge1$, the function $F(x)=\int_0^xf$ equals $0$ for $x\le1$ and $x-1$ for $x>1$; it is differentiable at every $x\ne1$ and not at $x=1$.

::: pf-proof
$f$ is a step function, hence integrable on $\RR$. Splitting the integral at $1$ gives $F(x)=0$ for $x\le1$ and $F(x)=x-1$ for $x\ge1$; on each side $F$ agrees with a polynomial, so it is differentiable away from $1$. At $x=1$ the left difference quotient is $0$ and the right one is $1$, so $F'(1)$ does not exist.
:::

:::

::: {.pf-step #part-b}
With $a_n=\frac{(-1)^n}{\sqrt n}$, the series $\sum a_n$ converges and $\sum a_n^2$ diverges.

::: pf-proof
$\frac{1}{\sqrt n}$ decreases to $0$, so the alternating series test gives convergence of $\sum_n(-1)^n/\sqrt n$. Meanwhile $a_n^2=\frac1n$ and the harmonic series diverges.
:::

:::

::: {.pf-step #columns}
Relative to the coefficient basis $(1,x,x^2,x^3)$ of $\mathcal P_3$, the four given polynomials are the columns
$$
p_1=(1,1,1,0),\quad p_2=(2,-1,0,1),\quad p_3=(3,0,1,1),\quad p_4=(1,2,1,-1).
$$

::: pf-proof
Reading off coefficients, $x^2+x+1$ gives $(1,1,1,0)$, $x^3-x+2$ gives $(2,-1,0,1)$, $x^3+x^2+3$ gives $(3,0,1,1)$ and $-x^3+x^2+2x+1$ gives $(1,2,1,-1)$.
:::

:::

::: {.pf-step #relation}
$p_3=p_1+p_2$, so the third polynomial is redundant.

::: pf-proof
$(x^2+x+1)+(x^3-x+2)=x^3+x^2+3$, since the linear terms cancel; in columns, $(1,1,1,0)+(2,-1,0,1)=(3,0,1,1)$.
:::

:::

::: {.pf-step #independent}
$p_1,p_2,p_4$ are linearly independent.

::: pf-proof
The $3\times3$ minor on the rows of $1,x,x^3$ and these three columns is
$$
\det\begin{pmatrix}1&2&1\\1&-1&2\\0&1&-1\end{pmatrix}=1(1-2)-2(-1-0)+1(1-0)=2\ne0,
$$
so those three rows of the coefficient matrix already have rank $3$; hence the three columns are independent.
:::

:::

::: {.pf-step}
(c) A basis of the span is $\{\,x^2+x+1,\ x^3-x+2,\ -x^3+x^2+2x+1\,\}$.

::: pf-proof
By step [](#relation){.pf-ref} the four polynomials span the same space as $p_1,p_2,p_4$, which step [](#independent){.pf-ref} shows to be independent; hence those three form a basis. In full,
$$
\boxed{\{x^2+x+1,\ x^3-x+2,\ -x^3+x^2+2x+1\}}.
$$
:::

:::

:::
:::
