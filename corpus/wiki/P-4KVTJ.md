---
schema: qual/card@1
id: P-4KVTJ
kind: problem
title: Cauchy integral of $f$ on a simple closed curve, equal to $A$ inside and $-f(z)+A$
  outside, when $\lim_{z\to\infty}f(z)=A$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Residues
  - Contour Integration
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega_1$ and exterior $\Omega_2$.
Assume $f'$ exists in an open set containing $\gamma$ and $\Omega_2$ with $\lim_{z\to \infty} f(z) = A$.
Show that
$$
F(z) \da \frac{1}{2 \pi i} \int_{\gamma} \frac{f(\xi)}{\xi-z} d \xi=\left\{\begin{array}{ll}
A, & \text { if } z \in \Omega_{1} \\
-f(z)+A, & \text { if } z \in \Omega_{2}
\end{array}\right.
.$$

> NOTE (DZG): I think there is a typo in this question....probably this should equal $f(z)$ for $z\in \Omega_1$, which is Cauchy's formula...

:::

:::{.solution}
Note that $G_z(\xi) \da {f(\xi) \over \xi - z}$ has a pole of order one at $\xi = z$ and also a pole at $\xi = \infty$.
If $z\in \Omega_1$, then $\gamma$ encloses just the pole $\xi = z$, so apply the residue theorem:
\[
F(z) 
&\da {1\over 2\pi i}\oint_\gamma {f(\xi) \over \xi - z}\dxi \\
&= {1\over 2\pi i}\oint_\gamma G_z(\xi) \dxi \\
&= \Res_{\xi = z} G_z(\xi) \\
&= \lim_{\xi\to z} (\xi - z) G_z(\xi) \\ 
&= \lim_{\xi\to z} (\xi - z) {f(\xi) \over \xi-z} \\ 
&= \lim_{\xi\to z} f(\xi) \\
&= f(z)
.\]

Now if $z\in \Omega_2$, then $\gamma$ encloses both $\xi=z, \infty$, and is oriented negatively,so
\[
F(z) 
&= {1\over 2\pi i} \oint_\gamma G_z(\xi) \dxi \\
&= -\qty{\Res_{\xi = z} G_z(\xi) + \Res_{\xi = \infty} G_z(\xi)}\\
&= -\qty{f(z) + \Res_{\xi = \infty} G_z(\xi)}\\
,\]
where the last line proceeds by the same calculation as above.
It remains to compute the unknown residue.
Residues at $\xi = \infty$ are computed as residues at $\xi =0$, and the change of variables $G_z(\xi)\dxi \mapsto G_z(w) \dw$ for $w\da 1/\xi$ yields $G_z(\xi)\dxi \to G_z\qty{1\over \xi}(-1/\xi^2)\dxi$.
Thus
\[
\Res_{\xi=\infty} G_z(\xi) 
&= -\Res_{\xi=0} G_z\qty{\xi\inv}\xi^{-2} \\
&= - \Res_{\xi=0} {f(\xi\inv) \over \xi^2(\xi\inv - z) } \\
&= - \Res_{\xi=0} {f(\xi\inv) \over \xi(1 - z\xi) } \\
&= -\lim_{\xi \to 0} {f(\xi\inv) \over 1-z\xi} \\
&= -\lim_{\xi \to 0}f(\xi \inv) \\
&= -\lim_{\xi\to\infty} f(\xi) \\
&= -A
.\]
So combining this yields
\[
F(z) = -\qty{f(z) - A} = -f(z) + A
.\]
:::
