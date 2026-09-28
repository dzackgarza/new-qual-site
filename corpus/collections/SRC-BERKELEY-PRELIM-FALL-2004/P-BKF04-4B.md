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

where the last step comes from the inequality $\sin x\leq2x/\pi$ for $x\in[0,\pi/2]$ (concavity of $\sin x$ on this interval). Therefore

$$
\abs{\int_{\gamma_2}f(u)\,du}\leq\int_0^\infty e^{-wR^2(2(2t)/\pi)}\,dt=\frac{\pi}{4wR^2},
$$

which goes to $0$ as $R\to\infty$. Hence

$$
\begin{array} { r l } { \iota ( w ) - 2 \displaystyle \operatorname* { l i m } _ { m \to \infty } \int _ { \gamma } \langle w | \hat { \sigma } \rangle \ : d w } \\ { } & { = - 2 \displaystyle \operatorname* { l i m } _ { m \to \infty } \int _ { - \infty } ^ { \infty } \int _ { \gamma } \langle i ( \lambda ) ^ { m } \rangle } \\ { } & { = 2 \displaystyle \int _ { \gamma } \eta _ { \varepsilon } \langle i ( \lambda ) ^ { m } | \hat { \sigma } \rangle \ : d w } \\ { } & { = - 2 \displaystyle \int _ { \gamma } \int _ { \gamma } \langle i ( \lambda ^ { m } ) ^ { m } \rangle \ : \theta \ : \mathrm { d } w } \\ { } & { = - \theta ^ { \mathrm { d i d } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = \theta ^ { \mathrm { d i d } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = \frac { 1 + \frac { 1 } { 2 } } { \sqrt { 2 } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = ( 1 + \lambda ) \displaystyle \frac { 1 } { \sqrt { 2 } } \frac { 1 } { \omega ^ { m } } . } \end{array}
$$

Also, $I(-w)$ is the complex conjugate of $I(w)$. Therefore, for every $w\neq0$,

$$
I(w)=\boxed{(1+i\operatorname{sgn}(w))\sqrt{\frac{\pi}{2\abs w}}}.
$$
:::
