---
schema: qual/card@1
id: P-KPLQU
kind: problem
title: Green's theorem for rectangles and Cauchy's theorem on a rectangle
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Cauchy Integral Theorem
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
State and prove Green's Theorem for rectangles.
Use this to prove Cauchy's Theorem for functions that are analytic in a rectangle.
:::

::: {.solution}
Let
\[
R=[a,b]\times[c,d]
\]
and let $P,Q$ have continuous first partial derivatives on a neighborhood of
$R$. Green's theorem for the positively oriented boundary of the rectangle is
\[
\boxed{
\int_{\partial R}P\,dx+Q\,dy
=\iint_R(Q_x-P_y)\,dA.}
\]

For a rectangle this follows directly from the one-variable fundamental theorem
of calculus. Indeed, summing the integrals on the horizontal sides gives
\[
\int_a^b P(x,c)\,dx-\int_a^b P(x,d)\,dx
=-\int_a^b\int_c^d P_y(x,y)\,dy\,dx,
\]
while summing the integrals on the vertical sides gives
\[
\int_c^d Q(b,y)\,dy-\int_c^d Q(a,y)\,dy
=\int_c^d\int_a^b Q_x(x,y)\,dx\,dy.
\]
Adding and using Fubini yields the displayed formula.

Now let $f=u+iv$ be holomorphic on a neighborhood of $R$. Then
\[
f(z)\,dz=(u+iv)(dx+i\,dy)
=(u\,dx-v\,dy)+i(v\,dx+u\,dy).
\]
Applying Green's theorem to the real part gives
\[
\int_{\partial R}(u\,dx-v\,dy)
=\iint_R(-v_x-u_y)\,dA=0,
\]
because the Cauchy--Riemann equation $v_x=-u_y$ holds. For the imaginary part,
\[
\int_{\partial R}(v\,dx+u\,dy)
=\iint_R(u_x-v_y)\,dA=0
\]
by $u_x=v_y$. Therefore
\[
\boxed{\int_{\partial R}f(z)\,dz=0,}
\]
which is Cauchy's theorem for a rectangle.
:::
