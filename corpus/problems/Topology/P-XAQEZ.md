---
schema: qual/card@1
id: P-XAQEZ
kind: problem
title: Homology of $\RP^2$ via Mayer-Vietoris
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Compute the integer homology groups $H_*(\RP^2; \ZZ)$ using the **Mayer–Vietoris sequence** by decomposing $\RP^2$ as the union of a Möbius strip $M$ and a 2-disk $D^2$ along their boundary circle $\partial M = S^1$.
:::

::: {.solution}
Write $\RP^2=M\cup_{S^1}D^2$, where the attaching map identifies $\partial D^2$ with $\partial M$.
Thicken $M$ and $D^2$ to open sets $U \simeq M$ and $V \simeq D^2$ whose intersection deformation retracts onto the common boundary circle, so that the Mayer--Vietoris sequence applies to $U$ and $V$.
Homology is with $\ZZ$ coefficients.

::: pf

::: {.pf-step #pieces}
$H_1(S^1)\cong\ZZ$, $H_1(M)\cong\ZZ$, $H_1(D^2)=0$, and $H_2$ of all three spaces is zero.

::: pf-proof
$M$ deformation retracts onto its core circle and $D^2$ is contractible.
:::

:::

::: {.pf-step #maps}
The inclusion $\partial M\hookrightarrow M$ induces multiplication by $2$ on $H_1$, and the inclusion $\partial D^2 \hookrightarrow D^2$ induces the zero map on $H_1$.

::: pf-proof
Under the deformation retraction of $M$ onto its core circle, the boundary circle winds twice around the core.
The second map has target $H_1(D^2) = 0$.
:::

:::

::: {.pf-step #h2h1}
$H_2(\RP^2)=0$ and $H_1(\RP^2)\cong\ZZ/2$.

::: pf-proof
By steps [](#pieces){.pf-ref} and [](#maps){.pf-ref}, the Mayer--Vietoris sequence in degrees $2$, $1$, and $0$ reads
$$
0\longrightarrow H_2(\RP^2)
\longrightarrow \ZZ
\xrightarrow{\,2\,}\ZZ
\longrightarrow H_1(\RP^2)
\longrightarrow \ZZ
\xrightarrow{(1,-1)}\ZZ\oplus\ZZ.
$$
Multiplication by $2$ is injective, so $H_2(\RP^2)=0$.
The map $(1,-1)$ on $H_0$ is injective, so the connecting map $H_1(\RP^2) \to H_0(S^1)$ is zero and $H_1(\RP^2)\cong\operatorname{coker}(\ZZ\xrightarrow{2}\ZZ)\cong\ZZ/2$.
:::

:::

::: pf-step
$$
H_k(\RP^2;\ZZ)\cong
\boxed{\begin{cases}
\ZZ,&k=0,\\
\ZZ/2,&k=1,\\
0,&k\ge2.
\end{cases}}
$$

::: pf-proof
$H_0(\RP^2) \cong \ZZ$ because $\RP^2$ is path connected, step [](#h2h1){.pf-ref} gives $H_1$ and $H_2$, and $H_k = 0$ for $k \geq 3$ because the Mayer--Vietoris terms $H_k$ and $H_{k-1}$ of $S^1$, $M$, and $D^2$ vanish there.
:::

:::

:::

:::
