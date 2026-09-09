---
schema: qual/card@1
id: P-RASP15H
kind: problem
title: "Distributional n-th derivative of f(|x|)"
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
  date: 2026-09-08
  note: Checked against Problem 8 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f$ be a $C^n$ function on $[0, +\infty)$.
Compute the distributional $n$-th derivative of $g(x) = f(|x|)$ (which is viewed as a distribution on $\mathbb{R}$). You may express your answer in terms of the delta distribution.

Hint: You may use induction on $n$ to prove the general formula which you may guess after working out the answer for $n = 1, 2, 3, \ldots$
:::

::: solution
<1>1. Record the jump formula for a piecewise smooth function.
::: proof
If $h$ is $C^1$ away from $0$ and has one-sided limits at $0$, then its distributional derivative is
\[
Dh=h'_{\mathrm{reg}}+[h]_0\,\delta_0,
\]
where
\[
[h]_0:=h(0+)-h(0-)
\]
and $h'_{\mathrm{reg}}$ is the ordinary derivative on $(-\infty,0)\cup(0,\infty)$.

Indeed, integrating by parts separately on the two half-lines against a test function $\varphi$ gives
\[
-\int h\varphi'
=\int h'_{\mathrm{reg}}\varphi+[h]_0\varphi(0).
\]
:::

<1>2. Compute the ordinary derivatives away from the origin and their jumps.
::: proof
For $x>0$,
\[
g(x)=f(x),
\]
while for $x<0$,
\[
g(x)=f(-x).
\]
Hence for every $m\le n$ and $x\ne0$,
\[
g^{(m)}_{\mathrm{reg}}(x)=
\begin{cases}
f^{(m)}(x),&x>0,\\
(-1)^m f^{(m)}(-x),&x<0.
\end{cases}
\]
Equivalently,
\[
g^{(m)}_{\mathrm{reg}}(x)
=\operatorname{sgn}(x)^m f^{(m)}(|x|).
\]

The jump at $0$ is therefore
\[
\begin{aligned}
[g^{(m)}_{\mathrm{reg}}]_0
&=f^{(m)}(0)-(-1)^m f^{(m)}(0)\\
&=\bigl(1-(-1)^m\bigr)f^{(m)}(0).
\end{aligned}
\]
Thus the jump is zero for even $m$ and equals
\[
2f^{(m)}(0)
\]
for odd $m$.
:::

<1>3. Iterate the jump formula.
::: proof
For a piecewise $C^n$ function, repeated use of Step 1 gives
\[
D^n g
=g^{(n)}_{\mathrm{reg}}
+\sum_{j=0}^{n-1}
[g^{(n-1-j)}_{\mathrm{reg}}]_0\,\delta_0^{(j)}.
\]
Substituting the jumps from Step 2 yields
\[
D^n g
=\operatorname{sgn}(x)^n f^{(n)}(|x|)
+\sum_{j=0}^{n-1}
\bigl(1-(-1)^{n-1-j}\bigr)
f^{(n-1-j)}(0)\,\delta_0^{(j)}.
\]

Only odd derivative orders of $f$ contribute. Writing those orders as $2r+1$, we obtain the compact form
\[
\boxed{
D^n(f(|x|))
=\operatorname{sgn}(x)^n f^{(n)}(|x|)
+2\sum_{r=0}^{\lfloor(n-2)/2\rfloor}
f^{(2r+1)}(0)\,
\delta_0^{(n-2r-2)}.}
\]
For $n=1$ the sum is empty.

For example,
\[
Dg=\operatorname{sgn}(x)f'(|x|),
\]
\[
D^2g=f''(|x|)+2f'(0)\delta_0,
\]
and
\[
D^3g=\operatorname{sgn}(x)f^{(3)}(|x|)+2f'(0)\delta_0'.
\]
:::
:::
