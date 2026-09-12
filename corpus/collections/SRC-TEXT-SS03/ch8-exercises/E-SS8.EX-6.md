---
schema: qual/card@1
id: E-SS8.EX-6
kind: problem
title: Conformal invariance of harmonicity via the Laplacian
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
6. Give another proof of Lemma 1.3 by showing directly that the Laplacian of $u \circ F$ is zero.

[Hint: The real and imaginary parts of F satisfy the Cauchy-Riemann equations.]
:::

::: solution
Write
\[
F(x,y)=(p(x,y),q(x,y)),
\]
where $F$ is holomorphic, and let $u$ be harmonic on the target of $F$. Put $v=u\circ F$. By the two-variable chain rule,
\[
\begin{aligned}
\Delta v
={}&u_{pp}(p_x^2+p_y^2)
+2u_{pq}(p_xq_x+p_yq_y)
+u_{qq}(q_x^2+q_y^2)\\
&+u_p\Delta p+u_q\Delta q.
\end{aligned}
\]
Because $F$ is holomorphic, the Cauchy--Riemann equations give
\[
p_x=q_y,\qquad p_y=-q_x.
\]
Hence
\[
p_xq_x+p_yq_y=0,
\qquad
p_x^2+p_y^2=q_x^2+q_y^2=|F'|^2.
\]
Moreover the real and imaginary parts $p,q$ of a holomorphic function are harmonic, so $\Delta p=\Delta q=0$. Therefore
\[
\Delta(u\circ F)
=|F'|^2(u_{pp}+u_{qq})\circ F
=|F'|^2(\Delta u)\circ F=0.
\]
Thus $u\circ F$ is harmonic.
:::
