---
schema: qual/card@1
id: PR-QZEJM
kind: proposition
title: Jordan's lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations:
- kind: variant-of
  target: T-ZO5UU
review: draft
---

::: {.proposition}
Let $a>0$ and $R>0$, let $C_R$ be the semicircle $t\mapsto Re^{it}$, $t\in[0,\pi]$, and let $g$ be continuous on $C_R$.
For $f(z)=e^{iaz}g(z)$,
$$
\abs{\int_{C_R}f(z)\dz}\le\frac{\pi M_R}{a},\qquad M_R\coloneqq\max_{t\in[0,\pi]}\abs{g(Re^{it})}.
$$
:::

::: {.proof}
For $z=Re^{it}$, $\abs{e^{iaz}}=e^{-aR\sin t}$ and $\abs{\dz}=R\dt$, so
$$
\abs{\int_{C_R}f(z)\dz}\le M_R\int_0^\pi e^{-aR\sin t}R\dt=2M_R\int_0^{\pi/2}e^{-aR\sin t}R\dt.
$$
On $[0,\pi/2]$ concavity of $\sin$ gives $\sin t\ge\frac{2t}{\pi}$, hence
$$
2M_R\int_0^{\pi/2}e^{-aR\sin t}R\dt\le2M_R\int_0^{\pi/2}e^{-2aRt/\pi}R\dt=\frac{\pi M_R}{a}\big(1-e^{-aR}\big)\le\frac{\pi M_R}{a}.
$$
:::
