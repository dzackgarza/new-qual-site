---
schema: qual/card@1
id: P-FBOFF
kind: problem
title: Dense values near an accumulation point of poles, versus Casorati–Weierstrass
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Poles
  - Singularities
  - Meromorphic Functions
relations: []
review: draft
---

::: {.problem}
(1) Let $f$ be analytic in $\Omega: 0<\abs{z-a}<r$ except at a sequence of poles $a_n \in \Omega$ with $\lim_{n \rightarrow \infty} a_n = a$.
Show that for any $w \in \CC$, there exists a sequence $z_n \in \Omega$ such that $\lim_{n \rightarrow \infty} f(z_n) = w$.

(2) Explain the similarity and difference between the above assertion and the Weierstrass-Casorati theorem.
:::

::: {.solution}
Fix $w\in\CC$. We prove the stronger conclusion that the sequence can be chosen with $z_n\to a$.

::: pf

::: {.pf-step #bounded-away}
If no sequence $z_n\to a$ of points that are not poles has $f(z_n)\to w$, then there are $\varepsilon>0$ and $\delta\in(0,r)$ with $\abs{f(z)-w}\geq\varepsilon$ whenever $0<\abs{z-a}<\delta$ and $z$ is not a pole of $f$.

::: pf-proof
Otherwise, for every $n$ there is a point $z_n$, not a pole, with $0<\abs{z_n-a}<1/n$ and $\abs{f(z_n)-w}<1/n$, and this sequence has $z_n\to a$ and $f(z_n)\to w$.
:::

:::

::: {.pf-step #G-extends}
Under the conclusion of step [](#bounded-away){.pf-ref}, $G \coloneqq 1/(f-w)$ extends to a holomorphic function on $\abs{z-a}<\delta$ with $G(a_k)=0$ for every pole $a_k$ in that disc and $G(a)=0$.

::: pf-proof
Off the poles, $G$ is holomorphic with $\abs{G}\leq\varepsilon^{-1}$. At a pole $a_k$ of $f$, $G(z)\to 0$ as $z\to a_k$, so $a_k$ is a removable singularity of $G$ with $G(a_k)=0$. The extended $G$ is holomorphic and bounded on $0<\abs{z-a}<\delta$, so $a$ is a removable singularity by Riemann's theorem, and $G(a) = \lim_k G(a_k) = 0$ by continuity.
:::

:::

::: {.pf-step #contradiction}
The conclusion of step [](#bounded-away){.pf-ref} is false.

::: pf-proof
By step [](#G-extends){.pf-ref}, the zeros $a_k$ of $G$ accumulate at the point $a$ of the disc $\abs{z-a}<\delta$, so $G\equiv 0$ by the identity theorem. But $G = 1/(f-w)\neq 0$ at every point that is not a pole.
:::

:::

::: pf-step
There is a sequence $z_n\to a$ in $\Omega$ with $f(z_n)\to w$.

::: pf-proof
This follows from steps [](#bounded-away){.pf-ref} and [](#contradiction){.pf-ref}.
:::

:::

:::

The assertion resembles Casorati--Weierstrass because every finite complex value is a limit of values of $f$ arbitrarily near $a$. The difference is that Casorati--Weierstrass concerns an isolated essential singularity, whereas here $a$ is not an isolated singularity at all: poles of $f$ accumulate at $a$.
:::
