---
schema: qual/card@1
id: P-BKS82-3
kind: problem
title: Cauchy-Schwarz inequality for the Hilbert-Schmidt trace pairing
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 3.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the entrywise trace identities and the application of Cauchy-Schwarz in $\CC^{n^2}$.
---

::: {.problem}
Let $A,B$ be complex $n\times n$ matrices. Prove that
\[
|\operatorname{tr}(AB^*)|^2
\le
\operatorname{tr}(AA^*)\operatorname{tr}(BB^*).
\]
:::

::: {.solution}
Write
$$
A=(a_{ij}),
\qquad
B=(b_{ij}).
$$

::: pf

::: {.pf-step #trace-pairing-formula}
The trace pairing is
$$
\operatorname{tr}(AB^*)
=
\sum_{i=1}^n\sum_{j=1}^n
a_{ij}\overline{b_{ij}}.
$$

::: pf-proof
Since
$$
(B^*)_{ji}=\overline{b_{ij}},
$$
the $i$th diagonal entry of $AB^*$ is
$$
(AB^*)_{ii}
=
\sum_{j=1}^n a_{ij}\overline{b_{ij}}.
$$
Summing the diagonal entries gives the displayed identity.
:::

:::

::: {.pf-step #trace-norm-formulas}
One has
$$
\operatorname{tr}(AA^*)
=
\sum_{i=1}^n\sum_{j=1}^n\abs{a_{ij}}^2
$$
and
$$
\operatorname{tr}(BB^*)
=
\sum_{i=1}^n\sum_{j=1}^n\abs{b_{ij}}^2.
$$

::: pf-proof
Apply step [](#trace-pairing-formula){.pf-ref} first with $B=A$ and then with $A=B$.
:::

:::

::: {.pf-step #inequality-boxed}
The required inequality holds:
$$
\boxed{
\abs{\operatorname{tr}(AB^*)}^2
\le
\operatorname{tr}(AA^*)\operatorname{tr}(BB^*)
}.
$$

::: pf-proof
By step [](#trace-pairing-formula){.pf-ref} and the Cauchy--Schwarz inequality in $\CC^{n^2}$,
$$
\begin{aligned}
\abs{\operatorname{tr}(AB^*)}^2
&=
\abs{
\sum_{i=1}^n\sum_{j=1}^n
a_{ij}\overline{b_{ij}}
}^2
\\
&\le
\left(
\sum_{i=1}^n\sum_{j=1}^n\abs{a_{ij}}^2
\right)
\left(
\sum_{i=1}^n\sum_{j=1}^n\abs{b_{ij}}^2
\right).
\end{aligned}
$$
Step [](#trace-norm-formulas){.pf-ref} identifies the two factors on the right with
$\operatorname{tr}(AA^*)$ and $\operatorname{tr}(BB^*)$.
:::

:::

::: pf-qed
Step [](#inequality-boxed){.pf-ref} is the stated inequality.
:::

:::
:::
