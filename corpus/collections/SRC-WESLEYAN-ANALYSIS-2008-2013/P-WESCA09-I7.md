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
$$
\{z\in\CC:\abs{\operatorname{Re}z}+\abs{\operatorname{Im}z}=1\},
$$
and orient $\partial D$ positively.
Calculate
$$
\int_{\partial D}\frac{\cos z}{z(z^2+8)}\,dz.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Among the poles of
$$
h(z)=\frac{\cos z}{z(z^2+8)},
$$
only $z=0$ lies in $D$.


::: pf-proof

The poles occur at
$$
z=0,
\qquad
z=\pm2\sqrt2\,i.
$$
The point $0$ lies in the interior of the diamond
$\abs{\operatorname{Re}z}+\abs{\operatorname{Im}z}<1$. For
$z=\pm2\sqrt2\,i$ one has
$$
\abs{\operatorname{Re}z}+\abs{\operatorname{Im}z}
=2\sqrt2>1,
$$
so these two poles lie outside $D$.

:::

:::

::: {.pf-step #s1-2}

The residue of $h$ at $0$ is
$$
\operatorname{Res}(0,h)=\frac18.
$$


::: pf-proof

The pole at $0$ is simple, and therefore
$$
\operatorname{Res}(0,h)
=\lim_{z\to0}z\frac{\cos z}{z(z^2+8)}
=\frac{\cos0}{8}
=\frac18.
$$

:::

:::

::: {.pf-step #s1-3}

The required integral is
$$
\boxed{\int_{\partial D}\frac{\cos z}{z(z^2+8)}\,dz
=\frac{\pi i}{4}}.
$$


::: pf-proof

The boundary is positively oriented, and by step [](#s1-1){.pf-ref} the only enclosed pole
is $0$. Hence the residue theorem and step [](#s1-2){.pf-ref} give
$$
\int_{\partial D}\frac{\cos z}{z(z^2+8)}\,dz
=2\pi i\operatorname{Res}(0,h)
=2\pi i\cdot\frac18
=\frac{\pi i}{4}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
