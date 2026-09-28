---
schema: qual/card@1
id: P-BKF00-4
kind: problem
title: The integral $\frac1{2\pi i}\int_{|z|=1}1/\sin(4z)\,dz$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    The poles inside the unit circle are 0 and plus or minus pi/4; their
    residues sum to -1/4, which is the normalized contour integral.
---

::: {.problem}
Evaluate
\[
\frac{1}{2\pi i}\int_{|z|=1}\frac{dz}{\sin(4z)},
\]
where the unit circle is oriented counterclockwise.
:::

::: {.solution}
<1>1. The poles of $1/\sin(4z)$ in the open unit disk are precisely
$$
-\frac{\pi}{4},\qquad 0,\qquad \frac{\pi}{4},
$$
and all three are simple.

::: {.proof}
The zeros of $\sin(4z)$ are
$$
z=\frac{k\pi}{4},\qquad k\in\ZZ.
$$
For $k=0,\pm1$ one has $\abs{k}\pi/4<1$, whereas for $\abs{k}\ge2$,
$$
\frac{\abs{k}\pi}{4}\ge\frac{\pi}{2}>1.
$$
Thus exactly $k=-1,0,1$ give zeros in the open unit disk. Moreover,
$$
\frac{d}{dz}\sin(4z)=4\cos(4z),
$$
and at $z=k\pi/4$ this derivative is $4(-1)^k\neq0$. Hence these zeros,
and therefore the corresponding poles of $1/\sin(4z)$, are simple. No zero
lies on $\abs{z}=1$.
:::

<1>2. The sum of the residues inside the unit circle is
$$
\sum_{\abs{z_0}<1}\Res_{z=z_0}\frac{1}{\sin(4z)}=-\frac14.
$$

::: {.proof}
At a simple zero $z_0$ of $\sin(4z)$,
$$
\Res_{z=z_0}\frac{1}{\sin(4z)}
=\frac{1}{4\cos(4z_0)}.
$$
Thus step <1>1 gives
$$
\begin{aligned}
\Res_{z=0}\frac{1}{\sin(4z)}&=\frac14,\\
\Res_{z=\pi/4}\frac{1}{\sin(4z)}&=-\frac14,\\
\Res_{z=-\pi/4}\frac{1}{\sin(4z)}&=-\frac14.
\end{aligned}
$$
Their sum is $-1/4$.
:::

<1>3. The value of the integral is
$$
\boxed{-\frac14}.
$$

::: {.proof}
By the residue theorem and step <1>2,
$$
\frac{1}{2\pi i}\int_{\abs{z}=1}\frac{dz}{\sin(4z)}
=\sum_{\abs{z_0}<1}\Res_{z=z_0}\frac{1}{\sin(4z)}
=-\frac14.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value.
:::
:::
