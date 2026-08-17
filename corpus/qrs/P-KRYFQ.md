---
schema: qual/card@1
id: P-KRYFQ
kind: problem
title: "Suppose $\\phi\\in L^1(\\RR)$ with"
classification:
  areas:
  - real-analysis
  topics:
  - approximations-to-the-identity
  - convolution
  - l1
relations: []
review: draft
solved: true
---

::: problem
Suppose $\phi\in L^1(\RR)$ with 
\[  
\int \phi(x) \, dx = \alpha
.\]
For each $\delta > 0$ and $f\in L^1(\RR)$, define
\[  
A_\delta f(x) \da \int f(x-y) \delta^{-1} \phi\qty{\delta^{-1} y}\, dy
.\]

a.
Prove that for all $\delta > 0$,
\[  
\norm{A_\delta f}_1 \leq \norm{\phi}_1 \norm{f}_1
.\]

b.
Prove that 
\[  
A_\delta f \to \alpha f \text{ in } L^1(\RR) \qtext{as} \delta\to 0^+
.\]

> Hint: you may use without proof the fact that for all $f\in L^1(\RR)$,
\[  
\lim_{y\to 0} \int_\RR \abs{f(x-y) - f(x)}\, dx = 0
.\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $\|A_\delta f\|_1 \le \|\phi\|_1\|f\|_1$ for every $\delta > 0$.
    <2>1. $|A_\delta f(x)| \le \int |f(x-y)|\,\delta^{-1}|\phi(\delta^{-1}y)|\,dy$.
        Proof: triangle inequality on the defining integral.
    <2>2. $\int_\RR |A_\delta f(x)|\,dx \le \int_\RR\int_\RR |f(x-y)||\delta^{-1}\phi(\delta^{-1}y)|\,dy\,dx = \|\phi\|_1\|f\|_1$.
        Proof: Tonelli, then substitute $z = \delta^{-1}y$ in the $y$-integral and use translation invariance of the $x$-integral: $\int|f(x - \delta z)|\,dx = \|f\|_1$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.

<1>2. $A_\delta f \to \alpha f$ in $L^1$ as $\delta \to 0^+$.
    <2>1. $A_\delta f(x) - \alpha f(x) = \int \phi(z)\big(f(x - \delta z) - f(x)\big)\,dz$.
        Proof: substitute $y = \delta z$ in $A_\delta f(x) = \int f(x - \delta z)\phi(z)\,dz$, and use $\int\phi = \alpha$ to write $\alpha f(x) = \int \phi(z) f(x)\,dz$.
    <2>2. $\|A_\delta f - \alpha f\|_1 \le \int |\phi(z)|\,\|f(\cdot - \delta z) - f\|_1\,dz$.
        Proof: integrate <2>1 in $x$ and use Minkowski's inequality for integrals.
    <2>3. For each fixed $z$, $\|f(\cdot - \delta z) - f\|_1 \to 0$ as $\delta \to 0$.
        Proof: the stated hint — $\lim_{y\to 0}\int|f(x-y) - f(x)|\,dx = 0$ — applied with $y = \delta z$.
    <2>4. Given $\eps > 0$, the integral in <2>2 is $< \eps$ for small $\delta$.
        <3>1. Choose $M$ with $2\|f\|_1\int_{|z| > M}|\phi(z)|\,dz < \eps/2$.
            Proof: $\phi \in L^1$; also $\|f(\cdot-\delta z) - f\|_1 \le 2\|f\|_1$.
        <3>2. $\sup_{|z| \le M}\|f(\cdot - \delta z) - f\|_1 \to 0$ as $\delta \to 0$.
            Proof: the translates $\{\delta z : |z| \le M\}$ lie in the ball of radius $\delta M$, and the hint gives convergence as the translation tends to $0$.
        <3>3. For small $\delta$: $\int_{|z|\le M}|\phi(z)|\,\|f(\cdot-\delta z)-f\|_1\,dz \le \|\phi\|_1 \sup_{|z|\le M}\|f(\cdot-\delta z)-f\|_1 < \eps/2$.
            Proof: <3>2.
        <3>4. Q.E.D.
            Proof: <3>1 bounds the tail by $\eps/2$ and <3>3 bounds the main part by $\eps/2$.
    <2>5. Q.E.D.
        Proof: <2>2 and <2>4 give $\|A_\delta f - \alpha f\|_1 \to 0$.
:::
