---
title: The transform
order: 10
topics:
- Fourier Transform
- Fourier Analysis
---

# The transform

For \(f\in L^1\), the Fourier transform is a continuous function vanishing at infinity; Riemann--Lebesgue supplies the vanishing, while injectivity says that two \(L^1\) functions with the same transform agree almost everywhere.
Fourier inversion is the recovery theorem, but its hypotheses must still be checked: \(f\in L^1\) alone does not license pointwise inversion everywhere.

[[PR-47TTS]]

[[PR-IGMH4]]

[[FT-BZLK7]]

[[T-DTXIA]]

[[PR-DPRY7]]

[[PR-DY2B3]]

::: {.remark title="The dictionary"}
The transform turns each operation into an easier one, and the exam uses the table rather than the definition:

| On $f$ | On $\hat f$ |
| --- | --- |
| translation | modulation |
| dilation by $a$ | dilation by $1/a$, times $\abs a\inv$ |
| differentiation | multiplication by $\xi$ |
| convolution | multiplication |

The last row is why convolution is the natural operation: the transform turns it into pointwise multiplication, so a convolution equation becomes an algebra problem.

Riemann--Lebesgue says $\hat f$ vanishes at infinity for $f \in L^1$, which is the standard way to show a given function is *not* a transform.
:::

## Fourier coefficients

For an orthonormal system, Bessel's inequality gives the safe estimate
\[
\sum_n |\langle f,e_n\rangle|^2\le \|f\|_2^2.
\]
Equality is the stronger Parseval statement and requires completeness of the orthonormal system.
Use Bessel before completeness has been established; use Parseval once the system is known to be an orthonormal basis.

[[T-4BDE3]]

[[T-4CDKK]]

[[FF-54Z44]]
