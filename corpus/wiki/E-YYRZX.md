---
schema: qual/card@1
id: E-YYRZX
kind: exercise
title: $e^{x/2} / 1+e^x,$ replication
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

:::{.exercise}
\[
I \da \int_\RR {e^{x\over 2}\over 1+e^x}\dx
.\]

:::

:::{.solution}
Replication: find $b$ such that $f(z) = f(z+ib)$ and use a rectangle.
\[
f(z+ib) 
= {e^{z\over 2}e^{ib\over 2} \over 1 + e^{ib}e^z} 
= e^{ib\over 2} {e^{z\over 2} \over 1 + e^{ib}e^z } = f(z) \impliedby e^{ib} = 1 \impliedby b=2\pi
,\]
in which case
\[
f(z + 2\pi i) = e^{ib\over 2}f(z) = e^{2\pi i \over 2}f(z) = -f(z)
.\]

So take the following rectangle where $H_-$ is at $2\pi i$ and $H_+$ is at 0, with sides at $\pm R$:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-21_21-25-04.png)

Write $\Gamma$ for the entire contour.
Note that integrating left-to-right on $H_-$ yields $-I$, since $w = z+2\pi i$ for $w\in H_-$ and $f(w) = -f(z)$.
Then reversing the orientation, going right-to-left yields $\int_{H_i} f = I$.

Claim: the integrals over the sides $V_{\pm}$ vanish. For the right,
\[
\abs{\int_{V_+} f(z) \dz} 
&\leq 2\pi \sup_{t\in [0, 2\pi]} \abs{e^{R + it\over 2} \over 1 + e^{R + it} } \\
&\leq 2\pi \sup_t {\abs{ e^{R\over 2} e^{it \over 2} }  \over \abs{e^{R}e^{it}} - 1} \\
&\leq 2\pi \sup_t {\abs{ e^{R\over 2} }  \over \abs{e^{R}} - 1} \\
&\in \bigo(e^{- {R\over 2} }) \to 0
.\]

For the left:
\[
\abs{\int_{V_-} f(z) \dz} 
&\leq \sup_{t\in [0, 2\pi] } \abs{ e^{-R-it\over 2} \over 1 + e^{-R- it}} \\
&\leq \sup_{t\in [0, 2\pi]}\abs{e^{-R\over 2} e^{-it\over 2}} \\
&\leq \sup_{t\in [0, 2\pi]}\abs{e^{-R\over 2}} \\
&\in \bigo(e^{- {R\over 2} }) \to 0
,\]
where we've thrown away positive terms in the denominator, which only makes this quantity larger.

Finding the poles within $\Gamma$: by inspection, there are poles when $e^z=-1$, so at $z=(2k+1)\pi i$ for $k\in \ZZ$.
Exactly one falls into this contour, $z_k = i\pi$.
By the residue theorem,
\[
2\pi i \Res_{z=i\pi} f(z) = \int_\Gamma f(z) \dz = \qty{\int_{H_-} + \int_{H_+}} f = 2I \implies I = \pi i \Res_{z=i\pi } f
.\]
Computing this residue:
\[
\pi i \Res_{z=i\pi }f(z) 
&= \pi i \lim_{z\to i\pi} { (z-i\pi) e^{z\over 2}\over e^z + 1} \\
&\eqLH \pi i \lim_{z\to i\pi} {e^{z\over 2} \over e^z} \\
&= \pi i  e^{-i\pi \over 2} \\
&= \pi
.\]

> DZG: This is much easier than trying to find the Laurent expansion about $z=i\pi$ -- trust me!

:::

