---
schema: qual/card@1
id: P-3JE4U
kind: problem
title: "Compute the following integrals. (i)"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
  - complex-logarithm
relations: []
review: draft
---

::: problem
Compute the following integrals. (i)
$\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$,
$0< a < n$ (ii)
$\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Compute (i) $\int_0^\infty \frac{x^{a-1}}{1 + x^n}\,dx$ for $0 < a < n$, and (ii) $\int_0^\infty \frac{\log x}{(1 + x^2)^2}\,dx$.

<1>1. For (i), use the keyhole contour or the sector contour of angle $2\pi/n$ around the pole $e^{i\pi/n}$.
    Proof: Integrate $f(z) = z^{a-1}/(1 + z^n)$ over the sector $\{0 \le \arg z \le 2\pi/n\}$ (with $z^{a-1}$ the branch $\abs{z}^{a-1}e^{i(a-1)\arg z}$): boundary rays are the positive real axis and the ray at angle $2\pi/n$; the only pole inside is $z_0 = e^{i\pi/n}$. Let $I = \int_0^\infty x^{a-1}/(1+x^n)\,dx$. On the second ray, $z = xe^{2\pi i/n}$, $z^{a-1} = x^{a-1} e^{2\pi i(a-1)/n}$, $dz = e^{2\pi i/n}dx$, so the integral there is $e^{2\pi i a/n} I$. The small circle around 0 and the large arc vanish ($a > 0$ handles the small circle; $a < n$ handles the large arc). Hence $I(1 - e^{2\pi i a/n}) = 2\pi i \Res_{z_0} f$.

<1>2. Compute the residue.
    Proof: $\Res_{z_0} \frac{z^{a-1}}{1+z^n} = \frac{z_0^{a-1}}{n z_0^{n-1}} = \frac{1}{n} z_0^{a-n} = \frac{1}{n} e^{i\pi(a-n)/n} = -\frac{1}{n} e^{i\pi a/n}$ since $e^{-i\pi} = -1$.

<1>3. Solve for $I$.
    Proof: From <1>1–<1>2: $I(1 - e^{2\pi i a/n}) = 2\pi i \cdot \qty(-\frac{1}{n} e^{i\pi a/n})$, so $I = \frac{-2\pi i}{n} \frac{e^{i\pi a/n}}{1 - e^{2\pi i a/n}} = \frac{2\pi i}{n} \frac{e^{i\pi a/n}}{e^{2\pi i a/n} - 1} = \frac{2\pi i}{n} \cdot \frac{1}{e^{i\pi a/n} - e^{-i\pi a/n}} = \frac{2\pi i}{n} \cdot \frac{1}{2i\sin(\pi a/n)} = \frac{\pi}{n \sin(\pi a/n)}$.

<1>4. For (ii), differentiate the $a$-family at the right point or integrate by parts: use $F(a) = \int_0^\infty \frac{x^{a-1}}{1 + x^2}\,dx = \frac{\pi}{\sin(\pi a/2)}$ (case $n = 2$ of (i), valid for $0 < a < 2$) and differentiate with respect to $a$ at $a = 1$... but the integrand is $\log x/(1+x^2)^2$, not $\log x \cdot x^{a-1}/(1+x^2)$. Instead, differentiate $G(a) = \int_0^\infty \frac{x^{a-1}}{1 + x^2}\,dx$: $G'(a) = \int_0^\infty \frac{\log x \, x^{a-1}}{1+x^2}\,dx$. We need $\int \frac{\log x}{(1+x^2)^2}$. Relate: $\dv{a} \int_0^\infty \frac{x^{a-1}}{(1+x^2)^2}\,dx = \int_0^\infty \frac{\log x \, x^{a-1}}{(1+x^2)^2}\,dx$; at $a = 1$ this is exactly the desired integral. So compute $H(a) = \int_0^\infty \frac{x^{a-1}}{(1+x^2)^2}\,dx$ by differentiating the standard $\int_0^\infty \frac{x^{a-1}}{1 + x^2}\,dx = \frac{\pi}{\sin(\pi a/2)}$ with respect to the exponent of the denominator: alternatively use $\frac{1}{(1+x^2)^2} = -\pdv{\beta}\frac{1}{\beta + x^2}\big|_{\beta = 1}$, or directly: $H(a) = \lim_{\beta \to 1} -\pdv{\beta} \int_0^\infty \frac{x^{a-1}}{\beta + x^2}\,dx$. Using $\int_0^\infty \frac{x^{a-1}}{\beta + x^2}\,dx = \beta^{a/2 - 1}\frac{\pi}{2\sin(\pi a/2)}$ (substitute $x = \sqrt\beta t$): $H(a) = -\pdv{\beta}\qty[\beta^{a/2 - 1}]\big|_{\beta=1} \frac{\pi}{2\sin(\pi a/2)} = \qty(1 - a/2)\frac{\pi}{2\sin(\pi a/2)}$. At $a = 1$: $H(1) = \frac{1}{2} \cdot \frac{\pi}{2\sin(\pi/2)} = \frac{\pi}{4}$.

<1>5. Then $\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx = H'(1)$.
    Proof: $H'(a) = \int_0^\infty \frac{\log x \, x^{a-1}}{(1+x^2)^2}\,dx$ by differentiation under the integral (justified by dominated convergence on $[\delta, R]$ plus uniform convergence of the derivative integrals away from $0$ and $\infty$). So evaluate $H'(1)$: with $H(a) = \frac{\pi}{2}\qty(1 - a/2)\csc(\pi a/2)$, $H'(a) = \frac{\pi}{2}\qty[-\frac12 \csc\qty(\frac{\pi a}{2}) + \qty(1 - \frac a2)\qty(-\frac{\pi}{2}\cot\qty(\frac{\pi a}{2})\csc\qty(\frac{\pi a}{2}))]$. At $a = 1$: $\csc(\pi/2) = 1$, $\cot(\pi/2) = 0$, so $H'(1) = \frac{\pi}{2} \cdot \qty(-\frac12) = -\frac{\pi}{4}$.

<1>6. Q.E.D.
    Proof: <1>3 gives (i): $\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx = \frac{\pi}{n\sin(\pi a/n)}$. <1>5 gives (ii): $\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx = -\frac{\pi}{4}$.

:::
