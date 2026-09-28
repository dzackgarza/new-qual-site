---
schema: qual/card@1
id: P-AGXGATHFINITEPTS
kind: problem
title: Finite point sets in $\AA^n$ as the zero locus of $n$ polynomials
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Varieties
  - Lagrange Interpolation
  - Zero Loci
relations: []
review: draft
---

::: {.problem}
Prove that every affine variety $X\subset \AA^n/k$ consisting of only finitely many points can be written as the zero locus of $n$ polynomials.

> Hint: use interpolation.
> It is useful to assume at first that all points in $X$ have different $x_1\dash$coordinates.
:::

::: {.solution}
Let $X = \ts{\mathbf{p}_1, \cdots, \mathbf{p}_d} = \ts{\mathbf{p}_j}_{j=1}^d$, where each $\mathbf{p}_j\in \AA^n$ is written in coordinates
\[
\mathbf{p}_j \da {\left[ {p_j^1, p_j^2, \cdots, p_j^n} \right]}
.\]

Proof idea: for some fixed $k$ with $2\leq k \leq n$, consider the pairs $(p_j^1, p_j^k) \in \AA^2$.
Letting $j$ range over $1\leq j \leq d$ yields $d$ points of the form $(x, y) \in \AA^2$, so construct an interpolating polynomial such that $f(x) = y$ for each tuple.
Then $f(x) - y$ vanishes at every such tuple.
Doing this for each $k$ (keeping the first coordinate always of the form $p_j^1$ and letting the second coordinate vary) yields $n-1$ polynomials in $k[x_1, x_k] \subseteq k[x_1, \cdots, x_{n}]$; adding the polynomial $p(x) = \prod_j (x-p_j^1)$ yields a system that vanishes precisely on $\ts{\mathbf{p}_j}$.

**Claim**: without loss of generality, all of the first components $\ts{p_j^1}_{j=1}^d$ are distinct.

We use the following fact.

**Lagrange interpolation**: given a set of $d$ points $\ts{(x_i, y_i)}_{i=1}^d$ with all $x_i$ distinct, there is a unique polynomial of degree $d$ in $f \in k[x]$ such that $\tilde f(x_i) = y_i$ for every $i$.
This is given explicitly by
\[
\tilde f(x) = \sum_{i=1}^d y_i \qty{\prod_{\substack{0\leq m \leq d \\ m\neq i}} \qty{x - x_m \over x_i - x_m }}
.\]
Equivalently, there is a polynomial $f$ defined by $f(x_i) = \tilde f(x_i) - y_i$ of degree $d$ whose roots are precisely the $x_i$.

Using this, define a system of $n$ polynomials:

- Define $f_1 \in k[x_1] \subseteq k[x_1, \cdots, x_n]$ by
  \[
  f_1(x) = \prod_{i=1}^d \qty{x - p_i^1}
  .\]
  The roots of $f_1$ are precisely the first components of the points $p$.

- Define $f_2 \in k[x_1, x_2] \subseteq k[x_1, \cdots, x_n]$ by considering the ordered pairs
  \[
  \ts{(x_1, x_2) = (p_j^1, p_j^2)}
  ,\]
  then taking the unique Lagrange interpolating polynomial $\tilde f_2$ satisfying $\tilde f_2(p_j^1) = p_j^2$ for all $1\leq j \leq d$.
  Set $f_2 \da \tilde f_2(x_1) - x_2 \in k[x_1, x_2]$.

- Define $f_3 \in k[x_1, x_3] \subseteq k[x_1, \cdots, x_n]$ by considering the ordered pairs
  \[
  \ts{(x_1, x_3) = (p_j^1, p_j^3)}
  ,\]
  then taking the unique Lagrange interpolating polynomial $\tilde f_3$ satisfying $\tilde f_3(p_j^1) = p_j^3$ for all $1\leq j \leq d$.
  Set $f_3 \da \tilde f_3(x_1) - x_3 \in k[x_1, x_3]$.

- Continuing in this way up to $f_n \in k[x_1, x_n]$ yields a system of $n$ polynomials.

**Proposition**: $V(f_1, \cdots, f_n) = X$.

$X\subseteq V(f_i)$: this is essentially by construction.
Letting $p_j\in X$ be arbitrary,
\[
f_1(p_j)  = \prod_{i=1}^d \qty{p_j^1 - p_i^1} = (p_j^1 - p_j^1) \prod_{\substack{i\leq d \\ i\neq j}} \qty{p_j^1 - p_i^1} = 0
.\]
Similarly, for $2\leq k \leq n$,
\[
f_k(p_j) = \tilde f_k(p_j^1) - p_j^k = 0
,\]
which follows from $\tilde f_k(p_j^1) = p_j^k$ for every $k$ and every $j$ by construction of $\tilde f_k$.

$X^c \subseteq V(f_i)^c$: this follows because the polynomials given by Lagrange interpolation are unique, so the roots of $\tilde f$ are unique.
If some other point were in $V(f_i)$, then one of its coordinates would be another root of some $\tilde f$.
:::

::: {.remark}
Erratum: the source argument has three gaps, retained above as written.

- The reduction to distinct first coordinates is asserted without the coordinate change it needs. Since $X$ is finite and $k$ is infinite, a linear change of coordinates on $\AA^n$ makes the $x_1$-coordinates of the $\mathbf{p}_j$ pairwise distinct, and a linear change of coordinates carries zero loci of $n$ polynomials to zero loci of $n$ polynomials.
- The interpolating polynomial through $d$ points with distinct $x_i$ has degree at most $d-1$, not $d$; the product in the Lagrange formula runs over $1\leq m\leq d$, and the sentence beginning "Equivalently" does not define a polynomial.
- The reverse inclusion $V(f_1,\cdots,f_n)\subseteq X$ does not follow from uniqueness of interpolating polynomials. If $\mathbf{q}\in V(f_1,\cdots,f_n)$, then $f_1(\mathbf{q})=0$ gives $q^1=p_j^1$ for some $j$, and then $f_k(\mathbf{q})=0$ gives $q^k=\tilde f_k(p_j^1)=p_j^k$ for $2\leq k\leq n$, so $\mathbf{q}=\mathbf{p}_j$.
:::
