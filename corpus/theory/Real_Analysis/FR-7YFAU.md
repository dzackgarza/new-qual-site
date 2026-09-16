---
schema: qual/card@1
id: FR-7YFAU
kind: proof
title: Translation invariance and dilation of the Lebesgue integral
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $f\colon\RR^d\to[0,\infty]$ be Lebesgue [[D-DHFN4|measurable]], or let $f\in L^1(\RR^d)$, and let $h\in\RR^d$ and $\lambda\in\RR\setminus\theset{0}$.
Then $x\mapsto f(x+h)$ and $x\mapsto f(\lambda x)$ are measurable, and
$$
\int_{\RR^d} f(x+h)\dx = \int_{\RR^d} f(x)\dx, \qquad \int_{\RR^d} f(\lambda x)\dx = \abs{\lambda}^{-d}\int_{\RR^d} f(x)\dx.
$$
:::

::: {.proof}
We use that for a Lebesgue measurable $E \subseteq \RR^d$ the sets $E + h \coloneqq \theset{x + h \suchthat x \in E}$ and $\lambda E\coloneqq\theset{\lambda x\suchthat x\in E}$ are measurable, with $m(E + h) = m(E)$ and $m(\lambda E) = \abs{\lambda}^d m(E)$.
Put $\tau f(x)\coloneqq f(x+h)$ and $\delta f(x)\coloneqq f(\lambda x)$.
For a Borel set $B$, $(\tau f)\inv(B) = f\inv(B) - h$ and $(\delta f)\inv(B) = \lambda^{-1}f\inv(B)$, so $\tau f$ and $\delta f$ are measurable.

**Characteristic functions.** For measurable $E$, $\tau\chi_E = \chi_{E-h}$ and $\delta\chi_E = \chi_{\lambda^{-1}E}$, so
$$
\int\tau\chi_E = m(E - h) = m(E) = \int\chi_E, \qquad \int\delta\chi_E = m(\lambda^{-1}E) = \abs{\lambda}^{-d}\int\chi_E.
$$

**Simple functions.** A nonnegative [[D-553MO|simple function]] is a finite sum $\phi = \sum_i c_i \chi_{E_i}$ with $c_i\geq 0$ and $E_i$ measurable, and $\tau\phi = \sum_i c_i\tau\chi_{E_i}$ and $\delta\phi = \sum_i c_i\delta\chi_{E_i}$.
By the case of characteristic functions, $\int\tau\phi = \int\phi$ and $\int\delta\phi = \abs{\lambda}^{-d}\int\phi$.

**Nonnegative measurable functions.** By the [[D-R4VKE|definition of the integral]], $\int f$ is the supremum of $\int\phi$ over simple $0 \leq \phi \leq f$.
The maps $\phi\mapsto\tau\phi$ and $\phi\mapsto\delta\phi$ are bijections from the simple functions $0\leq\phi\leq f$ onto the simple functions $0\leq\psi\leq\tau f$ and $0\leq\psi\leq\delta f$ respectively, with inverses given by translation by $-h$ and dilation by $\lambda^{-1}$.
They multiply integrals by $1$ and by $\abs{\lambda}^{-d}$, so the suprema satisfy $\int\tau f = \int f$ and $\int\delta f = \abs{\lambda}^{-d}\int f$.

**Integrable functions.** For real-valued $f\in L^1(\RR^d)$, write $f = f^+ - f^-$ with $f^\pm \geq 0$; then $\tau f = \tau f^+ - \tau f^-$ and $\delta f = \delta f^+ - \delta f^-$, and the nonnegative case applies to each part. For complex-valued $f$, apply the real case to $\operatorname{Re} f$ and $\operatorname{Im} f$.
:::
