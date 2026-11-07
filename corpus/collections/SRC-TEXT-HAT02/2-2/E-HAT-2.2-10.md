---
schema: qual/card@1
id: E-HAT-2.2-10
kind: problem
title: Homology of $S^2$ with equatorial antipodal identification, and $S^3$ with equatorial $S^2$ antipodal identification
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 10; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete degree/cellular proof checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both cases: the quotient equator is $\RP^1$, the two hemispheres are 2-cells attached by
    degree-$\pm2$ maps, so $\mathrm{im}\,d_2=2\ZZ$ and $\ker d_2\cong\ZZ$; for $S^3$ the 2-skeleton
    is $\RP^2$ and both 3-cells attach as in $\RP^3$, where the coefficient is $1+(-1)^3=0$, so
    $H_3\cong\ZZ^2$ and $H_2=0$.
---

::: {.problem}
Let $X$ be the quotient space of $S^2$ under the identifications $x \sim -x$ for $x$ in the equator $S^1$.
Compute the homology groups $H_i(X)$.
Do the same for $S^3$ with antipodal points of the equatorial $S^2 \subset S^3$ identified.
:::

::: {.solution}
Write $X_n$ for the quotient of $S^n$ by the identification $x\sim -x$ for $x$ in the equatorial $S^{n-1}$. Both answers are computed from the reduced Mayer–Vietoris sequence (Hatcher p. 149, in its reduced form on p. 150), which is the exact sequence of a pair (Theorem 2.13, p. 114) together with excision (Theorem 2.20, p. 119), applied to the two open sets obtained from the two closed hemispheres by adjoining a collar of the equator from the other side.

::: pf

::: {.pf-step #s1}

For $n=2$,
$$
H_i(X_2)\cong
\begin{cases}
\ZZ,&i=0,2,\\
\ZZ_2,&i=1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

The image of the closed upper hemisphere under the quotient map is the quotient of $D^2$ by the identification of antipodal points of $\partial D^2$, which is $\RP^2$ by Example 0.4 (p. 6); the image of the closed lower hemisphere is another copy of $\RP^2$; a collar of the equator in either hemisphere also retracts onto its boundary circle, so the two open sets $U$, $V$ are homotopy equivalent to $\RP^2$ and their intersection $U\cap V$, the image of a collar of the equator, retracts onto the quotient circle $\RP^1\cong S^1$.
For $\RP^2$ the cell structure $e^0\cup e^1\cup e^2$ of Example 0.4 (p. 6) has $d_2$ of degree $2$ and $d_1=0$ (the $2$ cell is attached by the quotient projection $S^1\to\RP^1$, of degree $2$), so by Theorem 2.35 (p. 139)
$$
H_0(\RP^2)=\ZZ,\qquad H_1(\RP^2)=\ZZ_2,\qquad H_2(\RP^2)=0.
$$
The relevant part of the reduced Mayer–Vietoris sequence is
$$
0=\widetilde H_2(U)\oplus\widetilde H_2(V)\to\widetilde H_2(X_2)\xrightarrow{\partial}\widetilde H_1(U\cap V)=\ZZ\xrightarrow{\varphi}\widetilde H_1(U)\oplus\widetilde H_1(V)=\ZZ_2\oplus\ZZ_2\to\widetilde H_1(X_2)\to\widetilde H_0(U\cap V)=0 .
$$
The circle $U\cap V$ includes into each half as the circle $\RP^1$ inside $\RP^2$, whose class generates $\ZZ_2$, so $\varphi(1)=(1,1)$: it is injective, whence $\widetilde H_2(X_2)\cong\ZZ$ and $\widetilde H_1(X_2)\cong(\ZZ_2\oplus\ZZ_2)/\langle(1,1)\rangle\cong\ZZ_2$. Together with $H_0(X_2)=\ZZ$, since $X_2$ is connected, this gives the displayed groups.

:::

:::

::: {.pf-step #s2}

For $n=3$,
$$
H_i(X_3)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ_2,&i=2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Here the image of a closed hemisphere is $D^3$ with antipodal points of $\partial D^3=S^2$ identified, which is the cone on $\RP^2$ — the cone on $S^2$ with its base quotiented by the antipodal map — hence a contractible space, so the open sets $U$, $V$ have $\widetilde H_i(U)=\widetilde H_i(V)=0$ for all $i$. Their intersection is the image of a collar $S^2\times[-\varepsilon,\varepsilon]$ of the equator with $(x,0)\sim(-x,0)$, which retracts equivariantly onto the middle slice $\RP^2$; so $U\cap V\simeq\RP^2$, with $\widetilde H_1(\RP^2)=\ZZ_2$, $\widetilde H_2(\RP^2)=0$ and $\widetilde H_0(\RP^2)=0$ as in step [](#s1){.pf-ref}.
The reduced Mayer–Vietoris sequence then reads, for each $n$,
$$
0=\widetilde H_n(U)\oplus\widetilde H_n(V)\to\widetilde H_n(X_3)\to\widetilde H_{n-1}(U\cap V)\to\widetilde H_{n-1}(U)\oplus\widetilde H_{n-1}(V)=0,
$$
so $\widetilde H_n(X_3)\cong\widetilde H_{n-1}(\RP^2)$: $\widetilde H_1(X_3)=0$, $\widetilde H_2(X_3)=\ZZ_2$ and $\widetilde H_3(X_3)=\widetilde H_2(\RP^2)=0$. With $H_0(X_3)=\ZZ$ this gives the displayed groups.

:::

:::

:::

:::
