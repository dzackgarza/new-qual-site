---
schema: qual/card@1
id: P-BKF12-1A
kind: problem
title: Arc length of the logarithmic spiral $r=e^\theta$, $\theta\le0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 1A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the polar arc-length integrand and the improper integral.
---

::: {.problem}
Find the length of the spiral given in polar coordinates by
$$
r=e^\theta,
\qquad
-\infty<\theta\le0.
$$
:::

::: {.solution}
<1>1. A polar curve $r=r(\theta)$ has arc-length element
$$
ds=\sqrt{r(\theta)^2+r'(\theta)^2}\,d\theta.
$$

::: {.proof}
The Cartesian parametrization is
$$
x(\theta)=r(\theta)\cos\theta,
\qquad
y(\theta)=r(\theta)\sin\theta.
$$
Differentiating and adding squares gives
$$
\begin{aligned}
x'(\theta)^2+y'(\theta)^2
&=(r'\cos\theta-r\sin\theta)^2
 +(r'\sin\theta+r\cos\theta)^2\\
&=r'(\theta)^2+r(\theta)^2.
\end{aligned}
$$
Taking the square root gives the stated arc-length element.
:::

<1>2. For $r=e^\theta$,
$$
ds=\sqrt2 e^\theta\,d\theta.
$$

::: {.proof}
Here
$$
r'(\theta)=e^\theta=r(\theta).
$$
Substitution into step <1>1 gives
$$
ds
=\sqrt{e^{2\theta}+e^{2\theta}}\,d\theta
=\sqrt2 e^\theta\,d\theta.
$$
:::

<1>3. The length of the spiral is
$$
\boxed{\sqrt2}.
$$

::: {.proof}
By step <1>2,
$$
\begin{aligned}
L
&=\int_{-\infty}^0\sqrt2 e^\theta\,d\theta\\
&=\sqrt2\,[e^\theta]_{-\infty}^0\\
&=\sqrt2.
\end{aligned}
$$
The improper integral converges because $e^\theta\to0$ as
$\theta\to-\infty$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested length.
:::
:::
