---
schema: qual/card@1
id: E-SS6.EX-11
kind: problem
title: "The Fourier transform of e^{az} e^{-e^z} is the Gamma function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a transcription defect in the exercise statement before solving.
---

::: {.exercise}
11. Let $f ( z ) = e ^ { a z } e ^ { - e ^ { z } }$ where $a > 0$ . Observe that in the strip $\{ x + i y : ~ | y | < \pi / 2 \}$ the function $f ( x + i y )$ is exponentially decreasing as $| x |$ tends to infinity.
    Prove that

$$
\hat {f} (\xi) = \Gamma (a - 2 \pi i \xi), \quad \text {   for   all   } \xi \in \mathbb {R}.
$$
:::

::: {.solution}
With the Fourier-transform convention used in this text,
\[
\widehat f(\xi)=\int_{-\infty}^{\infty}f(x)e^{-2\pi i x\xi}\,dx.
\]
For $f(x)=e^{ax}e^{-e^x}$ and $a>0$,
\[
\widehat f(\xi)
=\int_{-\infty}^{\infty}e^{(a-2\pi i\xi)x}e^{-e^x}\,dx.
\]
Set $t=e^x$. Then $dx=dt/t$ and $x$ runs from $-\infty$ to $\infty$ exactly as $t$ runs from $0$ to $\infty$. Therefore
\[
\widehat f(\xi)
=\int_0^\infty t^{a-2\pi i\xi-1}e^{-t}\,dt
=\Gamma(a-2\pi i\xi),
\]
since $\Re(a-2\pi i\xi)=a>0$.

The asserted decay of $f$ on every closed substrip $|y|\le \pi/2-\delta$ follows directly from
\[
|f(x+iy)|=e^{ax}e^{-e^x\cos y}.
\]
As $x\to-\infty$ this is $O(e^{ax})$. On $|y|\le\pi/2-\delta$ we have $\cos y\ge\sin\delta>0$, so as $x\to+\infty$ the factor $e^{-e^x\cos y}$ gives superexponential decay. Thus the stated strip decay holds.
:::
