---
schema: qual/card@1
id: P-HCAX18
kind: problem
title: The integral $\int_0^\infty \frac{\sqrt x}{1+x^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Evaluate
\[
\int_0^\infty \frac{x^{1/2}}{1+x^2}\,dx
\]
by complex-analytic methods.
:::

::: {.solution}
<1>1. A keyhole contour converts the contour integral into twice the real integral.
::: {.proof}
Use the branch
$$
z^{1/2}=e^{\frac12(\log|z|+i\arg z)},
\qquad 0<\arg z<2\pi,
$$
whose branch cut is the positive real axis, and set
$$
F(z)=\frac{z^{1/2}}{1+z^2}.
$$
Integrate $F$ around the positively oriented keyhole contour with inner radius $\varepsilon$ and outer radius $R$.

On the upper side of the cut, $z^{1/2}=x^{1/2}$. On the lower side, $\arg z\to2\pi$, so $z^{1/2}=-x^{1/2}$; the lower segment is traversed from $R$ to $\varepsilon$, so its contribution has the same sign as the upper segment. Near $0$, $F(z)=O(|z|^{1/2})$, while at infinity $F(z)=O(|z|^{-3/2})$. Hence the inner and outer circular contributions are respectively $O(\varepsilon^{3/2})$ and $O(R^{-1/2})$, and therefore vanish in the limits. Thus
$$
\oint F(z)\,dz
\longrightarrow
2\int_0^\infty\frac{x^{1/2}}{1+x^2}\,dx.
$$
:::

<1>2. The sum of the residues inside the keyhole contour is $-i/\sqrt2$.
::: {.proof}
The poles are $i$ and $-i$. With the chosen branch,
$$
i^{1/2}=e^{i\pi/4},
\qquad
(-i)^{1/2}=e^{3i\pi/4}.
$$
Therefore
$$
\operatorname{Res}(F,i)
=\frac{e^{i\pi/4}}{2i}
=\frac{1-i}{2\sqrt2},
$$
and
$$
\operatorname{Res}(F,-i)
=\frac{e^{3i\pi/4}}{-2i}
=\frac{-1-i}{2\sqrt2}.
$$
Adding gives
$$
\operatorname{Res}(F,i)+\operatorname{Res}(F,-i)
=-\frac{i}{\sqrt2}.
$$
:::

<1>3. The integral is $\boxed{\pi/\sqrt2}$.
::: {.proof}
By the [[T-HRPNO|residue theorem]] and steps <1>1--<1>2,
$$
2\int_0^\infty\frac{x^{1/2}}{1+x^2}\,dx
=2\pi i\left(-\frac{i}{\sqrt2}\right)
=\sqrt2\,\pi.
$$
Dividing by $2$ gives
$$
\int_0^\infty\frac{x^{1/2}}{1+x^2}\,dx
=\frac{\pi}{\sqrt2}.
$$
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 is the requested evaluation.
:::
:::
