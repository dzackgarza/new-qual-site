---
schema: qual/card@1
id: P-BKF78-9
kind: problem
title: Orthogonality-preserving linear maps are scalar-unitary
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the deterministic MinerU Flash extraction. The extraction garbles the implication symbols; the surrounding text uniquely states that orthogonal vectors are sent to orthogonal vectors.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Images of the standard basis are pairwise orthogonal. Applying the
    hypothesis to e_i+e_j and e_i-e_j forces all image basis vectors to
    have the same norm r, so the inner product scales by r^2. If r=0
    then T=0; otherwise r^{-1}T is unitary.
---

::: {.problem}
For $x,y\in\mathbb C^n$, let
\[
\langle x,y\rangle=\sum_j x_j\overline{y_j}
\]
be the Hermitian inner product.
Let $T$ be a linear operator on $\mathbb C^n$ such that
\[
\langle x,y\rangle=0
\quad\Longrightarrow\quad
\langle Tx,Ty\rangle=0.
\]
Prove that $T=kS$ for some scalar $k$ and some unitary operator $S$, i.e.
\[
\langle Sx,Sy\rangle=\langle x,y\rangle
\]
for all $x,y$.
:::

::: {.solution}
Let $e_1,\ldots,e_n$ be the standard orthonormal basis of $\CC^n$, and set
$$
r=\norm{Te_1}.
$$

::: pf

::: {.pf-step #images-orthogonal}
If $i\neq j$, then $Te_i$ and $Te_j$ are orthogonal.

::: pf-proof
Since the standard basis is orthonormal,
$$
\langle e_i,e_j\rangle=0
$$
for $i\neq j$. The hypothesis on $T$ therefore gives
$$
\langle Te_i,Te_j\rangle=0.
$$
:::

:::

::: {.pf-step #images-equal-norm}
For every $i$,
$$
\norm{Te_i}=r.
$$

::: pf-proof
The assertion is immediate for $i=1$. If $i\neq1$, then
$$
\langle e_1+e_i,e_1-e_i\rangle=0.
$$
Hence the hypothesis gives
$$
0
=
\langle T(e_1+e_i),T(e_1-e_i)\rangle.
$$
Using linearity of $T$ and step [](#images-orthogonal){.pf-ref},
$$
\begin{aligned}
0
&=
\langle Te_1+Te_i,Te_1-Te_i\rangle\\
&=
\norm{Te_1}^2-\norm{Te_i}^2.
\end{aligned}
$$
Thus $\norm{Te_i}=\norm{Te_1}=r$.
:::

:::

::: {.pf-step #inner-product-scales}
For all $x,y\in\CC^n$,
$$
\langle Tx,Ty\rangle=r^2\langle x,y\rangle.
$$

::: pf-proof
Write
$$
x=\sum_{i=1}^n x_i e_i,
\qquad
y=\sum_{i=1}^n y_i e_i.
$$
By steps [](#images-orthogonal){.pf-ref} and [](#images-equal-norm){.pf-ref},
$$
\begin{aligned}
\langle Tx,Ty\rangle
&=
\sum_{i,j=1}^n
x_i\overline{y_j}\langle Te_i,Te_j\rangle\\
&=
r^2\sum_{i=1}^n x_i\overline{y_i}\\
&=
r^2\langle x,y\rangle.
\end{aligned}
$$
:::

:::

::: {.pf-step #r-zero-case}
If $r=0$, then $T=0$, so the conclusion holds with $k=0$ and
$S=I$.

::: pf-proof
By step [](#images-equal-norm){.pf-ref}, $r=0$ implies $Te_i=0$ for every basis vector $e_i$.
Thus $T=0$. The identity operator $I$ is unitary, and
$$
T=0=0\cdot I.
$$
:::

:::

::: {.pf-step #r-positive-case}
If $r>0$, then
$$
S=r^{-1}T
$$
is unitary and
$$
T=rS.
$$

::: pf-proof
By step [](#inner-product-scales){.pf-ref},
$$
\langle Sx,Sy\rangle
=
r^{-2}\langle Tx,Ty\rangle
=
\langle x,y\rangle
$$
for all $x,y\in\CC^n$. Thus $S$ is unitary in the sense stated in the
problem, and its definition gives $T=rS$.
:::

:::

::: pf-qed
Step [](#r-zero-case){.pf-ref} proves the assertion when $r=0$, and step [](#r-positive-case){.pf-ref} proves it when
$r>0$.
:::

:::
:::
