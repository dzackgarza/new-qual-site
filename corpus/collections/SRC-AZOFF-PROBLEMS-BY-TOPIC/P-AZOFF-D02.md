---
schema: qual/card@1
id: P-AZOFF-D02
kind: problem
title: Cauchy's theorem for rectangles via Green's theorem
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Proved Green's theorem on a rectangle directly by pairing the two
    horizontal and the two vertical boundary integrals and applying the
    one-variable fundamental theorem of calculus. Applied the result to the
    real and imaginary parts of f dz; the two Green integrands vanish by the
    Cauchy-Riemann equations. The source compilation contains no worked
    solution.
---

::: {.problem}
State and prove Green’s Theorem for rectangles.
Then use it to prove Cauchy’s Theorem for functions analytic in a rectangle.
:::

::: {.solution}
Let
$$
R=[a,b]\times[c,d]\subseteq\RR^2
$$
and orient $\partial R$ counterclockwise.

::: pf

::: {.pf-step #s1}

Green's theorem for a rectangle states that if $P,Q$ have continuous
first partial derivatives on a neighborhood of $R$, then
$$
\boxed{
\int_{\partial R}P\,dx+Q\,dy
=
\iint_R
\left(
\frac{\partial Q}{\partial x}
-
\frac{\partial P}{\partial y}
\right)\,dA.
}
$$

:::

::: {.pf-step #s2}

The contribution of the two horizontal sides of $\partial R$ is
$$
-\iint_R P_y\,dA.
$$

::: pf-proof

The bottom side is traversed from $(a,c)$ to $(b,c)$ and the top side from
$(b,d)$ to $(a,d)$. Since $dy=0$ on both sides, their total contribution is
$$
\begin{aligned}
&\int_a^b P(x,c)\,dx
+
\int_b^a P(x,d)\,dx\\
&\qquad=
\int_a^b\bigl(P(x,c)-P(x,d)\bigr)\,dx\\
&\qquad=
-\int_a^b\int_c^d P_y(x,y)\,dy\,dx,
\end{aligned}
$$
where the last equality is the fundamental theorem of calculus in the
$y$-variable. This is
$$
-\iint_RP_y\,dA.
$$

:::

:::

::: {.pf-step #s3}

The contribution of the two vertical sides of $\partial R$ is
$$
\iint_R Q_x\,dA.
$$

::: pf-proof

The right side is traversed from $(b,c)$ to $(b,d)$ and the left side from
$(a,d)$ to $(a,c)$. Since $dx=0$ on both sides, their total contribution is
$$
\begin{aligned}
&\int_c^d Q(b,y)\,dy
+
\int_d^c Q(a,y)\,dy\\
&\qquad=
\int_c^d\bigl(Q(b,y)-Q(a,y)\bigr)\,dy\\
&\qquad=
\int_c^d\int_a^b Q_x(x,y)\,dx\,dy,
\end{aligned}
$$
by the fundamental theorem of calculus in the $x$-variable. This is
$$
\iint_RQ_x\,dA.
$$

:::

:::

::: {.pf-step #s4}

Green's theorem in step [](#s1){.pf-ref} holds.

::: pf-proof

Adding the horizontal contribution from step [](#s2){.pf-ref} and the vertical
contribution from step [](#s3){.pf-ref} gives
$$
\int_{\partial R}P\,dx+Q\,dy
=
\iint_R(Q_x-P_y)\,dA.
$$
This is the asserted formula.

:::

:::

::: {.pf-step #s5}

Let
$$
f=u+iv
$$
be analytic on an open neighborhood of $R$. Then
$$
u_x=v_y,
\qquad
u_y=-v_x
$$
on $R$.

::: pf-proof

The real and imaginary parts of an analytic function satisfy the
Cauchy--Riemann equations. In particular, the first partial derivatives used
below are continuous on the rectangle, so Green's theorem applies.

:::

:::

::: {.pf-step #s6}

The real part of
$$
\int_{\partial R}f(z)\,dz
$$
is zero.

::: pf-proof

Since
$$
dz=dx+i\,dy,
$$
one has
$$
f(z)\,dz
=
(u\,dx-v\,dy)
+
i(v\,dx+u\,dy).
$$
Hence the real part is
$$
\int_{\partial R}u\,dx-v\,dy.
$$
Apply Green's theorem with
$$
P=u,
\qquad
Q=-v.
$$
Then
$$
Q_x-P_y
=
-v_x-u_y
=
0
$$
by step [](#s5){.pf-ref}. Therefore
$$
\operatorname{Re}
\int_{\partial R}f(z)\,dz
=
0.
$$

:::

:::

::: {.pf-step #s7}

The imaginary part of
$$
\int_{\partial R}f(z)\,dz
$$
is zero.

::: pf-proof

From the expansion in step [](#s6){.pf-ref}, the imaginary part is
$$
\int_{\partial R}v\,dx+u\,dy.
$$
Apply Green's theorem with
$$
P=v,
\qquad
Q=u.
$$
Then
$$
Q_x-P_y
=
u_x-v_y
=
0
$$
by step [](#s5){.pf-ref}. Hence
$$
\operatorname{Im}
\int_{\partial R}f(z)\,dz
=
0.
$$

:::

:::

::: {.pf-step #s8}

Cauchy's theorem for a rectangle holds:
$$
\boxed{
\int_{\partial R}f(z)\,dz=0.
}
$$

::: pf-proof

Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} show that both the real and imaginary parts of the complex
integral vanish.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} state and prove Green's theorem for rectangles, and steps
[](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} use it to prove Cauchy's theorem on a rectangle.

:::

:::

:::
