---
title: The transform
order: 10
topics:
- Fourier Transform
- Fourier Analysis
---

# The transform

[[D-5LZQ4]]

[[PR-47TTS]]

[[PR-IGMH4]]

[[T-DTXIA]]

::: {.example}
The function $\chi_{[-1,1]}$ is not the Fourier transform of any $f\in L^1(\RR)$, since it is not continuous.
For $f=\chi_{[-1,1]}\in L^1(\RR)$, $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi}$ is not in $L^1(\RR)$, so Fourier inversion does not apply to it.

:::

[[PR-DPRY7]]

[[PR-DY2B3]]

::: {.remark}
The identity $\widehat{f*g}=\hat f\hat g$ converts a convolution equation $f*g = k$ into the pointwise equation $\hat f\hat g = \hat k$.

:::

## Fourier coefficients

[[T-4BDE3]]

::: {.remark}
For an orthonormal set $\theset{u_n}$ in a Hilbert space $H$, equality $\sum_n\abs{\inner{x}{u_n}}^2 = \norm x^2$ for every $x$ is Parseval's identity, which holds if and only if $\theset{u_n}$ is an orthonormal basis.

:::
