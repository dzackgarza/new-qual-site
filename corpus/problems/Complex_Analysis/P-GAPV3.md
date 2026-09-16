---
schema: qual/card@1
id: P-GAPV3
kind: problem
title: Holomorphy of $\Gamma$ on $\operatorname{Re}s>0$ and the reflection formula
  $\Gamma(s)\Gamma(1-s)=\pi/\sin(\pi s)$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Holomorphic Functions
  - Residues
relations: []
review: draft
---

::: {.problem}
For $s>0$, the **gamma function** is defined by $\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

- Show that the gamma function is analytic in the half-plane $\Re (s)>0$, and is still given there by the integral formula above.

- Apply the formula in the previous question to show that $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

> Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.
:::

::: {.solution}
Let
\[
\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt,
\qquad \Re s>0,
\]
where $t^{s-1}=e^{(s-1)\log t}$ for the real logarithm on $(0,\infty)$.

Fix a compact set $K\subset\{\Re s>0\}$. Choose numbers
$0<\sigma_0\le \Re s\le \sigma_1$ for $s\in K$. On $(0,1]$,
\[
|e^{-t}t^{s-1}\log t|
\le t^{\sigma_0-1}|\log t|,
\]
and on $[1,\infty)$,
\[
|e^{-t}t^{s-1}\log t|
\le e^{-t}t^{\sigma_1-1}\log t.
\]
Both majorants are integrable. Hence differentiation under the integral sign is
valid uniformly on compact subsets, so $\Gamma$ is holomorphic on
$\Re s>0$ and
\[
\Gamma'(s)=\int_0^\infty e^{-t}t^{s-1}\log t\,dt.
\]

Now suppose $0<\Re s<1$. Using the change of variables $u=vt$ in the second
factor,
\[
\Gamma(1-s)=t\int_0^\infty e^{-vt}(vt)^{-s}\,dv.
\]
Therefore Tonelli/Fubini gives
\[
\begin{aligned}
\Gamma(s)\Gamma(1-s)
&=\int_0^\infty\int_0^\infty
e^{-t(1+v)}v^{-s}\,dt\,dv \\
&=\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
\end{aligned}
\]
Equivalently, replacing $s$ by $1-s$,
\[
\Gamma(s)\Gamma(1-s)
=\int_0^\infty \frac{x^{s-1}}{1+x}\,dx.
\]

Evaluate this integral by a keyhole contour around the positive real axis for
\[
F(z)=\frac{z^{s-1}}{1+z},
\qquad 0<\arg z<2\pi.
\]
The small and large circular arcs vanish because $0<\Re s<1$. The upper bank
contributes $I(s)$ and the lower bank contributes $-e^{2\pi i(s-1)}I(s)$,
where
\[
I(s)=\int_0^\infty\frac{x^{s-1}}{1+x}\,dx.
\]
The only enclosed pole is at $z=-1$, with residue
\[
(-1)^{s-1}=e^{i\pi(s-1)}.
\]
Thus
\[
(1-e^{2\pi i(s-1)})I(s)=2\pi i e^{i\pi(s-1)}.
\]
Since
\[
1-e^{2\pi i(s-1)}=-2i e^{i\pi(s-1)}\sin(\pi(s-1))
=2i e^{i\pi(s-1)}\sin(\pi s),
\]
we obtain
\[
I(s)=\frac{\pi}{\sin\pi s}.
\]
Hence, for $0<\Re s<1$,
\[
\boxed{\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin\pi s}}.
\]
After the usual meromorphic continuation of $\Gamma$, the same identity extends
to every $s\notin\mathbb Z$ by the identity theorem.
:::
