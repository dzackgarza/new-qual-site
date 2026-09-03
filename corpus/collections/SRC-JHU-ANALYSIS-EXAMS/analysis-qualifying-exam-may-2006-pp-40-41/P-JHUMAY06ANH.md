---
schema: qual/card@1
id: P-JHUMAY06ANH
kind: problem
title: '$L^1\cap L^2\subseteq L^p$ for $1\le p\le2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Prove that any function $f \in L^1(I) \cap L^2(I)$ on an interval $I \subset \mathbb{R}$ must belong to $L^p(I)$ for all $p \in [1, 2]$.
:::

::: {.solution}
<1>1. Pointwise splitting method: <2>1. For $p = 1$ and $p = 2$, $f \in L^1(I)$ and $f \in L^2(I)$ by hypothesis.
::: {.proof}
hypothesis $f \in L^1(I) \cap L^2(I)$.
:::
<2>2. Fix $p \in (1, 2)$.
Partition $I$ into two disjoint measurable sets:
\[
E_1 = \{x \in I : |f(x)| \le 1\}, \quad E_2 = \{x \in I : |f(x)| > 1\}.
\]
::: {.proof}
preimage of Borel sets under the measurable function $|f|$.
:::
<2>3. On $E_1$, since $|f(x)| \le 1$ and $p > 1$, $|f(x)|^p \le |f(x)|$.
::: {.proof}
for $t \in [0, 1]$ and $p \ge 1$, $t^p \le t$.
:::
<2>4. On $E_2$, since $|f(x)| > 1$ and $p < 2$, $|f(x)|^p \le |f(x)|^2$.
::: {.proof}
for $t > 1$ and $p \le 2$, $t^p \le t^2$.
:::
<2>5. Integrating $|f|^p$ over $I$:
\[
\int_I |f|^p\,dx = \int_{E_1} |f|^p\,dx + \int_{E_2} |f|^p\,dx \le \int_{E_1} |f|\,dx + \int_{E_2} |f|^2\,dx \le \|f\|_{L^1(I)} + \|f\|_{L^2(I)}^2 < \infty.
\]
::: {.proof}
<2>3, <2>4, and additivity of the Lebesgue integral.
:::
<2>6. Thus $f \in L^p(I)$ for every $p \in (1, 2)$.
::: {.proof}
$\int_I |f|^p\,dx < \infty$.
:::

<1>2. Lyapounov / Riesz–Thorin interpolation inequality: <2>1. Choose $\theta = \frac{2(p-1)}{p} \in (0, 1)$, so that $1 - \theta = \frac{2-p}{p}$ and $\frac{1}{p} = \frac{1-\theta}{1} + \frac{\theta}{2}$.
::: {.proof}
arithmetic.
:::
<2>2. Decompose $|f|^p = |f|^{(1-\theta)p} |f|^{\theta p} = |f|^{2-p} |f|^{2(p-1)}$.
::: {.proof}
exponent addition $(1-\theta)p + \theta p = p$.
:::
<2>3. Apply Hölder’s inequality with conjugate exponents $r = \frac{1}{1-\theta} = \frac{p}{2-p} > 1$ and $s = \frac{1}{\theta} = \frac{p}{2(p-1)} > 1$:
\[
\int_I |f|^p\,dx \le \left(\int_I |f|^{(2-p) \cdot \frac{p}{2-p}}\,dx\right)^{\frac{2-p}{p}} \left(\int_I |f|^{2(p-1) \cdot \frac{p}{2(p-1)}}\,dx\right)^{\frac{2(p-1)}{p}} = \|f\|_{L^1(I)}^{2-p} \|f\|_{L^2(I)}^{2(p-1)}.
\]
::: {.proof}
Hölder's inequality.
:::
<2>4. Taking the $p$-th root yields the $L^p$ interpolation inequality:
\[
\|f\|_{L^p(I)} \le \|f\|_{L^1(I)}^{1-\theta} \|f\|_{L^2(I)}^\theta < \infty.
\]
::: {.proof}
<2>3.
:::

<1>3. Conclusion: $f \in L^p(I)$ for all $p \in [1, 2]$.
::: {.proof}
<1>1 and <1>2.
:::
Q.E.D.
:::
