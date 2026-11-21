---
schema: qual/card@1
id: E-SS6.EX-17
kind: problem
title: Analytic continuation of the Mellin transform of a Schwartz function
classification:
  areas:
  - complex-analysis
  topics:
  - Mellin Transform
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the derivative-index transcription defect using the supplied integration-by-parts identity.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the two parts already on the card, which are correct. The
    card's remark already records that the printed statement has two misprints — I(0) = 0 and
    I(-n) = (-1)^n f^{(n+1)}(0) — and that the correct values are I(0) = f(0) and I(-n) = (-1)^n
    f^{(n)}(0), verified against f(x) = e^{-x^2}; the statement is kept as printed and the
    remark stands. Added: the dominated-convergence majorant that gives holomorphy on the half-
    plane, the two boundary terms in the integration by parts with the reason each vanishes, the
    induction for the iterated formula including the shift in the parameter, and the
    identification of the continuation J_k as the unique one agreeing with I on the overlap. Not
    claimed: a retained solution set; the collection's provenance is the Stein--Shakarchi
    textbook.
---

::: {.exercise}
Let $f$ be an indefinitely differentiable function on $\RR$ that has compact support, or more generally, let $f$ belong to the Schwartz space. Consider
$$
I(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} f(x)\, x^{-1+s}\, dx.
$$

(a) Observe that $I(s)$ is holomorphic for $\Re(s) > 0$. Prove that $I$ has an analytic continuation as an entire function in the complex plane.

(b) Prove that $I(0) = f(0)$, and more generally
$$
I(-n) = (-1)^n f^{(n)}(0) \quad \text{for all } n \geq 0.
$$

[Hint: To prove the analytic continuation, as well as the formulas in the second part, integrate by parts to show that $I(s) = \frac{(-1)^k}{\Gamma(s + k)} \int_0^{\infty} f^{(k)}(x)\, x^{s+k-1}\, dx$.]
:::

::: {.remark}
The source prints $I(0) = 0$ and $I(-n) = (-1)^n f^{(n+1)}(0)$. The hint with $k = n+1$ gives $I(-n) = (-1)^{n+1}\int_0^\infty f^{(n+1)}(x)\,dx = (-1)^n f^{(n)}(0)$; for $f(x) = e^{-x^2}$, $I(0) = 1$.
:::

::: {.solution}
Throughout $f$ is a Schwartz function on $\RR$ — the compactly supported smooth case is included, since such an $f$ is Schwartz — and $I(s) \coloneqq \frac{1}{\Gamma(s)}\int_{0}^{\infty}f(x)x^{-1+s}dx$ for $\Re s > 0$, the only region where the integral is absolutely convergent. The exercise is Exercise 17 of Stein--Shakarchi, *Complex Analysis*, Chapter 6; the remark below the problem records the two misprints in the printed statement.

::: pf

::: {.pf-step #holomorphic}
(a) $I$ is holomorphic on $\Re s > 0$.

::: pf-proof
On a compact set $K$ contained in $\Re s > 0$ the integrand $f(x)x^{s-1}$ is bounded in modulus by $C_{K}\abs{f(x)}\bigl(x^{\alpha-1} + x^{\beta-1}\bigr)$, with $\alpha, \beta$ the extrema of $\Re s$ on $K$, and that majorant is integrable on $(0,\infty)$ for a Schwartz $f$ because $f$ is bounded near $0$ and rapidly decreasing at $\infty$; the integrand is holomorphic in $s$ for each $x$. Dominated convergence therefore gives holomorphy of the integral, and $1/\Gamma(s)$ is entire with $1/\Gamma$ vanishing nowhere, so the quotient is holomorphic.

:::

:::

::: {.pf-step #parts}
For $\Re s > 0$, $\int_{0}^{\infty}f(x)x^{s-1}dx = -\frac{1}{s}\int_{0}^{\infty}f'(x)x^{s}dx$, hence $I(s) = -\frac{1}{\Gamma(s+1)}\int_{0}^{\infty}f'(x)x^{s}dx$.

::: pf-proof
Integration by parts on $(\varepsilon, R)$ gives $\int_{\varepsilon}^{R}f(x)x^{s-1}dx = \bigl[f(x)\frac{x^{s}}{s}\bigr]_{\varepsilon}^{R} - \frac{1}{s}\int_{\varepsilon}^{R}f'(x)x^{s}dx$. As $R \to \infty$ the boundary term vanishes because $f$ is rapidly decreasing and $\abs{x^{s}} = x^{\Re s}$; as $\varepsilon \to 0$ it vanishes because $f$ is bounded and $\Re s > 0$. Finally $s\Gamma(s) = \Gamma(s+1)$ turns $\frac{1}{\Gamma(s)}\cdot\bigl(-\frac{1}{s}\bigr)$ into $-\frac{1}{\Gamma(s+1)}$, and $x^{s} = x^{(s+1)-1}$.

:::

:::

::: {.pf-step #iterate}
For every $k \ge 0$ and $\Re s > 0$, $I(s) = \frac{(-1)^{k}}{\Gamma(s+k)}\int_{0}^{\infty}f^{(k)}(x)x^{s+k-1}dx$.

::: pf-proof
Induction on $k$, the case $k = 0$ being the definition. If the identity holds for $k$, apply step [](#parts){.pf-ref} to the Schwartz function $f^{(k)}$ at the parameter $s + k$, which is legitimate because $\Re(s+k) > 0$: $\int_{0}^{\infty}f^{(k)}(x)x^{s+k-1}dx = -\frac{1}{s+k}\int_{0}^{\infty}f^{(k+1)}(x)x^{s+k}dx$, and $\Gamma(s+k+1) = (s+k)\Gamma(s+k)$ turns the coefficient into $\frac{(-1)^{k+1}}{\Gamma(s+k+1)}$ with the exponent $s+k = (s+k+1)-1$.

:::

:::

::: {.pf-step #continue}
(a) $I$ extends to an entire function.

::: pf-proof
Fix $k \ge 0$ and set $J_{k}(s) \coloneqq \frac{(-1)^{k}}{\Gamma(s+k)}\int_{0}^{\infty}f^{(k)}(x)x^{s+k-1}dx$. The integral is holomorphic on $\Re s > -k$ by the argument of step [](#holomorphic){.pf-ref} with $f$ replaced by the Schwartz function $f^{(k)}$, since the majorant is then integrable exactly when $\Re s + k - 1 > -1$ near $0$ and $f^{(k)}$ is rapidly decreasing at $\infty$; and $1/\Gamma$ is entire. So $J_{k}$ is holomorphic on the half-plane $\Re s > -k$, and by step [](#iterate){.pf-ref} it agrees with $I$ on $\Re s > 0$, which is a nonempty open subset of $\Re s > -k$. Hence $J_{k}$ is the unique analytic continuation of $I$ to $\Re s > -k$, and the half-planes $\Re s > -k$ exhaust $\CC$ as $k$ grows, so $I$ extends to an entire function.

:::

:::

::: pf-step
(b) $I(-n) = (-1)^{n}f^{(n)}(0)$ for every $n \ge 0$; in particular $I(0) = f(0)$.

::: pf-proof
Take $k = n+1$ in step [](#iterate){.pf-ref} and evaluate the continuation at $s = -n$, which lies in $\Re s > -(n+1)$: then $\Gamma(s+k) = \Gamma(1) = 1$ and the exponent is $s+k-1 = -n+n+1-1 = 0$, so the formula reads $I(-n) = (-1)^{n+1}\int_{0}^{\infty}f^{(n+1)}(x)dx$. Since $f^{(n)}$ is Schwartz, $f^{(n)}(x) \to 0$ as $x \to \infty$, and $\int_{0}^{\infty}f^{(n+1)}(x)dx = f^{(n)}(\infty) - f^{(n)}(0) = -f^{(n)}(0)$; hence $I(-n) = (-1)^{n+1}\bigl(-f^{(n)}(0)\bigr) = (-1)^{n}f^{(n)}(0)$. For $n = 0$ this is $I(0) = f(0)$, and for $f(x) = e^{-x^{2}}$ it gives $I(0) = 1$, which is the check recorded in the remark against the printed $I(0) = 0$.

:::

:::

:::
:::
