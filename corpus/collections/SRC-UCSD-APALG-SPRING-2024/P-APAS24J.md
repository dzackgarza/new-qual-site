---
schema: qual/card@1
id: P-APAS24J
kind: problem
title: Hilbert series of invariants under diagonal $\pm 1$ matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Invariant Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 10 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p.
    10 of the paper's own numbered pages, is the statement the card answers, and the head of the
    solution names it; the file retained at assets/attachments/SP24_math_202_exam.pdf puts a cover page
    before those pages, so paper p. 10 is its page 11. Checked: the statement against the paper's text
    layer at the page named; Molien's formula for the diagonal $\pm1$ group, giving $1/(1-t^2)^n$;
    `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no
    retained solution set exists for this paper to compare the argument with, and no other card of the
    collection in this pass.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps and supplied the two points the prose compressed:
    that the action of a diagonal sign matrix on a monomial multiplies it by a scalar, so invariance
    of the monomial is equivalent to all exponents being even (both directions, using that the signs
    may be chosen independently), and that a general polynomial is a sum of monomials on which the
    group acts by distinct characters, so it is invariant exactly when each of its monomials is.
    Also recorded the Hilbert series as the generating function of graded dimensions and the reason
    the n squares are algebraically independent. Every macro used is one the preamble defines.
    Nothing was checked against a printed page.
---

::: {.problem}
Let $n$ be a positive integer and let $G\subseteq\mathrm{GL}_n(\CC)$ be the subgroup
$$
G=\left\{\begin{pmatrix}
\varepsilon_1 & 0 & \cdots & 0 \\
0 & \varepsilon_2 & \cdots & 0 \\
 &  & \ddots &  \\
0 & 0 & \cdots & \varepsilon_n
\end{pmatrix}
\colon
\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n=\pm 1\right\}
$$
of diagonal matrices whose diagonal entries are $\pm 1$.
Find the Hilbert series of the invariant ring $\CC[x_1,x_2,\ldots,x_n]^G$.
:::

::: {.solution}

The problem is Problem 10 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p. 10 of the paper's numbered pages — the retained file `assets/attachments/SP24_math_202_exam.pdf` puts a cover page before them.

The argument is the card's own; no source text or solution set is retained for it.

Let $G\le\operatorname{GL}_{n}(\CC)$ be the group of diagonal matrices $\operatorname{diag}(\varepsilon_{1},\dots,\varepsilon_{n})$ with $\varepsilon_{i}=\pm1$, acting on $R=\CC[x_{1},\dots,x_{n}]$ in the usual way, and let $R^{G}$ be the ring of invariants. The Hilbert series of a graded ring $\bigoplus_{d}R_{d}$ with finite-dimensional graded pieces is $H(t)=\sum_{d}\dim_{\CC}R_{d}\,t^{d}$.

::: pf

::: {.pf-step #monomial}
$g=\operatorname{diag}(\varepsilon_{1},\dots,\varepsilon_{n})$ acts on the monomial $x^{a}=x_{1}^{a_{1}}\cdots x_{n}^{a_{n}}$ by the scalar $\varepsilon_{1}^{a_{1}}\cdots\varepsilon_{n}^{a_{n}}$, that is $g\cdot x^{a}=\varepsilon^{a}x^{a}$.

::: pf-proof
$g$ acts by $x_{i}\mapsto\varepsilon_{i}x_{i}$, and a ring automorphism carries a product to the product of the images, so $x_{i}^{a_{i}}\mapsto\varepsilon_{i}^{a_{i}}x_{i}^{a_{i}}$. Multiplying over $i$ gives the scalar $\prod_{i}\varepsilon_{i}^{a_{i}}$ times the monomial.
:::

:::

::: {.pf-step #even}
$x^{a}$ is fixed by every $g\in G$ if and only if every $a_{i}$ is even.

::: pf-proof
If all $a_{i}$ are even then $\varepsilon_{i}^{a_{i}}=1$ for every choice of sign, so the scalar is $1$. Conversely suppose some $a_{j}$ is odd, and take $g$ with $\varepsilon_{j}=-1$ and $\varepsilon_{i}=1$ for $i\neq j$, which lies in $G$ because the signs are chosen independently; then the scalar is $-1$ and $g\cdot x^{a}=-x^{a}\neq x^{a}$ in characteristic $0$. So the monomial is not invariant.
:::

:::

::: {.pf-step #polynomial}
$f=\sum_{a}c_{a}x^{a}\in R$ is invariant if and only if $c_{a}=0$ whenever some $a_{i}$ is odd.

::: pf-proof
By step [](#monomial){.pf-ref}, $g\cdot f=\sum_{a}c_{a}\varepsilon^{a}x^{a}$. The monomials $x^{a}$ are linearly independent over $\CC$, so $g\cdot f=f$ if and only if $c_{a}\varepsilon^{a}=c_{a}$ for every $a$ and every $g$; for $a$ with some odd exponent, step [](#even){.pf-ref} supplies a $g$ with $\varepsilon^{a}=-1$, forcing $c_{a}=0$ since the two values differ in characteristic $0$. If all exponents of $a$ are even, $\varepsilon^{a}=1$ for every $g$ and the condition is automatic.
:::

:::

::: {.pf-step #ring}
$R^{G}=\CC[x_{1}^{2},\dots,x_{n}^{2}]$.

::: pf-proof
By step [](#polynomial){.pf-ref} the invariant polynomials are exactly the linear combinations of monomials with all exponents even, and those are precisely the monomials in the $n$ elements $x_{i}^{2}$; the set of such combinations is the subring generated by them. The $x_{i}^{2}$ are algebraically independent, since a polynomial relation among them would be a nonzero polynomial vanishing on the nonempty open set in $\CC^{n}$ where all coordinates are nonzero; so this subring is a polynomial ring.
:::

:::

::: {.pf-step #hilbert}
$H_{R^{G}}(t)=\dfrac{1}{(1-t^{2})^{n}}$.

::: pf-proof
$R^{G}=\CC[y_{1},\dots,y_{n}]$ with $y_{i}=x_{i}^{2}$ of degree $2$ by step [](#ring){.pf-ref}. A polynomial ring on generators of a single degree has graded piece of dimension equal to the number of monomials of degree $2d$ in $n$ variables, namely $\binom{n+d-1}{n-1}$; summing,
$$
\sum_{d\geq0}\binom{n+d-1}{n-1}t^{2d}=\frac{1}{(1-t^{2})^{n}},
$$
the standard series for a product of $n$ geometric series $\prod_{i=1}^{n}(1+t^{2}+t^{4}+\cdots)$.
:::

:::

::: {.pf-step}
The Hilbert series of the invariant ring is $1/(1-t^{2})^{n}$.

::: pf-proof
Steps [](#ring){.pf-ref} and [](#hilbert){.pf-ref}.
:::

:::

:::

:::
