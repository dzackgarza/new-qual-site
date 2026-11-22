---
schema: qual/card@1
id: D-PV4RQ
kind: definition
title: Cauchy principal value of an integral over $\RR$
prompts:
- What is the Cauchy principal value of an integral with a simple pole on the real axis?
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Improper Integrals
  - Residues
relations: []
review: draft
---

::: {.definition}
Let $f$ be continuous on $\RR$ except at finitely many points $x_1<\cdots<x_m$, at each of which it has a [[D-AUD6K|simple pole]].
The \dfn{Cauchy principal value} of $\int_\RR f$ is
$$
\PV\int_{-\infty}^{\infty}f(x)\dx\coloneqq\lim_{R\to\infty}\lim_{\varepsilon\decreasesto0}\int_{I(R,\varepsilon)}f(x)\dx,
\qquad
I(R,\varepsilon)\coloneqq[-R,R]\setminus\bigcup_{j=1}^{m}\qty(x_j-\varepsilon,x_j+\varepsilon),
$$
when the limit exists.

This is the limit [@Ahl79, ch. 4, §5.3] forms by excising a small semicircle about each real pole; for $f(z)=R(z)e^{iz}$ with $R(\infty)=0$ the section evaluates it as $2\pi i\sum_{\Im z_0>0}\Res_{z=z_0}f+\pi i\sum_{\Im z_0=0}\Res_{z=z_0}f$.
:::
