---
schema: qual/card@1
id: P-BKF20-1A
kind: problem
title: Antiderivative of $e^{2x}\sin x$
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 solution: two integrations
    by parts give the stated antiderivative, and direct differentiation
    recovers e^(2x) sin x.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both integration-by-parts identities, the algebra solving for the
    original integral, and the derivative of the final expression.
---

::: {.problem}
Find the indefinite integral
\[
\int e^{2x}\sin x\,dx.
\]
:::

::: {.solution}
<1>1. Integration by parts gives
$$
\int e^{2x}\sin x\,dx
=
-e^{2x}\cos x
+
2\int e^{2x}\cos x\,dx.
$$

::: {.proof}
Take
$$
u=e^{2x},
\qquad
dv=\sin x\,dx.
$$
Then
$$
du=2e^{2x}\,dx,
\qquad
v=-\cos x.
$$
The integration-by-parts formula
$$
\int u\,dv=uv-\int v\,du
$$
gives the displayed identity, with the arbitrary additive constant
understood.
:::

<1>2. A second integration by parts gives
$$
\int e^{2x}\cos x\,dx
=
e^{2x}\sin x
-
2\int e^{2x}\sin x\,dx.
$$

::: {.proof}
Now take
$$
u=e^{2x},
\qquad
dv=\cos x\,dx.
$$
Then
$$
du=2e^{2x}\,dx,
\qquad
v=\sin x,
$$
and integration by parts gives the claim.
:::

<1>3. Therefore
$$
\boxed{
\int e^{2x}\sin x\,dx
=
\frac{e^{2x}(2\sin x-\cos x)}5+C.
}
$$

::: {.proof}
Substitute step <1>2 into step <1>1:
$$
\begin{aligned}
\int e^{2x}\sin x\,dx
&=
-e^{2x}\cos x
+
2\left(
e^{2x}\sin x
-
2\int e^{2x}\sin x\,dx
\right).
\end{aligned}
$$
Moving the last integral to the left gives
$$
5\int e^{2x}\sin x\,dx
=
e^{2x}(2\sin x-\cos x)+C,
$$
where the arbitrary constants from the preceding indefinite
integrations have been absorbed into one constant. Dividing by $5$
gives the stated formula.
:::

<1>4. The expression in step <1>3 is an antiderivative of
$e^{2x}\sin x$.

::: {.proof}
Differentiating its nonconstant part gives
$$
\begin{aligned}
\frac{d}{dx}
\left[
\frac{e^{2x}(2\sin x-\cos x)}5
\right]
&=
\frac{e^{2x}}5
\left[
2(2\sin x-\cos x)
+
2\cos x+\sin x
\right]\\
&=
e^{2x}\sin x.
\end{aligned}
$$
Thus the formula indeed gives all antiderivatives after adding the
arbitrary constant $C$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 gives the requested indefinite integral, and step <1>4
verifies it.
:::
:::
