---
schema: qual/card@1
id: P-KSRING17-027
kind: problem
title: A matrix model of $\mathbb Z[\sqrt p]$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 27 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let p be a prime and let R be the ring of all $2 \times 2$ matrices of the form $\left[ \begin{array} { c c } { a } & { b } \\ { p b } & { a } \end{array} \right]$ , where $a , b \in \mathbb { Z }$ . Prove that R is isomorphic to $\mathbb { Z } [ { \sqrt { p } } ]$
:::

Define
$$
\Phi:\ZZ[\sqrt p]\to R
$$
by
$$
\boxed{
\Phi(a+b\sqrt p)
\coloneqq
\begin{pmatrix}
a&b\\
pb&a
\end{pmatrix}.
}
$$

::: pf

::: pf-step

The map $\Phi$ is well-defined and bijective.


::: pf-proof

Every element of
$$
\ZZ[\sqrt p]
$$
has a unique expression
$$
a+b\sqrt p
$$
with
$$
a,b\in\ZZ,
$$
and every matrix in $R$ has a unique expression
$$
\begin{pmatrix}
a&b\\
pb&a
\end{pmatrix}.
$$
Hence $\Phi$ is well-defined and has inverse
$$
\begin{pmatrix}
a&b\\
pb&a
\end{pmatrix}
\longmapsto
a+b\sqrt p.
$$
Therefore $\Phi$ is bijective.

:::

:::

::: pf-step

The map $\Phi$ preserves addition.


::: pf-proof

For
$$
x=a+b\sqrt p,
\qquad
y=c+d\sqrt p,
$$
one has
$$
\begin{aligned}
\Phi(x+y)
&=
\begin{pmatrix}
a+c&b+d\\
p(b+d)&a+c
\end{pmatrix}\\
&=
\Phi(x)+\Phi(y).
\end{aligned}
$$

:::

:::

::: pf-step

The map $\Phi$ preserves multiplication.


::: pf-proof

In $\ZZ[\sqrt p]$,
$$
xy
=
(ac+pbd)
+
(ad+bc)\sqrt p.
$$
Therefore
$$
\Phi(xy)
=
\begin{pmatrix}
ac+pbd&ad+bc\\
p(ad+bc)&ac+pbd
\end{pmatrix}.
$$
On the other hand,
$$
\begin{aligned}
\Phi(x)\Phi(y)
&=
\begin{pmatrix}
a&b\\
pb&a
\end{pmatrix}
\begin{pmatrix}
c&d\\
pd&c
\end{pmatrix}\\
&=
\begin{pmatrix}
ac+pbd&ad+bc\\
p(ad+bc)&ac+pbd
\end{pmatrix}.
\end{aligned}
$$
Thus
$$
\Phi(xy)
=
\Phi(x)\Phi(y).
$$

:::

:::

::: pf-step

The map $\Phi$ preserves the identity.


::: pf-proof

One has
$$
\Phi(1)
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
R\cong\ZZ[\sqrt p]
}
$$
as rings.


::: pf-proof

Step <1>1 gives bijectivity, and steps <1>2--<1>4 show that $\Phi$ is a unital ring homomorphism. Hence it is a ring isomorphism.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
