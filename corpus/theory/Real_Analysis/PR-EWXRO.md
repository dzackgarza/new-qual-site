---
schema: qual/card@1
id: PR-EWXRO
kind: proposition
title: Closure of measurable functions under algebraic operations and limits
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm)$ be a measurable space.

(a) If $f,g\colon X\to\RR$ are [[D-DHFN4|measurable]], then $f+g$, $fg$, $\max(f,g)$, and $\min(f,g)$ are measurable.

(b) If $f_n\colon X\to[-\infty,\infty]$ are measurable for $n\geq1$, then $\sup_n f_n$, $\inf_n f_n$, $\limsup_n f_n$, and $\liminf_n f_n$ are measurable; if $f(x)\coloneqq\lim_n f_n(x)$ exists for every $x\in X$, then $f$ is measurable.

(c) For $E\subseteq X$, the characteristic function $\chi_E$ is measurable if and only if $E\in\mcm$.
:::

::: {.proof}
(a) The map $\Phi\colon X\to\RR^2$, $x\mapsto(f(x),g(x))$, is $(\mcm,\mcb_{\RR^2})$-measurable for the Borel $\sigma$-algebra $\mcb_{\RR^2}$, since $\Phi\inv(I\times J)=f\inv(I)\cap g\inv(J)$ and open rectangles generate $\mcb_{\RR^2}$.
The maps $(s,t)\mapsto s+t$, $st$, $\max(s,t)$, $\min(s,t)$ are continuous, hence Borel, and a composite of measurable maps is measurable.

(b) For $\alpha\in\RR$, $(\sup_n f_n)\inv((\alpha,\infty])=\bigcup_n f_n\inv((\alpha,\infty])\in\mcm$, and similarly $\inf_n f_n$ is measurable.
Then $\limsup_n f_n=\inf_k\sup_{n\geq k}f_n$ and $\liminf_n f_n=\sup_k\inf_{n\geq k}f_n$ are measurable, and a pointwise limit equals $\limsup_n f_n$.

(c) For a Borel set $B\subseteq\RR$, the preimage $\chi_E\inv(B)$ is one of $\emptyset$, $E$, $X\setminus E$, $X$, according to which of $0,1$ lie in $B$.
All four lie in $\mcm$ when $E\in\mcm$.
Conversely, $E=\chi_E\inv(\theset{1})$.
:::
