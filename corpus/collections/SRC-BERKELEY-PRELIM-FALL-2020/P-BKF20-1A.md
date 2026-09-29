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

::: pf

::: {.pf-step #s1}

Integration by parts gives
$$
\int e^{2x}\sin x\,dx
=
-e^{2x}\cos x
+
2\int e^{2x}\cos x\,dx.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

A second integration by parts gives
$$
\int e^{2x}\cos x\,dx
=
e^{2x}\sin x
-
2\int e^{2x}\sin x\,dx.
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{
\int e^{2x}\sin x\,dx
=
\frac{e^{2x}(2\sin x-\cos x)}5+C.
}
$$

::: pf-proof

Substitute step [](#s2){.pf-ref} into step [](#s1){.pf-ref}:
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

:::

::: {.pf-step #s4}

The expression in step [](#s3){.pf-ref} is an antiderivative of
$e^{2x}\sin x$.

::: pf-proof

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

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested indefinite integral, and step [](#s4){.pf-ref}
verifies it.

:::

:::

:::
