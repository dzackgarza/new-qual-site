---
schema: qual/card@1
id: P-RASP22G
kind: problem
title: "Distributional derivatives of f(|x|)"
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
  note: Checked against Problem 7 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
1. Compute the 2nd and 3rd distributional derivatives of $f(|x|)$, namely find the expressions of $\frac{d^2}{dx^2}f(|x|)$ and $\frac{d^3}{dx^3}f(|x|)$ in terms of locally integrable functions or measures and their derivatives, where $x \in \mathbb{R}$ and $f \in C^n(\overline{\mathbb{R}}_+)$ with $n \geq 3$.
   (Hint: You may express your answers in terms of $f$, its derivatives and the Delta measure.)

2. Find a formula for the $n$-th distributional derivative of $f(|x|)$.
:::

::: solution
Let
\[
F(x):=f(|x|).
\]
For $x\ne0$,
\[
F^{(k)}(x)=\operatorname{sgn}(x)^k f^{(k)}(|x|).
\]
Thus the one-sided limits at the origin satisfy
\[
F^{(k)}(0+)=f^{(k)}(0),
\qquad
F^{(k)}(0-)=(-1)^k f^{(k)}(0),
\]
so the jump of the piecewise classical $k$th derivative is
\[
[F^{(k)}]_0
:=F^{(k)}(0+)-F^{(k)}(0-)
=(1-(-1)^k)f^{(k)}(0).
\]
Hence this jump is zero for even $k$ and equals $2f^{(k)}(0)$ for odd $k$.

For a piecewise $C^n$ function with a single interface at $0$, repeated distributional differentiation gives
\[
D^nF
=F^{(n)}_{\rm pw}
+\sum_{k=0}^{n-1}[F^{(n-1-k)}]_0\,\delta_0^{(k)}.
\]
Since $F$ itself is continuous, the term involving $[F]_0$ is zero. Substituting the jumps above yields
\[
\boxed{
D^nF
=\operatorname{sgn}(x)^n f^{(n)}(|x|)
+2\sum_{j=0}^{\lfloor (n-2)/2\rfloor}
 f^{(2j+1)}(0)\,
 \delta_0^{(n-2j-2)}.
}
\]
Here the first term denotes the locally integrable function defined away from the origin, with any value assigned at $0$, and $\delta_0^{(r)}$ is the $r$th distributional derivative of the Dirac mass at $0$.

In particular,
\[
\boxed{
D^2F=f''(|x|)+2f'(0)\delta_0,
}
\]
and
\[
\boxed{
D^3F=\operatorname{sgn}(x)f'''(|x|)+2f'(0)\delta_0'.
}
\]
These are the requested second and third distributional derivatives, and the displayed formula gives the general $n$th derivative.
:::
