---
schema: qual/card@1
id: P-MAXAT-3-02
kind: problem
title: Integral cohomology of $\RP^\infty$, $\RP^{2n}$ and $\RP^{2n+1}$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 3, problem 2 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Calculate $H^{*}(\RP^{\infty}; \ZZ)$, $H^{*}(\RP^{2n}; \ZZ)$, $H^{*}(\RP^{2n+1}; \ZZ)$.
:::

::: {.solution}

Use the standard CW decomposition of $\RP^m$ with one cell in every dimension $0,1,\ldots,m$.

::: pf

::: {.pf-step #s1-1}

The integral cellular boundary map
$$
d_k:C_k\to C_{k-1}
$$
is multiplication by
$$
1+(-1)^k,
$$
so
$$
d_k=
\begin{cases}
0,&k\text{ odd},\\
2,&k\text{ even}.
\end{cases}
$$


::: pf-proof

The attaching map of the $k$-cell is the quotient map $S^{k-1}\to\RP^{k-1}$. Its incidence number with the unique $(k-1)$-cell is the sum of the contributions from the two hemispheres, which differ by the degree $(-1)^k$ of the antipodal map on $S^{k-1}$. Hence the coefficient is $1+(-1)^k$.

:::

:::

::: {.pf-step #s1-2}

The cellular cochain differential
$$
\delta^k:C^k\to C^{k+1}
$$
is therefore
$$
\delta^k=
\begin{cases}
2,&k\text{ odd},\\
0,&k\text{ even}.
\end{cases}
$$


::: pf-proof

Cellular cochains are $C^k=\operatorname{Hom}(C_k,\ZZ)\cong\ZZ$, and $\delta^k$ is dual to $d_{k+1}$. Apply step [](#s1-1){.pf-ref} to $k+1$.

:::

:::

::: {.pf-step #s1-3}

For $\RP^{\infty}$,
$$
\boxed{
H^k(\RP^{\infty};\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ/2,&k>0\text{ even},\\
0,&k\text{ odd}.
\end{cases}}
$$


::: pf-proof

The cochain complex is
$$
0\to\ZZ\xrightarrow{0}\ZZ
\xrightarrow{2}\ZZ\xrightarrow{0}\ZZ
\xrightarrow{2}\ZZ\xrightarrow{0}\cdots.
$$
At positive even degree, the outgoing map is zero and the incoming image is $2\ZZ$, giving $\ZZ/2$. At odd degree, multiplication by $2$ is injective, giving zero. Degree $0$ gives $\ZZ$.

:::

:::

::: {.pf-step #s1-4}

For $\RP^{2n}$,
$$
\boxed{
H^k(\RP^{2n};\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ/2,&k=2,4,\ldots,2n,\\
0,&\text{otherwise}.
\end{cases}}
$$


::: pf-proof

The cochain complex of step [](#s1-2){.pf-ref} truncates in degree $2n$. The calculation below the top is identical to step [](#s1-3){.pf-ref}. In top degree $2n$, there is no outgoing differential and the incoming differential is multiplication by $2$, so
$$
H^{2n}\cong\ZZ/2.
$$
This agrees with the fact that $\RP^{2n}$ is nonorientable but has top integral cohomology $\ZZ/2$.

:::

:::

::: {.pf-step #s1-5}

For $\RP^{2n+1}$,
$$
\boxed{
H^k(\RP^{2n+1};\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2n+1,\\
\ZZ/2,&k=2,4,\ldots,2n,\\
0,&\text{otherwise}.
\end{cases}}
$$


::: pf-proof

Again the calculation below the top is step [](#s1-3){.pf-ref}. In degree $2n+1$, the incoming differential $\delta^{2n}$ is zero and there is no outgoing differential, so the top cohomology is $\ZZ$. This is the integral orientation class of the orientable odd-dimensional real projective space.

:::

:::

::: {.pf-step #s1-6}

If the ring structure is also desired, let
$$
u\in H^2(\RP^{\infty};\ZZ)
$$
be the unique nonzero class. Then
$$
\boxed{H^*(\RP^{\infty};\ZZ)
\cong\ZZ[u]/(2u),\qquad \gradeddegree{u}=2.}
$$


::: pf-proof

The class $u$ is the Bockstein of the mod-$2$ generator $x\in H^1(\RP^{\infty};\FF_2)$. Naturality and the mod-$2$ ring $\FF_2[x]$ show that $u^j$ is the unique nonzero integral class in degree $2j$. Each such class has order $2$, giving the relation $2u=0$ and no further relation in the infinite case.

:::

:::

::: {.pf-step #s1-7}

For finite even-dimensional projective space,
$$
\boxed{H^*(\RP^{2n};\ZZ)
\cong\ZZ[u]/(2u,u^{n+1}),\qquad \gradeddegree{u}=2.}
$$


::: pf-proof

Restrict the class $u$ from $\RP^{\infty}$. Step [](#s1-4){.pf-ref} shows that $u^j$ supplies the unique nonzero class in degrees $2j$ for $1\leq j\leq n$, and dimension forces $u^{n+1}=0$.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} give the requested integral cohomology groups, and steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} record the corresponding standard ring presentations where no extra top odd-degree generator is needed.

:::

:::

:::
