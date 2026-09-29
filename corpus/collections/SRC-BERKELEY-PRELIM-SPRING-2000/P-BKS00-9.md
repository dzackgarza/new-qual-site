---
schema: qual/card@1
id: P-BKS00-9
kind: problem
title: Integral of $\cos^3z/z^3$ over the unit circle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Applied Cauchy's differentiation formula to h(z)=cos^3 z. The
    triple-angle identity gives h''(0)=-3, so the integral equals
    -3 pi i.
---

::: {.problem}
Evaluate
\[
\int_{|z|=1}\frac{\cos^3 z}{z^3}\,dz,
\]
where the unit circle is oriented counterclockwise.
:::

::: {.solution}
Set
$$
h(z)=\cos^3 z.
$$

::: pf

::: {.pf-step #s1}

The second derivative of $h$ at the origin is
$$
h''(0)=-3.
$$

::: pf-proof

The triple-angle identity gives
$$
\cos^3 z
=
\frac{3\cos z+\cos 3z}{4}.
$$
Differentiating twice,
$$
h''(z)
=
\frac{-3\cos z-9\cos 3z}{4}.
$$
Therefore
$$
h''(0)
=
\frac{-3-9}{4}
=
-3.
$$

:::

:::

::: {.pf-step #s2}

The integral is
$$
\boxed{-3\pi i}.
$$

::: pf-proof

The function $h$ is entire. Cauchy's differentiation formula on the
counterclockwise unit circle gives
$$
h''(0)
=
\frac{2!}{2\pi i}
\int_{\abs{z}=1}
\frac{h(z)}{z^3}\,dz.
$$
Hence, using step [](#s1){.pf-ref},
$$
\int_{\abs{z}=1}
\frac{\cos^3 z}{z^3}\,dz
=
\frac{2\pi i}{2}h''(0)
=
-3\pi i.
$$

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives the requested value.

:::

:::

:::
