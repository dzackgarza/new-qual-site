---
schema: qual/card@1
id: P-IPPKZ
kind: problem
title: Spring 2021
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
  - Integral Domains
relations: []
review: draft
solved: true
---

:::{.problem title="Spring 2021"}
Suppose that $f(x) \in (\ZZ/n\ZZ)[x]$ is a zero divisor.
Show that there is a nonzero $a\in \ZZ/n\ZZ$ with $af(x) = 0$.
:::

:::{.solution}
\envlist

- Write $f(x) = \sum_{k=0}^n a_k x^k$, and supposing it's a zero divisor choose $g(x) = \sum_{k=0}^m b_k x^k$ of minimal degree so that $g\neq 0, b_m\neq 0$, and $f(x)g(x) = 0$.
- The claim is that the top coefficient $b_m$ will suffice.
- Write the product:
\[
0 = f(x)g(x) 
= (a_0 + \cdots + a_{n-1}x^{n-1} + a_n x^n)
(b_0 + \cdots + b_{m-1}x^{m-1} + b_m x^m)
.\]
- Equating coefficients, the coefficient for $x^{m+n}$ must be zero, so (**importantly**) $a_n b_m = 0$.
  - Since $a_n b_m=0$, consider $a_ng(x)$.
    This has degree $d_1 \leq m-1$ but satisfies $a_ng(x)f(x) = a_n(g(x)f(x)) = 0$, so by minimality $a_ng(x) = 0$.
  - This forces $a_n b_0 = \cdots = a_n b_{m-1} = 0$, so $a_n$ annihilates all of the $b_k$.
- Now consider the coefficient of $x^{m+n-1}$, given by $a_{n-1}b_m + a_{n}b_{m-1}$.
  - The second term $a_n b_{m-1}=0$ since $a_n$ annihilates all $b_k$, so (**importantly**) $a_{n-1} b_m = 0$.
  - Considering now $a_{n-1}g(x)$:
    - The same argument shows this has degree $d_2 \leq m-1$ but $a_{n-1}g(x)f(x) = 0$, so $a_{n-1}g(x) = 0$.
    - So $a_{n-1}$ annihilates all $b_k$, and allowing this process to continue inductively.
- For good measure, the coefficient of $x^{m+n-2}$ is $a_{n-2}b_m + a_{n-1}b_{m-1} + a_{n}b_{m-2}$.
  - Note that $a_n, a_{n-1}$ annihilate all $b_k$, so (**importantly**) $a_{n-2} b_m=0$, and so on.

- Thus $a_k b_m = 0$ for all $0\leq k \leq n$, and by linearity and commutativity, we have
\[
b_m f(x) = b_m \sum_{k=0}^n a_k x^k = \sum_{k=0}^n (b_m a_k) x^k = 0
.\]

:::
