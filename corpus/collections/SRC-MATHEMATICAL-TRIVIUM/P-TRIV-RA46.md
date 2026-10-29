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

::: pf

::: {.pf-step #s1-1}

The inverse transform is
$$
f(x)
=
-\frac1\pi
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{k e^{ikx}}{k^2+a^2}
\,dk.
$$


::: pf-proof

Substitute the given $\widetilde f(k)$ into the inverse-transform formula from
the remark.

:::

:::

::: pf-step

Suppose $x>0$. Close the contour in the upper half-plane. The only pole
inside is
$$
k=ia.
$$


::: pf-proof

The poles of
$$
\frac{k e^{ikx}}{k^2+a^2}
$$
are $k=\pm ia$. For $x>0$, the factor $e^{ikx}$ decays on the upper
semicircle, so Jordan's lemma applies there.

:::

:::

::: pf-step

The residue at $k=ia$ is
$$
\frac12e^{-ax}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-4}

Therefore, for $x>0$,
$$
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{k e^{ikx}}{k^2+a^2}
\,dk
=
i\pi e^{-ax}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-5}

Hence for $x>0$,
$$
f(x)=-i e^{-ax}.
$$


::: pf-proof

Substitute step [](#s1-4){.pf-ref} into step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

Suppose $x<0$. Close the contour in the lower half-plane. The only pole
inside is
$$
k=-ia.
$$


::: pf-proof

For $x<0$, the factor $e^{ikx}$ decays on the lower semicircle. The contour is
clockwise, so the residue theorem contributes a factor $-2\pi i$.

:::

:::

::: pf-step

The residue at $k=-ia$ is
$$
\frac12e^{ax}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-8}

Therefore, for $x<0$,
$$
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{k e^{ikx}}{k^2+a^2}
\,dk
=
-i\pi e^{ax}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-9}

Hence for $x<0$,
$$
f(x)=i e^{ax}.
$$


::: pf-proof

Substitute step [](#s1-8){.pf-ref} into step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

At $x=0$, the principal value is zero.


::: pf-proof

The integrand
$$
\frac{k}{k^2+a^2}
$$
is odd, so its symmetric principal value over $\RR$ vanishes.

:::

:::

::: {.pf-step #s1-11}

Combining the cases gives
$$
\boxed{
f(x)
=
-i\operatorname{sgn}(x)e^{-a|x|},
}
$$
with the convention $\operatorname{sgn}(0)=0$.


::: pf-proof

For $x>0$, this reproduces step [](#s1-5){.pf-ref}. For $x<0$,
$$
-i\operatorname{sgn}(x)e^{-a|x|}
=
i e^{ax},
$$
which is step [](#s1-9){.pf-ref}. Step [](#s1-10){.pf-ref} handles $x=0$.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required inverse Fourier image.

:::

:::

:::
