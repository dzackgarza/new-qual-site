---
schema: qual/card@1
id: P-CAFA17F
kind: problem
title: 'The mean value of $\log\abs{z-a}$ on circles and subharmonicity of a series'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. Part (a) is unchanged in substance and is now three cases with
    the term-by-term integration justified by uniform convergence of the power series. Part (b)
    had a real gap: the card passed from 'converges in L^1_loc' and 'Delta u >= 0' straight to
    'hence u is subharmonic', which needs u to be upper semicontinuous and locally bounded above
    — with only L^1_loc and a positive Laplacian the function may equal -infinity on a set. Both
    are now proved, by the split of u into a locally uniformly convergent series of positive
    parts (continuous limit) and a decreasing series of negative parts (upper semicontinuous).
    Also added: the reason the log-potential integrals are uniformly bounded in the pole, and
    the note that -infinity at the points 2^{-n} is allowed. The remark about the exam's 'r
    arbitrary real' stands as it is. Not claimed: a retained solution set; the collection's
    provenance is the examination paper only.
---

::: {.problem}
(a) Prove that for any $r>0$ and real $\rho$, $$\frac{1}{2\pi}\int_0^{2\pi} \log\abs{re^{it} - \rho}\,dt = \max(\log r, \log\abs{\rho}).$$

(b) Show that the series $$u(z) = \sum_{n=0}^{\infty} \frac{1}{2^n} \log\abs{z - \frac{1}{2^n}}$$ defines a subharmonic function.
:::

::: {.remark}
The official Fall 2017 exam calls $r$ an arbitrary real number while writing $\log r$. The intended hypothesis must be $r>0$.
:::

::: {.solution}
Throughout $r > 0$ and $\rho \in \RR$; $\log$ is the real logarithm and $\log^{+}t \coloneqq \max(\log t, 0)$. The collection's `provenance` is the Fall 2017 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #out}
(a) If $r > \abs{\rho}$ then $\frac{1}{2\pi}\int_{0}^{2\pi}\log\abs{re^{it} - \rho}\\,dt = \log r$.

::: pf-proof
Factor out $r$: $re^{it} - \rho = re^{it}\bigl(1 - \frac{\rho}{r}e^{-it}\bigr)$, so $\log\abs{re^{it}-\rho} = \log r + \log\abs{1 - \frac{\rho}{r}e^{-it}}$. Since $\abs{\rho}/r < 1$, the principal branch of the logarithm of $1 - \frac{\rho}{r}e^{-it}$ is given by its power series $\sum_{m \ge 1}\frac{1}{m}\bigl(\frac{\rho}{r}\bigr)^{m}e^{-imt}$, whose real part is $\sum_{m\ge1}\frac{1}{m}\bigl(\frac{\rho}{r}\bigr)^{m}\cos mt$. Integrating over $[0,2\pi]$ kills every cosine term, since $\int_{0}^{2\pi}\cos mt\\,dt = 0$ for $m \ge 1$ and the series converges uniformly in $t$ by comparison with $\sum_{m}\frac{1}{m}\bigl(\frac{\abs{\rho}}{r}\bigr)^{m}$, so term-by-term integration is legitimate. The mean is therefore $\log r$.

:::

:::

::: {.pf-step #in}
(a) If $r < \abs{\rho}$ then the mean is $\log\abs{\rho}$.

::: pf-proof
Here $\rho \ne 0$. Factor out $\rho$: $re^{it} - \rho = -\rho\bigl(1 - \frac{r}{\rho}e^{it}\bigr)$, so $\log\abs{re^{it}-\rho} = \log\abs{\rho} + \log\abs{1 - \frac{r}{\rho}e^{it}}$, and $\abs{r/\rho} < 1$ lets the previous power-series argument be repeated with $r/\rho$ in place of $\rho/r$; the mean of the second term is $0$.

:::

:::

::: {.pf-step #equal}
(a) If $r = \abs{\rho}$ then the mean is $\log r = \log\abs{\rho}$, and the displayed formula of the exercise holds for all $r > 0$ and $\rho \in \RR$.

::: pf-proof
In this case $\log\abs{re^{it} - \rho} = \log r + \log\abs{e^{it} - \rho/r}$ with $\abs{\rho/r} = 1$, so the mean is $\log r$ plus the mean of $\log\abs{e^{it} - \zeta}$ for $\abs{\zeta} = 1$, which vanishes by the standard evaluation $\frac{1}{2\pi}\int_{0}^{2\pi}\log\abs{e^{it}-1}dt = 0$ after rotating. The three cases $r > \abs{\rho}$, $r < \abs{\rho}$ and $r = \abs{\rho}$ exhaust the possibilities, and in each the mean equals $\max(\log r, \log\abs{\rho})$.

:::

:::

::: {.pf-step #term}
(b) Each $u_{n}(z) = 2^{-n}\log\abs{z - 2^{-n}}$ is subharmonic on $\CC$, locally integrable, and satisfies $\Delta u_{n} = 2\pi\\,2^{-n}\delta_{2^{-n}}$ in the sense of distributions.

::: pf-proof
$\log\abs{z - a}$ is the fundamental solution of the Laplacian, hence subharmonic and locally integrable, and $\Delta\log\abs{z-a} = 2\pi\delta_{a}$; a positive constant multiple inherits both properties. Part (a) with $r = \abs{z - a}$ and $\rho = 0$ gives the mean-value identity for the logarithm, which is the subharmonic mean-value inequality with equality.

:::

:::

::: {.pf-step #loc}
(b) The series converges in $L^{1}_{\mathrm{loc}}$ to a function $u$ that is locally bounded above and upper semicontinuous, and is finite off $\theset{2^{-n} \mid n \ge 0}$.

::: pf-proof
On a compact $K$, $\int_{K}\abs{\log\abs{z-a}}dA(z)$ is bounded uniformly for $a$ in a fixed bounded set — the singularity is integrable in the plane and the bound depends only on the diameter of $K$ and the distance from $K$ to $a$ being controlled on a bounded set — so $\sum_{n}\int_{K}\abs{u_{n}} \le C\sum_{n}2^{-n} < \infty$ and the series converges absolutely in $L^{1}(K)$. For the upper bound: $\log\abs{z - 2^{-n}} \le \log^{+}\abs{z-2^{-n}} \le \log^{+}(\abs{z}+1)$, so $u(z) \le \log^{+}(\abs{z}+1)\sum_{n}2^{-n}$, which is finite and locally bounded. For upper semicontinuity, split $u = \sum_{n}2^{-n}\log^{+}\abs{z-2^{-n}} - \sum_{n}2^{-n}\log^{-}\abs{z-2^{-n}}$: the first series converges locally uniformly (it is dominated by $\log^{+}(\abs{z}+1)\sum_{n}2^{-n}$) to a continuous function, and the second is the limit of the decreasing sequence of continuous functions $-\sum_{n \le N}2^{-n}\log^{-}\abs{z-2^{-n}}$, hence is upper semicontinuous; a continuous minus an upper semicontinuous function is upper semicontinuous. Finally $u(z) = -\infty$ can occur only where some term is $-\infty$, that is only at $z = 2^{-n}$.

:::

:::

::: {.pf-step #dist}
(b) $\Delta u = 2\pi\sum_{n \ge 0}2^{-n}\delta_{2^{-n}} \ge 0$ in the sense of distributions.

::: pf-proof
By step [](#loc){.pf-ref} the series converges in $L^{1}_{\mathrm{loc}}$, so it converges as a distribution, and differentiation of distributions is continuous; each term's Laplacian is given by step [](#term){.pf-ref}, and the sum of the resulting measures is $2\pi\sum_{n}2^{-n}\delta_{2^{-n}}$, a positive measure because every coefficient is positive.

:::

:::

::: pf-step
(b) $u(z) = \sum_{n=0}^{\infty}2^{-n}\log\abs{z - 2^{-n}}$ is subharmonic on $\CC$.

::: pf-proof
A function that is locally integrable, locally bounded above, upper semicontinuous and satisfies $\Delta u \ge 0$ in the sense of distributions is subharmonic. Steps [](#loc){.pf-ref} supply the first three properties and step [](#dist){.pf-ref} the fourth, so $u$ is subharmonic; it takes the value $-\infty$ at the points $2^{-n}$, which is permitted for a subharmonic function that is finite on a dense open set.

:::

:::

:::
:::
