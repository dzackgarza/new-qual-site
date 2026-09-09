---
schema: qual/card@1
id: P-LZDYV
kind: problem
title: van Kampen's theorem, and $\pi_1$ of glued tori, the Klein bottle, and wedges
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
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
(a) State the Seifert–van Kampen Theorem.
(b) Calculate the fundamental group of the space obtained by taking two copies of the torus $T = S^1 \times S^1$ and gluing them along a circle $S^1 \times \{p\}$.
(c) Calculate the fundamental group of the Klein bottle $K$.
(d) Calculate the fundamental group of the wedge sum $T^2 \vee S^1 = (S^1 \times S^1) \vee S^1$.
(e) Calculate the fundamental group of the wedge sum $T^2 \vee \mathbb{RP}^2$.
:::

::: solution
<1>1. **Seifert--van Kampen.** If $X=U\cup V$, where $U,V,U\cap V$ are path-connected open sets containing a common basepoint $x_0$, then
$$
\pi_1(X,x_0)
\cong
\pi_1(U,x_0)*_{\pi_1(U\cap V,x_0)}\pi_1(V,x_0),
$$
where the amalgamation uses the two inclusion-induced homomorphisms.

<1>2. For two tori glued along a circle representing one standard generator in each torus,
$$
\pi_1
\cong
\langle a,b_1,b_2\mid[a,b_1]=1,\ [a,b_2]=1\rangle.
$$
Since $a$ commutes with both free generators $b_1,b_2$, this is
$$
\mathbb Z\times F_2.
$$

<1>3. The Klein bottle has the standard presentation
$$
\pi_1(K)
\cong
\langle a,b\mid aba^{-1}=b^{-1}\rangle
\cong \mathbb Z\rtimes_{-1}\mathbb Z,
$$
where the generator represented by $a$ acts on $\langle b\rangle\cong\mathbb Z$ by inversion.

<1>4. For a wedge of connected CW complexes, van Kampen gives a free product. Hence
$$
\pi_1(T^2\vee S^1)
\cong
\mathbb Z^2*\mathbb Z
\cong
\langle a,b,c\mid[a,b]=1\rangle.
$$

<1>5. Likewise,
$$
\pi_1(T^2\vee\mathbb{RP}^2)
\cong
\mathbb Z^2*(\mathbb Z/2)
\cong
\langle a,b,d\mid[a,b]=1,\ d^2=1\rangle.
$$
:::
