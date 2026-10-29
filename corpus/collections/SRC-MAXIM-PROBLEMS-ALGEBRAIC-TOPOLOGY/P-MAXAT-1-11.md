---
schema: qual/card@1
id: P-MAXAT-1-11
kind: problem
title: Maxim algebraic topology 1.11
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 11 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Let M be a closed, connected, n-dimensional manifold.
Show that:

$$
\mathrm { T o r } ( H _ { n - 1 } ( M ; \ZZ ) = \left\{ \begin{array} { l l } { 0 , \mathrm { i f ~ M ~ i s ~ o r i e n t a b l e } } \\ { \ZZ _ { 2 } , \mathrm { i f ~ M ~ i s ~ n o n { - } o r i e n t a b l e } } \end{array} \right.
$$
:::

::: {.solution}

All homology and cohomology groups in the proof have integral coefficients.

::: pf

::: {.pf-step #s1-1}

The universal coefficient theorem in degree $n$ gives
$$
0\to\operatorname{Ext}^1(H_{n-1}(M),\ZZ)
\longrightarrow H^n(M)
\longrightarrow\operatorname{Hom}(H_n(M),\ZZ)
\to0.
$$


::: pf-proof

This is the universal coefficient short exact sequence for cohomology applied in degree $n$.

:::

:::

::: {.pf-step #s1-2}

Since $H_{n-1}(M)$ is finitely generated,
$$
\operatorname{Ext}^1(H_{n-1}(M),\ZZ)
\cong\operatorname{Tor}H_{n-1}(M).
$$


::: pf-proof

Write
$$
H_{n-1}(M)\cong\ZZ^r\oplus
\bigoplus_j\ZZ/d_j.
$$
Then $\operatorname{Ext}^1(\ZZ,\ZZ)=0$ and
$$
\operatorname{Ext}^1(\ZZ/d_j,\ZZ)
\cong\ZZ/d_j.
$$
Taking direct sums gives precisely the torsion subgroup.

:::

:::

::: {.pf-step #s1-3}

If $M$ is orientable, then
$$
H_n(M)\cong\ZZ,
\qquad
H^n(M)\cong\ZZ.
$$


::: pf-proof

A closed connected orientable $n$-manifold has an integral fundamental class generating $H_n(M)$. Poincaré duality gives
$$
H^n(M)\cong H_0(M)\cong\ZZ.
$$

:::

:::

::: {.pf-step #s1-4}

In the orientable case,
$$
\operatorname{Tor}H_{n-1}(M)=0.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\operatorname{Hom}(H_n(M),\ZZ)\cong\ZZ.
$$
The right map in step [](#s1-1){.pf-ref} is the evaluation map $H^n(M)\to\operatorname{Hom}(H_n(M),\ZZ)$; on the cohomological orientation class and fundamental class it takes value $1$, hence is an isomorphism $\ZZ\to\ZZ$. Its kernel, which is the Ext term by exactness, is therefore zero. Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

If $M$ is nonorientable, then
$$
H_n(M)=0.
$$


::: pf-proof

For a closed connected manifold, a nonzero integral top-dimensional homology class supplies coherent local orientation generators and hence an orientation. Since $M$ is assumed nonorientable, no such class exists.

:::

:::

::: {.pf-step #s1-6}

If $M$ is nonorientable, then
$$
H^n(M)\cong\ZZ/2.
$$


::: pf-proof

Poincaré duality with the orientation local system $\mathcal O$ gives
$$
H^n(M;\ZZ)\cong H_0(M;\mathcal O).
$$
For connected $M$, the latter is the group of coinvariants of the fiber $\ZZ$ under the orientation character
$$
\pi_1(M)\to\{\pm1\}.
$$
Nonorientability means some loop acts by $-1$. Thus the coinvariant relation identifies $a$ with $-a$, i.e. imposes $2a=0$, and no stronger relation occurs. Hence
$$
H_0(M;\mathcal O)\cong\ZZ/2.
$$

:::

:::

::: {.pf-step #s1-7}

In the nonorientable case,
$$
\operatorname{Tor}H_{n-1}(M)\cong\ZZ/2.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
\operatorname{Hom}(H_n(M),\ZZ)=0.
$$
Therefore step [](#s1-1){.pf-ref} identifies
$$
\operatorname{Ext}^1(H_{n-1}(M),\ZZ)
\cong H^n(M).
$$
Apply steps [](#s1-2){.pf-ref} and [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\operatorname{Tor}H_{n-1}(M;\ZZ)
\cong
\begin{cases}
0,&M\text{ orientable},\\
\ZZ/2,&M\text{ nonorientable}.
\end{cases}}
$$


::: pf-proof

The two cases are steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required dichotomy.

:::

:::

:::
