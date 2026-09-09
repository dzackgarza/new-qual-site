---
schema: qual/card@1
id: E-DFUYC
kind: problem
title: Recognizing direct products
classification:
  areas:
  - algebra
  topics:
  - Direct Products
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Prove the "recognizing direct products" theorem.
Can the conditions be relaxed?
:::


::: {.solution}
The recognizing-direct-products theorem says that if $H,K\le G$ satisfy
\[
H\trianglelefteq G,
\qquad
K\trianglelefteq G,
\qquad
H\cap K=\{e\},
\qquad
HK=G,
\]
then $G\cong H\times K$.

<1>1. Every element of $H$ commutes with every element of $K$.
::: {.proof}
Let $h\in H$ and $k\in K$. Since $H$ is normal,
\[
kh^{-1}k^{-1}\in H,
\]
so
\[
[h,k]=hkh^{-1}k^{-1}\in H.
\]
Since $K$ is normal,
\[
hkh^{-1}\in K,
\]
so $[h,k]\in K$ as well. Hence
\[
[h,k]\in H\cap K=\{e\},
\]
and therefore $hk=kh$.
:::

<1>2. The multiplication map
\[
\mu:H\times K\longrightarrow G,
\qquad
\mu(h,k)=hk,
\]
is a homomorphism.
::: {.proof}
For $(h_1,k_1),(h_2,k_2)\in H\times K$, <1>1 gives $k_1h_2=h_2k_1$. Thus
\[
\mu(h_1,k_1)\mu(h_2,k_2)
=h_1k_1h_2k_2
=h_1h_2k_1k_2
=\mu(h_1h_2,k_1k_2).
\]
:::

<1>3. The map $\mu$ is surjective.
::: {.proof}
The hypothesis $HK=G$ says exactly that every $g\in G$ can be written $g=hk$ with $h\in H$ and $k\in K$.
:::

<1>4. The map $\mu$ is injective.
::: {.proof}
If $\mu(h,k)=e$, then $hk=e$, so
\[
h=k^{-1}.
\]
The left side lies in $H$ and the right side lies in $K$, hence
\[
h=k^{-1}\in H\cap K=\{e\}.
\]
Thus $h=k=e$, so $\ker\mu=\{(e,e)\}$.
:::

<1>5. Therefore $G\cong H\times K$.
::: {.proof}
By <1>2--<1>4, $\mu$ is a bijective homomorphism.
:::

<1>6. The normality hypotheses can be replaced by the weaker-looking condition that $H$ and $K$ commute elementwise.
::: {.proof}
Assume only
\[
HK=G,
\qquad
H\cap K=\{e\},
\qquad
[h,k]=e\quad\text{for all }h\in H,\ k\in K.
\]
Then the proofs of <1>2--<1>5 apply verbatim, so $G\cong H\times K$. Thus direct elementwise commutation is the condition actually needed to make the multiplication map a homomorphism; normality in the original theorem is a sufficient way to obtain it from the trivial-intersection hypothesis.
:::
:::
