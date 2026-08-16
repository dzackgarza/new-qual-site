---
schema: qual/card@1
id: P-UV6A7
kind: problem
title: Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$ converges in...
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
relations: []
review: draft
---

::: problem
(1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$
    converges in $|z| < R$. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
    \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

(2) Deduce Liouville's theorem from (1).
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(1) Parseval's identity for power series:**
Since $r < R$, the power series $f(re^{i\theta}) = \sum_{n=0}^\infty c_n r^n e^{in\theta}$ converges uniformly on $\theta \in [0, 2\pi]$.
The complex conjugate is $\overline{f(re^{i\theta})} = \sum_{m=0}^\infty \overline{c_m} r^m e^{-im\theta}$.
Then $|f(re^{i\theta})|^2 = f(re^{i\theta}) \overline{f(re^{i\theta})}$.
Due to uniform convergence, we can integrate term by term:
$$
\frac{1}{2\pi} \int_0^{2\pi} |f(re^{i\theta})|^2 \, d\theta = \frac{1}{2\pi} \int_0^{2\pi} \left( \sum_{n=0}^\infty c_n r^n e^{in\theta} \right) \left( \sum_{m=0}^\infty \overline{c_m} r^m e^{-im\theta} \right) d\theta
$$
$$
= \sum_{n=0}^\infty \sum_{m=0}^\infty c_n \overline{c_m} r^{n+m} \left( \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)\theta} \, d\theta \right).
$$
By orthogonality of the complex exponentials:
$$
\frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)\theta} \, d\theta = \begin{cases} 1 & \text{if } n = m, \\ 0 & \text{if } n \neq m. \end{cases}
$$
Therefore, all terms with $n \neq m$ vanish, leaving:
$$
\frac{1}{2\pi} \int_0^{2\pi} |f(re^{i\theta})|^2 \, d\theta = \sum_{n=0}^\infty c_n \overline{c_n} r^{2n} = \sum_{n=0}^\infty |c_n|^2 r^{2n}.
$$

**(2) Deducing Liouville's Theorem:**
*Liouville's Theorem: Every bounded entire function is constant.*

Let $f: \CC \to \CC$ be an entire function (so $f(z) = \sum_{n=0}^\infty c_n z^n$ with radius of convergence $R = \infty$), and suppose $f$ is bounded on $\CC$, i.e. $|f(z)| \leq M$ for all $z \in \CC$.

For any $r > 0$, applying part (1):
$$
\sum_{n=0}^\infty |c_n|^2 r^{2n} = \frac{1}{2\pi} \int_0^{2\pi} |f(re^{i\theta})|^2 \, d\theta \leq \frac{1}{2\pi} \int_0^{2\pi} M^2 \, d\theta = M^2.
$$
In particular, for every integer $k \geq 1$:
$$
|c_k|^2 r^{2k} \leq \sum_{n=0}^\infty |c_n|^2 r^{2n} \leq M^2 \implies |c_k|^2 \leq \frac{M^2}{r^{2k}}.
$$
Since this holds for arbitrarily large $r > 0$, taking $r \to \infty$ gives:
$$
|c_k|^2 \leq \lim_{r \to \infty} \frac{M^2}{r^{2k}} = 0 \implies c_k = 0 \quad \text{for all } k \geq 1.
$$
Therefore, $f(z) = c_0$ is constant for all $z \in \CC$.
:::
