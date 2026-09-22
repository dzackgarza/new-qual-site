---
schema: qual/card@1
id: P-BERK90S-11
kind: problem
title: A bounded analytic function on a half-plane is uniformly continuous away from the boundary
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the boundedness and analyticity hypotheses and the conclusion for every positive c with Problem 11 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Applied the Cauchy derivative estimate on discs of radius c and integrated along segments to obtain a global Lipschitz bound.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked closed-disc containment in the analytic domain, the derivative constant, convexity of the smaller half-plane, and the point-independent epsilon-delta estimate with a positive bound M.
---

::: {.problem}
Let $f$ be bounded and analytic in the half-plane
$$
\Re z>0.
$$
Prove that for every $c>0$, the restriction of $f$ to
$$
\Re z>c
$$
is uniformly continuous.
:::

::: {.hint}
For fixed $c>0$, every closed disc of radius $c$ centered at a
point with real part greater than $c$ lies in the domain of $f$.
Apply the [[FF-HO7RN|Cauchy estimate]] for the first derivative
on these discs, then integrate along a line segment in the
smaller half-plane.
:::

::: {.solution}
Fix $c>0$ and put
$$
H\coloneqq\{z\in\CC:\Re z>0\},\qquad
H_c\coloneqq\{z\in\CC:\Re z>c\}.
$$
Choose $M>0$ such that $\abs{f(z)}\leq M$ for all $z\in H$.

<1>1. For every $z\in H_c$, the derivative satisfies
$\abs{f'(z)}\leq M/c$.

::: {.proof}
Fix $z\in H_c$. For $\abs{\zeta-z}\leq c$,
$$
\Re\zeta\geq\Re z-\abs{\zeta-z}\geq\Re z-c>0.
$$
Thus the closed disc of radius $c$ centered at $z$ lies in $H$.
The [[FT-AK34G|Cauchy integral formula for derivatives]] on its
counterclockwise boundary circle gives
$$
f'(z)=\frac{1}{2\pi i}
\int_{\abs{\zeta-z}=c}\frac{f(\zeta)}{(\zeta-z)^2}\,d\zeta.
$$
The circle has length $2\pi c$, and the integrand has modulus
at most $M/c^2$. Therefore $\abs{f'(z)}\leq M/c$.
:::

<1>2. For all $z,w\in H_c$,
$$
\abs{f(w)-f(z)}\leq\frac{M}{c}\abs{w-z}.
$$

::: {.proof}
Define $\gamma\colon[0,1]\to H_c$ by
$\gamma(t)\coloneqq(1-t)z+tw$. Its image lies in $H_c$ because
$$
\Re\gamma(t)=(1-t)\Re z+t\Re w>c
\qquad(0\leq t\leq1).
$$
The chain rule and the fundamental theorem of calculus give
$$
f(w)-f(z)=\int_0^1 f'(\gamma(t))(w-z)\,dt.
$$
Taking absolute values and applying step <1>1 proves the bound.
:::

<1>3. Q.E.D.

::: {.proof}
Given $\varepsilon>0$, set $\delta\coloneqq c\varepsilon/M>0$.
For any $z,w\in H_c$ with $\abs{w-z}<\delta$, step <1>2 gives
$\abs{f(w)-f(z)}<\varepsilon$. The number $\delta$ is independent
of $z$ and $w$, so $f|_{H_c}$ is
[[FD-ST7TD|uniformly continuous]]. Since $c>0$ was arbitrary,
the conclusion holds for every half-plane in the statement.
:::
:::
