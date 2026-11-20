---
schema: qual/card@1
id: PR-AQFRA
kind: proposition
title: Upper half-plane to sectors and back
slogan: 'Power maps multiply arguments, giving biholomorphisms between the upper half-plane and sectors.'
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

This is the sector correspondence of [@Ahl73, ch. 3, §4.1, The Use of Level Curves]: for the sector $S_0(\varphi_1,\varphi_2)$ defined by (14) there, the map $w=z^\alpha$ is one-to-one when $\alpha(\varphi_2-\varphi_1)\le2\pi$ and carries it onto $S_0(\alpha\varphi_1,\alpha\varphi_2)$. Part (a) is the case $\alpha=n$ and $(\varphi_1,\varphi_2)=(0,\pi/n)$, whose image is $S_0(0,\pi)=\HH$.

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

::: {.remark}
The map $z\mapsto z^{\alpha/\pi}$ of (b) extends continuously to the boundary of $\HH$.
As $x$ increases from $0$ to $\infty$ along the positive real axis, $x^{\alpha/\pi}$ increases from $0$ to $\infty$ along the positive real axis.
As $x$ increases from $-\infty$ to $0$ along the negative real axis, $x^{\alpha/\pi}=\abs{x}^{\alpha/\pi}e^{i\alpha}$ moves from $\infty$ to $0$ along the ray $\theset{te^{i\alpha}\st t>0}$.
:::
