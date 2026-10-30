---
schema: qual/card@1
id: P-TRIV-RA57
kind: problem
title: Finite geometric sums $\sum r^ke^{ik\phi}$, $\sum r^k\cos k\phi$ and $\sum r^k\sin k\phi$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 57, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the following series:

(a) $\sum_{k=0}^{n} r^k e^{ik\phi}$, (b) $\sum_{k=0}^{n} r^k\cos k\phi$, (c) $\sum_{k=0}^{n} r^k\sin k\phi$.
:::

::: {.solution}

Put
$$
z=re^{i\phi}.
$$

::: pf

::: {.pf-step #s1-1}

If $z\neq1$, then
$$
\boxed{
\sum_{k=0}^{n}r^ke^{ik\phi}
=
\frac{1-r^{n+1}e^{i(n+1)\phi}}
{1-re^{i\phi}}.
}
$$


::: pf-proof

The sum is
$$
1+z+z^2+\cdots+z^n.
$$
Multiplying by $1-z$ gives
$$
(1-z)(1+z+\cdots+z^n)
=
1-z^{n+1}.
$$
Divide by $1-z$.

:::

:::

::: {.pf-step #s1-2}

Part (a) follows for $z\neq1$.


::: pf-proof

This is step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

Define
$$
D
=
\abs{1-re^{i\phi}}^2
=
1-2r\cos\phi+r^2.
$$


::: pf-proof

Multiply
$$
(1-re^{i\phi})(1-re^{-i\phi})
$$
and use
$$
e^{i\phi}+e^{-i\phi}=2\cos\phi.
$$

:::

:::

::: {.pf-step #s1-4}

Rationalizing the expression in step [](#s1-1){.pf-ref} gives
$$
\sum_{k=0}^{n}r^ke^{ik\phi}
=
\frac{
1-re^{-i\phi}
-
r^{n+1}e^{i(n+1)\phi}
+
r^{n+2}e^{in\phi}
}{D}.
$$


::: pf-proof

Multiply numerator and denominator in step [](#s1-1){.pf-ref} by
$$
1-re^{-i\phi}.
$$
The denominator becomes $D$, and expanding the numerator gives the displayed
expression.

:::

:::

::: {.pf-step #s1-5}

Taking real parts gives
$$
\boxed{
\sum_{k=0}^{n}r^k\cos(k\phi)
=
\frac{
1-r\cos\phi
-
r^{n+1}\cos((n+1)\phi)
+
r^{n+2}\cos(n\phi)
}{
1-2r\cos\phi+r^2
}.
}
$$


::: pf-proof

By Euler's formula,
$$
\operatorname{Re}(r^ke^{ik\phi})
=
r^k\cos(k\phi).
$$
Take real parts of step [](#s1-4){.pf-ref} term by term.

:::

:::

::: {.pf-step #s1-6}

Part (b) follows for $z\neq1$.


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Taking imaginary parts of step [](#s1-4){.pf-ref} gives
$$
\boxed{
\sum_{k=0}^{n}r^k\sin(k\phi)
=
\frac{
r\sin\phi
-
r^{n+1}\sin((n+1)\phi)
+
r^{n+2}\sin(n\phi)
}{
1-2r\cos\phi+r^2
}.
}
$$


::: pf-proof

The imaginary parts in the numerator of step [](#s1-4){.pf-ref} are
$$
r\sin\phi,
\qquad
-r^{n+1}\sin((n+1)\phi),
\qquad
r^{n+2}\sin(n\phi).
$$
Also
$$
\operatorname{Im}(r^ke^{ik\phi})
=
r^k\sin(k\phi).
$$

:::

:::

::: {.pf-step #s1-8}

Part (c) follows for $z\neq1$.


::: pf-proof

This is step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

If
$$
re^{i\phi}=1,
$$
then
$$
\boxed{
\sum_{k=0}^{n}r^ke^{ik\phi}=n+1,
}
$$
$$
\boxed{
\sum_{k=0}^{n}r^k\cos(k\phi)=n+1,
}
$$
and
$$
\boxed{
\sum_{k=0}^{n}r^k\sin(k\phi)=0.
}
$$


::: pf-proof

If $re^{i\phi}=1$, then every factor
$$
r^ke^{ik\phi}
=
(re^{i\phi})^k
=1.
$$
Thus the complex sum consists of $n+1$ copies of $1$, and its real and
imaginary parts are $n+1$ and $0$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref}, [](#s1-6){.pf-ref}, and [](#s1-8){.pf-ref}, and [](#s1-9){.pf-ref} give all three finite sums in every case.

:::

:::

:::
