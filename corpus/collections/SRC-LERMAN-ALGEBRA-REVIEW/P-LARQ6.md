---
schema: qual/card@1
id: P-LARQ6
kind: problem
title: Dimension of a polynomial quotient
classification:
  areas: [algebra]
  topics: [Linear Algebra, Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the degree hypothesis and proposed quotient basis with Lerman practice problem 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used polynomial division for spanning and a degree argument for linear independence, and checked the quotient carries the induced F-vector-space structure."
---

::: problem
Let $F$ be a field, and let $p\in F[x]$ have degree $n\geq1$.
Prove that $F[x]/(p)$ is an $n$-dimensional vector space over $F$.
Show that
$$
\{1+(p),x+(p),\ldots,x^{n-1}+(p)\}
$$
is a basis.
:::

::: solution
<1>1. The quotient is naturally an $F$-vector space.
::: proof
The ideal $(p)$ is closed under multiplication by constants from $F$. Hence scalar multiplication
$$
a\cdot(f+(p))=af+(p)
$$
is well-defined for $a\in F$ and $f\in F[x]$. Together with the quotient addition, this gives the usual $F$-vector-space structure on $F[x]/(p)$.
:::

<1>2. The displayed classes span the quotient.
::: proof
For any $f\in F[x]$, the division algorithm gives unique polynomials $q,r\in F[x]$ such that
$$
f=qp+r,
\qquad \deg r<n
$$
or $r=0$. Therefore
$$
f+(p)=r+(p).
$$
Writing
$$
r=a_0+a_1x+\cdots+a_{n-1}x^{n-1}
$$
shows that every coset is an $F$-linear combination of
$$
1+(p),x+(p),\ldots,x^{n-1}+(p).
$$
:::

<1>3. The displayed classes are linearly independent.
::: proof
Suppose
$$
a_0(1+(p))+a_1(x+(p))+\cdots+a_{n-1}(x^{n-1}+(p))=0+(p).
$$
Then the polynomial
$$
r=a_0+a_1x+\cdots+a_{n-1}x^{n-1}
$$
belongs to $(p)$, so $r=qp$ for some $q\in F[x]$. If $q\ne0$, then
$$
\deg r=\deg q+\deg p\ge n,
$$
contrary to $\deg r<n$. Thus $q=0$, hence $r=0$, so every coefficient $a_i$ is zero. Therefore the classes are linearly independent.

They are consequently a basis of size $n$, and
$$
\dim_F F[x]/(p)=n.
$$
:::
:::
