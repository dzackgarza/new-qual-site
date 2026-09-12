---
schema: qual/card@1
id: P-EHKFZ
kind: problem
title: Area of $f(\{r<|z|<R\})$ is $\pi\sum_{n=-\infty}^\infty n|c_n|^2(R^{2n}-r^{2n})$
  for a univalent Laurent series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $f(z) = \sum_{n=-\infty}^\infty c_n z^n$ be analytic and one-to-one (univalent) in the open annulus $r_0 < |z| < R_0$.
For $r_0 < r < R < R_0$, let $D(r, R) = \{z \in \mathbb{C} \mid r < |z| < R\}$ be the concentric sub-annulus.
Prove that the area $S$ of the image domain $f(D(r, R))$ is finite and given by the series formula:
$$S = \pi \sum_{n=-\infty}^\infty n |c_n|^2 (R^{2n} - r^{2n}).$$
:::

::: solution
Since $f$ is univalent and holomorphic on $D(r,R)$, the real Jacobian is
\[
J_f(z)=|f'(z)|^2,
\]
and change of variables gives
\[
S=\operatorname{Area}(f(D(r,R)))
=\iint_{D(r,R)}|f'(z)|^2\,dA(z).
\]

The Laurent series may be differentiated termwise on compact subannuli:
\[
f'(z)=\sum_{n\in\mathbb Z}n c_n z^{n-1}.
\]
For $z=\rho e^{i\theta}$, Parseval's identity gives
\[
\int_0^{2\pi}|f'(\rho e^{i\theta})|^2\,d\theta
=2\pi\sum_{n\in\mathbb Z}n^2|c_n|^2\rho^{2n-2}.
\]
Hence, by Tonelli's theorem (all terms are nonnegative),
\[
\begin{aligned}
S
&=2\pi\sum_{n\in\mathbb Z}n^2|c_n|^2
\int_r^R\rho^{2n-1}\,d\rho\\
&=\pi\sum_{n\in\mathbb Z}n|c_n|^2(R^{2n}-r^{2n}),
\end{aligned}
\]
where the $n=0$ term is $0$.

The area is finite because $\overline{D(r,R)}$ is a compact subset of the annulus of holomorphy, so $f'$ is bounded there and
\[
S\le \operatorname{Area}(D(r,R))\,\sup_{\overline{D(r,R)}}|f'|^2<\infty.
\]
:::
