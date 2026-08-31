---
schema: qual/card@1
id: P-MSHRB
kind: problem
title: Nonzero smooth compactly supported function with compactly supported Fourier transform
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Determine whether there is a nonzero smooth compactly supported function on $\mathbb{R}$ whose Fourier transform is also compactly supported?

::: {.solution}
<1>1. Suppose $f$ is a nonzero smooth compactly supported function with $\widehat f$ also compactly supported.
::: {.proof}
assume such a function exists.
:::

<1>2. Since $f$ is compactly supported, $\widehat f$ extends to an entire function (the Fourier transform of a compactly supported function is entire).
::: {.proof}
$\widehat f(\xi) = \int f(x) e^{-2\pi i x \xi}\,dx$ is entire in $\xi$ (the integral converges for all complex $\xi$ since $f$ has compact support).
:::

<1>3. Since $\widehat f$ is compactly supported (on $\mathbb{R}$) and entire, and it vanishes on an interval (outside its support), it vanishes identically.
::: {.proof}
an entire function that vanishes on a set with an accumulation point (e.g. an interval) is identically zero.
:::

<1>4. Hence $\widehat f \equiv 0$, so $f \equiv 0$ (by Fourier inversion).
::: {.proof}
<1>3 and the Fourier inversion theorem.
:::

<1>5. This contradicts $f$ being nonzero.
::: {.proof}
<1>4.
:::

<1>6. Hence no such nonzero function exists.
::: {.proof}
<1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
