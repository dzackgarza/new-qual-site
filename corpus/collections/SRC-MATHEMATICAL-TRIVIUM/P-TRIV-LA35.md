---
schema: qual/card@1
id: P-TRIV-LA35
kind: problem
title: Change of basis for a matrix exponential
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 35, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A linear transformation is given by the matrix $e ^ { A }$ in some basis in $\RR ^ { n }$ . Consider the change of the basis determined by the transition matrix U. Find the matrix of the transformation in the new basis.
:::

::: {.solution}

Use the convention
$$
x_{\mathrm{old}}=U x_{\mathrm{new}},
$$
so the columns of $U$ are the new basis vectors written in the old basis.

::: pf

::: {.pf-step #s1-1}

If a linear transformation has matrix $T$ in the old basis, then its
matrix in the new basis is
$$
U^{-1}TU.
$$


::: pf-proof

If
$$
x_{\mathrm{old}}=Ux_{\mathrm{new}},
$$
then after applying the transformation,
$$
y_{\mathrm{old}}
=
T x_{\mathrm{old}}
=
TUx_{\mathrm{new}}.
$$
Converting the output back to new coordinates gives
$$
y_{\mathrm{new}}
=
U^{-1}y_{\mathrm{old}}
=
U^{-1}TUx_{\mathrm{new}}.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore the matrix of the given transformation in the new basis is
$$
\boxed{U^{-1}e^AU}.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} with
$$
T=e^A.
$$

:::

:::

::: {.pf-step #s1-3}

For every integer $k\geq0$,
$$
(U^{-1}AU)^k
=
U^{-1}A^kU.
$$


::: pf-proof

Proceed by induction. The cases $k=0$ and $k=1$ are immediate. If the identity
holds for $k$, then
$$
\begin{aligned}
(U^{-1}AU)^{k+1}
&=
(U^{-1}A^kU)(U^{-1}AU)\\
&=
U^{-1}A^{k+1}U.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
U^{-1}e^AU
=
e^{U^{-1}AU}.
$$


::: pf-proof

Using the exponential series and step [](#s1-3){.pf-ref},
$$
\begin{aligned}
e^{U^{-1}AU}
&=
\sum_{k=0}^{\infty}
\frac{(U^{-1}AU)^k}{k!}\\
&=
\sum_{k=0}^{\infty}
\frac{U^{-1}A^kU}{k!}\\
&=
U^{-1}
\left(
\sum_{k=0}^{\infty}\frac{A^k}{k!}
\right)U\\
&=
U^{-1}e^AU.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

Therefore the transformed matrix may be written as
$$
\boxed{
U^{-1}e^AU
=
e^{U^{-1}AU}.
}
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required change-of-basis formula.

:::

:::

:::
