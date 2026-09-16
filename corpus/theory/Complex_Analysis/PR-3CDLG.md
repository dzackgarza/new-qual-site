---
schema: qual/card@1
id: PR-3CDLG
kind: proposition
title: Upper half-plane to horizontal strip
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
---

::: {.proposition}
Let $S\coloneqq\theset{w\in\CC : 0<\Im w<\pi}=\RR\times i(0,\pi)$.
The [[D-4CSPM|principal branch]] $\Log$ of the logarithm restricts to a [[D-TM4TE|biholomorphism]]
$$
\begin{aligned}
F\colon \HH &\to S, \\
z &\mapsto \Log(z),
\end{aligned}
$$
with inverse $w\mapsto e^w$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_18-09-31.png)
:::

::: {.proof}
Every $z\in\HH$ is $z=re^{i\theta}$ with $r>0$ and $\theta\in(0,\pi)$, so $\Log(z)=\log r+i\theta\in S$ and $e^{\Log(z)}=z$.
Conversely, for $w=s+it\in S$, $e^w=e^se^{it}$ has argument $t\in(0,\pi)$, so $e^w\in\HH$ and $\Log(e^w)=s+it=w$.
Thus $F$ and $w\mapsto e^w$ are mutually inverse, and both are holomorphic.
:::
