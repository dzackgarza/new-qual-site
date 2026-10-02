---
schema: qual/card@1
id: P-CHAVAN-CA-8-2
kind: problem
title: No nonconstant entire function omits a half-line
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Show that there is no nonconstant entire function whose range is contained in the complement of a half-line.
:::

::: {.solution}
Write the half-line as
$$
L=\{a+te^{i\alpha}:t\geq0\}
$$
for some $a\in\CC$ and $\alpha\in\RR$.

<1>1. Suppose, for contradiction, that a nonconstant entire function $f$
satisfies $f(\CC)\subseteq\CC\setminus L$. Then
$$
g(z)=e^{-i\alpha}(f(z)-a)
$$
is a nonconstant entire function with
$$
g(\CC)\subseteq\CC\setminus[0,\infty).
$$

::: {.proof}
The affine map $w\mapsto e^{-i\alpha}(w-a)$ sends $L$ onto
$[0,\infty)$ and preserves holomorphy and nonconstancy.
:::

<1>2. There is an entire function $h$ such that
$$
h^2=g
\qquad\text{and}\qquad
\operatorname{Im}h(z)>0
\quad(z\in\CC).
$$

::: {.proof}
On the slit plane $\CC\setminus[0,\infty)$, use the holomorphic logarithm
$$
\Log(re^{i\theta})=\log r+i\theta,
\qquad r>0,
\quad 0<\theta<2\pi.
$$
Define
$$
h(z)=\exp\left(\frac12\Log(g(z))\right).
$$
Since $g$ is entire and takes values in the slit plane, $h$ is entire. Also
$h(z)^2=g(z)$. If $g(z)=re^{i\theta}$ with $0<\theta<2\pi$, then
$$
h(z)=\sqrt r\,e^{i\theta/2},
$$
whose argument lies in $(0,\pi)$; hence $\operatorname{Im}h(z)>0$.
:::

<1>3. The function
$$
k(z)=e^{ih(z)}
$$
is a bounded entire function.

::: {.proof}
It is entire because $h$ is entire. Moreover,
$$
\abs{k(z)}
=e^{-\operatorname{Im}h(z)}
<1
$$
by step <1>2.
:::

<1>4. The function $f$ is constant.

::: {.proof}
Liouville's theorem applied to step <1>3 makes $k$ constant. Since
$$
k'(z)=ih'(z)e^{ih(z)}
$$
and $e^{ih(z)}$ never vanishes, $h'\equiv0$. Thus $h$ is constant, so
$g=h^2$ is constant, and step <1>1 then implies that $f$ is constant.
:::

<1>5. No nonconstant entire function can have range contained in the complement
of a half-line.

::: {.proof}
Step <1>4 contradicts the nonconstancy assumed in step <1>1.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
