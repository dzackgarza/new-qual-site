---
schema: qual/card@1
id: P-BKF04-4B
kind: problem
title: The Fresnel-type integral $\int_0^\infty e^{iwt}t^{-1/2}\,dt$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate $I(w)\coloneqq\int_0^\infty\frac{e^{iwt}}{\sqrt t}\,dt$ for every nonzero real number $w$. You may use the formula $\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi$.
:::

::: {.solution}
The substitution $t=u^2$ yields

$$
I(w)=2\int_0^\infty f(u)\,du,
$$

where $f(u)\coloneqq e^{iwu^2}$. Suppose $w>0$. For $R>0$, let $\gamma_1$ be the straight-line path from $0$ to $R$, let $\gamma_2$ be the circular arc $Re^{it}$ for $t\in[0,\pi/4]$, and let $\gamma_3$ be the straight-line path from $Re^{i\pi/4}$ to $0$. By Cauchy's theorem, $\sum_{j=1}^3\int_{\gamma_j}f(u)\,du=0$. For $u=Re^{it}$,

$$
\abs{f(u)}=e^{\operatorname{Re}(iwu^2)}=e^{-w\operatorname{Im}(u^2)}=e^{-wR^2\sin(2t)}\le e^{-wR^2(2(2t)/\pi)},
$$

where the last step comes from the inequality $\sin x\geq2x/\pi$ for $x\in[0,\pi/2]$ (concavity of $\sin x$ on this interval). Since $\abs{du}=R\,dt$ on $\gamma_2$,

$$
\abs{\int_{\gamma_2}f(u)\,du}\leq R\int_0^\infty e^{-wR^2(2(2t)/\pi)}\,dt=\frac{\pi}{4wR},
$$

which goes to $0$ as $R\to\infty$. On $\gamma_3$, write $u=se^{i\pi/4}$ with $s$ running from $R$ to $0$; then $u^2=is^2$ and $f(u)=e^{-ws^2}$. Letting $R\to\infty$ in Cauchy's theorem therefore gives

$$
\int_0^\infty f(u)\,du
=e^{i\pi/4}\int_0^\infty e^{-ws^2}\,ds
=e^{i\pi/4}\cdot\frac12\sqrt{\frac{\pi}{w}},
$$

where the last integral follows from $\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi$ with $x=\sqrt w\,s$. Hence, for $w>0$,

$$
I(w)=e^{i\pi/4}\sqrt{\frac{\pi}{w}}=(1+i)\sqrt{\frac{\pi}{2w}}.
$$

Also, $I(-w)$ is the complex conjugate of $I(w)$. Therefore, for every $w\neq0$,

$$
I(w)=\boxed{(1+i\operatorname{sgn}(w))\sqrt{\frac{\pi}{2\abs w}}}.
$$
:::
