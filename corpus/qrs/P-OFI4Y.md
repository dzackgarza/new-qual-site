---
schema: qual/card@1
id: P-OFI4Y
kind: problem
title: $\int_0^\infty\frac{dx}{1+x^n}=\frac{\pi}{n\sin(\pi/n)}$ by a wedge of angle $\frac{2\pi}{n}$
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Suppose $n \geq 2$.
Use a wedge of angle $\frac{2 \pi}{n}$ to evaluate the integral
\[
I=\int_{0}^{\infty} \frac{1}{1+x^{n}} d x
\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Use a wedge of angle $\frac{2\pi}{n}$ to evaluate $I = \int_0^\infty \frac{dx}{1 + x^n}$ for integer $n \geq 2$.

<1>1. The poles of $f(z) = \frac{1}{1 + z^n}$ are the $n$ simple poles $z_k = e^{i(1 + 2k)\pi/n}$, $k = 0, \ldots, n-1$.
Proof: $1 + z^n = 0$ iff $z^n = -1 = e^{i\pi}$, so $z_k = e^{i(\pi + 2\pi k)/n}$; each is simple since $\dv{z}(1 + z^n) = nz^{n-1} \neq 0$ at each root.

<1>2. Exactly one pole, $z_0 = e^{i\pi/n}$, lies inside the wedge $\theset{0 < \arg z < 2\pi/n}$.
Proof: The arguments of the poles from <1>1 are $\arg z_k = \frac{(1+2k)\pi}{n}$, which lie strictly between $0$ and $2\pi/n$ only for $k = 0$ ($\arg z_0 = \pi/n$); $k = 1$ gives $3\pi/n > 2\pi/n$ and $k = n-1$ gives a negative (or $> 2\pi$) argument modulo $2\pi$.

<1>3. Integrate $f$ over the wedge $\Gamma_R$: the segment $[0, R]$ on the real axis, the arc $\abs{z} = R$ with $0 \leq \arg z \leq 2\pi/n$, and the ray $\arg z = 2\pi/n$ back to $0$.
Proof: Standard contour setup; by the residue theorem, $\int_{\Gamma_R} f = 2\pi i\, \Res_{z = e^{i\pi/n}} f$ for $R > 1$ (using <1>2).

<1>4. $\Res_{z = e^{i\pi/n}} \frac{1}{1 + z^n} = -\frac{1}{n} e^{i\pi/n}$.
Proof: For a simple pole, $\Res_{z=\zeta} \frac{1}{1+z^n} = \frac{1}{n\zeta^{n-1}}$; with $\zeta = e^{i\pi/n}$, $\zeta^{n-1} = e^{i(n-1)\pi/n} = e^{i\pi} e^{-i\pi/n} = -e^{-i\pi/n}$, so the residue is $\frac{1}{n(-e^{-i\pi/n})} = -\frac{1}{n} e^{i\pi/n}$.

<1>5. The arc integral tends to $0$ as $R \to \infty$.
Proof: On the arc, $\abs{1 + z^n} \geq \abs{z}^n - 1 = R^n - 1$, so $\abs{f(z)} \leq \frac{1}{R^n - 1}$ and the arc contributes at most $\frac{2\pi R/n}{R^n - 1} \to 0$.

<1>6. The two ray integrals combine to $\qty(1 - e^{2\pi i/n}) \int_0^R \frac{dx}{1 + x^n}$.
Proof: On the real segment, $\int_0^R \frac{dx}{1+x^n}$.
On the second ray, $z = re^{2\pi i/n}$ with $r$ decreasing from $R$ to $0$: $z^n = r^n e^{2\pi i} = r^n$ and $dz = e^{2\pi i/n} dr$, so the integral is $-e^{2\pi i/n}\int_0^R \frac{dr}{1+r^n}$.

<1>7. Take $R \to \infty$ and solve for $I$.
Proof: By <1>3, <1>4, <1>5 and <1>6, $\qty(1 - e^{2\pi i/n}) I = 2\pi i\qty(-\frac{1}{n} e^{i\pi/n})$.
Since $1 - e^{2\pi i/n} = -2i e^{i\pi/n}\sin\frac{\pi}{n}$, we get $I = \frac{-2\pi i e^{i\pi/n}/n}{-2i e^{i\pi/n}\sin(\pi/n)} = \frac{\pi/n}{\sin(\pi/n)}$.

<1>8. Q.E.D. Proof: <1>7 gives $I = \int_0^\infty \frac{dx}{1+x^n} = \frac{\pi}{n \sin(\pi/n)}$.
:::
