---
schema: qual/card@1
id: P-RASP15C
kind: problem
title: "Extension of a Radon measure from a closed subspace via Riesz-Markov"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be a locally compact Hausdorff space.
Let $Y$ be a closed subspace and $\mu$ be a Radon measure on $Y$.
Define a linear functional on $C_c(X)$ by $I(f) = \int_Y (f|_Y)\,d\mu$.

Prove that: (i) $I(f)$ is a positive linear functional; (ii) The functional $I(f) = \int_X f\,d\nu$ induces a Radon measure $\nu$ (via the Riesz-Markov theorem) which satisfies $\nu(E) = \mu(E \cap Y)$.

Precisely you need to show that (a) $\nu$ as defined above is a Radon measure; (b) the linear functional $I(f)$ can be represented by $\int_X f\,d\nu$.
:::

::: solution
<1>1. The functional $I$ is well defined, linear, and positive.
::: proof
If $f\in C_c(X)$, then $f|_Y\in C_c(Y)$ because
\[
\operatorname{supp}(f|_Y)\subseteq \operatorname{supp}(f)\cap Y,
\]
and the latter is compact: $Y$ is closed and $\operatorname{supp}(f)$ is compact. Thus
\[
I(f)=\int_Y f|_Y\,d\mu
\]
is well defined. Linearity is immediate from linearity of the integral. If $f\ge0$ on $X$, then $f|_Y\ge0$, hence
\[
I(f)\ge0.
\]
So $I$ is a positive linear functional on $C_c(X)$.
:::

<1>2. Define the candidate measure and prove that it is Radon.
::: proof
For each Borel set $E\subseteq X$, define
\[
\nu(E):=\mu(E\cap Y).
\]
Since $Y$ is closed, $E\cap Y$ is Borel in $Y$, and countable additivity of $\nu$ follows directly from that of $\mu$.

If $K\subseteq X$ is compact, then $K\cap Y$ is compact in $Y$, so
\[
\nu(K)=\mu(K\cap Y)<\infty.
\]

For inner regularity, let $E$ be Borel. Since $\mu$ is Radon on $Y$,
\[
\begin{aligned}
\nu(E)
&=\mu(E\cap Y)\\
&=\sup\{\mu(K):K\subseteq E\cap Y,\ K\text{ compact in }Y\}.
\end{aligned}
\]
Every such $K$ is also compact in $X$, and $\nu(K)=\mu(K)$, so
\[
\nu(E)=\sup\{\nu(K):K\subseteq E,\ K\text{ compact in }X\}.
\]

For outer regularity, let $E\subseteq X$ be Borel and $\varepsilon>0$. Choose an open set $W\subseteq Y$ with
\[
E\cap Y\subseteq W,
\qquad
\mu(W)\le\mu(E\cap Y)+\varepsilon.
\]
Write $W=V\cap Y$ for some open $V\subseteq X$, and set
\[
U:=V\cup(X\setminus Y).
\]
Then $U$ is open in $X$, contains $E$, and
\[
U\cap Y=W.
\]
Hence
\[
\nu(U)=\mu(W)\le\nu(E)+\varepsilon.
\]
Thus $\nu$ is outer regular as well. Therefore $\nu$ is a Radon measure on $X$.
:::

<1>3. Show that $I$ is integration against $\nu$.
::: proof
For every nonnegative Borel measurable function $h$ on $X$, the definition of $\nu$ gives
\[
\int_X h\,d\nu=\int_Y h|_Y\,d\mu;
\]
this follows first for indicators, then for simple functions, and finally by monotone convergence.

Applying this identity to the positive and negative parts of $f\in C_c(X)$ yields
\[
\int_X f\,d\nu
=\int_Y f|_Y\,d\mu
=I(f).
\]

The Riesz--Markov theorem says that a positive linear functional on $C_c(X)$ is represented by a unique Radon measure. Since $\nu$ is Radon and represents $I$, it is precisely the measure supplied by that theorem. Therefore
\[
\boxed{\nu(E)=\mu(E\cap Y)}
\]
for every Borel set $E\subseteq X$.
:::
:::
