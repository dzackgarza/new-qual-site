---
schema: qual/card@1
id: P-QZE53
kind: problem
title: Local integrability of $F(z)=\int_{\CC}\frac{1}{z-w}\,d\mu(w)$, integrability
  along almost every horizontal line, and $\mu(S)=\frac{1}{2\pi i}\int_{\partial S}F(z)\,dz$
  for almost every axis-parallel square
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\mu$ be a finite positive Borel measure on $\mathbb{C}$.

a. Prove that $F(z) = \int_\mathbb{C} \frac{1}{z-w}\,d\mu(w)$ exists for almost all $z\in\mathbb{C}$ and that $\int_K |F(z)|\,dx\,dy < \infty$ for every compact $K\subseteq\mathbb{C}$.

b. Prove that for almost every horizontal line $L$ and all compact $K\subseteq L$, $\int_K |F(x+iy)|\,dx < \infty$.

c. Prove that for almost all open squares $S$ with sides parallel to the axes, $$\mu(S) = \frac{1}{2\pi i}\int_{\partial S} F(z)\,dz.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): Local integrability and almost-everywhere existence of $F(z)$:

::: pf-proof

::: pf-step

Let $K \subset \mathbb{C}$ be any compact subset. Let $R = \operatorname{diam}(K) + 1$.

::: pf-proof

compact sets are bounded.

:::

:::

::: pf-step

For each fixed $w \in \mathbb{C}$, the shift $z \mapsto z - w$ maps $K$ into the closed disk $\overline{B}(0, R)$.
Using polar coordinates centered at $w$:
\[
\int_K \frac{1}{|z - w|}\,dx\,dy \le \int_{\overline{B}(w, R)} \frac{1}{|z - w|}\,dx\,dy = \int_0^R \int_0^{2\pi} \frac{1}{r} r\,dr\,d\theta = 2\pi R.
\]

::: pf-proof

polar integration of $1/r$.

:::

:::

::: pf-step

By Tonelli’s Theorem, integrating over $K$ and $\mathbb{C}$ gives:
\[
\int_K |F(z)|\,dx\,dy \le \int_K \left(\int_\mathbb{C} \frac{1}{|z - w|}\,d\mu(w)\right) dx\,dy = \int_\mathbb{C} \left(\int_K \frac{1}{|z - w|}\,dx\,dy\right) d\mu(w) \le 2\pi R \mu(\mathbb{C}) < \infty.
\]

::: pf-proof

Tonelli's Theorem for non-negative measurable functions and finiteness of $\mu$.

:::

:::

::: pf-step

Since $\int_K |F(z)|\,dx\,dy < \infty$ for every compact $K \subset \mathbb{C}$, $F \in L^1_{\mathrm{loc}}(\mathbb{C})$, which implies $|F(z)| < \infty$ for almost every $z \in \mathbb{C}$ with respect to Lebesgue measure.

::: pf-proof

a locally integrable function is finite almost everywhere.

:::

:::

:::

:::

::: {.pf-step #s2}

Part (b): Integrability along almost every horizontal line:

::: pf-proof

::: pf-step

For any $n \ge 1$, let $Q_n = [-n, n] \times [-n, n] \subset \mathbb{C}$.
By Part (a), $\int_{Q_n} |F(x+iy)|\,dx\,dy < \infty$.

::: pf-proof

Step [](#s1){.pf-ref} applied to the compact set $Q_n$.

:::

:::

::: pf-step

By Fubini–Tonelli Theorem:
\[
\int_{-n}^n \left(\int_{-n}^n |F(x+iy)|\,dx\right) dy = \int_{Q_n} |F(x+iy)|\,dx\,dy < \infty.
\]
Thus the function $y \mapsto \int_{-n}^n |F(x+iy)|\,dx$ is finite for almost every $y \in [-n, n]$.

::: pf-proof

Fubini–Tonelli Theorem on product measure spaces.

:::

:::

::: pf-step

Taking the countable union of the exceptional null sets over all $n \ge 1$, for almost every $y \in \mathbb{R}$, $\int_{-n}^n |F(x+iy)|\,dx < \infty$ for all $n$.
Thus $\int_K |F(x+iy)|\,dx < \infty$ for every compact $K \subset L_y$.

::: pf-proof

countable unions of measure zero sets have measure zero.

:::

:::

:::

:::

::: {.pf-step #s3}

Part (c): Recovering $\mu(S)$ via contour integration along $\partial S$:

::: pf-proof

::: pf-step

Let $S = (a, b) \times (c, d)$ be an open axis-parallel square.
Since $\mu$ is a finite measure, $\mu(\partial S) = 0$ for almost all choices of boundary coordinates $(a, b, c, d)$.

::: pf-proof

the family of parallel lines carrying positive $\mu$-measure is at most countable.

:::

:::

::: pf-step

By Part (b) and the analogous statement for vertical lines, the 1D integral $\int_{\partial S} |F(z)|\,|dz| < \infty$ for almost all squares $S$.

::: pf-proof

Step [](#s2){.pf-ref} applied to the four boundary segments of $\partial S$.

:::

:::

::: pf-step

By Fubini’s Theorem, we can interchange the contour integral and the measure integral:
\[
\frac{1}{2\pi i} \int_{\partial S} F(z)\,dz = \frac{1}{2\pi i} \int_{\partial S} \left(\int_\mathbb{C} \frac{1}{z - w}\,d\mu(w)\right) dz = \int_\mathbb{C} \left(\frac{1}{2\pi i} \int_{\partial S} \frac{1}{z - w}\,dz\right) d\mu(w).
\]

::: pf-proof

Fubini's Theorem on product space $\partial S \times \mathbb{C}$.

:::

:::

::: pf-step

By Cauchy’s Integral Formula / Residue Theorem for the winding number:
\[
\frac{1}{2\pi i} \int_{\partial S} \frac{1}{z - w}\,dz = \operatorname{Ind}_{\partial S}(w) = \begin{cases} 1 & w \in S \\ 0 & w \in \mathbb{C} \setminus \overline{S}. \end{cases}
\]

::: pf-proof

Cauchy's Integral Formula.

:::

:::

::: pf-step

Since $\mu(\partial S) = 0$, the integrand equals $\mathbf{1}_S(w)$ $\mu$-almost everywhere.
Thus:
\[
\int_\mathbb{C} \left(\frac{1}{2\pi i} \int_{\partial S} \frac{1}{z - w}\,dz\right) d\mu(w) = \int_\mathbb{C} \mathbf{1}_S(w)\,d\mu(w) = \mu(S).
\]

::: pf-proof

Lebesgue integration of characteristic functions.

:::

:::

:::

:::

::: pf-step

Conclusion:
$F \in L^1_{\mathrm{loc}}(\mathbb{C})$, $F$ is integrable along almost every horizontal line segment, and $\mu(S) = \frac{1}{2\pi i}\int_{\partial S} F(z)\,dz$ for almost all axis-parallel squares. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
