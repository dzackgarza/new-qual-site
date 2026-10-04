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
Compute the following series: (a) $\sum _ { k = 0 } ^ { n } r ^ { k } e ^ { i k \phi } ,$ (b) $\sum _ { k = 0 } ^ { n } r ^ { k } \cos k \phi ,$ (c) $\sum _ { k = 0 } ^ { n } r ^ { k } \sin k \phi .$
:::

::: {.solution}
Put
$$
z=re^{i\phi}.
$$

<1>1. If $z\neq1$, then
$$
\boxed{
\sum_{k=0}^{n}r^ke^{ik\phi}
=
\frac{1-r^{n+1}e^{i(n+1)\phi}}
{1-re^{i\phi}}.
}
$$

::: {.proof}
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

<1>2. Part (a) follows for $z\neq1$.

::: {.proof}
This is step <1>1.
:::

<1>3. Define
$$
D
=
|1-re^{i\phi}|^2
=
1-2r\cos\phi+r^2.
$$

::: {.proof}
Multiply
$$
(1-re^{i\phi})(1-re^{-i\phi})
$$
and use
$$
e^{i\phi}+e^{-i\phi}=2\cos\phi.
$$
:::

<1>4. Rationalizing the expression in step <1>1 gives
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

::: {.proof}
Multiply numerator and denominator in step <1>1 by
$$
1-re^{-i\phi}.
$$
The denominator becomes $D$, and expanding the numerator gives the displayed
expression.
:::

<1>5. Taking real parts gives
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

::: {.proof}
By Euler's formula,
$$
\operatorname{Re}(r^ke^{ik\phi})
=
r^k\cos(k\phi).
$$
Take real parts of step <1>4 term by term.
:::

<1>6. Part (b) follows for $z\neq1$.

::: {.proof}
This is step <1>5.
:::

<1>7. Taking imaginary parts of step <1>4 gives
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

::: {.proof}
The imaginary parts in the numerator of step <1>4 are
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

<1>8. Part (c) follows for $z\neq1$.

::: {.proof}
This is step <1>7.
:::

<1>9. If
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

::: {.proof}
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

<1>10. Q.E.D.

::: {.proof}
Steps <1>2, <1>6, <1>8, and <1>9 give all three finite sums in every case.
:::
:::
