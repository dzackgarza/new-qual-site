---
schema: qual/card@1
id: P-BKF99-8
kind: problem
title: The contour integral $\frac1{2\pi i}\int_{|z|=1}\frac{(z+2)^2}{z^2(2z-1)}\,dz$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Computed the residues at the double pole 0 and simple pole 1/2 and summed
    them using the residue theorem.
---

::: {.problem}
Evaluate
\[
I=\frac1{2\pi i}\int_{|z|=1}\frac{(z+2)^2}{z^2(2z-1)}\,dz,
\]
where the circle is oriented counterclockwise.
:::

::: {.solution}

Set
$$
F(z)=\frac{(z+2)^2}{z^2(2z-1)}.
$$

::: pf

::: {.pf-step #poles-identified}
The poles of $F$ inside $\abs{z}=1$ are a double pole at $0$ and a
simple pole at $1/2$.

::: pf-proof
The denominator is $z^2(2z-1)$. Its zeros are $0$, with multiplicity $2$,
and $1/2$, with multiplicity $1$. The numerator is nonzero at both points,
and both have modulus less than $1$.
:::

:::

::: {.pf-step #residue-at-zero}
$$
\operatorname{Res}(F,0)=-12.
$$

::: pf-proof
For the double pole at $0$,
$$
\operatorname{Res}(F,0)
=
\left.
\frac{d}{dz}
\left(\frac{(z+2)^2}{2z-1}\right)
\right|_{z=0}.
$$
Differentiating gives
$$
\frac{d}{dz}
\left(\frac{(z+2)^2}{2z-1}\right)
=
\frac{2(z+2)(2z-1)-2(z+2)^2}{(2z-1)^2}
=
\frac{2(z+2)(z-3)}{(2z-1)^2}.
$$
At $z=0$ this equals $-12$.
:::

:::

::: {.pf-step #residue-at-half}
$$
\operatorname{Res}(F,1/2)=25.
$$

::: pf-proof
Since $2z-1=2(z-1/2)$,
$$
\operatorname{Res}(F,1/2)
=
\left.
\frac{(z+2)^2}{2z^2}
\right|_{z=1/2}
=
\frac{(5/2)^2}{2(1/2)^2}
=25.
$$
:::

:::

::: {.pf-step #integral-value}
$$
I=\boxed{13}.
$$

::: pf-proof
By the residue theorem and steps [](#poles-identified){.pf-ref}, [](#residue-at-zero){.pf-ref} and [](#residue-at-half){.pf-ref},
$$
I
=
\frac{1}{2\pi i}\int_{\abs{z}=1}F(z)\,dz
=
\operatorname{Res}(F,0)+\operatorname{Res}(F,1/2)
=
-12+25
=13.
$$
:::

:::

::: pf-qed
Step [](#integral-value){.pf-ref} gives the requested value.
:::

:::

:::
