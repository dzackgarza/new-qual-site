---
order: 100003
---

# Techniques

[[PR-V4MOK]]

:::{.example title="Gaussian moments"}
For $t>0$ the identity $\int_0^\infty e^{-tx}\,\dx = t^{-1}$ differentiates under the integral: $\abs{-x e^{-tx}}\leq x e^{-t_0 x}$ on any interval $t\geq t_0>0$, which is integrable, so
\[
\int_0^\infty x^n e^{-tx}\,\dx
= \frac{n!}{t^{n+1}}
.\]

:::

:::{.example title="Differentiating a parameter in a Gaussian"}
$\int_{-\infty}^\infty e^{-tx^2}\,\dx = \sqrt{\pi/t}$ for $t>0$.
On $t\geq t_0>0$ one has $\abs{-x^2 e^{-tx^2}}\leq x^2 e^{-t_0 x^2}\in L^1(\RR)$, so
\[
\dd{}{t}\int_{-\infty}^\infty e^{-tx^2}\,\dx
= \int_{-\infty}^\infty -x^2 e^{-tx^2}\,\dx
= -\frac12\sqrt{\pi}\, t^{-3/2}
.\]

:::

:::{.example title="Laplace transform of $\sin x / x$"}
For $a>0$ set $F(a)\da\int_0^\infty e^{-ax}\frac{\sin x}{x}\,\dx$.
Then $\abs{e^{-ax}\sin x}\leq e^{-a_0 x}$ for $a\geq a_0>0$, so
\[
F'(a)
= -\int_0^\infty e^{-ax}\sin x\,\dx
= -\frac{1}{1+a^2}
,\]
and $F(a)\to 0$ as $a\to\infty$, hence $F(a)=\frac{\pi}{2}-\arctan a$.

:::

[[E-IAQ6D]]
