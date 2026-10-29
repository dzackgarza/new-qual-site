---
schema: qual/card@1
id: P-KSRING17-026
kind: problem
title: The matrices $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ form a ring isomorphic to $\CC$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 26 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be the ring of all $2 \times 2$ matrices of the form $\left[ \begin{array} { r r } { a } & { b } \\ { - b } & { a } \end{array} \right]$ where a and b are real numbers.
Prove that R is isomorphic to C, the field of complex numbers.
:::

::: {.solution}

Define
$$
\Phi:\CC\to R
$$
by
$$
\boxed{
\Phi(a+bi)
\coloneqq
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}.
}
$$

::: pf

::: {.pf-step #s1-1}

The map $\Phi$ is well-defined and bijective.


::: pf-proof

Every complex number has a unique expression
$$
a+bi
$$
with
$$
a,b\in\RR,
$$
and every element of $R$ has a unique expression
$$
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}.
$$
Hence $\Phi$ is well-defined and has inverse
$$
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
\longmapsto
a+bi.
$$
Therefore $\Phi$ is bijective.

:::

:::

::: {.pf-step #s1-2}

The map $\Phi$ preserves addition.


::: pf-proof

Let
$$
z=a+bi,
\qquad
w=c+di.
$$
Then
$$
\begin{aligned}
\Phi(z+w)
&=
\Phi((a+c)+(b+d)i)\\
&=
\begin{pmatrix}
a+c&b+d\\
-(b+d)&a+c
\end{pmatrix}\\
&=
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
+
\begin{pmatrix}
c&d\\
-d&c
\end{pmatrix}\\
&=
\Phi(z)+\Phi(w).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The map $\Phi$ preserves multiplication.


::: pf-proof

For
$$
z=a+bi,
\qquad
w=c+di,
$$
one has
$$
zw
=
(ac-bd)
+
(ad+bc)i.
$$
Hence
$$
\Phi(zw)
=
\begin{pmatrix}
ac-bd&ad+bc\\
-(ad+bc)&ac-bd
\end{pmatrix}.
$$
On the other hand,
$$
\begin{aligned}
\Phi(z)\Phi(w)
&=
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
\begin{pmatrix}
c&d\\
-d&c
\end{pmatrix}\\
&=
\begin{pmatrix}
ac-bd&ad+bc\\
-(ad+bc)&ac-bd
\end{pmatrix}.
\end{aligned}
$$
Thus
$$
\Phi(zw)=\Phi(z)\Phi(w).
$$

:::

:::

::: {.pf-step #s1-4}

The map $\Phi$ preserves the multiplicative identity.


::: pf-proof

One has
$$
\Phi(1)
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
=
I_2.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
R\cong\CC
}
$$
as rings.


::: pf-proof

By step [](#s1-1){.pf-ref}, $\Phi$ is bijective. By steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref}, it is a unital ring homomorphism. Hence it is a ring isomorphism.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
