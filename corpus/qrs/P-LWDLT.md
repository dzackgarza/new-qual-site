---
schema: qual/card@1
id: P-LWDLT
kind: problem
title: "Let $A$ be an $n \\times n$ matrix."
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $A$ be an $n \times n$ matrix.

a.
Suppose that $v$ is a column vector such that the set $\{v, Av, . . . , A^{n-1} v\}$ is linearly independent. Show that any matrix $B$ that commutes with $A$ is a polynomial in $A$.

b.
Show that there exists a column vector $v$ such that the set $\{v, Av, . . . , A^{n-1} v\}$ is linearly independent $\iff$ the characteristic polynomial of $A$ equals the minimal polynomial of A.

:::{.concept}
\envlist

- Powers of $A$ commute with polynomials in $A$.
- The image of a linear map is determined by the image of a basis
:::

:::{.strategy}
\envlist

- Use Cayley-Hamilton to relate the minimal polynomial to a linear dependence.
- Get a lower bound on the degree of the minimal polynomial.
- Use $A\actson k[x]$ to decompose into cyclic $k[x]\dash$modules, and use special form of denominators in the invariant factors.
- Reduce to monomials.
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
Letting $\vector v$ be fixed, since $\theset{A^j \vector v}$ spans $V$ we have A
\[
B\vector v = \sum_{j=0}^{n-1}c_j A^j \vector v
.\]

So let $p(x) = \sum_{j=0}^{n-1}c_jx^j$.
Then consider how $B$ acts on any basis vector $A^k \vector v$.

We have 
\[
BA^k \vector v 
&= A^k B\vector v \\
&= A^k p(A) \vector v \\
&= p(A) A^k \vector v
,\]

so $B = p(A)$ as operators since their actions agree on every basis vector in $V$.

:::

:::{.proof title="of b, $\implies$"}
\envlist

- If $\theset{A^j \vector v_k \suchthat 0\leq j \leq n-1}$ is linearly independent, this means that $A$ does satisfy any polynomial of degree $d < n$.

- So $\deg m_A(x) = n$, and since $m_A(x)$ divides $\chi_A(x)$ and both are monic degree polynomials of degree $n$, they must be equal.
:::

:::{.proof title="of b, $\impliedby$"}
\envlist

- Let $A\actson k[x]$ by $A \actson p(x) \definedas p(A)$.
  This induces an invariant factor decomposition $V =\cong \bigoplus k[x]/(f_i)$.

- Since the product of the invariant factors is the characteristic polynomial, the largest invariant factor is the minimal polynomial, and these two are equal, there can only be one invariant factor and thus the invariant factor decomposition is
$$
V\cong \frac{k[x]}{(\chi_A(x))}
$$
  as an isomorphism of $k[x]\dash$modules.

- So $V$ is a cyclic $k[x]$ module, which means that $V = k[x]\actson \vector v$ for some $\vector v\in V$ such that $\ann(\vector v) = \chi_A(x)$, i.e. there is some element $\vector v\in V$ whose orbit is all of $V$.

- But then noting that monomials span $k[x]$ as a $k\dash$module, we can write
\[
V &\cong
k[x] \actson \vector v \\
&\definedas \theset{f(x) \actson \vector v \suchthat f \in k[x]} \\
&= \spanof_k \theset{x^k \actson \vector v \suchthat k \geq 0} \\
&\definedas \spanof_k \theset{A^k\vector v \suchthat k \geq 0}
,\]
  where we've used that $x$ acts by $A$ and thus $x^k$ acts by $A^k$.

- Moreover, we can note that if $\ell \geq \deg \chi_A(x)$, then $A^\ell$ is a linear combination of $\theset{A^j \mid 0 \leq j \leq n-1}$, and so
\[
V &\cong \spanof_k \theset{A^\ell\vector v \suchthat \ell \geq 0} \\
&= \spanof_k \theset{A^\ell \vector v \suchthat 1 \leq \ell \leq n-1}
.\]

:::

:::

