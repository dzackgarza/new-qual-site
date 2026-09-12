---
schema: qual/card@1
id: P-RASP16A
kind: problem
title: "True or false: limsup measures, Lebesgue points, weak+norm convergence, Schwartz convolution, second derivative of |x|"
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Lebesgue Points
  - Weak Convergence
  - Schwartz Space
  - Distributions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample or prove your assertion.

(1) Let $(X, \mathcal{M}, \mu)$ be a measure space and $E_j \in \mathcal{M}$ ($j = 1, 2, \ldots$). Denote by $E = \{x \in X : x \in E_j \text{ for infinitely many } j\}$.
If $E \neq \emptyset$, $\mu(E_j) < \infty$, then $\mu(E) = 0$.

(2) Let $f \in L^1(\mathbb{R}^n)$ and denote the Lebesgue set of $f$ by $L_f$.
Let $z_0 \in \mathbb{R}^n$ and suppose $f$ is continuous at $z_0$.
Then $z_0 \in L_f$.

(3) Let $H$ be a real Hilbert space.
Let $z_k \in H$ ($k = 1, 2, \ldots$) and $z \in H$.
If $z_k \to z$ weakly in $H$ and $\|z_k\| = \|z\|$, then $\|z_k - z\| \to 0$.

(4) Let $\mathcal{S}$ denote the Schwartz space on $\mathbb{R}^n$.
Let $f, g \in \mathcal{S}$.
If $f * g = 0$ in $\mathbb{R}^n$ then either $f = 0$ in $\mathbb{R}^n$ or $g = 0$ in $\mathbb{R}^n$.

(5) Let $f(x) = |x|$ ($x \in \mathbb{R}$) and identify $f$ as a distribution on $\mathbb{R}$.
Then the second-order distributional derivative $f''$ is the zero distribution on $\mathcal{D}(\mathbb{R})$.
:::

::: solution
<1>1. Statement (1) is false.
::: proof
Take $X=[0,1]$ with Lebesgue measure and set
\[
E_j=[0,1]
\]
for every $j$. Then each $\mu(E_j)=1<\infty$, and every point lies in infinitely many $E_j$, so
\[
E=[0,1].
\]
Hence
\[
\mu(E)=1\ne0.
\]
The missing hypothesis in the first Borel--Cantelli lemma is the summability of $\sum_j\mu(E_j)$, not merely finiteness of each term.
:::

<1>2. Statement (2) is true.
::: proof
Continuity of $f$ at $z_0$ means that for every $\varepsilon>0$ there is $r_0>0$ such that
\[
|f(y)-f(z_0)|<\varepsilon
\]
whenever $|y-z_0|<r_0$. Hence for $0<r<r_0$,
\[
\frac1{|B_r|}\int_{B_r(z_0)}|f(y)-f(z_0)|\,dy
\le\varepsilon.
\]
Letting $r\downarrow0$ gives the Lebesgue-point condition. Thus
\[
z_0\in L_f.
\]
:::

<1>3. Statement (3) is true.
::: proof
Weak convergence gives
\[
\langle z_k,z\rangle\to\|z\|^2.
\]
Since $\|z_k\|=\|z\|$ for every $k$,
\[
\begin{aligned}
\|z_k-z\|^2
&=\|z_k\|^2+\|z\|^2-2\langle z_k,z\rangle\\
&\longrightarrow2\|z\|^2-2\|z\|^2=0.
\end{aligned}
\]
Hence $z_k\to z$ in norm.
:::

<1>4. Statement (4) is false.
::: proof
Choose nonzero functions
\[
\phi,\psi\in C_c^\infty(\mathbb R^n)
\]
with disjoint supports. Let
\[
f=\mathcal F^{-1}\phi,
\qquad
g=\mathcal F^{-1}\psi.
\]
The inverse Fourier transform maps $C_c^\infty$ into the Schwartz space, so $f,g\in\mathcal S$ and both are nonzero.

But
\[
\widehat{f*g}=\widehat f\,\widehat g=\phi\psi=0.
\]
Fourier-transform injectivity gives
\[
f*g=0,
\]
although neither factor is zero.
:::

<1>5. Statement (5) is false.
::: proof
For $f(x)=|x|$, the first distributional derivative is
\[
Df=\operatorname{sgn}(x).
\]
For a test function $\varphi$,
\[
\begin{aligned}
\langle D^2f,\varphi\rangle
&=-\int_{\mathbb R}\operatorname{sgn}(x)\varphi'(x)\,dx\\
&=-\int_0^\infty\varphi'(x)\,dx
+\int_{-\infty}^0\varphi'(x)\,dx\\
&=2\varphi(0).
\end{aligned}
\]
Thus
\[
\boxed{D^2|x|=2\delta_0,}
\]
not the zero distribution.
:::
:::
