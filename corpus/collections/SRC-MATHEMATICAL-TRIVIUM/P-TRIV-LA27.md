---
schema: qual/card@1
id: P-TRIV-LA27
kind: problem
title: Orthogonal transformation sending $(1,\sqrt2,\sqrt3)$ to $(0,\sqrt2,2)$
classification:
  areas: [prelim]
  topics:
  - Orthogonal Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 27, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
For the vectors $A = \begin{bmatrix} 1 \\ \sqrt{2} \\ \sqrt{3} \end{bmatrix}$, $B = \begin{bmatrix} 0 \\ \sqrt{2} \\ 2 \end{bmatrix}$ find an orthogonal transformation that maps $A$ to $B$.
:::

::: {.solution}

Let
$$
a=
\begin{pmatrix}
1\\
\sqrt2\\
\sqrt3
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
0\\
\sqrt2\\
2
\end{pmatrix}.
$$

::: pf

::: pf-step

The two vectors have the same norm:
$$
\norm{a}^2=\norm{b}^2=6.
$$


::: pf-proof

Directly,
$$
\norm{a}^2=1+2+3=6,
$$
and
$$
\norm{b}^2=0+2+4=6.
$$

:::

:::

::: {.pf-step #s1-2}

Put
$$
u=a-b
=
\begin{pmatrix}
1\\
0\\
\sqrt3-2
\end{pmatrix}.
$$
Then the Householder matrix
$$
H
=
I
-
2\frac{uu^T}{u^Tu}
$$
is orthogonal.


::: pf-proof

Let
$$
P=\frac{uu^T}{u^Tu}.
$$
Then $P^T=P$ and $P^2=P$. Hence
$$
H^T=H
$$
and
$$
H^2=(I-2P)^2=I-4P+4P^2=I.
$$
Therefore
$$
H^TH=I.
$$

:::

:::

::: pf-step

The Householder transformation sends $a$ to $b$.


::: pf-proof

Because $\norm{a}=\norm{b}$,
$$
u^Ta
=(a-b)^Ta
=
\norm{a}^2-a^Tb,
$$
while
$$
u^Tu
=
\norm{a-b}^2
=
2(\norm{a}^2-a^Tb).
$$
Thus
$$
2\frac{u^Ta}{u^Tu}=1.
$$
Therefore
$$
Ha
=
a-2u\frac{u^Ta}{u^Tu}
=
a-u
=
b.
$$

:::

:::

::: {.pf-step #s1-4}

Here
$$
u^Tu
=
8-4\sqrt3
$$
and
$$
\frac{2}{u^Tu}
=
1+\frac{\sqrt3}{2}.
$$


::: pf-proof

One has
$$
u^Tu
=
1+(\sqrt3-2)^2
=
8-4\sqrt3.
$$
Rationalizing gives
$$
\frac2{8-4\sqrt3}
=
\frac1{4-2\sqrt3}
=
1+\frac{\sqrt3}{2}.
$$

:::

:::

::: pf-step

The matrix simplifies to
$$
\boxed{
H=
\begin{pmatrix}
-\frac{\sqrt3}{2}&0&\frac12\\
0&1&0\\
\frac12&0&\frac{\sqrt3}{2}
\end{pmatrix}.
}
$$


::: pf-proof

Substitute the vector $u$ and the scalar from step [](#s1-4){.pf-ref} into the Householder
formula in step [](#s1-2){.pf-ref}. The mixed coefficient uses
$$
\left(1+\frac{\sqrt3}{2}\right)(\sqrt3-2)=-\frac12,
$$
and the lower-right correction uses
$$
\left(1+\frac{\sqrt3}{2}\right)(\sqrt3-2)^2
=
1-\frac{\sqrt3}{2}.
$$

:::

:::

::: {.pf-step #s1-6}

Directly,
$$
Ha=b.
$$


::: pf-proof

Multiplication gives
$$
H
\begin{pmatrix}
1\\
\sqrt2\\
\sqrt3
\end{pmatrix}
=
\begin{pmatrix}
-\sqrt3/2+\sqrt3/2\\
\sqrt2\\
1/2+3/2
\end{pmatrix}
=
\begin{pmatrix}
0\\
\sqrt2\\
2
\end{pmatrix}.
$$

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-6){.pf-ref} show that the displayed matrix is orthogonal and maps
$A$ to $B$.

:::

:::

:::
