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

::: problem
Compute the integer homology groups $H_*(\mathbb{RP}^2; \mathbb{Z})$ using the **Mayer–Vietoris sequence** by decomposing $\mathbb{RP}^2$ as the union of a Möbius strip $M$ and a 2-disk $D^2$ along their boundary circle $\partial M = S^1$.
:::

::: solution
Write
\[
\mathbb{RP}^2=M\cup_{S^1}D^2,
\]
where $M$ is a Möbius band and the attaching map identifies $\partial D^2$ with $\partial M$.
Use Mayer--Vietoris for this excisive CW decomposition (equivalently, replace $M$ and $D^2$ by open neighborhoods deformation retracting onto them whose intersection deformation retracts onto the common boundary circle).

<1>1. The relevant homology groups are
\[
H_1(S^1)\cong\mathbb Z,
\qquad
H_1(M)\cong\mathbb Z,
\qquad
H_1(D^2)=0,
\]
and $H_2$ of all three pieces is zero.

<1>2. Under a deformation retraction of $M$ onto its core circle, the boundary circle of the Möbius band winds twice around the core. Hence the inclusion
\[
i:S^1=\partial M\hookrightarrow M
\]
induces multiplication by $2$ on $H_1$. The inclusion into $D^2$ induces the zero map on $H_1$.

<1>3. The Mayer--Vietoris sequence in degrees $2$ and $1$ is therefore
\[
0\longrightarrow H_2(\mathbb{RP}^2)
\longrightarrow \mathbb Z
\xrightarrow{\,2\,}\mathbb Z
\longrightarrow H_1(\mathbb{RP}^2)
\longrightarrow \mathbb Z
\xrightarrow{(1,-1)}\mathbb Z\oplus\mathbb Z.
\]
<2>1. Multiplication by $2$ is injective, so exactness gives
\[
H_2(\mathbb{RP}^2)=0.
\]
<2>2. The map $(1,-1)$ is injective, so the preceding connecting map is zero. Hence
\[
H_1(\mathbb{RP}^2)
\cong\operatorname{coker}(\mathbb Z\xrightarrow{2}\mathbb Z)
\cong\mathbb Z/2.
\]

<1>4. Since $\mathbb{RP}^2$ is connected,
\[
H_0(\mathbb{RP}^2)\cong\mathbb Z,
\]
and all homology groups above degree $2$ vanish. Thus
\[
H_k(\mathbb{RP}^2;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&k=1,\\
0,&k\ge2.
\end{cases}
\]
:::
