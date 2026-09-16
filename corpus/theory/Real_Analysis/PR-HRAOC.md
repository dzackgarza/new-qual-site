---
schema: qual/card@1
id: PR-HRAOC
kind: proposition
title: Existence of nonzero smooth compactly supported functions
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Differentiation
relations: []
review: draft
---

::: {.proposition}
Let $f\colon\RR\to\RR$ be given by $f(x)\coloneqq e^{-1/x^2}$ for $x>0$ and $f(x)\coloneqq0$ for $x\leq0$.
Then $f\in C^\infty(\RR)$, and $\psi(x)\coloneqq f(x)\,f(1-x)$ is a $C^\infty$ function on $\RR$ with $\psi>0$ on $(0,1)$ and $\psi=0$ outside $(0,1)$.
For $n\geq1$, $\phi(x)\coloneqq f\big(1-\abs{x}^2\big)$ is a $C^\infty$ function on $\RR^n$ with $\supp\phi=\theset{x : \abs{x}\leq1}$.
:::

::: {.proof}
By induction on $k$, for $x>0$ one has $f^{(k)}(x)=p_k(1/x)\,e^{-1/x^2}$ for a polynomial $p_k$: differentiating gives $p_{k+1}(t)=-t^2p_k'(t)+2t^3p_k(t)$.
Since $t^me^{-t^2}\to0$ as $t\to\infty$ for every $m$, $f^{(k)}(x)\to0$ as $x\to0^+$.
By induction and the mean value theorem, each $f^{(k)}$ is differentiable at $0$ with $f^{(k+1)}(0)=\lim_{x\to0}f^{(k)}(x)/x=0$, so $f\in C^\infty(\RR)$.
Products and composites of $C^\infty$ functions are $C^\infty$, and $x\mapsto1-\abs{x}^2$ is a polynomial.
The statements about where $\psi$ and $\phi$ vanish follow from $f(t)>0\iff t>0$.
:::
