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
\mathrm { T o r } ( H _ { n - 1 } ( M ; \mathbb { Z } ) = \left\{ \begin{array} { l l } { 0 , \mathrm { i f ~ M ~ i s ~ o r i e n t a b l e } } \\ { \mathbb { Z } _ { 2 } , \mathrm { i f ~ M ~ i s ~ n o n { - } o r i e n t a b l e } } \end{array} \right.
$$
:::

::: {.solution}
All homology and cohomology groups in the proof have integral coefficients.

<1>1. The universal coefficient theorem in degree $n$ gives
\[
0\to\operatorname{Ext}^1(H_{n-1}(M),\mathbb Z)
\longrightarrow H^n(M)
\longrightarrow\operatorname{Hom}(H_n(M),\mathbb Z)
\to0.
\]

::: {.proof}
This is the universal coefficient short exact sequence for cohomology applied in degree $n$.
:::

<1>2. Since $H_{n-1}(M)$ is finitely generated,
\[
\operatorname{Ext}^1(H_{n-1}(M),\mathbb Z)
\cong\operatorname{Tor}H_{n-1}(M).
\]

::: {.proof}
Write
\[
H_{n-1}(M)\cong\mathbb Z^r\oplus
\bigoplus_j\mathbb Z/d_j.
\]
Then $\operatorname{Ext}^1(\mathbb Z,\mathbb Z)=0$ and
\[
\operatorname{Ext}^1(\mathbb Z/d_j,\mathbb Z)
\cong\mathbb Z/d_j.
\]
Taking direct sums gives precisely the torsion subgroup.
:::

<1>3. If $M$ is orientable, then
\[
H_n(M)\cong\mathbb Z,
\qquad
H^n(M)\cong\mathbb Z.
\]

::: {.proof}
A closed connected orientable $n$-manifold has an integral fundamental class generating $H_n(M)$. Poincaré duality gives
\[
H^n(M)\cong H_0(M)\cong\mathbb Z.
\]
:::

<1>4. In the orientable case,
\[
\operatorname{Tor}H_{n-1}(M)=0.
\]

::: {.proof}
By step <1>3,
\[
\operatorname{Hom}(H_n(M),\mathbb Z)\cong\mathbb Z.
\]
The right map in step <1>1 is the evaluation map $H^n(M)\to\operatorname{Hom}(H_n(M),\mathbb Z)$; on the cohomological orientation class and fundamental class it takes value $1$, hence is an isomorphism $\mathbb Z\to\mathbb Z$. Its kernel, which is the Ext term by exactness, is therefore zero. Apply step <1>2.
:::

<1>5. If $M$ is nonorientable, then
\[
H_n(M)=0.
\]

::: {.proof}
For a closed connected manifold, a nonzero integral top-dimensional homology class supplies coherent local orientation generators and hence an orientation. Since $M$ is assumed nonorientable, no such class exists.
:::

<1>6. If $M$ is nonorientable, then
\[
H^n(M)\cong\mathbb Z/2.
\]

::: {.proof}
Poincaré duality with the orientation local system $\mathcal O$ gives
\[
H^n(M;\mathbb Z)\cong H_0(M;\mathcal O).
\]
For connected $M$, the latter is the group of coinvariants of the fiber $\mathbb Z$ under the orientation character
\[
\pi_1(M)\to\{\pm1\}.
\]
Nonorientability means some loop acts by $-1$. Thus the coinvariant relation identifies $a$ with $-a$, i.e. imposes $2a=0$, and no stronger relation occurs. Hence
\[
H_0(M;\mathcal O)\cong\mathbb Z/2.
\]
:::

<1>7. In the nonorientable case,
\[
\operatorname{Tor}H_{n-1}(M)\cong\mathbb Z/2.
\]

::: {.proof}
By step <1>5,
\[
\operatorname{Hom}(H_n(M),\mathbb Z)=0.
\]
Therefore step <1>1 identifies
\[
\operatorname{Ext}^1(H_{n-1}(M),\mathbb Z)
\cong H^n(M).
\]
Apply steps <1>2 and <1>6.
:::

<1>8. Therefore
\[
\boxed{
\operatorname{Tor}H_{n-1}(M;\mathbb Z)
\cong
\begin{cases}
0,&M\text{ orientable},\\
\mathbb Z/2,&M\text{ nonorientable}.
\end{cases}}
\]

::: {.proof}
The two cases are steps <1>4 and <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required dichotomy.
:::
:::
