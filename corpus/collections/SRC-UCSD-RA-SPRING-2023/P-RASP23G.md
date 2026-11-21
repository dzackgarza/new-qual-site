---
schema: qual/card@1
id: P-RASP23G
kind: problem
title: "Riesz fractional integration formula via Fourier transform"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 7 and the Fourier-transform convention on the cover page of the official UCSD Spring 2023 real-analysis qualifying exam. The source says only "compact support function"; the card makes the standard test-function regularity phi in C_c^infty explicit so both displayed integrals are ordinary absolutely convergent Lebesgue integrals.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Every step checked: the two Gamma substitutions (t = pi lambda |x|^2 and t = pi |xi|^2/lambda, with the change of orientation in the second written out), the exponent arithmetic s - 1 - n/2 = -alpha/2 - 1, the Gaussian transform lambda^{-n/2} e^{-pi |xi|^2/lambda} obtained from the lambda = 1 case by the substitution x = lambda^{-1/2}u, and both interchanges with their absolute convergence. What the prose asserted in one clause ("the relevant integrals are absolutely convergent, and Fubini applies") is now split into: rapid decrease of the Fourier transform of a compactly supported smooth function giving integrability at infinity once N > n - alpha, local integrability of |x|^{alpha-n} near 0 because alpha > 0, and the same for the second interchange using local integrability of |xi|^{-alpha} and compact support of phi. No statement repair; the identity and both constants are correct as stated.
---

::: {.problem}
Let $\Gamma(z)$ be the gamma function defined by $\Gamma(z) = \int_0^\infty e^{-t} t^{z-1}\,dt$ for $z$ with $\operatorname{Re}(z) > 0$.
For $\phi\in C_c^\infty(\RR^n)$, prove that for any $0 < \alpha < n$,
$$
\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}} \int_{\RR^n} \norm{x}^{\alpha-n} \hat{\phi}(x)\,dx = \frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}} \int_{\RR^n} \norm{\xi}^{-\alpha} \phi(\xi)\,d\xi.
$$

Hint: Use the Fourier transform of the Gaussian, the identity $\int \hat{f} g = \int f \hat{g}$ for $L^1$ functions and the change of variables for the integral in the definition of $\Gamma$.
:::


::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, following the hint and the transform conventions printed on the examination.

Throughout $\widehat h(\xi)=\int_{\RR^n}e^{-2\pi i\langle\xi,y\rangle}h(y)\,dy$, and $s=(n-\alpha)/2>0$ because $0<\alpha<n$.

::: pf

::: {.pf-step #gamma}
For $x\ne0$, $\displaystyle\int_0^\infty e^{-\pi\lambda\norm x^2}\lambda^{s-1}\,d\lambda=\frac{\Gamma(s)}{\pi^s}\norm x^{-2s}=\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}}\norm x^{\alpha-n}$.

::: pf-proof
Substitute $t=\pi\lambda\norm x^2$, so $\lambda=t/(\pi\norm x^2)$ and $d\lambda=dt/(\pi\norm x^2)$; then
$$
\int_0^\infty e^{-\pi\lambda\norm x^2}\lambda^{s-1}d\lambda=\int_0^\infty e^{-t}\Bigl(\frac{t}{\pi\norm x^2}\Bigr)^{s-1}\frac{dt}{\pi\norm x^2}=(\pi\norm x^2)^{-s}\int_0^\infty e^{-t}t^{s-1}dt=\frac{\Gamma(s)}{\pi^s}\norm x^{-2s},
$$
and $\norm x^{-2s}=\norm x^{-(n-\alpha)}=\norm x^{\alpha-n}$.
:::

:::

::: {.pf-step #fubini1}
$\displaystyle\int_{\RR^n}\norm x^{\alpha-n}\widehat\phi(x)\,dx=\int_0^\infty\lambda^{s-1}\Bigl(\int_{\RR^n}\widehat\phi(x)e^{-\pi\lambda\norm x^2}dx\Bigr)d\lambda$.

::: pf-proof
Replace the weight by the $\lambda$-integral of step [](#gamma){.pf-ref}. Since $\phi\in C_c^\infty$, $\widehat\phi$ is rapidly decreasing: $\abs{\widehat\phi(x)}\le C_N(1+\norm x)^{-N}$ for every $N$, so $\abs{\widehat\phi(x)}\norm x^{\alpha-n}$ is integrable at infinity once $N>n-\alpha$, and integrable near $0$ because $\alpha-n>-n$. The joint integrand $\abs{\widehat\phi(x)}e^{-\pi\lambda\norm x^2}\lambda^{s-1}$ has $\lambda$-integral $\Gamma(s)\pi^{-s}\abs{\widehat\phi(x)}\norm x^{-2s}$, integrable in $x$ by the same bound, so Fubini–Tonelli applies.
:::

:::

::: {.pf-step #duality}
For every $\lambda>0$, $\displaystyle\int_{\RR^n}\widehat\phi(x)e^{-\pi\lambda\norm x^2}dx=\lambda^{-n/2}\int_{\RR^n}\phi(\xi)e^{-\pi\norm\xi^2/\lambda}d\xi$.

::: pf-proof
The Fourier transform of $g_\lambda(x)=e^{-\pi\lambda\norm x^2}$ is $\widehat g_\lambda(\xi)=\lambda^{-n/2}e^{-\pi\norm\xi^2/\lambda}$: the case $\lambda=1$ is the standard computation $\int e^{-\pi\norm x^2}e^{-2\pi i\langle\xi,x\rangle}dx=e^{-\pi\norm\xi^2}$, and the general case follows by the substitution $x=\lambda^{-1/2}u$. Both $\widehat\phi$ and $g_\lambda$ are integrable, as are $\phi$ and $\widehat g_\lambda$, and both sides of $\int\widehat\phi\,g_\lambda=\int\phi\,\widehat g_\lambda$ equal $\iint\phi(y)e^{-2\pi i\langle x,y\rangle}g_\lambda(x)\,dx\,dy$, which is absolutely convergent, so Fubini gives the identity: integrating first in $x$ produces $\widehat g_\lambda(y)$.
:::

:::

::: {.pf-step #lambda}
For $\xi\ne0$, $\displaystyle\int_0^\infty\lambda^{-\alpha/2-1}e^{-\pi\norm\xi^2/\lambda}d\lambda=\frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}}\norm\xi^{-\alpha}$.

::: pf-proof
Substitute $t=\pi\norm\xi^2/\lambda$, so $\lambda=\pi\norm\xi^2/t$ and $d\lambda=-\pi\norm\xi^2t^{-2}dt$; as $\lambda$ runs over $(0,\infty)$, $t$ runs over $(\infty,0)$, so
$$
\int_0^\infty\lambda^{-\alpha/2-1}e^{-\pi\norm\xi^2/\lambda}d\lambda=\int_0^\infty\Bigl(\frac{\pi\norm\xi^2}{t}\Bigr)^{-\alpha/2-1}e^{-t}\frac{\pi\norm\xi^2}{t^2}dt=(\pi\norm\xi^2)^{-\alpha/2}\int_0^\infty t^{\alpha/2-1}e^{-t}dt,
$$
and the last integral is $\Gamma(\alpha/2)$.
:::

:::

::: {.pf-step #identity}
$\displaystyle\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}}\int_{\RR^n}\norm x^{\alpha-n}\widehat\phi(x)\,dx=\frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}}\int_{\RR^n}\norm\xi^{-\alpha}\phi(\xi)\,d\xi$.

::: pf-proof
By steps [](#fubini1){.pf-ref} and [](#duality){.pf-ref} the left side equals
$$
\int_0^\infty\lambda^{s-1-n/2}\Bigl(\int_{\RR^n}\phi(\xi)e^{-\pi\norm\xi^2/\lambda}d\xi\Bigr)d\lambda,
$$
and $s-1-n/2=\frac{n-\alpha}{2}-1-\frac n2=-\frac\alpha2-1$. The second Fubini is justified by absolute convergence: the inner $\lambda$-integral equals $\Gamma(\alpha/2)\pi^{-\alpha/2}\abs{\xi}^{-\alpha}$ by step [](#lambda){.pf-ref}, which is integrable against $\abs{\phi(\xi)}$ because $\phi$ has compact support and $\alpha<n$. Interchanging and applying step [](#lambda){.pf-ref} pointwise in $\xi$ gives $\int_{\RR^n}\phi(\xi)\frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}}\norm\xi^{-\alpha}d\xi$, which is the right side.
:::

:::

:::
:::
