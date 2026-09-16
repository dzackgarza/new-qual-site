---
schema: qual/card@1
id: E-FPZDC
kind: problem
title: Analyticity of $\Gamma$ on $\Re(s)>0$ and Euler's reflection formula
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

::: {.exercise}
-   For real $s>0$, define
  \[
  \Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt.
  \]
  Show that the same integral defines an analytic function in the half-plane $\Re(s)>0$.

-   Using
  \[
  \int_0^\infty {x^{a-1}\over1+x^n}\,dx
  ={\pi\over n\sin(a\pi/n)},
  \qquad 0<a<n,
  \]
  show that, for $0<\Re(s)<1$,
  $$
\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}
.$$

> Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.
:::

::: {.solution}
Fix a compact set $K\subset\{s:\Re s>0\}$ and put
\[
\sigma_0=\min_{s\in K}\Re s>0,
\qquad
\sigma_1=\max_{s\in K}\Re s.
\]
For $0<t\le1$ and $s\in K$,
\[
|e^{-t}t^{s-1}|\le t^{\sigma_0-1},
\]
while for $t\ge1$,
\[
|e^{-t}t^{s-1}|\le e^{-t}t^{\sigma_1-1}.
\]
Both majorants are integrable. The same argument, with an additional factor
$|\log t|^m$, applies after any number $m$ of differentiations in $s$.
Therefore differentiation under the integral sign is valid locally uniformly,
and
\[
\Gamma^{(m)}(s)=\int_0^\infty e^{-t}t^{s-1}(\log t)^m\,dt.
\]
In particular, $\Gamma$ is holomorphic on $\Re s>0$.

Now assume $0<\Re s<1$. Using the substitution $u=vt$ in the second gamma
factor,
\[
\Gamma(1-s)
=t\int_0^\infty e^{-vt}(vt)^{-s}\,dv.
\]
Hence, by absolute convergence and Fubini,
\[
\begin{aligned}
\Gamma(s)\Gamma(1-s)
&=\int_0^\infty\int_0^\infty
 e^{-t}t^{s-1}\,t e^{-vt}(vt)^{-s}\,dv\,dt\\
&=\int_0^\infty v^{-s}
\left(\int_0^\infty e^{-(1+v)t}\,dt\right)dv\\
&=\int_0^\infty {v^{-s}\over1+v}\,dv.
\end{aligned}
\]
For
\[
M(a)=\int_0^\infty {v^{a-1}\over1+v}\,dv,
\qquad 0<\Re a<1,
\]
the same compact-majorant argument used above shows that $M$ is holomorphic
on the strip $0<\Re a<1$. The function $\pi/\sin(\pi a)$ is holomorphic there
as well. The preceding exercise proves
\[
M(a)={\pi\over\sin(\pi a)}
\]
for every real $a\in(0,1)$, so the identity theorem extends this equality to
the whole strip. Taking $a=1-s$ therefore gives
\[
\int_0^\infty {v^{-s}\over1+v}\,dv
={\pi\over\sin(\pi(1-s))}
={\pi\over\sin(\pi s)}.
\]
Thus
\[
\Gamma(s)\Gamma(1-s)={\pi\over\sin\pi s},
\qquad 0<\Re s<1.
\]
:::
