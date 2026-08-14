---
schema: qual/card@1
id: S-WTH5Z
kind: solution
title: Solution to P-B2P3P
classification:
  areas:
  - algebra
  topics:
  - jordan-canonical-form
  - rational-canonical-form
  - nilpotence
relations:
- kind: solves
  target: P-B2P3P
review: draft
---

:::{.solution}
**(a) i.** The Jordan normal form is
$$\begin{pmatrix} 1&1&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&0\\ 0&0&0&2&0\\ 0&0&0&0&2 \end{pmatrix}$$
(Jordan blocks of sizes $2,1$ for eigenvalue $1$, since the minimal polynomial has $(x-1)^2$ while the characteristic polynomial has $(x-1)^3$; and blocks of sizes $1,1$ for eigenvalue $2$, since the minimal polynomial has $(x-2)^1$ while the characteristic polynomial has $(x-2)^2$.)

**(a) ii.** This is the $F[x]$-module
$$\frac{F[x]}{(x-1)} \oplus \frac{F[x]}{(x-1)^2} \oplus \frac{F[x]}{(x-2)} \oplus \frac{F[x]}{(x-2)}$$
By CRT, this is
$$\cong \frac{F[x]}{(x-1)(x-2)} \oplus \frac{F[x]}{(x-1)^2(x-2)}$$
with invariant factors $x^2-3x+2$ and $x^3-4x^2+5x-2$. So the rational normal form is
$$S_0 = \begin{pmatrix} 0&-2&0&0&0\\ 1&3&0&0&0\\ 0&0&0&0&2\\ 0&0&1&0&-5\\ 0&0&0&1&4 \end{pmatrix}$$

**(b) i.** One — it must be a single Jordan block:
$$\begin{pmatrix} 0&1&&&\\ &0&1&&\\ &&0&1&\\ &&&0&1\\ &&&&0 \end{pmatrix}$$

**(b) ii.** The orbit size equals the index of the centralizer in $GL_5(\mathbb{F}_q)$. The centralizer of a regular nilpotent (single Jordan block) consists of invertible matrices of the form
$$\begin{pmatrix} a&b&c&d&e\\ &a&b&c&d\\ &&a&b&c\\ &&&a&b\\ &&&&a \end{pmatrix}$$
which has order $(q-1)q^4$. Since $|GL_5(\mathbb{F}_q)| = q^{10}(q^5-1)(q^4-1)(q^3-1)(q^2-1)(q-1)$, the number of such linear maps $T$ is
$$\frac{q^{10}(q^5-1)(q^4-1)(q^3-1)(q^2-1)(q-1)}{(q-1)q^4} = q^6(q^5-1)(q^4-1)(q^3-1)(q^2-1)$$
:::
