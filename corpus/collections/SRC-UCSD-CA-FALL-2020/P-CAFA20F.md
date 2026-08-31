---
schema: qual/card@1
id: P-CAFA20F
kind: problem
title: "Weierstrass product representation of z - sin z"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $f: \mathbb{C} \to \mathbb{C}$ be given by $f(z) = z - \sin z$.

(a) Show that $f$ is an odd entire function of order less than or equal to 1.

(b) Show that $f$ can be represented as a product $$f(z) = \frac{z^3}{6} \prod_{n=1}^{\infty}\left(1 - \frac{z^2}{a_n^2}\right)$$ where $\{a_n\}$ is a sequence of non-zero complex numbers with $\sum_{n=1}^{\infty} \frac{1}{|a_n|^2} < \infty$.
:::

::: {.solution}
<1>1. Part (a): $f$ is an odd entire function of order $\le 1$:
<2>1. The function $f(z) = z - \sin z$ is entire because $z$ and $\sin z = \frac{e^{iz} - e^{-iz}}{2i}$ are entire functions on $\mathbb{C}$.
::: {.proof}
linear combination of entire functions.
:::
<2>2. $f(-z) = -z - \sin(-z) = -z - (-\sin z) = -(z - \sin z) = -f(z)$, so $f$ is an odd function.
::: {.proof}
$\sin(-z) = -\sin z$.
:::
<2>3. For any $z = x + iy \in \mathbb{C}$:
\[
|f(z)| \le |z| + |\sin z| \le |z| + \frac{e^{|y|} + e^{-|y|}}{2} \le |z| + e^{|z|} \le C e^{|z|} \quad \text{for some constant } C > 0.
\]
Thus the growth order of $f$ is:
\[
\rho(f) = \limsup_{r \to \infty} \frac{\log \log M(r)}{\log r} \le 1.
\]
::: {.proof}
exponential bound on sine.
:::

<1>2. Part (b): Hadamard product representation:
<2>1. Near $z = 0$, using the Taylor series of $\sin z$:
\[
f(z) = z - \left( z - \frac{z^3}{6} + \frac{z^5}{120} - \cdots \right) = \frac{z^3}{6} - \frac{z^5}{120} + \cdots = z^3 \left( \frac{1}{6} - \frac{z^2}{120} + \cdots \right).
\]
Thus $f$ has a zero of order 3 at $z = 0$, with $\lim_{z \to 0} \frac{f(z)}{z^3} = \frac{1}{6}$.
::: {.proof}
Taylor expansion of $\sin z$.
:::
<2>2. Since $f$ is an odd function, its non-zero zeros occur in symmetric pairs $\pm a_n$ ($n \ge 1$), where $0 < |a_1| \le |a_2| \le \cdots \to \infty$.
Because $\rho(f) \le 1$, the exponent of convergence of the zeros is at most 1, so:
\[
\sum_{n=1}^\infty \frac{1}{|a_n|^2} < \infty.
\]
::: {.proof}
Hadamard Factorization Theorem.
:::
<2>3. By the Hadamard Factorization Theorem for an entire function of order $\le 1$, paired symmetric factors yield:
\[
E_1\left(\frac{z}{a_n}\right) E_1\left(-\frac{z}{a_n}\right) = \left(1 - \frac{z}{a_n}\right) e^{z/a_n} \left(1 + \frac{z}{a_n}\right) e^{-z/a_n} = 1 - \frac{z^2}{a_n^2}.
\]
Therefore the product simplifies without individual exponential convergence factors:
\[
f(z) = z^3 e^{Az + B} \prod_{n=1}^\infty \left( 1 - \frac{z^2}{a_n^2} \right).
\]
::: {.proof}
cancellation of exponential factors in symmetric root pairs.
:::
<2>4. Since $f(-z) = -f(z)$ and $1 - \frac{(-z)^2}{a_n^2} = 1 - \frac{z^2}{a_n^2}$:
\[
-z^3 e^{-Az + B} \prod_{n=1}^\infty \left(1 - \frac{z^2}{a_n^2}\right) = -z^3 e^{Az + B} \prod_{n=1}^\infty \left(1 - \frac{z^2}{a_n^2}\right) \implies e^{-2Az} = 1 \implies A = 0.
\]
::: {.proof}
oddness constraint.
:::
<2>5. Thus $e^{Az+B} = e^B$ is a constant $C$.
Evaluating the limit as $z \to 0$:
\[
C = e^B = \lim_{z \to 0} \frac{f(z)}{z^3} = \frac{1}{6}.
\]
Therefore:
\[
f(z) = \frac{z^3}{6} \prod_{n=1}^\infty \left( 1 - \frac{z^2}{a_n^2} \right).
\]
::: {.proof}
matching leading Taylor coefficient.
:::

<1>3. Conclusion:
$f(z) = z - \sin z$ is an odd entire function of order $\le 1$, and its Weierstrass/Hadamard product is $\frac{z^3}{6} \prod_{n=1}^\infty (1 - z^2/a_n^2)$ with $\sum |a_n|^{-2} < \infty$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
