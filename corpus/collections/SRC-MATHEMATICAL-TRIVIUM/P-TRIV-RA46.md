---
schema: qual/card@1
id: P-TRIV-RA46
kind: problem
title: Inverse Fourier transform of $-\frac1\pi\frac{k}{a^2+k^2}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 46, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate the inverse Fourier image f (x) of the function $\tilde { f } ( k ) = - \frac { 1 } { \pi } \frac { k } { a ^ { 2 } + k ^ { 2 } } .$
:::

::: {.remark}
Use the Fourier convention fixed in Problem 45:
$$
\widetilde f(k)
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
f(x)e^{-ikx}
\,dx,
\qquad
f(x)
=
\int_{-\infty}^{\infty}
\widetilde f(k)e^{ikx}
\,dk.
$$
The parameter is taken to satisfy $a>0$, consistent with the adjacent
one-sided exponential problem. Since $\widetilde f(k)=O(1/k)$, the inverse
integral is interpreted as an oscillatory principal value.
:::

::: {.solution}
<1>1. The inverse transform is
$$
f(x)
=
-\frac1\pi
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{k e^{ikx}}{k^2+a^2}
\,dk.
$$

::: {.proof}
Substitute the given $\widetilde f(k)$ into the inverse-transform formula from
the remark.
:::

<1>2. Suppose $x>0$. Close the contour in the upper half-plane. The only pole
inside is
$$
k=ia.
$$

::: {.proof}
The poles of
$$
\frac{k e^{ikx}}{k^2+a^2}
$$
are $k=\pm ia$. For $x>0$, the factor $e^{ikx}$ decays on the upper
semicircle, so Jordan's lemma applies there.
:::

<1>3. The residue at $k=ia$ is
$$
\frac12e^{-ax}.
$$

::: {.proof}
Since
$$
k^2+a^2=(k-ia)(k+ia),
$$
one has
$$
\begin{aligned}
\operatorname{Res}_{k=ia}
\frac{k e^{ikx}}{k^2+a^2}
&=
\frac{ia\,e^{i(ia)x}}{2ia}\\
&=
\frac12e^{-ax}.
\end{aligned}
$$
:::

<1>4. Therefore, for $x>0$,
$$
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{k e^{ikx}}{k^2+a^2}
\,dk
=
i\pi e^{-ax}.
$$

::: {.proof}
The residue theorem gives
$$
2\pi i
\left(
\frac12e^{-ax}
\right)
=
i\pi e^{-ax}.
$$
The upper semicircle contribution tends to zero.
:::

<1>5. Hence for $x>0$,
$$
f(x)=-i e^{-ax}.
$$

::: {.proof}
Substitute step <1>4 into step <1>1.
:::

<1>6. Suppose $x<0$. Close the contour in the lower half-plane. The only pole
inside is
$$
k=-ia.
$$

::: {.proof}
For $x<0$, the factor $e^{ikx}$ decays on the lower semicircle. The contour is
clockwise, so the residue theorem contributes a factor $-2\pi i$.
:::

<1>7. The residue at $k=-ia$ is
$$
\frac12e^{ax}.
$$

::: {.proof}
Directly,
$$
\operatorname{Res}_{k=-ia}
\frac{k e^{ikx}}{k^2+a^2}
=
\frac{-ia\,e^{i(-ia)x}}{-2ia}
=
\frac12e^{ax}.
$$
:::

<1>8. Therefore, for $x<0$,
$$
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{k e^{ikx}}{k^2+a^2}
\,dk
=
-i\pi e^{ax}.
$$

::: {.proof}
The clockwise residue theorem gives
$$
-2\pi i
\left(
\frac12e^{ax}
\right)
=
-i\pi e^{ax}.
$$
:::

<1>9. Hence for $x<0$,
$$
f(x)=i e^{ax}.
$$

::: {.proof}
Substitute step <1>8 into step <1>1.
:::

<1>10. At $x=0$, the principal value is zero.

::: {.proof}
The integrand
$$
\frac{k}{k^2+a^2}
$$
is odd, so its symmetric principal value over $\mathbb R$ vanishes.
:::

<1>11. Combining the cases gives
$$
\boxed{
f(x)
=
-i\operatorname{sgn}(x)e^{-a|x|},
}
$$
with the convention $\operatorname{sgn}(0)=0$.

::: {.proof}
For $x>0$, this reproduces step <1>5. For $x<0$,
$$
-i\operatorname{sgn}(x)e^{-a|x|}
=
i e^{ax},
$$
which is step <1>9. Step <1>10 handles $x=0$.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 is the required inverse Fourier image.
:::
:::
