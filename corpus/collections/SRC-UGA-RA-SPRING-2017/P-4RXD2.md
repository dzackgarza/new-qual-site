---
schema: qual/card@1
id: P-4RXD2
kind: problem
title: '$f_n(x)=ae^{-nax}-be^{-nbx}$ with $0<a<b$: $\sum|f_n|\notin L^1([0,\infty))$
  while $\sum f_n\in L^1$ with integral $\ln(b/a)$'
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - L¹
  - Convergence of Integrals
relations: []
review: draft
---

::: problem
Let $0 < a < b$, and define the sequence of functions on $[0, \infty)$ by
$$
f_n(x) = a e^{-n a x} - b e^{-n b x} \quad (n \ge 1).
$$

(a) Show that $\sum_{n=1}^\infty |f_n| \notin L^1([0, \infty))$.

(b) Show that $\sum_{n=1}^\infty f_n \in L^1([0, \infty))$ and
$$
\int_0^\infty \sum_{n=1}^\infty f_n(x) \, dx = \ln\left(\frac{b}{a}\right).
$$
:::

::: solution
**Goal:** Prove divergence of the integrated absolute sum via Tonelli's Theorem in (a), and compute the closed form of the geometric series and its improper integral in (b).

<1>1. Part (a): Integration of single terms and root location.
    *Proof:*
    <2>1. For each $n \ge 1$, compute the integral of $f_n$ over $[0, \infty)$:
    $$\int_0^\infty f_n(x) \, dx = \left[ -\frac{1}{n} e^{-n a x} + \frac{1}{n} e^{-n b x} \right]_0^\infty = \frac{1}{n} - \frac{1}{n} = 0.$$
    <2>2. Find the unique root $x_n \in (0, \infty)$ of $f_n(x) = 0$:
    $$a e^{-n a x_n} = b e^{-n b x_n} \iff e^{n(b - a) x_n} = \frac{b}{a} \iff x_n = \frac{\ln(b/a)}{n(b - a)} > 0.$$
    <2>3. Sign of $f_n(x)$:
        - For $x \in [0, x_n)$, $f_n(x) < 0$.
        - For $x \in (x_n, \infty)$, $f_n(x) > 0$.
    <2>4. Since $\int_0^\infty f_n(x) \, dx = 0$, we have $-\int_0^{x_n} f_n(x) \, dx = \int_{x_n}^\infty f_n(x) \, dx$.
    <2>5. Compute the $L^1$ norm of $f_n$:
    $$\int_0^\infty |f_n(x)| \, dx = 2 \int_{x_n}^\infty f_n(x) \, dx = 2 \left[ -\frac{1}{n} e^{-n a x} + \frac{1}{n} e^{-n b x} \right]_{x_n}^\infty = \frac{2}{n} \left( e^{-n a x_n} - e^{-n b x_n} \right).$$
    <2>6. Note that $n x_n = \frac{\ln(b/a)}{b - a} =: c$ is independent of $n$.
    <2>7. Thus $C = e^{-a c} - e^{-b c} > 0$ (since $b > a \implies a c < b c \implies e^{-a c} > e^{-b c}$) is a strictly positive constant independent of $n$.
    <2>8. Therefore:
    $$\int_0^\infty |f_n(x)| \, dx = \frac{2 C}{n}.$$

<1>2. Part (a): Divergence of the integral of $\sum |f_n|$.
    *Proof:*
    <2>1. By Tonelli's Theorem for non-negative measurable functions:
    $$\int_0^\infty \sum_{n=1}^\infty |f_n(x)| \, dx = \sum_{n=1}^\infty \int_0^\infty |f_n(x)| \, dx = \sum_{n=1}^\infty \frac{2 C}{n} = 2 C \sum_{n=1}^\infty \frac{1}{n} = \infty.$$
    <2>2. Therefore $\sum_{n=1}^\infty |f_n| \notin L^1([0, \infty))$.

<1>3. Part (b): Pointwise sum of the geometric series.
    *Proof:*
    <2>1. For each fixed $x > 0$, $0 < e^{-a x} < 1$ and $0 < e^{-b x} < 1$.
    <2>2. Summing the two geometric series:
    $$S(x) = \sum_{n=1}^\infty f_n(x) = a \sum_{n=1}^\infty (e^{-a x})^n - b \sum_{n=1}^\infty (e^{-b x})^n = \frac{a e^{-a x}}{1 - e^{-a x}} - \frac{b e^{-b x}}{1 - e^{-b x}} = \frac{a}{e^{a x} - 1} - \frac{b}{e^{b x} - 1}.$$

<1>4. Part (b): Integrability of $S(x)$ on $[0, \infty)$.
    *Proof:*
    <2>1. Near $x = 0$, expand $e^{u} - 1 = u + \frac{u^2}{2} + O(u^3)$:
    $$\frac{a}{e^{a x} - 1} = \frac{1}{x} - \frac{a}{2} + O(x), \quad \frac{b}{e^{b x} - 1} = \frac{1}{x} - \frac{b}{2} + O(x).$$
    <2>2. Subtracting gives:
    $$\lim_{x \to 0^+} S(x) = \lim_{x \to 0^+} \left[ \left(\frac{1}{x} - \frac{a}{2}\right) - \left(\frac{1}{x} - \frac{b}{2}\right) + O(x) \right] = \frac{b - a}{2} > 0.$$
    <2>3. Since $S(x)$ is continuous on $(0, \infty)$ and extends continuously to $x = 0$, $S$ is bounded on $(0, 1]$, so $\int_0^1 |S(x)| \, dx < \infty$.
    <2>4. As $x \to \infty$, $S(x) \sim a e^{-a x}$, which decays exponentially, so $\int_1^\infty |S(x)| \, dx < \infty$.
    <2>5. Thus $S \in L^1([0, \infty))$.

<1>5. Part (b): Exact computation of $\int_0^\infty S(x) \, dx$.
    *Proof:*
    <2>1. Observe the antiderivative:
    $$\frac{d}{dx} \ln\left( \frac{1 - e^{-a x}}{1 - e^{-b x}} \right) = \frac{a e^{-a x}}{1 - e^{-a x}} - \frac{b e^{-b x}}{1 - e^{-b x}} = S(x).$$
    <2>2. For $0 < \varepsilon < R < \infty$:
    $$\int_\varepsilon^R S(x) \, dx = \left[ \ln\left( \frac{1 - e^{-a x}}{1 - e^{-b x}} \right) \right]_\varepsilon^R = \ln\left( \frac{1 - e^{-a R}}{1 - e^{-b R}} \right) - \ln\left( \frac{1 - e^{-a \varepsilon}}{1 - e^{-b \varepsilon}} \right).$$
    <2>3. Upper limit as $R \to \infty$:
    $$\lim_{R \to \infty} \frac{1 - e^{-a R}}{1 - e^{-b R}} = \frac{1 - 0}{1 - 0} = 1 \implies \lim_{R \to \infty} \ln\left( \frac{1 - e^{-a R}}{1 - e^{-b R}} \right) = \ln(1) = 0.$$
    <2>4. Lower limit as $\varepsilon \to 0^+$:
    $$\lim_{\varepsilon \to 0^+} \frac{1 - e^{-a \varepsilon}}{1 - e^{-b \varepsilon}} = \lim_{\varepsilon \to 0^+} \frac{a e^{-a \varepsilon}}{b e^{-b \varepsilon}} = \frac{a}{b}.$$
    <2>5. Taking limits as $\varepsilon \to 0^+$ and $R \to \infty$:
    $$\int_0^\infty S(x) \, dx = 0 - \ln\left(\frac{a}{b}\right) = \ln\left(\frac{b}{a}\right).$$

<1>6. Conclusion:
    *Proof:*
    $\sum_{n=1}^\infty |f_n| \notin L^1([0, \infty))$, whereas $\sum_{n=1}^\infty f_n \in L^1([0, \infty))$ with integral equal to $\ln(b/a)$.
:::
