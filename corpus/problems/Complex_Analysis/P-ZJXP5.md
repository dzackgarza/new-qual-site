---
schema: qual/card@1
id: P-ZJXP5
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx=\frac{\pi}{n\sin(a\pi/n)}$ for $0<a<n$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Show that 
\[
\displaystyle \int_0^\infty \frac{x^{a-1}} {1+x^n} \dx=\frac{\pi}{n\sin \frac{a\pi}{n}}
.\]
using complex analysis, $0< a < n$. Here $n$ is a positive integer.
:::

::: {.solution}
<1>1. Choose the integrand and contour:
<2>1. Let $f(z) = \frac{z^{a-1}}{1 + z^n}$, where $z^{a-1} = \exp\bigl((a-1)\operatorname{Log}(z)\bigr)$ using the branch of the logarithm with argument $\arg(z) \in [0, 2\pi)$.
Proof: definition of power function.
<2>2. Let $\Gamma = \Gamma_1 + \Gamma_R - \Gamma_2 - \Gamma_\varepsilon$ be the closed wedge contour in the complex plane:
- $\Gamma_1$: the line segment along the positive real axis from $\varepsilon$ to $R$.
- $\Gamma_R$: the circular arc $z = R e^{i\theta}$ with $\theta \in [0, 2\pi/n]$.
- $\Gamma_2$: the ray $z = r e^{i 2\pi/n}$ with $r \in [\varepsilon, R]$.
- $\Gamma_\varepsilon$: the circular arc $z = \varepsilon e^{i\theta}$ with $\theta \in [0, 2\pi/n]$.
Proof: standard sector contour of angle $2\pi/n$.

<1>2. Locate the poles of $f(z)$ inside $\Gamma$ and calculate the residue:
<2>1. The poles of $f(z)$ occur where $1 + z^n = 0 \iff z^n = -1 = e^{i\pi}$.
Proof: roots of the denominator.
<2>2. The only pole strictly inside the sector $0 < \arg(z) < 2\pi/n$ is $z_0 = e^{i\pi/n}$.
Proof: $\arg(z_0) = \pi/n \in (0, 2\pi/n)$, while the next root has argument $3\pi/n > 2\pi/n$.
<2>3. $z_0$ is a simple pole, and its residue is:
\[
\operatorname{Res}(f, z_0) = \frac{z_0^{a-1}}{\left.\frac{d}{dz}(1+z^n)\right|_{z=z_0}} = \frac{z_0^{a-1}}{n z_0^{n-1}} = \frac{z_0^a}{n z_0^n} = \frac{e^{i a\pi/n}}{n (-1)} = -\frac{1}{n} e^{i a\pi/n}.
\]
Proof: residue at a simple pole for a quotient $g(z)/h(z)$ with $h'(z_0) \neq 0$.

<1>3. Evaluate the integrals along the boundary pieces:
<2>1. Along $\Gamma_1$:
\[
\int_{\Gamma_1} f(z)\,dz = \int_\varepsilon^R \frac{x^{a-1}}{1 + x^n}\,dx \xrightarrow[\substack{\varepsilon \to 0^+ \\ R \to \infty}]{} I = \int_0^\infty \frac{x^{a-1}}{1 + x^n}\,dx.
\]
Proof: definition of improper integral.
<2>2. Along $\Gamma_2$: substitute $z = r e^{i 2\pi/n}$ so $dz = e^{i 2\pi/n}\,dr$ and $z^n = r^n e^{i 2\pi} = r^n$:
\[
\int_{\Gamma_2} f(z)\,dz = \int_\varepsilon^R \frac{r^{a-1} e^{i(a-1)2\pi/n}}{1 + r^n} e^{i 2\pi/n}\,dr = e^{i 2\pi a/n} \int_\varepsilon^R \frac{r^{a-1}}{1 + r^n}\,dr \xrightarrow[\substack{\varepsilon \to 0^+ \\ R \to \infty}]{} e^{i 2\pi a/n} I.
\]
Proof: parametrization of $\Gamma_2$ and $e^{i(a-1)2\pi/n} e^{i 2\pi/n} = e^{i 2\pi a/n}$.
<2>3. Along the outer arc $\Gamma_R$: for $R > 1$, $|1 + z^n| \ge R^n - 1$, so:
\[
\left|\int_{\Gamma_R} f(z)\,dz\right| \le \frac{R^{a-1}}{R^n - 1} \cdot \frac{2\pi R}{n} = \frac{2\pi}{n} \frac{R^a}{R^n - 1} \xrightarrow[R \to \infty]{} 0 \quad (\text{since } a < n).
\]
Proof: ML estimate on arc of length $2\pi R / n$.
<2>4. Along the inner arc $\Gamma_\varepsilon$: for $\varepsilon < 1$, $|1 + z^n| \ge 1 - \varepsilon^n$, so:
\[
\left|\int_{\Gamma_\varepsilon} f(z)\,dz\right| \le \frac{\varepsilon^{a-1}}{1 - \varepsilon^n} \cdot \frac{2\pi \varepsilon}{n} = \frac{2\pi}{n} \frac{\varepsilon^a}{1 - \varepsilon^n} \xrightarrow[\varepsilon \to 0^+]{} 0 \quad (\text{since } a > 0).
\]
Proof: ML estimate on arc of length $2\pi \varepsilon / n$.

<1>4. Apply the Cauchy Residue Theorem and solve for $I$:
<2>1. By the Residue Theorem:
\[
\oint_\Gamma f(z)\,dz = 2\pi i \operatorname{Res}(f, z_0) = -\frac{2\pi i}{n} e^{i a\pi/n}.
\]
Proof: Cauchy Residue Theorem.
<2>2. Taking the limit as $\varepsilon \to 0^+$ and $R \to \infty$:
\[
(1 - e^{i 2\pi a/n}) I = -\frac{2\pi i}{n} e^{i a\pi/n}.
\]
Proof: <1>3 and <2>1.
<2>3. Solving for $I$:
\[
I = \frac{-2\pi i e^{i a\pi/n}}{n(1 - e^{i 2\pi a/n})} = \frac{2\pi i}{n(e^{i a\pi/n} - e^{-i a\pi/n})} = \frac{\pi}{n \left(\frac{e^{i a\pi/n} - e^{-i a\pi/n}}{2i}\right)} = \frac{\pi}{n \sin\left(\frac{a\pi}{n}\right)}.
\]
Proof: Euler's formula $\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$ with $\theta = a\pi/n$.

<1>5. Conclusion:
$\int_0^\infty \frac{x^{a-1}}{1 + x^n}\,dx = \frac{\pi}{n \sin(a\pi/n)}$. Q.E.D.
Proof: <1>4.
:::
