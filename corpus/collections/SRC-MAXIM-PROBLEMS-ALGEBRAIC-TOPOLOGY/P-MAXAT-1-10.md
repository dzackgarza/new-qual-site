---
schema: qual/card@1
id: P-MAXAT-1-10
kind: problem
title: Torsion in $H^i(M)$ and $H^{n-i+1}(M)$ agree for a closed oriented $n$-manifold
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 10 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
If $M$ is a compact, closed, oriented manifold of dimension $n$, show that the torsion subgroups of $H^{i}(M)$ and $H^{n-i+1}(M)$ are isomorphic.
:::

::: {.solution}

All (co)homology groups below have integral coefficients. Write
$$
T(A)=\{a\in A: ma=0\text{ for some }m>0\}
$$
for the torsion subgroup of a finitely generated abelian group $A$.

::: pf

::: {.pf-step #s1-1}

The universal coefficient theorem gives a short exact sequence
$$
0\to\operatorname{Ext}^1(H_{i-1}(M),\ZZ)
\longrightarrow H^i(M)
\longrightarrow\operatorname{Hom}(H_i(M),\ZZ)
\to0.
$$


::: pf-proof

This is the universal coefficient theorem for cohomology applied to the singular chain complex of $M$.

:::

:::

::: {.pf-step #s1-2}

The group $\operatorname{Hom}(H_i(M),\ZZ)$ is torsion-free, and
$$
\operatorname{Ext}^1(H_{i-1}(M),\ZZ)
\cong T(H_{i-1}(M)).
$$


::: pf-proof

The manifold has finite CW type, so its homology groups are finitely generated. Write
$$
H_{i-1}(M)\cong\ZZ^r\oplus
\bigoplus_j\ZZ/d_j.
$$
Then
$$
\operatorname{Ext}^1(\ZZ,\ZZ)=0,
\qquad
\operatorname{Ext}^1(\ZZ/d_j,\ZZ)
\cong\ZZ/d_j,
$$
so the Ext group is isomorphic to the torsion summand. Also every subgroup of a free abelian group is torsion-free, and $\operatorname{Hom}$ of a finitely generated abelian group into $\ZZ$ is free abelian.

:::

:::

::: {.pf-step #s1-3}

Consequently,
$$
T(H^i(M))
\cong T(H_{i-1}(M)).
$$


::: pf-proof

In the exact sequence of step [](#s1-1){.pf-ref}, the left group is torsion by step [](#s1-2){.pf-ref} and the right group is torsion-free. Hence every torsion element of $H^i(M)$ lies in the image of the left injection, while every element of that image is torsion. Thus the injection identifies the left group with the full torsion subgroup of $H^i(M)$. Apply the second isomorphism of step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Poincaré duality gives
$$
H^{n-i+1}(M)\cong H_{i-1}(M).
$$


::: pf-proof

For a closed oriented $n$-manifold, cap product with the fundamental class is an isomorphism
$$
H^k(M;\ZZ)\xrightarrow{\ \cong\ }H_{n-k}(M;\ZZ).
$$
Set $k=n-i+1$. Then $n-k=i-1$.

:::

:::

::: {.pf-step #s1-5}

Taking torsion subgroups in step [](#s1-4){.pf-ref} gives
$$
T(H^{n-i+1}(M))
\cong T(H_{i-1}(M)).
$$


::: pf-proof

An isomorphism of abelian groups carries torsion elements exactly to torsion elements, so it restricts to an isomorphism of torsion subgroups.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
T(H^i(M))\cong T(H^{n-i+1}(M)).}
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref} identify both groups with $T(H_{i-1}(M))$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required torsion duality.

:::

:::

:::
