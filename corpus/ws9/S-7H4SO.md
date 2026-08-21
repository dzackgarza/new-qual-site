---
schema: qual/card@1
id: S-7H4SO
kind: solution
title: Solution to P-B6E7Q
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Simple Groups
relations:
- kind: solves
  target: P-B6E7Q
review: draft
---

::: {.solution}
**(a)** Take $g \in G$.
As $g^N=1$ for some $N$, the min.
poly.
of $\rho(g)$ divides $x^N-1$, which has distinct linear factors.
Hence, $\rho(g)$ is diagonalizable, say to $\operatorname{diag}(c_1,\dots,c_n)$, each $c_i$ a root of unity.
So $\chi(g) = c_1+\cdots+c_n$, and by the triangle inequality $|c_1+\cdots+c_n| \le |c_1|+\cdots+|c_n| = n$, with equality iff $c_1=\cdots=c_n$.

Now $\chi(g)=\chi(1) \iff c_1+\cdots+c_n = n \iff c_1=\cdots=c_n=1 \iff \rho(g)=I \iff g\in\ker\rho$.

**(b)** Note $\alpha,\beta$ are real: by definition of the inner product, $(\chi_2\chi_2^*,\chi_1) = (\chi_2,\chi_2) = 1$.
So $\chi_2\chi_2^* - \chi_1$ is a character of degree 3 with no trivial constituents, so could only be $\chi_4$ or $\chi_5$ (using $\delta\ne1$, else what's $\chi_2\chi_9$?). Also real-valued, so $\alpha,\beta$ are real as values of $\chi_4/\chi_5$.

Dot columns together using this to see: $$0 = C_1\cdot C_2 \Rightarrow \delta^2 = 36 \Rightarrow \delta=6,\ \gamma=0$$ $$0 = C_4\cdot C_7 \Rightarrow 2\gamma = 0$$ $$0 = C_4\cdot C_5 \Rightarrow \alpha+\beta=1$$ $$0 = C_8\cdot C_9 \Rightarrow \alpha\beta=-1$$ so $\alpha,\beta$ are roots of $x^2-x-1$, giving $\alpha,\beta = \dfrac{1\pm\sqrt5}{2}$.

Note now we can also find the conjugacy class sizes.
(See table.)

**(c)** $Z(G) = $ union of classes of size $1$.
So $Z(G) = C_1 \cup C_2$, size $2$, while $|G|=120$.
So $|G/Z(G)| = 60$.

If $C_2=\{z\}$, $z^2=1$, so it's either $+1$ or $-1$ on each irrep.
The irreps of $G/Z(G)$ are the same as ones of $G$ on which $z$ is $+1$.
Classes in $G/Z(G)$ are either images of $1$ or $2$ classes in $G$:

|  | $C_1\cup C_2$ | $C_3\cup C_7$ | $C_4$ | $C_5\cup C_9$ | $C_6\cup C_8$ |
| --- | --- | --- | --- | --- | --- |
| $\chi_1$ | 1 | 1 | 1 | 1 | 1 |
| $\chi_4$ | 3 | 0 | -1 | $\beta$ | $\alpha$ |
| $\chi_5$ | 3 | 0 | -1 | $\alpha$ | $\beta$ |
| $\chi_7$ | 4 | 1 | 0 | -1 | -1 |
| $\chi_8$ | 5 | -1 | 1 | 0 | 0 |

Observe it's a simple group of order 60. So it must be $A_5$.
:::
