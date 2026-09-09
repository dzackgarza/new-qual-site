---
schema: qual/card@1
id: P-6ASCF
kind: problem
title: 'A real $5\times 5$ matrix with eigenvalues $0$, $1+i$, and $1+2i$: injectivity,
  characteristic and minimal polynomials, and fixed points'
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
  - Rank and Nullity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $M \in M_5(\RR)$ be a $5\times 5$ square matrix with real coefficients defining a linear map $L: \Bbb{R}^5 \to \Bbb R^5$.
Assume that when considered as an element of $M_5(\Bbb C)$, then the scalars $0, 1+i, 1+2i$ are eigenvalues of $M$.

1. Show that the associated linear map $L$ is neither injective nor surjective.

2. Compute the characteristic polynomial and minimal polynomial of $M$.

3. How many fixed points can $L$ have?

   *(That is, how many solutions are there to the equation $L(v) = v$ with $v\in \Bbb R^5$?)*
:::


::: {.solution}
Because $M$ has real coefficients, every nonreal eigenvalue occurs together with its complex conjugate. Thus, besides the given eigenvalues
\[
0,\qquad1+i,\qquad1+2i,
\]
the numbers
\[
1-i,\qquad1-2i
\]
are also eigenvalues. These five eigenvalues are distinct.

<1>1. The map $L$ is neither injective nor surjective.
::: {.proof}
Since $0$ is an eigenvalue, there exists $0\ne v\in\RR^5$ with
\[
L(v)=0.
\]
Hence $\ker L\ne0$, so $L$ is not injective. A linear map from a finite-dimensional vector space to itself is injective if and only if it is surjective, so $L$ is not surjective either.
:::

<1>2. The characteristic polynomial is
\[
\chi_M(x)
=x(x-(1+i))(x-(1-i))(x-(1+2i))(x-(1-2i)).
\]
::: {.proof}
A $5\times5$ matrix has a degree-$5$ characteristic polynomial counting eigenvalues with algebraic multiplicity. We already have five distinct eigenvalues, so these are all roots and each has multiplicity $1$.
:::

<1>3. Over $\RR[x]$, this becomes
\[
\chi_M(x)=x(x^2-2x+2)(x^2-2x+5).
\]
::: {.proof}
Pair the conjugate roots:
\[
(x-(1+i))(x-(1-i))=(x-1)^2+1=x^2-2x+2,
\]
\[
(x-(1+2i))(x-(1-2i))=(x-1)^2+4=x^2-2x+5.
\]
:::

<1>4. The minimal polynomial equals the characteristic polynomial.
::: {.proof}
The minimal polynomial over $\CC$ must vanish at every eigenvalue, so it is divisible by the five distinct linear factors listed in <1>2. Hence it has degree at least $5$. But the minimal polynomial divides the degree-$5$ characteristic polynomial, so equality holds. Therefore, over $\RR$,
\[
\mu_M(x)=x(x^2-2x+2)(x^2-2x+5).
\]
:::

<1>5. The only fixed point of $L$ is $0$.
::: {.proof}
A fixed point satisfies
\[
L(v)=v,
\]
i.e.
\[
(M-I)v=0.
\]
A nonzero fixed point would make $1$ an eigenvalue of $M$. But the complete eigenvalue list above does not contain $1$; equivalently,
\[
\chi_M(1)=1\cdot1\cdot4=4\ne0.
\]
Thus $\ker(M-I)=0$, so the only fixed point is the zero vector. Hence there is exactly one fixed point.
:::
:::
