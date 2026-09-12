---
schema: qual/card@1
id: P-RAF06A
kind: problem
title: "True or false: five statements in measure theory and functional analysis"
classification:
  areas:
  - real-analysis
  topics:
  - Borel Measures
  - Stone-Weierstrass
  - Radon-Nikodym
  - Uniform Boundedness Principle
  - Banach-Alaoglu Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample.

(a) Let $\mu$ be a Borel measure on $\mathbb{R}$ such that $\mu(B) < \infty$ for every bounded Borel set $B$.
Let $E$ be a Borel set and assume that $\mu(K) = 0$ for every compact set $K \subset E$.
Then $\mu(E) = 0$.

(b) Let $f : [-1, 1] \to \mathbb{R}$ be continuous with $f(0) = 0$.
For every $\varepsilon > 0$, there exists an integer $n \geq 1$ and continuous functions $u_j : [-1, 1] \to \mathbb{R}$, $j = 1, \ldots, n$, such that $u_j(x) = 0$ only at $x = 0$ and $\sup_{x \in [-1,1]} \left|f(x) - \sum_{j=1}^n u_j(x)\right| < \varepsilon$.

(c) Let $\nu$ be a complex measure and $\mu$ a (positive) measure on $(X, \mathcal{M})$.
Suppose that $X = A \cup B$ with $A \cap B = \emptyset$ and $\nu(A) = 0$.
Moreover, assume that there is a measurable function $f : B \to \mathbb{C}$ such that $\nu(E) = \int_E f \, d\mu$ for every measurable $E \subset B$.
Then there is a measurable function $g : X \to \mathbb{C}$ such that $\nu = g \, d\mu$.

(d) Let $\{f_n\}$ be a sequence in $L^4(X, \mu)$.
Suppose that $\lim_{n \to \infty} \int_X f_n g \, d\mu$ exists (as a complex number) for every $g \in L^{4/3}(X, \mu)$.
Then there is $M > 0$ such that $\|f_n\|_4 \leq M$ for every $n$.

(e) Let $\{f_n\}$ be a sequence in $L^4(X, \mu)$.
Suppose that there is $M > 0$ such that $\|f_n\|_4 \leq M$ for every $n$.
Then there is a subsequence $\{f_{n_k}\}$ such that $\lim_{k \to \infty} \int_X f_{n_k} g \, d\mu$ exists (as a complex number) for every $g \in L^{4/3}(X, \mu)$.
:::

::: solution
<1>1. Part (a) is true.
::: proof
The assumption that $\mu(B)<\infty$ for every bounded Borel set makes $\mu$ locally finite. A locally finite Borel measure on $\mathbb R$ is a Radon measure, hence is inner regular on Borel sets. Therefore
\[
\mu(E)=\sup\{\mu(K):K\subseteq E,\ K\text{ compact}\}.
\]
Every compact $K\subseteq E$ has $\mu(K)=0$ by hypothesis, so
\[
\boxed{\mu(E)=0.}
\]
:::

<1>2. Part (b) is true.
::: proof
Define
\[
\eta(x):=|f(x)|+|x|.
\]
Then $\eta$ is continuous, $\eta(0)=0$, and $\eta(x)>0$ for every $x\ne0$. Put
\[
u_1(x):=f(x)+\eta(x),
\qquad
u_2(x):=-\eta(x).
\]
Both are continuous and
\[
u_1+u_2=f.
\]
Moreover, $u_2$ vanishes only at $0$. For $x\ne0$,
\[
u_1(x)=f(x)+|f(x)|+|x|>0,
\]
so $u_1$ also vanishes only at $0$. Thus the required approximation holds exactly with $n=2$:
\[
\sup_{[-1,1]}|f-u_1-u_2|=0<\varepsilon.
\]
:::

<1>3. Part (c) is false.
::: proof
Let
\[
X=\{1,2,3\},\qquad
A=\{1,2\},\qquad
B=\{3\},
\]
with the full power-set sigma-algebra. Define the positive measure $\mu$ by
\[
\mu(\{1\})=\mu(\{2\})=0,
\qquad
\mu(\{3\})=1,
\]
and define the complex measure $\nu$ by
\[
\nu(\{1\})=1,
\qquad
\nu(\{2\})=-1,
\qquad
\nu(\{3\})=0.
\]
Then $\nu(A)=0$. On $B$, taking $f\equiv0$ gives
\[
\nu(E)=\int_E f\,d\mu
\]
for every measurable $E\subseteq B$.

If there were a measurable $g:X\to\mathbb C$ with $\nu=g\,d\mu$, then
\[
\nu(\{1\})=\int_{\{1\}}g\,d\mu=0,
\]
contradicting $\nu(\{1\})=1$. Hence the assertion is false. The missing condition is domination on all measurable subsets of $A$, equivalently $|\nu|(A)=0$, not merely $\nu(A)=0$.
:::

<1>4. Part (d) is true.
::: proof
For each $n$, define
\[
T_n:L^{4/3}(X,\mu)\to\mathbb C,
\qquad
T_n(g)=\int_X f_ng\,d\mu.
\]
By Hölder's inequality, $T_n$ is bounded and
\[
\|T_n\|\le\|f_n\|_4.
\]
Conversely, if $f_n\ne0$, choose
\[
g_n=\frac{\overline{f_n}|f_n|^2}{\|f_n\|_4^3}.
\]
Then $\|g_n\|_{4/3}=1$ and
\[
T_n(g_n)=\|f_n\|_4,
\]
so
\[
\|T_n\|=\|f_n\|_4.
\]

For every fixed $g\in L^{4/3}$, the scalar sequence $T_n(g)$ converges by hypothesis, hence is bounded. Since $L^{4/3}$ is Banach, the Uniform Boundedness Principle gives
\[
\sup_n\|T_n\|<\infty.
\]
Therefore
\[
\boxed{\sup_n\|f_n\|_4<\infty.}
\]
:::

<1>5. Part (e) is true.
::: proof
For $1<p<\infty$, the Banach space $L^p(X,\mu)$ is reflexive. Hence the closed ball
\[
\{f\in L^4:\|f\|_4\le M\}
\]
is weakly compact. By the Eberlein--Smulian theorem, weak compactness in a Banach space is equivalent to weak sequential compactness. Therefore the bounded sequence $(f_n)$ has a weakly convergent subsequence $(f_{n_k})$.

Thus there exists $f\in L^4(X,\mu)$ such that for every $g\in L^{4/3}(X,\mu)$,
\[
\int_X f_{n_k}g\,d\mu
\longrightarrow
\int_X fg\,d\mu.
\]
In particular, the required scalar limit exists for every $g\in L^{4/3}$.
:::
:::
