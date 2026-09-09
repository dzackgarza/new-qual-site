---
schema: qual/card@1
id: P-RASP23F
kind: problem
title: "Interpolation of weak-type bounds"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $1 \leq p < \infty$.
Recall that $\lambda_g(\alpha) = \mu(\{x : |g(x)| > \alpha\})$.
Assume that $T$ is a linear operator from $L^p$ into $L^{q_1}$ and $L^{q_2}$ with $1 \leq q_1 < q_2$ such that $\lambda_{Tf}(\alpha) \leq (C_1 \|f\|_p / \alpha)^{q_1}$ and $\lambda_{Tf}(\alpha) \leq (C_2 \|f\|_p / \alpha)^{q_2}$.
Prove that for any $q_1 < q < q_2$, $\|Tf\|_q \leq C_q \|f\|_p$.
Here $C_q$ depends on $q, q_1, q_2$ and $C_1, C_2$.
:::


::: solution
Let
\[
A:=C_1\|f\|_p,
\qquad
B:=C_2\|f\|_p.
\]
If $A=0$ or $B=0$, one of the weak-type estimates forces $Tf=0$ almost everywhere, so the conclusion is immediate. Assume $A,B>0$.

The two hypotheses give
\[
\lambda_{Tf}(\alpha)
\le
\min\left\{
\left(\frac A\alpha\right)^{q_1},
\left(\frac B\alpha\right)^{q_2}
\right\}.
\]
Let $\alpha_0>0$ be the point where the two bounds agree:
\[
\alpha_0
:=\left(\frac{B^{q_2}}{A^{q_1}}\right)^{1/(q_2-q_1)}.
\]
For $0<\alpha\le\alpha_0$, the $q_1$ bound is the smaller one, while for $\alpha\ge\alpha_0$, the $q_2$ bound is smaller.

Using the layer-cake formula for the $L^q$ norm,
\[
\|Tf\|_q^q
=q\int_0^\infty \alpha^{q-1}\lambda_{Tf}(\alpha)\,d\alpha.
\]
Therefore
\[
\begin{aligned}
\|Tf\|_q^q
&\le
qA^{q_1}\int_0^{\alpha_0}\alpha^{q-q_1-1}\,d\alpha
+qB^{q_2}\int_{\alpha_0}^\infty\alpha^{q-q_2-1}\,d\alpha\\
&=
\frac{q}{q-q_1}A^{q_1}\alpha_0^{q-q_1}
+
\frac{q}{q_2-q}B^{q_2}\alpha_0^{q-q_2}.
\end{aligned}
\]
Both integrals converge because
\[
q_1<q<q_2.
\]

Since $A=C_1\|f\|_p$ and $B=C_2\|f\|_p$, the splitting scale is
\[
\alpha_0
=\left(\frac{C_2^{q_2}}{C_1^{q_1}}\right)^{1/(q_2-q_1)}\|f\|_p.
\]
Substituting this into the previous bound shows that
\[
\|Tf\|_q^q\le C_q^q\|f\|_p^q,
\]
where $C_q$ depends only on $q,q_1,q_2,C_1,C_2$. Hence
\[
\boxed{\|Tf\|_q\le C_q\|f\|_p.}
\]
:::
