---
schema: qual/card@1
id: PR-AQFRA
kind: proposition
title: Upper half-plane to sectors and back
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
For $0<\alpha\le2\pi$, let $S_\alpha\coloneqq\theset{re^{i\theta} : r>0,\ 0<\theta<\alpha}$, so that $S_\pi=\HH$.

(a) For an integer $n\ge1$,
$$
\begin{aligned}
F\colon S_{\pi/n} &\to \HH, \\
z &\mapsto z^n
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]] with inverse $w\mapsto w^{1/n}$, the [[D-4CSPM|principal branch]].

(b) For $0 < \alpha \le 2\pi$,
$$
\begin{aligned}
F\colon \HH &\to S_\alpha, \\
z &\mapsto z^{\alpha/\pi}
\end{aligned}
$$
is a biholomorphism with inverse $w\mapsto w^{\pi/\alpha}$.
Here $z^{\alpha/\pi}=e^{(\alpha/\pi)\Log z}$ uses the principal branch on $\HH$, and $w^{\pi/\alpha}=e^{(\pi/\alpha)(\log\abs{w}+i\theta)}$ uses the argument $\theta\in(0,\alpha)$ of $w\in S_\alpha$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_19-05-03.png)
:::

::: {.proof}
For (b), write $z=re^{i\theta}$ with $r>0$ and $\theta\in(0,\pi)$; then $z^{\alpha/\pi}=r^{\alpha/\pi}e^{i\alpha\theta/\pi}$, whose argument $\alpha\theta/\pi$ ranges over $(0,\alpha)$.
Since $r\mapsto r^{\alpha/\pi}$ is a bijection of $(0,\infty)$ and $\theta\mapsto\alpha\theta/\pi$ is a bijection $(0,\pi)\to(0,\alpha)$, $F$ is a bijection $\HH\to S_\alpha$, and the stated inverse multiplies the argument by $\pi/\alpha$ and raises the modulus to the power $\pi/\alpha$.
Both maps are holomorphic, since on $S_\alpha$ the chosen argument is a continuous branch of $\arg$.
Part (a) is the case $\alpha=\pi/n$ of (b), read in the opposite direction: $z\mapsto z^n$ is the inverse $w\mapsto w^{\pi/\alpha}$, and on $\HH$ the principal branch of $w^{1/n}$ is $z\mapsto z^{\alpha/\pi}$.
:::
