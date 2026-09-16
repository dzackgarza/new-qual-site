---
title: The transform
order: 10
topics:
- Fourier Transform
- Fourier Analysis
---

# The transform

For $f\in L^1(\RR^n)$ let $\hat f(\xi)\coloneqq\int_{\RR^n}f(x)e^{-2\pi i x\cdot\xi}\dx$.
Then $\hat f$ is continuous, bounded by $\norm f_1$, and vanishes at infinity by the Riemann--Lebesgue lemma; two functions in $L^1$ with the same transform agree almost everywhere.
Fourier inversion recovers $f$ from $\hat f$ under the additional hypothesis $\hat f\in L^1$.

[[PR-47TTS]]

[[PR-IGMH4]]

[[FT-BZLK7]]

[[T-DTXIA]]

::: {.example}
The function $\hat f = \chi_{[-1,1]}$ is not the Fourier transform of any $f\in L^1(\RR)$, since it is not continuous.
For $f=\chi_{[-1,1]}\in L^1(\RR)$, $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi}$ is not in $L^1(\RR)$, so Fourier inversion does not apply to it.

:::

[[PR-DPRY7]]

[[PR-DY2B3]]

::: {.remark title="Operations under the transform"}
For $f, g\in L^1(\RR)$, $h\in\RR$, and $a\neq 0$, with the convention above:

| Operation on $f$ | Transform |
| --- | --- |
| $f(x-h)$ | $e^{-2\pi i h\xi}\hat f(\xi)$ |
| $e^{2\pi i hx}f(x)$ | $\hat f(\xi-h)$ |
| $f(ax)$ | $\abs a^{-1}\hat f(\xi/a)$ |
| $f'$, for $f$ absolutely continuous with $f'\in L^1$ | $2\pi i\xi\hat f(\xi)$ |
| $f*g$ | $\hat f(\xi)\hat g(\xi)$ |

The last row converts a convolution equation $f*g = k$ into the pointwise equation $\hat f\hat g = \hat k$.

:::

## Fourier coefficients

[[T-4BDE3]]

::: {.remark}
For an orthonormal set $\theset{u_n}$ in a Hilbert space, Bessel's inequality holds without further hypotheses.
Equality $\sum_n\abs{\inner{x}{u_n}}^2 = \norm x^2$ for every $x$ is Parseval's identity, which holds if and only if $\theset{u_n}$ is an orthonormal basis.

:::
