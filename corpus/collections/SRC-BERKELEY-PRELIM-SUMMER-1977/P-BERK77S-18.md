---
schema: qual/card@1
id: P-BERK77S-18
kind: problem
title: Continuous dependence of a simple polynomial root on the coefficients
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Applied the implicit function theorem to
    F(a,z)=sum_j a_j z^j. Simplicity of the reference root says the
    derivative with respect to z is nonzero; as a real 2-by-2 Jacobian this
    is multiplication by a nonzero complex number and hence invertible.
    The resulting local root function is C^1, in particular continuous.
---

::: {.problem}
Let
\[
\widehat a_0+\widehat a_1z+\cdots+\widehat a_nz^n
\]
have $\widehat z$ as a simple root. Show that there are a neighborhood
\[
U\subset\mathbb C^{n+1}
\]
of $(\widehat a_0,\dots,\widehat a_n)$ and a continuous function $r:U\to\mathbb C$ such that $r(a_0,\dots,a_n)$ is a root of
\[
a_0+a_1z+\cdots+a_nz^n
\]
for every $(a_0,\dots,a_n)\in U$, and
\[
r(\widehat a_0,\dots,\widehat a_n)=\widehat z.
\]
:::

::: {.solution}
For
$$
a=(a_0,\ldots,a_n)\in\CC^{n+1},
$$
define
$$
F(a,z)=\sum_{j=0}^n a_jz^j.
$$
Also write
$$
\widehat a=(\widehat a_0,\ldots,\widehat a_n).
$$

::: pf

::: {.pf-step #s1}

One has
$$
F(\widehat a,\widehat z)=0
$$
and
$$
\frac{\partial F}{\partial z}(\widehat a,\widehat z)\neq0.
$$

::: pf-proof

The first equality says exactly that $\widehat z$ is a root of the
reference polynomial. Since that root is simple, the derivative of the
reference polynomial does not vanish there:
$$
\sum_{j=1}^n
j\widehat a_j\widehat z^{\,j-1}
\neq
0.
$$
This sum is $\partial F/\partial z$ at
$(\widehat a,\widehat z)$.

:::

:::

::: {.pf-step #s2}

Regard
$$
F:\CC^{n+1}\times\CC\longrightarrow\CC
$$
as a real $C^1$ map
$$
F:\RR^{2n+2}\times\RR^2\longrightarrow\RR^2.
$$
Its real derivative with respect to the final $\RR^2$ variable is
invertible at $(\widehat a,\widehat z)$.

::: pf-proof

Set
$$
c=\frac{\partial F}{\partial z}(\widehat a,\widehat z).
$$
By step [](#s1){.pf-ref}, $c\neq0$. Because $F$ is holomorphic in $z$, its real
differential in the $z$ variable is multiplication by the complex number
$c$. If
$$
c=u+iv,
$$
the corresponding real matrix is
$$
\begin{pmatrix}
u&-v\\
v&u
\end{pmatrix},
$$
whose determinant is
$$
u^2+v^2
=
\abs{c}^2
>
0.
$$
Hence this real derivative is invertible.

:::

:::

::: {.pf-step #s3}

There are neighborhoods
$$
U\subset\CC^{n+1}
\quad\text{of }\widehat a
$$
and
$$
W\subset\CC
\quad\text{of }\widehat z
$$
and a $C^1$ function
$$
r:U\longrightarrow W
$$
such that
$$
F(a,r(a))=0
$$
for every $a\in U$, with
$$
r(\widehat a)=\widehat z.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
F(\widehat a,\widehat z)=0,
$$
and step [](#s2){.pf-ref} gives invertibility of the derivative in the $z$ variable.
The real implicit function theorem therefore applies to $F$ at
$(\widehat a,\widehat z)$ and gives the stated neighborhoods and function
$r$.

:::

:::

::: {.pf-step #s4}

For every
$$
a=(a_0,\ldots,a_n)\in U,
$$
the number $r(a)$ is a root of
$$
a_0+a_1z+\cdots+a_nz^n.
$$

::: pf-proof

By step [](#s3){.pf-ref},
$$
0
=
F(a,r(a))
=
\sum_{j=0}^n a_jr(a)^j.
$$
This is precisely the assertion that $r(a)$ is a root of the polynomial
with coefficient vector $a$.

:::

:::

::: {.pf-step #s5}

The function
$$
\boxed{
r:U\longrightarrow\CC
}
$$
has all the required properties.

::: pf-proof

Step [](#s3){.pf-ref} says that $r$ is $C^1$, hence continuous, and that
$$
r(\widehat a)=\widehat z.
$$
Step [](#s4){.pf-ref} says that $r(a)$ is always a root of the polynomial with
coefficients $a$. These are exactly the requested properties.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the statement.

:::

:::

:::
