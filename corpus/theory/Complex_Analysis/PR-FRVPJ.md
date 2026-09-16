---
schema: qual/card@1
id: PR-FRVPJ
kind: proposition
title: Half-disc to upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
Let $D^+\coloneqq\theset{z\in\CC : \abs{z}<1,\ \Im z>0}$ be the upper half-disc.
Then
$$
\begin{aligned}
F\colon D^+ &\to \HH, \\
z & \mapsto -{1\over 2}\qty{z + z\inv}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]].
:::

::: {.proof}
For $z=re^{i\theta}$ with $0<r<1$ and $0<\theta<\pi$, $\Im F(z)=-\frac12\qty{r-r\inv}\sin\theta>0$, so $F(D^+)\subseteq\HH$.
For $c\in\HH$, the solutions of $F(z)=c$ are the roots of $z^2+2cz+1=0$, whose product is $1$.
A root on the unit circle would make $F(z)=-\Re z$ real, so neither root lies on the circle and exactly one root $z$ satisfies $\abs{z}<1$; then $\Im F(z)>0$ forces $\sin\theta>0$, so $z\in D^+$.
Hence $F\colon D^+\to\HH$ is a holomorphic bijection, and a bijective holomorphic map has a holomorphic inverse.
:::
