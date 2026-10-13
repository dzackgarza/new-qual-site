---
schema: qual/card@1
id: P-WESCA09-I7
kind: problem
title: 'Contour integral around a diamond'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section I, item 7 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $D$ be the bounded region inside
\[
\{z\in\mathbb C:|\operatorname{Re}z|+|\operatorname{Im}z|=1\},
\]
and orient $\partial D$ positively.
Calculate
\[
\int_{\partial D}\frac{\cos z}{z(z^2+8)}\,dz.
\]
:::

::: {.solution}
<1>1. Among the poles of
\[
h(z)=\frac{\cos z}{z(z^2+8)},
\]
only $z=0$ lies in $D$.

::: {.proof}
The poles occur at
\[
z=0,
\qquad
z=\pm2\sqrt2\,i.
\]
The point $0$ lies in the interior of the diamond
$|\operatorname{Re}z|+|\operatorname{Im}z|<1$. For
$z=\pm2\sqrt2\,i$ one has
\[
|\operatorname{Re}z|+|\operatorname{Im}z|
=2\sqrt2>1,
\]
so these two poles lie outside $D$.
:::

<1>2. The residue of $h$ at $0$ is
\[
\operatorname{Res}(0,h)=\frac18.
\]

::: {.proof}
The pole at $0$ is simple, and therefore
\[
\operatorname{Res}(0,h)
=\lim_{z\to0}z\frac{\cos z}{z(z^2+8)}
=\frac{\cos0}{8}
=\frac18.
\]
:::

<1>3. The required integral is
\[
\boxed{\int_{\partial D}\frac{\cos z}{z(z^2+8)}\,dz
=\frac{\pi i}{4}}.
\]

::: {.proof}
The boundary is positively oriented, and by step <1>1 the only enclosed pole
is $0$. Hence the residue theorem and step <1>2 give
\[
\int_{\partial D}\frac{\cos z}{z(z^2+8)}\,dz
=2\pi i\operatorname{Res}(0,h)
=2\pi i\cdot\frac18
=\frac{\pi i}{4}.
\]
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value.
:::
:::
