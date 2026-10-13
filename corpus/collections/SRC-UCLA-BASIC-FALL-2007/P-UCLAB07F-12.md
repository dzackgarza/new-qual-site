---
schema: qual/card@1
id: P-UCLAB07F-12
kind: problem
title: Evaluation functionals and interpolatory quadrature
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $x_0<x_1<\cdots<x_n$ be points in $[a,b]$, and let $\mathbb P^n$ be the vector space of polynomials of degree at most $n$.
Define $l_j:\mathbb P^n\to\mathbb R$ by $l_j(p)=p(x_j)$.

(a) Show that $\{l_j\}_{j=0}^n$ is linearly independent.

(b) Show that there are unique coefficients $c_j$ such that \[\int_a^b p(x)\,dx=\sum_{j=0}^n c_jl_j(p)\] for every $p\in\mathbb P^n$.
:::

::: {.solution}
For each $j=0,\ldots,n$, define the Lagrange polynomial
\[
L_j(x)
=
\prod_{\substack{0\le m\le n\\m\ne j}}
\frac{x-x_m}{x_j-x_m}.
\]

<1>1. For all $j,k\in\{0,\ldots,n\}$,
\[
L_j(x_k)=\delta_{jk}.
\]

::: {.proof}
If $k=j$, every factor in the product equals $1$, so
\[
L_j(x_j)=1.
\]
If $k\ne j$, the factor corresponding to $m=k$ has numerator
\[
x_k-x_k=0,
\]
so
\[
L_j(x_k)=0.
\]
:::

<1>2. The functionals
\[
l_0,\ldots,l_n
\]
are linearly independent in $(\mathbb P^n)^*$.

::: {.proof}
Suppose
\[
\sum_{j=0}^n a_jl_j=0
\]
as a linear functional on $\mathbb P^n$. Fix $k$. Evaluating this functional at $L_k$ gives
\[
0
=
\sum_{j=0}^n a_jl_j(L_k)
=
\sum_{j=0}^n a_jL_k(x_j)
=
a_k
\]
by step <1>1. Since $k$ was arbitrary, every $a_k=0$. Thus the functionals are linearly independent.
:::

<1>3. The set
\[
\{l_0,\ldots,l_n\}
\]
is a basis of $(\mathbb P^n)^*$.

::: {.proof}
The vector space $\mathbb P^n$ has dimension $n+1$, so its dual also has dimension $n+1$. Step <1>2 gives $n+1$ linearly independent vectors in the dual, hence a basis.
:::

<1>4. The map
\[
I:\mathbb P^n\to\mathbb R,
\qquad
I(p)=\int_a^b p(x)\,dx,
\]
is a linear functional.

::: {.proof}
For polynomials $p,q$ and scalars $\alpha,\beta$,
\[
\begin{aligned}
I(\alpha p+\beta q)
&=
\int_a^b(\alpha p(x)+\beta q(x))\,dx\\
&=
\alpha\int_a^b p(x)\,dx
+
\beta\int_a^b q(x)\,dx\\
&=
\alpha I(p)+\beta I(q).
\end{aligned}
\]
:::

<1>5. There exist unique scalars
\[
c_0,\ldots,c_n
\]
such that
\[
I=\sum_{j=0}^n c_jl_j.
\]

::: {.proof}
By step <1>3, the functionals $l_0,\ldots,l_n$ form a basis of $(\mathbb P^n)^*$. By step <1>4, $I$ is an element of this dual space. Therefore $I$ has a unique expansion in that basis.
:::

<1>6. The unique coefficients are
\[
\boxed{
c_j=\int_a^b L_j(x)\,dx
},
\qquad
j=0,\ldots,n.
\]

::: {.proof}
Evaluate the identity from step <1>5 at $L_k$:
\[
\int_a^bL_k(x)\,dx
=
\sum_{j=0}^n c_jL_k(x_j)
=
c_k
\]
by step <1>1.
:::

<1>7. For every $p\in\mathbb P^n$,
\[
\boxed{
\int_a^b p(x)\,dx
=
\sum_{j=0}^n c_jp(x_j)
}.
\]

::: {.proof}
Since
\[
l_j(p)=p(x_j),
\]
the basis expansion in step <1>5 is exactly the displayed identity.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), and steps <1>5--<1>7 prove existence and uniqueness in part (b).
:::
:::
