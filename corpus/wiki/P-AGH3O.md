---
schema: qual/card@1
id: P-AGH3O
kind: problem
title: "Consider the function"
classification:
  areas:
  - real-analysis
  topics:
  - maximal-functions
  - l1
  - counterexamples
relations: []
review: draft
---

::: problem
Consider the function
\[
f(x) \da 
\begin{cases}
{1\over \abs{x} \qty{ \log\qty{1\over x}}^2 } &  \abs{x} \leq {1\over 2}
\\
0 & \text{else}.
\end{cases}
\]

a. Show that $f \in L^1(\RR)$.

b. Show that there exists a $c>0$ such that for all $\abs{x} \leq 1/2$,
\[
Hf(x) \geq {c \over \abs{x} \log\qty{1\over \abs x} }
.\]
Conclude that $Hf$ is not locally integrable.
:::

::: {.solution}
> **AI-Generated Solution**

**Honesty note:** the formula as printed uses $\log(1/x)$, which is undefined for $x < 0$; the intended (standard) function is symmetric, $f(x) = \frac{1}{|x|\log^2(1/|x|)}$ for $0 < |x| \le 1/2$ and $0$ otherwise. The solution uses that version.

<1>1. $f \in L^1(\RR)$.
    <2>1. $\int_\RR f = 2\int_0^{1/2}\frac{dx}{x\log^2(1/x)}$.
        Proof: symmetry of $f$ about $0$.
    <2>2. $\int_0^{1/2}\frac{dx}{x\log^2(1/x)} = \int_{\log 2}^\infty u^{-2}\,du = \frac{1}{\log 2} < \infty$.
        Proof: substitute $u = \log(1/x)$, $du = -dx/x$; as $x \to 0^+$, $u \to \infty$; at $x = 1/2$, $u = \log 2$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 give $\int f = 2/\log 2 < \infty$.

<1>2. For $0 < x \le 1/2$: $Hf(x) \ge \frac{2}{3x\log(1/x)}$ (and symmetrically for negative $x$), where $Hf$ is the Hilbert transform $Hf(x) = \mathrm{p.v.}\int_\RR \frac{f(t)}{x - t}\,dt$ (up to a convention constant).
    <2>1. Restrict the integral to $|t| < x/2$: $Hf(x) \ge \int_{-x/2}^{x/2}\frac{f(t)}{x - t}\,dt \ge \frac{2}{3x}\int_{-x/2}^{x/2}f(t)\,dt$.
        Proof: on $|t| < x/2$, $x - t \ge x - x/2 = x/2$... more carefully $x - t \le x + x/2 = 3x/2$, so $\frac{1}{x - t} \ge \frac{2}{3x} > 0$; and the excluded p.v. region $|t - x| < \eps$ lies outside $|t| < x/2$ for $\eps < x/2$, so this is a genuine lower bound on the truncated integral.
    <2>2. $\int_{-x/2}^{x/2}f(t)\,dt = 2\int_0^{x/2}\frac{dt}{t\log^2(1/t)} = \frac{2}{\log(2/x)}$.
        Proof: substitute $u = \log(1/t)$: $2\int_{\log(2/x)}^\infty u^{-2}du = \frac{2}{\log(2/x)}$.
    <2>3. $\frac{2}{\log(2/x)} \ge \frac{1}{\log(1/x)}$ for $0 < x \le 1/2$.
        Proof: $\log(2/x) = \log(1/x) + \log 2 \le 2\log(1/x)$ since $\log(1/x) \ge \log 2$.
    <2>4. Q.E.D.
        Proof: <2>1, <2>2, and <2>3 give $Hf(x) \ge \frac{2}{3x}\cdot\frac{1}{\log(1/x)}$, i.e. the claim with $c = 2/3$.

<1>3. $Hf$ is not locally integrable.
    <2>1. $\int_{-1/2}^{1/2}|Hf(x)|\,dx \ge c\int_0^{1/2}\frac{dx}{x\log(1/x)}$.
        Proof: <1>2 gives $|Hf(x)| = Hf(x) \ge \frac{c}{x\log(1/x)}$ for $x \in (0, 1/2]$ (the transform of the even $f$ is odd, and the bound is symmetric).
    <2>2. $\int_0^{1/2}\frac{dx}{x\log(1/x)} = \infty$.
        Proof: substitute $u = \log(1/x)$: $\int_{\log 2}^\infty \frac{du}{u} = \infty$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 show $\int_{-1/2}^{1/2}|Hf| = \infty$, so $Hf$ is not integrable on any neighborhood of $0$.
:::
