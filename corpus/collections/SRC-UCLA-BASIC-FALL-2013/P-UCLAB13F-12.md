---
schema: qual/card@1
id: P-UCLAB13F-12
kind: problem
title: Similarity classes with a prescribed characteristic polynomial
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Suppose $A$ is an endomorphism of a complex vector space with characteristic polynomial
$$
C_A(X)=X^4-6X^3+13X^2-12X+4.
$$
How many similarity classes of endomorphisms can have this characteristic polynomial?

Suppose also that the minimal polynomial $M_A(X)$ equals $C_A(X)$. How many classes satisfy this additional condition?

Prove your answers, quoting any general theorems you need.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial factors as
$$
\boxed{
C_A(X)
=(X-1)^2(X-2)^2
}.
$$


::: pf-proof

One computes
$$
(X-1)(X-2)
=
X^2-3X+2,
$$
and therefore
$$
\begin{aligned}
(X^2-3X+2)^2
&=
X^4-6X^3+13X^2-12X+4.
\end{aligned}
$$

:::

:::

::: pf-step

Over $\CC$, the similarity class of $A$ is determined by the sizes of the Jordan blocks for eigenvalues $1$ and $2$.


::: pf-proof

The Jordan canonical form theorem states that every complex matrix is similar to a direct sum of Jordan blocks, and two Jordan forms are similar exactly when, for each eigenvalue, they have the same multiset of block sizes.
By step [](#s1-1){.pf-ref}, the only eigenvalues are $1$ and $2$, each with algebraic multiplicity $2$.

:::

:::

::: {.pf-step #s1-3}

For an eigenvalue of algebraic multiplicity $2$, there are exactly two possible Jordan-block patterns:
$$
2
\qquad\text{or}\qquad
1+1.
$$


::: pf-proof

The sizes of the Jordan blocks for a fixed eigenvalue form a partition of its algebraic multiplicity.
The integer $2$ has exactly the two partitions
$$
2
\quad\text{and}\quad
1+1.
$$

:::

:::

::: {.pf-step #s1-4}

Hence there are exactly
$$
\boxed{4}
$$
similarity classes with the prescribed characteristic polynomial.


::: pf-proof

For eigenvalue $1$, choose independently one of the two block patterns from step [](#s1-3){.pf-ref}.
For eigenvalue $2$, choose independently one of the two block patterns.
Thus there are
$$
2\cdot2=4
$$
possibilities.

Explicit representatives are
$$
J_2(1)\oplus J_2(2),
$$
$$
J_2(1)\oplus[2]\oplus[2],
$$
$$
[1]\oplus[1]\oplus J_2(2),
$$
and
$$
[1]\oplus[1]\oplus[2]\oplus[2].
$$

:::

:::

::: {.pf-step #s1-5}

For a Jordan form, the exponent of
$$
(X-\lambda)
$$
in the minimal polynomial equals the size of the largest Jordan block for eigenvalue $\lambda$.


::: pf-proof

For a Jordan block
$$
J_r(\lambda)=\lambda I+N,
$$
where $N$ is nilpotent with
$$
N^r=0
\qquad\text{and}\qquad
N^{r-1}\ne0,
$$
the least power of
$$
J_r(\lambda)-\lambda I=N
$$
that vanishes is $r$.
For a direct sum of blocks with the same eigenvalue, the least annihilating exponent is therefore the largest block size.
Taking the product over distinct eigenvalues gives the stated rule for the minimal polynomial.

:::

:::

::: {.pf-step #s1-6}

The condition
$$
M_A(X)=C_A(X)
=(X-1)^2(X-2)^2
$$
forces a size-$2$ Jordan block for eigenvalue $1$ and a size-$2$ Jordan block for eigenvalue $2$.


::: pf-proof

By step [](#s1-5){.pf-ref}, the exponent $2$ of $(X-1)$ in the minimal polynomial means that the largest Jordan block for eigenvalue $1$ has size $2$.
Since the total algebraic multiplicity at $1$ is also $2$, the only possible block pattern is the single block
$$
J_2(1).
$$
The same argument applies to eigenvalue $2$.

:::

:::

::: {.pf-step #s1-7}

Therefore exactly
$$
\boxed{1}
$$
similarity class satisfies the additional condition
$$
M_A=C_A.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} uniquely determines the Jordan form:
$$
\boxed{
J_2(1)\oplus J_2(2)
}.
$$
Hence there is exactly one similarity class.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the number of classes with the prescribed characteristic polynomial, and step [](#s1-7){.pf-ref} gives the number satisfying the additional minimal-polynomial condition.

:::

:::

:::
