---
schema: qual/card@1
id: P-GREPT-08
kind: problem
title: "Upper limits $b$ with $\\int_0^b\\tan x\\,dx=2$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 8 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $\int_0^b \tan x \, dx = 2$, then $b$ could equal

(A) $\arccos 2$
(B) $\arccos(2e)$
(C) $\operatorname{arcsec} 2$
(D) $\operatorname{arcsec}^2 e$
(E) $\operatorname{arcsec}(e^2)$
:::

::: pf

::: pf-step

On every interval containing $0$ on which $\tan x$ is continuous,
$$
\int_0^b\tan x\,dx=-\log(\cos b).
$$


::: pf-proof

Since
$$
\tan x=\frac{\sin x}{\cos x},
$$
the substitution $u=\cos x$, $du=-\sin x\,dx$, gives
$$
\int\tan x\,dx=-\log|\cos x|+C.
$$
If the definite integral from $0$ to $b$ is proper, the interval between
$0$ and $b$ contains no zero of $\cos x$, so it lies in
$(-\pi/2,\pi/2)$ and $\cos x>0$ there. Hence
$$
\int_0^b\tan x\,dx
=\left[-\log(\cos x)\right]_0^b
=-\log(\cos b).
$$

:::

:::

::: pf-step

If $b=\operatorname{arcsec}(e^2)$, then
$$
\int_0^b\tan x\,dx=2.
$$


::: pf-proof

For the principal inverse secant,
$b=\operatorname{arcsec}(e^2)$ lies in $(0,\pi/2)$ and satisfies
$$
\sec b=e^2,
\qquad\text{so}\qquad
\cos b=e^{-2}.
$$
Applying step <1>1 gives
$$
\int_0^b\tan x\,dx
=-\log(e^{-2})=2.
$$

:::

:::

::: pf-step

Therefore
$$
b=\boxed{\operatorname{arcsec}(e^2)}
$$
is a possible value, so the answer is (E).


::: pf-proof

Step <1>2 verifies directly that this choice satisfies the required integral
equation.

:::

:::

::: pf-qed

Step <1>3 gives the requested choice.

:::

:::
