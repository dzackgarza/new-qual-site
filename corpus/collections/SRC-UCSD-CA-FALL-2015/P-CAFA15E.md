---
schema: qual/card@1
id: P-CAFA15E
kind: problem
title: "A bounded harmonic function on a punctured disk extends harmonically to the full disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
If $u$ is harmonic and bounded in $0 < \abs{z} < \rho$, then show that $u$ may be extended to a harmonic function on the whole disk $\abs{z} < \rho$.
:::

::: {.solution}
Fix $R$ with $0<R<\rho$. Let $h$ be the harmonic function on $\abs{z}<R$ whose boundary values on $\abs{z}=R$ equal those of $u$; for example, $h$ is given by the Poisson integral. Set
$$
w=u-h
$$
on $0<\abs{z}<R$. Then $w$ is harmonic there, bounded, and $w=0$ on $\abs{z}=R$.

Choose $M$ with $\abs{w}\le M$. For $0<\varepsilon<\abs{z}<R$, define
$$
\phi_\varepsilon(z)=\frac{\log(R/\abs{z})}{\log(R/\varepsilon)}.
$$
This is harmonic on the annulus $\varepsilon<\abs{z}<R$, equals $1$ on the inner circle and $0$ on the outer circle. By the maximum principle applied to $w\pm M\phi_\varepsilon$,
$$
\abs{w(z)}\le M\phi_\varepsilon(z).
$$
For fixed $z\ne0$, letting $\varepsilon\downarrow0$ gives $\phi_\varepsilon(z)\to0$, hence $w(z)=0$. Therefore $u=h$ on $0<\abs{z}<R$, so $u$ extends harmonically across $0$ by defining $u(0)=h(0)$.

Since $R<\rho$ was arbitrary, this gives a harmonic extension to the whole disk $\abs{z}<\rho$.
:::
