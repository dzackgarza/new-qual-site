---
schema: qual/card@1
id: P-APAS11I
kind: problem
title: Finite variety implies finite-dimensional quotient, and radical membership
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
---

::: problem
(a) Show that if $I$ is an ideal in $\mathbb{C}[x_1,\ldots,x_n]$ and $V(I)$ is finite, then $\mathbb{C}[x_1,\ldots,x_n]/I$ is finite dimensional when considered as a vector space of $\mathbb{C}$.

(b) Find a reduced Gröbner basis for $I=\langle x^2+xy+y,\ xy+y^2\rangle$ with respect to the graded lexicographic order where $x>y$.

(c) Show that $x^2+y^2\in\sqrt{I}\setminus I$.
:::

::: solution
Let $R=\mathbb C[x_1,\ldots,x_n]$.

For (a), suppose
\[
V(I)=\{a_1,\ldots,a_r\}.
\]
By the Nullstellensatz,
\[
\sqrt I=\mathfrak m_{a_1}\cap\cdots\cap\mathfrak m_{a_r},
\]
where each $\mathfrak m_{a_j}$ is the corresponding maximal ideal. Distinct maximal ideals are comaximal, so by the Chinese remainder theorem
\[
R/\sqrt I\cong \prod_{j=1}^r R/\mathfrak m_{a_j}\cong \mathbb C^r.
\]
Thus $R/\sqrt I$ is finite-dimensional over $\mathbb C$.

Since $R/I$ is Noetherian, the ideal $\sqrt I/I$ is finitely generated. Every one of its generators is nilpotent, so some power of the whole ideal is zero; equivalently, there exists $N$ such that
\[
(\sqrt I)^N\subseteq I.
\]
Hence $R/I$ is a quotient of $R/(\sqrt I)^N$. The latter has a finite filtration
\[
R/(\sqrt I)^N\supset \sqrt I/(\sqrt I)^N\supset\cdots\supset (\sqrt I)^{N-1}/(\sqrt I)^N\supset0,
\]
and each successive quotient is a finitely generated module over $R/\sqrt I$, hence finite-dimensional over $\mathbb C$. Therefore $R/(\sqrt I)^N$, and consequently $R/I$, is finite-dimensional over $\mathbb C$.

For (b), with graded lexicographic order $x>y$, a reduced Gröbner basis is
\[
G=\{y^2,\ xy,\ x^2+y\}.
\]
Indeed, the original generators are
\[
f_1=x^2+xy+y,\qquad f_2=xy+y^2.
\]
From $f_2$ and $f_1-f_2$ we obtain
\[
xy+y^2,\qquad x^2-y^2+y.
\]
Buchberger reduction yields $y^2$, and then these reduce to $xy$ and $x^2+y$. The leading monomials are $y^2,xy,x^2$, and the corresponding $S$-polynomials reduce to zero, so $G$ is a Gröbner basis. Its nonleading terms are reduced with respect to the other leading monomials, hence $G$ is reduced.

For (c), division by $G$ gives
\[
x^2+y^2\equiv -y\pmod I,
\]
so $x^2+y^2\notin I$ because $-y$ is a nonzero standard monomial remainder.

On the other hand, in $R/I$ the Gröbner-basis relations give
\[
y^2=0,\qquad x^2=-y.
\]
Therefore
\[
(x^2+y^2)^2=x^4=y^2=0
\]
in $R/I$. Thus some power of $x^2+y^2$ lies in $I$, so
\[
x^2+y^2\in\sqrt I.
\]
Combining the two conclusions,
\[
x^2+y^2\in\sqrt I\setminus I.
\]
:::
