---
schema: qual/card@1
id: P-AGH4421CONDUCTOROFANORDER
kind: problem
title: Every order in an imaginary quadratic field has the form $\ZZ + f \cdot \OO$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.21 and cross-checked the lattice classification of
    quadratic orders against MIT 18.783, Theorem 12.27. The proof below also
    records uniqueness by identifying the conductor with the lattice index.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $\OO$ be the ring of integers in a quadratic number field $\QQ(\sqrt{-d})$.
Show that any subring $R \subseteq \OO$, $R \neq \ZZ$, is of the form $R=\ZZ+f \cdot \OO$, for a uniquely determined integer $f \geq 1$.
This integer $f$ is called the **conductor** of the ring $R$.
:::

::: {.solution}
Put
$$
K=\QQ(\sqrt{-d}).
$$
Since $[K:\QQ]=2$, the ring of integers has an integral basis
$$
\OO=\ZZ\oplus\ZZ\omega
$$
with $1,\omega$ a $\ZZ$-basis.

::: pf

::: {.pf-step #s1}

There is a unique integer $f\ge1$ such that
$$
\{b\in\ZZ:b\omega\in R\}=f\ZZ.
$$

::: pf-proof

Because $R$ is a subring with identity, $\ZZ\subseteq R$.  Since
$R\ne\ZZ$, choose
$$
\alpha=a+b\omega\in R\setminus\ZZ,
\qquad
a,b\in\ZZ.
$$
Then $b\ne0$, and
$$
b\omega=\alpha-a\in R.
$$
Thus
$$
I=\{b\in\ZZ:b\omega\in R\}
$$
is a nonzero additive subgroup of $\ZZ$.  Every nonzero subgroup of
$\ZZ$ has the form $f\ZZ$ for a unique positive integer $f$.

:::

:::

::: {.pf-step #s2}

For the integer $f$ of step [](#s1){.pf-ref},
$$
\boxed{R=\ZZ+f\OO.}
$$

::: pf-proof

Since
$$
\OO=\ZZ\oplus\ZZ\omega,
$$
we have
$$
\ZZ+f\OO
=
\ZZ+f(\ZZ\oplus\ZZ\omega)
=
\ZZ\oplus f\ZZ\omega.
$$
Step [](#s1){.pf-ref} gives $f\omega\in R$, while $\ZZ\subseteq R$.  Hence
$$
\ZZ\oplus f\ZZ\omega\subseteq R.
$$

Conversely, let
$$
\alpha=a+b\omega\in R.
$$
Since $a\in\ZZ\subseteq R$, we have
$$
b\omega=\alpha-a\in R.
$$
By the definition of $f$ in step [](#s1){.pf-ref}, this means $b\in f\ZZ$.  Therefore
$$
\alpha\in\ZZ\oplus f\ZZ\omega.
$$
Thus the reverse inclusion also holds.

:::

:::

::: {.pf-step #s3}

The integer $f$ is uniquely determined by $R$; indeed
$$
\boxed{f=[\OO:R].}
$$

::: pf-proof

With respect to the basis $1,\omega$ of $\OO$, step [](#s2){.pf-ref} gives the basis
$$
1,f\omega
$$
of $R$.  Therefore
$$
[\OO:R]
=
\left|
\det
\begin{pmatrix}
1&0\\
0&f
\end{pmatrix}
\right|
=f.
$$
The index depends only on $R$, so no other positive integer can give the
same subring.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove existence of the required representation, and step
[](#s3){.pf-ref} proves uniqueness of its conductor.

:::

:::

:::
