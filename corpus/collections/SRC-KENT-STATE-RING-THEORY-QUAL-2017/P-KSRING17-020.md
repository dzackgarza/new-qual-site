---
schema: qual/card@1
id: P-KSRING17-020
kind: problem
title: Chinese remainder theorem for two comaximal ideals
classification:
  areas: [algebra]
  topics:
  - Chinese Remainder Theorem
  - Comaximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 20 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with 1 and let I and J be ideals of R such that $I + J = R$ Show that $R / ( I \cap J ) \cong R / I \oplus R / J$ .
:::

::: {.solution}

Define
$$
\varphi:R\to R/I\oplus R/J
$$
by
$$
\varphi(r)
\coloneqq
(r+I,r+J).
$$

::: pf

::: {.pf-step #s1-1}

The map $\varphi$ is a ring homomorphism.


::: pf-proof

For
$$
r,s\in R,
$$
coordinatewise operations give
$$
\begin{aligned}
\varphi(r+s)
&=
(r+s+I,r+s+J)\\
&=
\varphi(r)+\varphi(s),
\end{aligned}
$$
and
$$
\begin{aligned}
\varphi(rs)
&=
(rs+I,rs+J)\\
&=
\varphi(r)\varphi(s).
\end{aligned}
$$
Also
$$
\varphi(1_R)
=
(1_R+I,1_R+J),
$$
the identity of the product ring.

:::

:::

::: {.pf-step #s1-2}

The kernel of $\varphi$ is
$$
I\cap J.
$$


::: pf-proof

One has
$$
\varphi(r)=(0+I,0+J)
$$
if and only if
$$
r\in I
\qquad\text{and}\qquad
r\in J.
$$
Thus
$$
\ker\varphi
=
I\cap J.
$$

:::

:::

::: {.pf-step #s1-3}

Because
$$
I+J=R,
$$
there exist
$$
i\in I,
\qquad
j\in J
$$
such that
$$
i+j=1.
$$


::: pf-proof

The equality
$$
I+J=R
$$
means in particular that
$$
1\in I+J.
$$
Hence
$$
1=i+j
$$
for suitable
$$
i\in I,
\qquad
j\in J.
$$

:::

:::

::: {.pf-step #s1-4}

The map $\varphi$ is surjective.


::: pf-proof

Let
$$
(a+I,b+J)
\in
R/I\oplus R/J
$$
be arbitrary. Choose $i,j$ as in step [](#s1-3){.pf-ref} and set
$$
r
\coloneqq
aj+bi.
$$

Modulo $I$,
$$
i\equiv0
\pmod I
$$
and
$$
j=1-i\equiv1\pmod I,
$$
so
$$
r
\equiv
a
\pmod I.
$$
Thus
$$
r+I=a+I.
$$

Similarly, modulo $J$,
$$
j\equiv0
\pmod J
$$
and
$$
i=1-j\equiv1\pmod J,
$$
so
$$
r+J=b+J.
$$
Therefore
$$
\varphi(r)
=
(a+I,b+J),
$$
and $\varphi$ is surjective.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
R/(I\cap J)
\cong
R/I\oplus R/J.
}
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref}, $\varphi$ is a surjective ring homomorphism with kernel
$$
I\cap J.
$$
The first isomorphism theorem gives
$$
R/\ker\varphi
\cong
R/I\oplus R/J.
$$
Substitute
$$
\ker\varphi=I\cap J.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the desired ring isomorphism.

:::

:::

:::
