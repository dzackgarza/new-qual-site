---
schema: qual/card@1
id: P-JTON2
kind: problem
title: "Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show that $2^{n-1} \\sin\\frac{\\pi}{n} \\sin\\frac{2\\pi}{n} \\cdots \\sin\\frac{(n-1)\\pi}{n} = n \\;$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - trigonometry
  - polynomials
  - cauchy-riemann
relations: []
review: draft
solved: true
---

::: problem
Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show
that
$$2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n}
= n
\; .$$

> Hint: $1 - \cos 2 \theta = 2 \sin^2 \theta,\; \sin 2 \theta = 2 \sin \theta \cos \theta$.

(a) Show that in polar coordinates, the Cauchy-Riemann
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Using the $n$-th roots of unity, show $2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n} = n$.

<1>1. Factor $z^n - 1$ over $\CC$: $z^n - 1 = \prod_{k=0}^{n-1}\qty(z - \omega^k)$ with $\omega = e^{2\pi i/n}$.
    Proof: The $n$ distinct numbers $\omega^0, \ldots, \omega^{n-1}$ are precisely the roots of $z^n - 1$ (each satisfies $(\omega^k)^n = \omega^{kn} = 1$), and both sides are monic polynomials of degree $n$ with these roots.

<1>2. Divide by $z - 1$: $\frac{z^n - 1}{z - 1} = \prod_{k=1}^{n-1}\qty(z - \omega^k)$.
    Proof: In <1>1 the $k = 0$ factor is $z - 1$; since $\frac{z^n-1}{z-1}$ is a polynomial (sum of geometric series), cancellation of $z-1$ is valid as an identity of polynomials.

<1>3. Evaluate <1>2 at $z = 1$: $n = \prod_{k=1}^{n-1}\qty(1 - \omega^k)$.
    Proof: $\frac{z^n - 1}{z - 1}$ evaluated at $z = 1$ is $\lim_{z\to1}\frac{z^n-1}{z-1} = n$ (derivative of $z^n$ at $1$), or directly $1 + 1 + \cdots + 1 = n$.

<1>4. $\abs{1 - \omega^k} = 2\sin\frac{k\pi}{n}$ for $1 \leq k \leq n-1$.
    Proof: $1 - \omega^k = 1 - e^{2\pi i k/n} = e^{\pi i k/n}\qty(e^{-\pi i k/n} - e^{\pi i k/n}) = -2i e^{\pi i k/n}\sin\frac{k\pi}{n}$, whose modulus is $2\sin\frac{k\pi}{n}$ (positive since $0 < \frac{k\pi}{n} < \pi$).

<1>5. Take moduli in <1>3 and substitute <1>4.
    Proof: $n = \abs{n} = \prod_{k=1}^{n-1}\abs{1 - \omega^k} = \prod_{k=1}^{n-1} 2\sin\frac{k\pi}{n} = 2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}$, which is the desired identity.

<1>6. Q.E.D.
    Proof: <1>5 establishes the identity $2^{n-1}\sin\frac{\pi}{n}\cdots\sin\frac{(n-1)\pi}{n} = n$.

:::
