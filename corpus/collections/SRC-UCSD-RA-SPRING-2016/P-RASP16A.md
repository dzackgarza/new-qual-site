---
schema: qual/card@1
id: P-RASP16A
kind: problem
title: 'True or false: limsup of sets, Lebesgue points, weak plus norm convergence, Schwartz convolution, second derivative of $\abs{x}$'
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

::: {.problem}
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample or prove your assertion.

(1) Let $(X, \mathcal{M}, \mu)$ be a measure space and $E_j \in \mathcal{M}$ ($j = 1, 2, \ldots$). Denote by $E = \{x \in X : x \in E_j \text{ for infinitely many } j\}$.
If $\sum_{j=1}^\infty \mu(E_j) < \infty$, then $\mu(E) = 0$.

(2) Let $f \in L^1_{\mathrm{loc}}(\RR^n)$ and denote the Lebesgue set of $f$ by $L_f$.
Let $z_0 \in \RR^n$ and suppose $f$ is continuous at $z_0$.
Then $z_0 \in L_f$.

(3) Let $H$ be a real Hilbert space.
Let $z_k \in H$ ($k = 1, 2, \ldots$) and $z \in H$.
If $z_k \to z$ weakly in $H$ and $\norm{z_k} \to \norm{z}$, then $\norm{z_k - z} \to 0$.

(4) Let $\mathcal{S}$ denote the Schwartz space on $\RR^n$.
Let $f, g \in \mathcal{S}$.
If $f * g = 0$ in $\RR^n$ then either $f = 0$ in $\RR^n$ or $g = 0$ in $\RR^n$.

(5) Let $f(x) = \abs{x}$ ($x \in \RR$) and identify $f$ as a distribution on $\RR$.
Then the second-order distributional derivative $f''$ is the zero distribution on $\mathcal{D}(\RR)$.
:::

::: {.solution}

::: pf

::: pf-step

Statement (1) is true.

::: pf-proof

By definition,
$$
E=\bigcap_{N=1}^\infty\bigcup_{j\ge N}E_j,
$$
so $E\in\mathcal M$ and, for every $N$,
$$
\mu(E)\le\mu\Big(\bigcup_{j\ge N}E_j\Big)\le\sum_{j\ge N}\mu(E_j).
$$
The right side is the tail of a convergent series, so it tends to $0$ as $N\to\infty$. Hence
$$
\mu(E)=0.
$$
This is the first Borel--Cantelli lemma.

:::

:::

::: pf-step

Statement (2) is true.

::: pf-proof

Continuity of $f$ at $z_0$ means that for every $\varepsilon>0$ there is $r_0>0$ such that
$$
\abs{f(y)-f(z_0)}<\varepsilon
$$
whenever $\norm{y-z_0}<r_0$. Hence for $0<r<r_0$,
$$
\frac1{\setmeasure{B_r}}\int_{B_r(z_0)}\abs{f(y)-f(z_0)}\,dy
\le\varepsilon.
$$
Letting $r\downarrow0$ gives the Lebesgue-point condition. Thus
$$
z_0\in L_f.
$$

:::

:::

::: pf-step

Statement (3) is true.

::: pf-proof

Weak convergence gives
$$
\langle z_k,z\rangle\to\norm{z}^2.
$$
Since $\norm{z_k}\to\norm{z}$,
$$
\begin{aligned}
\norm{z_k-z}^2
&=\norm{z_k}^2+\norm{z}^2-2\langle z_k,z\rangle\\
&\longrightarrow2\norm{z}^2-2\norm{z}^2=0.
\end{aligned}
$$
Hence $z_k\to z$ in norm.

:::

:::

::: pf-step

Statement (4) is false.

::: pf-proof

Choose nonzero functions
$$
\phi,\psi\in C_c^\infty(\RR^n)
$$
with disjoint supports. Let
$$
f=\mathcal F^{-1}\phi,
\qquad
g=\mathcal F^{-1}\psi.
$$
The inverse Fourier transform maps $C_c^\infty$ into the Schwartz space, so $f,g\in\mathcal S$ and both are nonzero.

But
$$
\widehat{f*g}=\widehat f\,\widehat g=\phi\psi=0.
$$
Fourier-transform injectivity gives
$$
f*g=0,
$$
although neither factor is zero.

:::

:::

::: pf-step

Statement (5) is false.

::: pf-proof

For $f(x)=\abs{x}$, the first distributional derivative is
$$
Df=\operatorname{sgn}(x).
$$
For a test function $\varphi$,
$$
\begin{aligned}
\langle D^2f,\varphi\rangle
&=-\int_{\RR}\operatorname{sgn}(x)\varphi'(x)\,dx\\
&=-\int_0^\infty\varphi'(x)\,dx
+\int_{-\infty}^0\varphi'(x)\,dx\\
&=2\varphi(0).
\end{aligned}
$$
Thus
$$
\boxed{D^2\abs{x}=2\delta_0,}
$$
not the zero distribution.

:::

:::

:::

:::
