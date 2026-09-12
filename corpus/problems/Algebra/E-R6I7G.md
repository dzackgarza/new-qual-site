---
schema: qual/card@1
id: E-R6I7G
kind: problem
title: Recognition theorem for internal direct products
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
Let $H,K\le G$. Assume
\[
G=HK,
\qquad
H\cap K=\{e\},
\qquad
H\trianglelefteq G,
\qquad
K\trianglelefteq G.
\]
Prove that the multiplication map
\[
\Gamma:H\times K\longrightarrow G,
\qquad
\Gamma(h,k)=hk,
\]
is an isomorphism. Determine how the normality hypotheses can be weakened.
:::

::: {.solution}
<1>1. Every element of $H$ commutes with every element of $K$.
::: {.proof}
Let $h\in H$ and $k\in K$. Because $H\trianglelefteq G$,
\[
kh^{-1}k^{-1}\in H,
\]
so
\[
[h,k]=hkh^{-1}k^{-1}=h(kh^{-1}k^{-1})\in H.
\]
Because $K\trianglelefteq G$,
\[
hkh^{-1}\in K,
\]
so
\[
[h,k]=(hkh^{-1})k^{-1}\in K.
\]
Thus
\[
[h,k]\in H\cap K=\{e\},
\]
hence $[h,k]=e$ and therefore $hk=kh$.
:::

<1>2. The map $\Gamma$ is a homomorphism.
::: {.proof}
For $(h_1,k_1),(h_2,k_2)\in H\times K$, <1>1 gives $k_1h_2=h_2k_1$. Hence
\[
\begin{aligned}
\Gamma(h_1,k_1)\Gamma(h_2,k_2)
&=h_1k_1h_2k_2\\
&=h_1h_2k_1k_2\\
&=\Gamma(h_1h_2,k_1k_2).
\end{aligned}
\]
:::

<1>3. The map $\Gamma$ is surjective.
::: {.proof}
The hypothesis $G=HK$ says exactly that every $g\in G$ has the form $g=hk$ with $h\in H$, $k\in K$. Thus every $g$ lies in the image of $\Gamma$.
:::

<1>4. The map $\Gamma$ is injective.
::: {.proof}
Suppose
\[
\Gamma(h,k)=hk=e.
\]
Then
\[
h=k^{-1}.
\]
The left side belongs to $H$ and the right side belongs to $K$, so
\[
h=k^{-1}\in H\cap K=\{e\}.
\]
Hence $h=e$ and $k=e$, so the kernel is trivial. Since $\Gamma$ is a homomorphism, it is injective.
:::

<1>5. Therefore
\[
G\cong H\times K.
\]
::: {.proof}
By <1>2--<1>4, $\Gamma$ is a bijective homomorphism.
:::

<1>6. The normality assumptions can be weakened to the single condition
\[
[H,K]=1,
\]
i.e. every element of $H$ commutes with every element of $K$.
::: {.proof}
The proof of <1>2 uses only elementwise commutation, while <1>3 and <1>4 use only $G=HK$ and $H\cap K=\{e\}$. Thus the three conditions
\[
G=HK,
\qquad
H\cap K=\{e\},
\qquad
[H,K]=1
\]
already imply $G\cong H\times K$.

Conversely, if the multiplication map $H\times K\to G$ is a homomorphism, then
\[
(h,e)(e,k)=(h,k)=(e,k)(h,e)
\]
in $H\times K$, so their images satisfy $hk=kh$ in $G$. Hence elementwise commutation is exactly the condition needed in place of normality for this multiplication-map proof.
:::

<1>7. In the finite coprime-order case, trivial intersection is automatic.
::: {.proof}
If $H$ and $K$ are finite and $\gcd(|H|,|K|)=1$, then $|H\cap K|$ divides both $|H|$ and $|K|$ by Lagrange's theorem. Hence $|H\cap K|=1$, so $H\cap K=\{e\}$.
:::
:::
