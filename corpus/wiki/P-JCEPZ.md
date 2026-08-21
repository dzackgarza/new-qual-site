---
schema: qual/card@1
id: P-JCEPZ
kind: problem
title: Convergence and limit of $x_{n+1}=\frac{1+x_n}{2+x_n}$ with $x_1>0$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Fixed Points
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Let $\left\{x_{n}\right\}_{n-1}^{\infty}$ be a sequence of real numbers such that $x_{1}>0$ and
\[
x_{n+1}=1-\left(2+x_{n}\right)^{-1}=\frac{1+x_{n}}{2+x_{n}} \text {. }
\]
Prove that the sequence $\left\{x_{n}\right\}$ converges, and find its limit.
:::


:::{.solution}
If a limit $L$ exists, we have $x_n\to L$ for all $n$, so
\[
L = {1+L\over 2+L} \implies L^2 + L - 1 = 0 \implies L = -{1\over 2}\qty{-1 \pm \sqrt 5}
.\]
Noting that $\sqrt{5} > 1$, the condition $x_1>0$ and a small induction noting that if $x_n>0$ then ${1+x_n \over 2+x_n}>0$, the only solution can be $L = -1 + \sqrt 5$.
To see that this does converge, write $f(z) = 1 - (2+z)\inv$ so that $x_{n+1} = f(x_n)$.
The claim is that $f$ is a contracting map on a metric space, which implies it has a unique fixed point $z_0$ by the Banach fixed point theorem, and if $f(z_0) = z_0$ then $z_0 = L$.
This follows from the mean value theorem, since
\[
\abs{f(z) - f(w)} = \abs{f'(\xi)}\abs{z-w} < \abs{z-w} && \text{for some } \xi \in (z, w)
.\]
Since $f'(z) = (2+z)^{-2}$ satisfies $0 < f'(z) < 1$ for all $z$, we have
\[
\abs{f(z) - f(w)} \leq \abs{z-w}
.\]
:::
