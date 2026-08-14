---
schema: qual/card@1
id: P-NVVZJ
kind: problem
title: "Let $f\\in L^1([0, 1])$. Prove that $\\lim_{n \\to \\infty} \\int_{0}^{1} f(x) \\abs{\\sin n x} ~d x= \\frac{2}{\\pi} \\int_{0}^{1} f(x) ~d x$ Converting floor/ceiling functions to\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - l1
relations: []
review: draft
---
Let $f\in L^1([0, 1])$.
Prove that
\[
\lim_{n \to \infty} \int_{0}^{1} f(x) \abs{\sin n x} ~d x= \frac{2}{\pi} \int_{0}^{1} f(x) ~d x
\]

> Hint: Begin with the case that $f$ is the characteristic function of an interval.

:::{.solution}
\envlist
:::{.concept}
\envlist
- Converting floor/ceiling functions to inequalities: $x-1 \leq \floor{x} \leq x$.
:::

Case of a characteristic function of an interval $[a, b]$:

- First suppose $f(x) = \chi_{[a, b]}(x)$.
- Note that $\sin(nx)$ has a period of $2\pi/n$, and thus $\floor{ (b-a) \over (2\pi / n)} = \floor{n(b-a)\over 2\pi}$ full periods in $[a, b]$.
- Taking the absolute value yields a new function with half the period
  - So $\abs{\sin(nx)}$ has a period of $\pi/n$ with $\floor{n(b-a) \over \pi}$ full periods in $[a, b]$.
- We can compute the integral over one full period (which is independent of *which* period is chosen)
  - We can use translation invariance of the integral to compute this over the period $0$ to $\pi/n$.
  - Since $\sin(nx)$ is positive, it equals $\abs{\sin(nx)}$ on its first period, so we have
\[
\int_{\text{One Period}} \abs{\sin(nx)} \, dx 
&= \int_0^{\pi/n} \sin(nx)\,dx \\
&= {1\over n} \int_0^\pi \sin(u) \,du \quad u = nx \\
&= {1\over n} \qty{-\cos(u)\mid_0^\pi} \\
&= {2 \over n}
.\]

- Then break the integral up into integrals over full periods $P_1, P_2, \cdots, P_N$ where $N \definedas \floor{n(b-a)/\pi}$
- Noting that each period is of length $\pi\over n$, so letting $L_n$ be the regions falling *outside* of a full period, we have

- Thus
\[
\int_a^b \abs{\sin(nx)} \, dx 
&= \qty{ \sum_{j=1}^{N} \int_{P_j} \abs{\sin(nx)} \, dx } +  \int_{L_n} \abs{\sin(nx)}\,dx \\
&= \qty{ \sum_{j=1}^{N} {2\over n} } +  \int_{L_n} \abs{\sin(nx)}\,dx \\
&= N \qty{2\over n} +  \int_{L_n} \abs{\sin(nx)}\,dx \\
&\definedas \floor{(b-a) n \over \pi} {2\over n} +  R_n \\
&\definedas (b-a)C_n + R_n 
\]
  where (claim) $C_n \converges{n\to\infty}\to {2\over \pi}$ and $R(n) \converges{n\to\infty}\to 0$. 

- $C_n \to {2\over \pi}$:
\[  
{n-1 \over n} \qty{2\over \pi} = {n-1 \over \pi} \qty{2\over n} \leq \floor{n\over \pi}\qty{2\over n} \leq {n \over \pi}\qty{2\over n} = {2 \over \pi}
,\]
  then use the fact that ${n-1 \over n} \to 1$.
  - Then equality follows by the Squeeze theorem.

- $R_n \to 0$:
  - We use the fact that $m(L_n) \to 0$, then $\int_{L_n} \abs{\sin(nx)} \leq \int_{L_n} 1 = m(L_n) \to 0$.
  - This follows from the fact that $L_n$ is the complement of $\union_j P_j$, the set of full periods, so
\[  
m(L_n) 
&= m(b-a) - \sum m(P_j) \\
&= \qty{b-a} -  \floor{n(b-a) \over \pi}\qty{\pi \over n} \\
&\converges{n\to \infty}\to (b-a) - (b-a) \\
&= 0
.\]
  where we've used the fact that
\[  
\qty{\pi \over n} \qty{(b-a)n-1 \over \pi} 
&\leq \floor{n(b-a) \over \pi}\qty{\pi \over n}  \\
&\leq \qty{\pi \over n} \qty{(b-a)n\over \pi}  \\
&= (b-a)
,\]
  then taking $n\to \infty$ sends the LHS to $b-a$, forcing the middle term to be $b-a$ by the Squeeze theorem.

General case:

- By linearity of the integral, the result holds for simple functions:
  - If $f = \sum c_j \chi_{E_j}$ where $E_j = [a_j, b_j]$, we have
  \[  
  \int_0^1 f(x) \abs{\sin(nx)}\,dx 
  &= \int_0^1 \sum c_j \chi_{E_j}(x) \abs{\sin(nx)}\,dx  \\
  &= \sum c_j \int_0^1 \chi_{E_j}(x) \abs{\sin(nx)}\,dx \\
  &= \sum c_j (b_j - a_j) {2\over \pi} \\
  &= {2\over \pi} \sum c_j (b_j - a_j) \\
  &= {2\over \pi} \sum c_j m(E_j) \\
  &\definedas {2\over \pi} \int_0^1 f
  .\]
- Since $f\in L^1$, where simple functions are dense, choose $s_n\nearrow f$ where $\norm{s_N - f}_1 < \eps$, then
\[  
\abs{ \int_0^1 f(x) \abs{\sin(nx)} \,dx - \int_0^1 s_N(x) \abs{\sin(nx)}\,dx } 
&= \abs{ \int_0^1 \qty{f(x) - s_N(x)} \abs{\sin(nx)} \,dx } \\
&\leq \int_0^1 \abs{ f(x) - s_N(x)} \abs{\sin(nx)} \,dx \\
&= \norm{ \qty{f - s_N} \abs{\sin(nx)} }_1 \\
&\leq \norm{f-s_N}_1 \cdot \norm{\abs{\sin(nx)}}_\infty \quad\text{by Holder}\\
&\leq \eps \cdot 1
,\]

- So the integrals involving $s_N$ converge to the integral involving $f$, and
\[
\lim_{n\to\infty} \int f(x)\abs{\sin(nx)} 
&= \lim_{n\to\infty} \lim_{N\to\infty} \int s_N(x) \abs{\sin(nx)} \\
&= \lim_{N\to\infty} \lim_{n\to\infty} \int s_N(x) \abs{\sin(nx)} \quad\text{because ?}\\
&= \lim_{N\to \infty} {2\over \pi} \int s_N(x) \\
&= {2\over \pi} \int f
,\]
  which is the desired result.
:::
