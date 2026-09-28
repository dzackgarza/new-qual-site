---
schema: qual/card@1
id: E-YZUOC
kind: problem
title: Residue at a pole of order $m$, and $\oint_C e^\tau/(\tau^2+\pi^2)^2\,d\tau$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
  - Contour Integration
relations: []
review: draft
---

::: {.exercise}
a.
Let $F$ be an analytic function inside and on a simple closed curve $C$, except for a pole of order $m\geq 1$ at $z=a$ inside $C$.
Prove that

$$\frac{1}{2 \pi i}\oint_{C} F(\tau) d\tau =
\lim_{\tau\rightarrow a} \frac{d^{m-1}}{d\tau^{m-1}}\big((\tau-a)^m F(\tau))\big).$$

b.
Evaluate $$\oint_{C}\frac{e^{\tau}}{(\tau^2+\pi^2)^2}d\tau$$
where $C$ is the circle $|z|=4$.
:::

::: {.solution}
Part (a) is missing the standard factor $1/(m-1)!$ and is false as
printed when $m>2$. The correct formula is
\[
\frac{1}{2\pi i}\oint_C F(\tau)\,d\tau
=\operatorname{Res}_{\tau=a}F
=\frac1{(m-1)!}\lim_{\tau\to a}
\frac{d^{m-1}}{d\tau^{m-1}}
\bigl((\tau-a)^mF(\tau)\bigr).
\]
Indeed, if
\[
F(\tau)=\sum_{k=-m}^{\infty}c_k(\tau-a)^k,
\]
then $(\tau-a)^mF(\tau)$ is holomorphic at $a$, and its
$(m-1)$-st derivative at $a$ is $(m-1)!c_{-1}$. The residue theorem gives
$(2\pi i)^{-1}\oint_C F=c_{-1}$.

For part (b), the double poles inside $|z|=4$ are $z=\pm i\pi$. At $i\pi$,
\[
\operatorname{Res}_{z=i\pi}
\frac{e^z}{(z^2+\pi^2)^2}
=\left.\frac{d}{dz}\frac{e^z}{(z+i\pi)^2}\right|_{z=i\pi}
=\frac1{4\pi^2}+\frac{i}{4\pi^3}.
\]
Similarly,
\[
\operatorname{Res}_{z=-i\pi}
\frac{e^z}{(z^2+\pi^2)^2}
=\frac1{4\pi^2}-\frac{i}{4\pi^3}.
\]
Thus the sum of the residues is $1/(2\pi^2)$, and
\[
\boxed{\displaystyle
\oint_C\frac{e^\tau}{(\tau^2+\pi^2)^2}\,d\tau
=2\pi i\frac1{2\pi^2}=\frac{i}{\pi}.}
\]
:::
