---
schema: qual/card@1
id: P-NORI-GT-6-05
kind: problem
title: Additive subgroups of an algebraically closed field and additive polynomials
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 6.5 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Assume that $F$ is algebraically closed. Show that $A \mapsto f_{A}$ is a one-to-one correspondence from the collection of additive subgroups $A \subset F$ of order $p^{n}$ and the set of polynomials in $F[X]$ of the form $f = a_{0}X + a_{1}X^{p} + \cdots + a_{n-1}X^{p^{n-1}} + X^{p^{n}}$ with $a_{0} \neq 0$.
:::

::: {.solution}

As in the preceding problems of this section, $F$ has characteristic $p>0$.

::: pf

::: {.pf-step #s1-1}

Let $A\subset F$ be an additive subgroup of order $p^n$. Then
$$
f_A(X)=\prod_{a\in A}(X-a)
$$
is monic of degree $p^n$ and satisfies
$$
f_A(X+Y)=f_A(X)+f_A(Y).
$$


::: pf-proof

The product defining $f_A$ has exactly $p^n$ monic linear factors, so it is monic of degree $p^n$. By Problem 6.3, the polynomial attached to every finite additive subgroup satisfies the displayed additivity identity.

:::

:::

::: {.pf-step #s1-2}

There exist coefficients $a_0,\ldots,a_{n-1}\in F$ such that
$$
f_A(X)=a_0X+a_1X^p+\cdots+a_{n-1}X^{p^{n-1}}+X^{p^n}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $f_A$ is additive. Problem 6.4 therefore shows that every exponent occurring in $f_A$ is a power of $p$. Since $f_A$ is monic of degree $p^n$, its highest term is exactly $X^{p^n}$, and all lower possible terms have exponents $1,p,\ldots,p^{n-1}$.

:::

:::

::: {.pf-step #s1-3}

The coefficient $a_0$ in step [](#s1-2){.pf-ref} is nonzero.


::: pf-proof

The roots of $f_A$ are exactly the distinct elements of $A$. Hence $f_A$ is separable. On the other hand, differentiating the expression in step [](#s1-2){.pf-ref} in characteristic $p$ gives
$$
f_A'(X)=a_0,
$$
because the derivative of $X^{p^i}$ is zero for every $i\geq1$. A polynomial with zero derivative cannot be separable unless it is constant, whereas $f_A$ has degree $p^n\geq1$. Therefore $a_0\neq0$.

:::

:::

::: {.pf-step #s1-4}

The map
$$
A\longmapsto f_A
$$
is injective.


::: pf-proof

The roots of $f_A$ in $F$ are exactly the elements of $A$. Thus if
$$
f_A=f_{A'},
$$
then the two polynomials have the same root set, so $A=A'$.

:::

:::

::: {.pf-step #s1-5}

Conversely, let
$$
f(X)=a_0X+a_1X^p+\cdots+a_{n-1}X^{p^{n-1}}+X^{p^n}
$$
with $a_0\neq0$. Then $f$ has exactly $p^n$ distinct roots in $F$.


::: pf-proof

The polynomial $f$ is monic of degree $p^n$. Since $F$ is algebraically closed, it has $p^n$ roots counted with multiplicity. Its derivative is
$$
f'(X)=a_0\neq0,
$$
so $f$ has no repeated roots. Therefore it has exactly $p^n$ distinct roots in $F$.

:::

:::

::: pf-step

The root set
$$
A_f=\{x\in F:f(x)=0\}
$$
is an additive subgroup of $F$ of order $p^n$.


::: pf-proof

By Problem 6.4, the displayed form of $f$ implies
$$
f(X+Y)=f(X)+f(Y).
$$
Hence $f(0)=0$. If $x,y\in A_f$, then
$$
f(x+y)=f(x)+f(y)=0,
$$
so $x+y\in A_f$. Also
$$
0=f(0)=f(x+(-x))=f(x)+f(-x),
$$
and therefore $f(-x)=0$ whenever $f(x)=0$. Thus $A_f$ is an additive subgroup. By step [](#s1-5){.pf-ref}, it has exactly $p^n$ elements.

:::

:::

::: {.pf-step #s1-7}

One has
$$
f=f_{A_f}.
$$


::: pf-proof

Both polynomials are monic of degree $p^n$, and by definition both have precisely the elements of $A_f$ as their roots. Step [](#s1-5){.pf-ref} shows these roots are distinct. Therefore
$$
f(X)=\prod_{a\in A_f}(X-a)=f_{A_f}(X).
$$

:::

:::

::: {.pf-step #s1-8}

The assignment $A\mapsto f_A$ is a bijection between the two collections in the statement.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} show that the assignment lands in the stated set of polynomials. Step [](#s1-4){.pf-ref} proves injectivity. Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} show that every polynomial in the stated set equals $f_A$ for the additive subgroup formed by its roots, proving surjectivity.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is exactly the claimed one-to-one correspondence.

:::

:::

:::
