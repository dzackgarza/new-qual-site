---
schema: qual/card@1
id: P-FY3WB
kind: problem
title: "Prove that for every $n\\in \\ZZ^{\\geq 0}$ the following polynomial has no roots\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
---
:::{.problem title="?"}
Prove that for every $n\in \ZZ^{\geq 0}$ the following polynomial has no roots in the open unit disc:
\[
f_n(z) \definedas \sum_{k=0}^n {z^k \over k!}
.\]

> Hint: check $n=1,2$ directly.

:::

:::{.solution title="Using Rouché"}
For the $n=1$ case, $f_1(z) = 0 \iff 1+z = 0 \iff z=-1$, so this has no roots in $\DD$.
For $n=2$, factor
\[
f_2(z) = 1 + z + z^2 = (z-\zeta_3^2)(z-\zeta_3^{-2})
,\]
using that
\[
\zeta_3^2\cdot \zeta_3^{-2} = 1,\qquad 
-(\zeta_3^2 + \zeta_3^{-2}) = -2\Re(\zeta_3^2) = -2\cos\qty{2\pi \over 3} = 1
.\]
Now use that $\abs{\zeta_3^{k}} = 1$, which is not in $\DD$.

For $n\geq 3$: toward applying Rouche's theorem, let $M(z) = 1 + z$ and $m(z) = {1\over 2}z^2 + \cdots + {1\over n!}z^n$.
Note that on $\abs{z} = 1$, $\abs{m(z)} = 2$, and 
\[
\abs{m(z)} 
&= \abs{\sum_{k\geq n+1} {z^k\over k!} } \\
&\leq \sum_{k\geq n+1} { \abs{z}^k \over k!} \\
&\leq \sum_{k\geq n+1} { 1 \over k!} \\
&= e^1 - \sum_{k\leq n} {1\over k!}
.\]
Suppose $n\geq 3$, 
\[
\abs{m(z)} < e - (1 + 1 + \cdots) \approx 0.718 < 2
,\]
then Rouché applies directly and 
\[
0 = \size Z_M(\DD) =\size Z_{M+m}(\DD) \da \size Z_f(\DD)
,\]
noting that $M(z) = 0 \iff z= -1$, which isn't contained in the open disc $\DD$.
:::

