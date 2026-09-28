---
schema: qual/card@1
id: P-AGH38REGCONST
kind: problem
title: Regular functions off a codimension two linear subspace of $\PP^n$ are constant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Regular Functions
  - Hyperplanes
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with Hartshorne I.3.8. The proof uses the standard affine charts D_+(x_i) and D_+(x_j), writes a regular function as homogeneous fractions there, and uses coprimality of x_i and x_j.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the chart description and homogeneous-fraction divisibility argument against published discussions of I.3.8.'
---

::: {.problem}
Let $H_i$ and $H_j$ be the hyperplanes in $\PP^n$ defined by $x_i = 0$ and $x_j = 0$, with $i \neq j$.
Show that any regular function on $\PP^n \sm (H_i \intersect H_j)$ is constant.
:::

::: {.solution}
Put
$$
U_i=\PP^n\setminus H_i=D_+(x_i),
\qquad
U_j=\PP^n\setminus H_j=D_+(x_j).
$$
Then
$$
\PP^n\setminus(H_i\cap H_j)=U_i\cup U_j.
$$

<1>1. Every regular function on $U_i$ has the form
$$
\frac{F}{x_i^a}
$$
for some $a\ge0$ and some homogeneous polynomial $F\in k[x_0,\ldots,x_n]$ of degree $a$, and similarly on $U_j$.

::: {.proof}
The standard chart $U_i$ is isomorphic to $\AA^n$ with affine coordinates $x_\ell/x_i$ for $\ell\ne i$.
A regular function on $U_i$ is therefore a polynomial in these ratios.
Choose $a$ at least the total degree of that polynomial and put all terms over the common denominator $x_i^a$.
Multiplying each numerator monomial by the required power of $x_i$ produces a homogeneous polynomial $F$ of degree $a$.
The same argument applies to $U_j$.
:::

<1>2. A regular function on $U_i\cup U_j$ is constant.

::: {.proof}
Let $f$ be regular on $U_i\cup U_j$.
By step <1>1, choose homogeneous polynomials $F,G$ with
$$
f|_{U_i}=\frac{F}{x_i^a},
\qquad
f|_{U_j}=\frac{G}{x_j^b},
$$
where $\deg F=a$ and $\deg G=b$.
On the nonempty overlap $U_i\cap U_j$, these rational functions agree, hence in the polynomial ring
$$
F x_j^b=G x_i^a.
$$
The variables $x_i$ and $x_j$ are relatively prime prime elements of the UFD $k[x_0,\ldots,x_n]$.
Therefore $x_i^a$ divides $F$.
Since $F$ is homogeneous of degree exactly $a$, we have
$$
F=cx_i^a
$$
for some $c\in k$.
Thus $f=c$ on $U_i$.
Substituting in the equality on the overlap gives $G=cx_j^b$, so $f=c$ on $U_j$ as well.
Hence $f$ is constant on their union.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 applies to every regular function on $\PP^n\setminus(H_i\cap H_j)$.
:::
:::
