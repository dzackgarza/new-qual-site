---
schema: qual/card@1
id: P-NYOLD
kind: problem
title: $\sup_{y>0}|f*P_y|\le C\,Hf$ and $f*P_y\to f$ a.e. for the Poisson kernel
classification:
  areas:
  - real-analysis
  topics:
  - maximal-functions
  - approximations-to-the-identity
  - convolution
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
Let $f\in L^1(\RR)$ and let \( \mathcal{U}\da \ts{(x, y) \in \RR^2 \st y > 0}  \) denote the upper half plane.
For $(x, y) \in \mathcal{U}$ define 
\[
u(x, y) \da f \convolve P_y(x) && \text{where } P_y(x) \da {1\over \pi}\qty{y \over t^2 + y^2}
.\]

a. Prove that there exists a constant $C$ independent of $f$ such that for all $x\in \RR$, 
\[
\sup_{y > 0} \abs{ u(x, y) } \leq C\cdot Hf(x)
.\]


    *Hint: write the following and try to estimate each term:*
\[
u(x, y) = \int_{\abs t < y} f(x - t) P_y(t) \dt + \sum_{k=0}^{\infty } \int_{A_k} f(x-t) P_y(t)\dt && A_k \da \ts{2^ky \leq \abs t < 2^{k+1}y}
.\]

b. Following the proof of the Lebesgue differentiation theorem, show that for $f\in L^1(\RR)$ and for almost every $x\in \RR$,
\[
u(x, y) \converges{y\to 0} \to f(x)
.\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (a) Setup: $P_y(x) = \frac{1}{\pi}\frac{y}{x^2 + y^2}$ (the card's formula writes $t$ in place of $x$; the kernel lives in the $x$-variable), $u(x,y) = (f \ast P_y)(x)$. The hint splits $\RR$ into $|t| < y$ and dyadic annuli $A_k = \{2^k y \le |t| < 2^{k+1} y\}$.
    Proof: $\int_\RR P_y = 1$ (substitute $s = t/y$: $\frac{1}{\pi}\int \frac{y}{t^2+y^2}dt = \frac{1}{\pi}\int\frac{ds}{1+s^2} = 1$).

<1>2. Pointwise bounds on $P_y$:
    <2>1. For $|t| < y$: $P_y(t) \le \dfrac{1}{\pi y}$.
        Proof: $t^2 + y^2 \ge y^2$, so $P_y(t) = \frac{1}{\pi}\frac{y}{t^2+y^2} \le \frac{1}{\pi y}$.
    <2>2. For $2^k y \le |t| < 2^{k+1}y$: $P_y(t) \le \dfrac{1}{\pi 2^{2k} y}$.
        Proof: $t^2 \ge 2^{2k}y^2$, so $t^2 + y^2 \ge 2^{2k}y^2$.

<1>3. Central term: $\int_{|t| < y}|f(x-t)|P_y(t)\,dt \le \dfrac{2}{\pi}\,Mf(x)$, where $Mf$ is the Hardy–Littlewood maximal function $Mf(x) = \sup_{r>0}\frac{1}{2r}\int_{x-r}^{x+r}|f(s)|\,ds$.
    Proof: <1>2<2>1 gives $P_y(t) \le \frac{1}{\pi y}$; then $\frac{1}{\pi y}\int_{|t|<y}|f(x-t)|\,dt = \frac{2y}{\pi y}\cdot\frac{1}{2y}\int_{x-y}^{x+y}|f(s)|\,ds \le \frac{2}{\pi}Mf(x)$ (change $s = x - t$; the average is $\le Mf(x)$).

<1>4. Annulus terms: for each $k \ge 0$, $\int_{A_k}|f(x-t)|P_y(t)\,dt \le \dfrac{4}{\pi 2^k}\,Mf(x)$.
    <2>1. $P_y(t) \le \frac{1}{\pi 2^{2k} y}$ on $A_k$.
        Proof: <1>2<2>2.
    <2>2. $\int_{A_k}|f(x-t)|\,dt = \int_{\{2^ky \le |s - x| < 2^{k+1}y\}}|f(s)|\,ds \le \int_{x - 2^{k+1}y}^{x + 2^{k+1}y}|f(s)|\,ds \le 2^{k+2}y\cdot Mf(x)$.
        Proof: the annulus is contained in the interval $[x - 2^{k+1}y, x + 2^{k+1}y]$ of length $2^{k+2}y$, whose average is $\le Mf(x)$.
    <2>3. $\int_{A_k}|f(x-t)|P_y(t)\,dt \le \frac{1}{\pi 2^{2k}y}\cdot 2^{k+2}y\,Mf(x) = \frac{4}{\pi 2^k}Mf(x)$.
        Proof: <2>1 and <2>2.

<1>5. Summing over the annuli: $\sum_{k=0}^\infty \int_{A_k} \le \frac{4}{\pi}Mf(x)\sum_{k=0}^\infty 2^{-k} = \frac{8}{\pi}Mf(x)$.
    Proof: <1>4 and the geometric series.

<1>6. Q.E.D. (a): $|u(x,y)| \le \left(\frac{2}{\pi} + \frac{8}{\pi}\right)Mf(x) = \frac{10}{\pi}Mf(x) \le C\,Hf(x)$ for all $x \in \RR$, all $y > 0$.
    Proof: $|u(x,y)| \le \int |f(x-t)|P_y(t)\,dt$ (triangle inequality), split into the central term (<1>3) and the annuli (<1>5); the card's $Hf$ denotes (a constant multiple of) the Hardy–Littlewood maximal function, so $C$ is a fixed constant independent of $f$.

<1>7. (b) $u(x,y) \to f(x)$ for a.e. $x$ as $y \to 0$.
    <2>1. $P_y$ is an approximation to the identity: $\int P_y = 1$ and $\int_{|t| \ge \delta}P_y(t)\,dt \to 0$ as $y \to 0$ for every $\delta > 0$.
        Proof: $\int_{|t|\ge\delta}P_y = \frac{2}{\pi}\int_\delta^\infty\frac{y}{t^2+y^2}dt = \frac{2}{\pi}\int_{\delta/y}^\infty\frac{du}{1+u^2} = \frac{2}{\pi}\left(\frac{\pi}{2} - \arctan(\delta/y)\right) \to 0$.
    <2>2. $|u(x,y) - f(x)| \le \int |f(x-t) - f(x)|P_y(t)\,dt$.
        Proof: $\int P_y = 1$, so $u - f = \int (f(x-t) - f(x))P_y(t)\,dt$; triangle inequality.
    <2>3. For a Lebesgue point $x$ of $f$ (a.e. $x$ is one): $\frac{1}{2r}\int_{x-r}^{x+r}|f(s) - f(x)|\,ds \to 0$ as $r \to 0$.
        Proof: Lebesgue differentiation theorem.
    <2>4. Given $\eps > 0$, choose $\delta > 0$ with $\frac{1}{2r}\int_{x-r}^{x+r}|f(s) - f(x)|\,ds < \eps'$ for all $r < \delta$; split the integral in <2>2 at $|t| < \delta$:
        <3>1. Small-$t$ part: $\int_{|t| < \delta}|f(x-t) - f(x)|P_y(t)\,dt \le \frac{1}{\pi y}\int_{|t|<\delta}|f(x-t) - f(x)|\,dt = \frac{2}{\pi}\cdot\frac{1}{2y}\int_{x-y}^{x+y}|f(s) - f(x)|\,ds < \frac{2}{\pi}\eps'$ for $y < \delta$.
            Proof: <1>2<2>1 and the Lebesgue-point estimate with $r = y$.
        <3>2. Large-$t$ part: $\int_{|t| \ge \delta}|f(x-t) - f(x)|P_y(t)\,dt \le \int_{|t|\ge\delta}|f(x-t)|P_y(t)\,dt + |f(x)|\int_{|t|\ge\delta}P_y(t)\,dt \le \|f\|_1\frac{y}{\pi\delta^2} + |f(x)|\int_{|t|\ge\delta}P_y \to 0$.
            Proof: $|f(x-t) - f(x)| \le |f(x-t)| + |f(x)|$; first term: on $|t| \ge \delta$, $P_y(t) \le \frac{y}{\pi\delta^2}$, so $\int_{|t|\ge\delta}|f(x-t)|P_y \le \frac{y}{\pi\delta^2}\|f\|_1 \to 0$ as $y \to 0$; second term: <2>1.
        <3>3. Q.E.D.: both parts vanish as $y \to 0$ (after taking $y < \delta$ and then $y \to 0$).
            Proof: <3>1 and <3>2, then let $\eps' \to 0$.
    <2>5. Q.E.D.
        Proof: <2>3 and <2>4 give $u(x,y) \to f(x)$ at every Lebesgue point, i.e. for a.e. $x$.
:::
