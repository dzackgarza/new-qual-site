---
schema: qual/card@1
id: P-BERK78S-02
kind: problem
title: When the ring of matrices $\begin{psmallmatrix}a&-b\\b&a\end{psmallmatrix}$ is a field
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
    Wrote the matrices as M(a,b) and checked
    M(a,b)M(c,d)=M(ac-bd,ad+bc), giving a commutative subring with identity.
    A nonzero M(a,b) is invertible exactly when a^2+b^2 is nonzero, so R is
    a field exactly when -1 is not a square in F. This holds for Q and
    Z_7, but not for C or Z_5.
---

::: {.problem}
Let $R$ be the set of $2\times2$ matrices
\[
\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
\qquad a,b\in F,
\]
where $F$ is a field. Show that, with the usual matrix operations, $R$ is a commutative ring with identity.

For which of
\[
F=\mathbb Q,\qquad \mathbb C,\qquad \mathbb Z_5,\qquad \mathbb Z_7
\]
is $R$ a field?
:::

::: {.solution}
For $a,b\in F$, write
$$
M(a,b)
=
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

The set $R$ is closed under addition and additive inverses.

::: pf-proof

For $a,b,c,d\in F$,
$$
M(a,b)+M(c,d)
=
M(a+c,b+d),
$$
and
$$
-M(a,b)
=
M(-a,-b).
$$
Both matrices again lie in $R$. Also
$$
M(0,0)
$$
is the zero matrix.

:::

:::

::: {.pf-step #s2}

The set $R$ is closed under multiplication, and multiplication in
$R$ is commutative.

::: pf-proof

Direct multiplication gives
$$
\begin{aligned}
M(a,b)M(c,d)
&=
\begin{pmatrix}
ac-bd&-(ad+bc)\\
ad+bc&ac-bd
\end{pmatrix}\\
&=
M(ac-bd,ad+bc).
\end{aligned}
$$
The expressions
$$
ac-bd
\quad\text{and}\quad
ad+bc
$$
are symmetric under interchange of $(a,b)$ with $(c,d)$ because $F$ is a
field and hence commutative. Therefore
$$
M(a,b)M(c,d)=M(c,d)M(a,b).
$$

:::

:::

::: {.pf-step #s3}

The ring $R$ has identity
$$
\boxed{
M(1,0)=I_2.
}
$$

::: pf-proof

The matrix $M(1,0)$ is the ordinary $2\times2$ identity matrix, so it is
the multiplicative identity for every element of $R$.

:::

:::

::: {.pf-step #s4}

With the usual matrix operations, $R$ is a commutative ring with
identity.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} give closure under the ring operations, additive inverses,
commutativity of multiplication, and an identity. All remaining ring
axioms are inherited from the matrix ring $M_2(F)$.

:::

:::

::: {.pf-step #s5}

For $M(a,b)\in R$,
$$
\det M(a,b)=a^2+b^2.
$$

::: pf-proof

By the $2\times2$ determinant formula,
$$
\det
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix}
=
a^2-(-b)b
=
a^2+b^2.
$$

:::

:::

::: {.pf-step #s6}

A nonzero element $M(a,b)$ is invertible in $R$ exactly when
$$
a^2+b^2\neq0.
$$

::: pf-proof

If $a^2+b^2\neq0$, then
$$
M(a,b)^{-1}
=
\frac1{a^2+b^2}
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
=
M\left(
\frac{a}{a^2+b^2},
\frac{-b}{a^2+b^2}
\right),
$$
which lies in $R$.

If $a^2+b^2=0$, step [](#s5){.pf-ref} shows that $M(a,b)$ is singular as a matrix, so
it cannot have an inverse in $R$.

:::

:::

::: {.pf-step #s7}

The ring $R$ is a field exactly when $-1$ is not a square in $F$.

::: pf-proof

By step [](#s6){.pf-ref}, $R$ fails to be a field exactly when there are
$(a,b)\neq(0,0)$ such that
$$
a^2+b^2=0.
$$
If $b=0$, then $a^2=0$ and hence $a=0$, so any nontrivial solution has
$b\neq0$. Dividing by $b^2$ gives
$$
\left(\frac ab\right)^2=-1.
$$
Conversely, if $u^2=-1$ in $F$, then
$$
u^2+1^2=0,
$$
so the nonzero matrix $M(u,1)$ is not invertible. Thus the criterion is
exactly that $-1$ have no square root in $F$.

:::

:::

::: {.pf-step #s8}

For $F=\QQ$, the ring $R$ is a field.

::: pf-proof

No rational number has square $-1$, since the square of a rational number
is nonnegative when viewed in $\RR$. Step [](#s7){.pf-ref} applies.

:::

:::

::: {.pf-step #s9}

For $F=\CC$, the ring $R$ is not a field.

::: pf-proof

In $\CC$,
$$
i^2=-1.
$$
Thus step [](#s7){.pf-ref} shows that $R$ is not a field. Explicitly,
$$
M(i,1)
$$
is nonzero and has determinant zero.

:::

:::

::: {.pf-step #s10}

For $F=\ZZ_5$, the ring $R$ is not a field.

::: pf-proof

Modulo $5$,
$$
2^2=4=-1.
$$
Hence $-1$ is a square, and step [](#s7){.pf-ref} applies.

:::

:::

::: {.pf-step #s11}

For $F=\ZZ_7$, the ring $R$ is a field.

::: pf-proof

The squares modulo $7$ are
$$
0,\ 1,\ 2,\ 4.
$$
Since
$$
-1=6
$$
is not among them, $-1$ is not a square in $\ZZ_7$. Step [](#s7){.pf-ref} therefore
shows that $R$ is a field.

:::

:::

::: {.pf-step #s12}

Among the four listed fields,
$$
\boxed{
R\text{ is a field exactly for }F=\QQ\text{ and }F=\ZZ_7.
}
$$

::: pf-proof

This collects steps [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the ring assertion, and step [](#s12){.pf-ref} gives the complete
field classification.

:::

:::

:::
