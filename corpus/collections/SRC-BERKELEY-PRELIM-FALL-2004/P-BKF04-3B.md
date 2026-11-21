---
schema: qual/card@1
id: P-BKF04-3B
kind: problem
title: Sizes of rational matrices satisfying $A^3+A+I=0$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose proof into numbered steps and re-checked it: the rational root
    test, the identification of the minimal polynomial with the irreducible cubic, the passage to
    the characteristic polynomial, and the companion-block construction for n = 3 and its block
    sums. Nothing was changed mathematically. Not checked against a printed source: the Berkeley
    preliminary examinations themselves are not retained in tmp/sources, and the card records no
    page; the statement is the card's transcription.
---

::: {.problem}
For which positive integers $n$ does there exist an $n\times n$ matrix $A$ with rational entries such that $A^3+A+I=0$?
:::

::: {.solution}

The argument is the card's own: no solution set for this source is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f(x)=x^{3}+x+1\in\QQ[x]$ and $A$ is an $n\times n$ matrix over $\QQ$ with $f(A)=0$; the minimal polynomial of $A$ divides every polynomial that annihilates $A$, and its irreducible factors are exactly the irreducible factors of the characteristic polynomial.

::: pf

::: {.pf-step #irred}

$f$ is irreducible over $\QQ$.

::: pf-proof

$f$ is a cubic; a reducible cubic has a rational root, and by the rational root test the only candidates are $\pm1$, while $f(1)=3$ and $f(-1)=-1$.

:::

:::

::: {.pf-step #minpoly}

The minimal polynomial of $A$ is $f$.

::: pf-proof

It is monic and nonconstant, divides $f$ because $f(A)=0$, and $f$ is irreducible, so it equals $f$.

:::

:::

::: {.pf-step #charpoly}

The characteristic polynomial of $A$ is $f^{k}$ with $3k=n$.

::: pf-proof

Every irreducible factor of the characteristic polynomial is an irreducible factor of the minimal polynomial, by the Cayley-Hamilton theorem combined with the divisibility of the minimal polynomial by each such factor; here the only irreducible factor is $f$, so the characteristic polynomial is $f^{k}$, and degrees give $3k=n$.

:::

:::

::: {.pf-step #nec}

If such $A$ exists then $3\mid n$.

::: pf-proof

Step [](#charpoly){.pf-ref}.

:::

:::

::: {.pf-step #suf}

If $3\mid n$ then such $A$ exists.

::: pf-proof

For $n=3$ let $V=\QQ[x]/\langle f\rangle$, a $3$-dimensional $\QQ$-vector space since $f$ is irreducible, and let $A$ be the matrix of multiplication by the class of $x$ in some basis; then $f(A)=0$ because $f(x)=0$ in $V$. For $n=3k$ take the block diagonal matrix with $k$ copies of that block, which again satisfies $f(A)=0$.

:::

:::

::: {.pf-step #done}

The integers $n$ that occur are exactly the multiples of $3$.

::: pf-proof

Steps [](#nec){.pf-ref} and [](#suf){.pf-ref}.

:::

:::

:::

:::
