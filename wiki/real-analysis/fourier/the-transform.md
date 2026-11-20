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
The function $\chi_{[-1,1]}$ is not the Fourier transform of any $f\in L^1(\RR)$, since the Fourier transform of an $L^1$ function is continuous ([[PR-IGMH4|Riemann--Lebesgue]]).
For $f=\chi_{[-1,1]}\in L^1(\RR)$, $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi}$ is not in $L^1(\RR)$, its absolute value having divergent integral: $\int_k^{k+1}\frac{\abs{\sin 2\pi\xi}}{\xi}\dxi\geq\frac{2}{\pi(k+1)}$ for $k\geq1$, and $\sum_k\frac{1}{k+1}$ diverges. So [[T-DTXIA|Fourier inversion]] does not apply to it.

:::

[[PR-DPRY7]]

[[PR-DY2B3]]

::: {.remark}
The identity $\widehat{f*g}=\hat f\hat g$ of [[PR-DY2B3|the transforms of convolutions]] converts a convolution equation $f*g = k$ into the pointwise equation $\hat f\hat g = \hat k$.

:::

## Fourier coefficients

[[T-4BDE3]]

[[T-5AALA]]
