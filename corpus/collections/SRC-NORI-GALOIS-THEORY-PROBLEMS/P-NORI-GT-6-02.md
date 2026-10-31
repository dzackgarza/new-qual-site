---
schema: qual/card@1
id: P-NORI-GT-6-02
kind: problem
title: The splitting algebra of a monic polynomial is free with monomial basis
classification:
  areas: [algebra]
  topics:
  - Splitting Algebras
  - Symmetric Polynomials
  - Free Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 6.2 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rejoined the split quotient formula and removed the section note that belongs to the following problems, against Problem 6.2 on p. 5 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $f(T) = T^n - a_1 T^{n-1} + \cdots + (-1)^n a_n \in A[T]$.
Let $B = A[X_1, X_2, \ldots, X_n]/(s_1 - a_1, s_2 - a_2, \ldots, s_n - a_n)$, where $s_1, s_2, \ldots, s_n$ are the elementary symmetric polynomials in $X_1, X_2, \ldots, X_n$.
Prove that $B$ is a free $A$-module with basis (as the image in $B$) of the monomials $X_1^{m_1} X_2^{m_2} \cdots X_n^{m_n}$ where all the $m_i$ are non-negative integers such that $m_i + i \leq n$ for all $i = 1, 2, \ldots, n$.

Prove this for $n = 3$.
:::

::: {.solution}

Write
$$
f_0(T)=f(T)=T^n-a_1T^{n-1}+\cdots+(-1)^n a_n.
$$
We construct a tower of $A$-algebras by adjoining the roots one at a time.

::: pf

::: {.pf-step #s1-1}

Define recursively
$$
R_0=A,
$$
and, for $1\leq i\leq n$,
$$
R_i=R_{i-1}[x_i]/(f_{i-1}(x_i)),
$$
where $f_{i-1}(T)\in R_{i-1}[T]$ is monic of degree $n-i+1$, and define
$$
f_i(T)=\frac{f_{i-1}(T)}{T-x_i}\in R_i[T].
$$
Then $f_i(T)$ is monic of degree $n-i$ and
$$
f(T)=\prod_{j=1}^i(T-x_j)f_i(T)
$$
in $R_i[T]$.


::: pf-proof

For $i=1$, the class $x_1\in R_1$ satisfies $f_0(x_1)=0$. Since $T-x_1$ is monic, polynomial division in $R_1[T]$ gives
$$
f_0(T)=(T-x_1)q(T)+r
$$
with $q$ monic of degree $n-1$ and $r\in R_1$. Evaluating at $T=x_1$ gives $r=f_0(x_1)=0$, so $f_0(T)=(T-x_1)q(T)$. Set $f_1=q$.

The same argument applies inductively. In $R_i$, the element $x_i$ is a root of the monic polynomial $f_{i-1}$ by construction, so division by $T-x_i$ has zero remainder and produces a monic polynomial $f_i$ of degree one less. Multiplying the factorizations obtained at each stage yields
$$
f(T)=\prod_{j=1}^i(T-x_j)f_i(T).
$$

:::

:::

::: {.pf-step #s1-2}

For each $1\leq i\leq n$, the algebra $R_i$ is free as an $R_{i-1}$-module with basis
$$
1,x_i,x_i^2,\ldots,x_i^{n-i}.
$$


::: pf-proof

The polynomial $f_{i-1}(T)$ is monic of degree $n-i+1$. For any commutative ring $R$ and monic polynomial $h(T)$ of degree $d$, every polynomial admits a unique division
$$
q(T)h(T)+r(T),
\qquad
\deg r<d.
$$
Therefore $R[T]/(h)$ is a free $R$-module with basis
$$
1,T,\ldots,T^{d-1}.
$$
Applying this with $R=R_{i-1}$, $h=f_{i-1}$, and $d=n-i+1$ gives the asserted basis.

:::

:::

::: {.pf-step #s1-3}

The algebra $R_n$ is free as an $A$-module with basis
$$
\boxed{x_1^{m_1}x_2^{m_2}\cdots x_n^{m_n}
: 0\leq m_i\leq n-i}.
$$


::: pf-proof

Apply step [](#s1-2){.pf-ref} successively through the tower
$$
A=R_0\subseteq R_1\subseteq\cdots\subseteq R_n.
$$
At the $i$-th stage, multiplication by the $R_{i-1}$-basis
$$
1,x_i,\ldots,x_i^{n-i}
$$
extends every $A$-basis of $R_{i-1}$ to an $A$-basis of $R_i$. Induction therefore gives precisely all products
$$
x_1^{m_1}\cdots x_n^{m_n}
$$
with $0\leq m_i\leq n-i$, equivalently $m_i+i\leq n$.

:::

:::

::: {.pf-step #s1-4}

In $R_n[T]$ one has
$$
f(T)=\prod_{i=1}^n(T-x_i).
$$
Consequently the elementary symmetric polynomials in $x_1,\ldots,x_n$ satisfy
$$
s_i(x_1,\ldots,x_n)=a_i
$$
for $1\leq i\leq n$.


::: pf-proof

Step [](#s1-1){.pf-ref} with $i=n$ gives
$$
f(T)=\prod_{j=1}^n(T-x_j)f_n(T).
$$
The polynomial $f_n$ is monic of degree $0$, hence $f_n(T)=1$. Thus
$$
f(T)=\prod_{j=1}^n(T-x_j).
$$
Expanding the product and comparing coefficients with
$$
f(T)=T^n-a_1T^{n-1}+\cdots+(-1)^na_n
$$
gives $s_i(x_1,\ldots,x_n)=a_i$ for every $i$.

:::

:::

::: pf-step

There is an $A$-algebra homomorphism
$$
\Phi:B\longrightarrow R_n
$$
sending the class of $X_i$ to $x_i$.


::: pf-proof

By step [](#s1-4){.pf-ref}, the elements $x_1,\ldots,x_n$ satisfy all relations
$$
s_i-a_i=0
$$
defining $B$. Hence the homomorphism
$$
A[X_1,\ldots,X_n]\longrightarrow R_n,
\qquad
X_i\longmapsto x_i,
$$
annihilates the ideal $(s_1-a_1,\ldots,s_n-a_n)$ and therefore factors through $B$.

:::

:::

::: pf-step

There is an $A$-algebra homomorphism
$$
\Psi:R_n\longrightarrow B
$$
sending $x_i$ to the class of $X_i$.


::: pf-proof

Let $\overline X_i$ denote the class of $X_i$ in $B$. By the defining relations of $B$,
$$
\prod_{i=1}^n(T-\overline X_i)
=T^n-s_1T^{n-1}+\cdots+(-1)^ns_n
=f(T)
$$
in $B[T]$.

Thus $\overline X_1$ is a root of $f_0=f$, so the map $A\to B$ extends to
$$
R_1=A[x_1]/(f_0(x_1))\longrightarrow B,
\qquad
x_1\longmapsto\overline X_1.
$$
After dividing the displayed factorization by $T-\overline X_1$, the image of $f_1(T)$ is
$$
\prod_{j=2}^n(T-\overline X_j),
$$
so $\overline X_2$ is a root of the image of $f_1$. Hence the map extends to $R_2$. Repeating this argument extends successively through the tower to a map
$$
\Psi:R_n\to B
$$
with $\Psi(x_i)=\overline X_i$ for all $i$.

:::

:::

::: {.pf-step #s1-7}

The homomorphisms $\Phi$ and $\Psi$ are inverse isomorphisms.


::: pf-proof

The algebra $B$ is generated over $A$ by the classes $\overline X_1,\ldots,\overline X_n$, and
$$
(\Psi\circ\Phi)(\overline X_i)=\overline X_i
$$
for each $i$. Hence $\Psi\circ\Phi=\operatorname{id}_B$.

Likewise, $R_n$ is generated over $A$ by $x_1,\ldots,x_n$, and
$$
(\Phi\circ\Psi)(x_i)=x_i
$$
for each $i$. Hence $\Phi\circ\Psi=\operatorname{id}_{R_n}$.

:::

:::

::: {.pf-step #s1-8}

Therefore $B$ is a free $A$-module with basis
$$
\boxed{X_1^{m_1}X_2^{m_2}\cdots X_n^{m_n}
: m_i\geq0,\ m_i+i\leq n}.
$$


::: pf-proof

By step [](#s1-7){.pf-ref}, $B\cong R_n$ via an isomorphism carrying the class of $X_i$ to $x_i$. The basis of step [](#s1-3){.pf-ref} therefore transports to the displayed basis of $B$.

:::

:::

::: {.pf-step #s1-9}

For $n=3$, a basis is
$$
\boxed{1,\ X_1,\ X_1^2,\ X_2,\ X_1X_2,\ X_1^2X_2}.
$$


::: pf-proof

When $n=3$, the inequalities $m_i+i\leq3$ give
$$
0\leq m_1\leq2,
\qquad
0\leq m_2\leq1,
\qquad
m_3=0.
$$
Thus the monomials in step [](#s1-8){.pf-ref} are exactly the six displayed elements.

Concretely, the tower is
$$
A
\subseteq
A[x_1]/(f(x_1))
\subseteq
A[x_1,x_2]/\bigl(f(x_1),q(x_2)\bigr),
$$
where
$$
q(T)=T^2+(x_1-a_1)T+(x_1^2-a_1x_1+a_2).
$$
The first extension has basis $1,x_1,x_1^2$ and the second has basis $1,x_2$, giving the same six $A$-basis elements.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves the general statement, and step [](#s1-9){.pf-ref} gives the requested case $n=3$ explicitly.

:::

:::

:::
