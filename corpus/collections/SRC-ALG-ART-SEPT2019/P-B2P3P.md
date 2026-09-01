---
schema: qual/card@1
id: P-B2P3P
kind: problem
title: Jordan and rational forms from characteristic and minimal polynomials;
  nilpotents with a unique two-dimensional invariant subspace
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Nilpotence
relations: []
review: draft
---

:::{.problem}
Let $V$ be a 5-dimensional vector space over a field $F$.

a. Let $T: V \to V$ be a linear transformation with characteristic polynomial $(x-1)^3(x-2)^2$ and minimal polynomial $(x-1)^2(x-2)$.
    i. Write down a matrix which represents $T$ in Jordan normal form.
    ii. Write down the matrix which represents $T$ in rational normal form.
b. Instead, let $T: V \to V$ be a *nilpotent* linear transformation which has exactly one 2-dimensional invariant subspace.
    i. How many similarity classes of such linear maps $T$ are there?
    ii. Assuming finally that $F$ is the finite field $\mathbb{F}_q$ with $q$ elements, find an explicit formula for the number of such linear maps $T$.
:::

::: {.solution}
**(a) i.** The Jordan normal form is $$\begin{pmatrix} 1&1&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&0\\ 0&0&0&2&0\\ 0&0&0&0&2 \end{pmatrix}$$ (Jordan blocks of sizes $2,1$ for eigenvalue $1$, since the minimal polynomial has $(x-1)^2$ while the characteristic polynomial has $(x-1)^3$; and blocks of sizes $1,1$ for eigenvalue $2$, since the minimal polynomial has $(x-2)^1$ while the characteristic polynomial has $(x-2)^2$.)

**(a) ii.** This is the $F[x]$-module $$\frac{F[x]}{(x-1)} \oplus \frac{F[x]}{(x-1)^2} \oplus \frac{F[x]}{(x-2)} \oplus \frac{F[x]}{(x-2)}$$ By CRT, this is $$\cong \frac{F[x]}{(x-1)(x-2)} \oplus \frac{F[x]}{(x-1)^2(x-2)}$$ with invariant factors $x^2-3x+2$ and $x^3-4x^2+5x-2$.
So the rational normal form is $$S_0 = \begin{pmatrix} 0&-2&0&0&0\\ 1&3&0&0&0\\ 0&0&0&0&2\\ 0&0&1&0&-5\\ 0&0&0&1&4 \end{pmatrix}$$

**(b) i.** One — it must be a single Jordan block: $$\begin{pmatrix} 0&1&&&\\ &0&1&&\\ &&0&1&\\ &&&0&1\\ &&&&0 \end{pmatrix}$$

**(b) ii.** The orbit size equals the index of the centralizer in $GL_5(\mathbb{F}_q)$.
The centralizer of a regular nilpotent (single Jordan block) consists of invertible matrices of the form $$\begin{pmatrix} a&b&c&d&e\\ &a&b&c&d\\ &&a&b&c\\ &&&a&b\\ &&&&a \end{pmatrix}$$ which has order $(q-1)q^4$.
Since $|GL_5(\mathbb{F}_q)| = q^{10}(q^5-1)(q^4-1)(q^3-1)(q^2-1)(q-1)$, the number of such linear maps $T$ is $$\frac{q^{10}(q^5-1)(q^4-1)(q^3-1)(q^2-1)(q-1)}{(q-1)q^4} = q^6(q^5-1)(q^4-1)(q^3-1)(q^2-1)$$
:::
