---
schema: qual/card@1
id: P-AMD-O7GYSQZO
kind: problem
title: The quotient $HK/(H\cap K)$ as a product of quotients
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Direct Products
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 4. The source
    assumes H and K are normal in HK and asks for the canonical isomorphism
    HK/(H cap K) to (HK/H) times (HK/K).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used the diagonal quotient homomorphism x -> (xH,xK). Its kernel is
    H cap K. Surjectivity follows because every coset in HK/H has a
    representative in K and every coset in HK/K has a representative in H.
---

::: {.problem}
Let $H,K\leq G$ and suppose
\[
H\normal HK,
\qquad
K\normal HK.
\]

Show that there is a canonical isomorphism
\[
\frac{HK}{H\cap K}
\cong
\frac{HK}{H}\times\frac{HK}{K}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Define
\[
\Phi:HK\longrightarrow (HK/H)\times(HK/K),
\qquad
\Phi(x)=(xH,xK).
\]
Then $\Phi$ is a homomorphism.

::: pf-proof

Because $H\normal HK$ and $K\normal HK$, both quotient groups are defined and their quotient maps
\[
q_H:HK\to HK/H,
\qquad
q_K:HK\to HK/K
\]
are homomorphisms.
The map $\Phi=(q_H,q_K)$ is therefore a homomorphism into the direct product.

:::

:::

::: {.pf-step #s2}

The kernel of $\Phi$ is $H\cap K$.

::: pf-proof

For $x\in HK$,
\[
\begin{aligned}
x\in\ker\Phi
&\iff xH=H\text{ and }xK=K\\
&\iff x\in H\text{ and }x\in K\\
&\iff x\in H\cap K.
\end{aligned}
\]
Hence
\[
\ker\Phi=H\cap K.
\]

:::

:::

::: {.pf-step #s3}

Every coset in $HK/H$ has a representative in $K$, and every coset in $HK/K$ has a representative in $H$.

::: pf-proof

Let $x\in HK$.
Write $x=hk$ with $h\in H$ and $k\in K$.
Since $H\normal HK$,
\[
xH=hkH=k(k^{-1}hk)H=kH.
\]
Thus every coset of $H$ in $HK$ is $kH$ for some $k\in K$.

Similarly, because $K\normal HK$,
\[
xK=hkK=hK,
\]
so every coset of $K$ in $HK$ is $hK$ for some $h\in H$.

:::

:::

::: {.pf-step #s4}

The homomorphism $\Phi$ is surjective.

::: pf-proof

Take an arbitrary element
\[
(uH,vK)\in(HK/H)\times(HK/K).
\]
By step [](#s3){.pf-ref}, choose $k\in K$ and $h\in H$ such that
\[
uH=kH,
\qquad
vK=hK.
\]
For $x=hk\in HK$, normality of $H$ gives
\[
xH=hkH=kH=uH,
\]
while $k\in K$ gives
\[
xK=hkK=hK=vK.
\]
Therefore
\[
\Phi(x)=(uH,vK),
\]
so $\Phi$ is surjective.

:::

:::

::: pf-step

The induced map
\[
\overline\Phi:HK/(H\cap K)
\longrightarrow
(HK/H)\times(HK/K),
\qquad
x(H\cap K)\longmapsto(xH,xK),
\]
is the required canonical isomorphism.

::: pf-proof

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s4){.pf-ref}, $\Phi$ is a surjective homomorphism with kernel $H\cap K$.
The first isomorphism theorem therefore induces an isomorphism
\[
HK/(H\cap K)\cong(HK/H)\times(HK/K).
\]
The displayed formula for $\overline\Phi$ is exactly the map induced by the two canonical quotient maps, so the isomorphism is canonical.

:::

:::

:::

:::
