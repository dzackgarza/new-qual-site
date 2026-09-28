---
schema: qual/card@1
id: P-AE7QC
kind: problem
title: Weak $L^1$ and weak-$*$ $L^\infty$ convergence of $\exp(\sin(2\pi nx))$ on
  $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - L¹
  - L∞
relations: []
review: draft
---

::: {.problem}
Consider the following sequence of functions: $$f_n:[0,1]\to\mathbb{R} \quad \text{by} \quad f_n(x) = \exp(\sin(2\pi n x)).$$

a. Prove that $f_n$ converges weakly in $L^1([0,1])$.

b. Prove that $f_n$ converges weak-$*$ in $L^\infty([0,1])$, viewed as the dual of $L^1([0,1])$.
:::

::: {.solution}
(a) Weak convergence in $L^1([0,1])$ means that there is $f\in L^1$ with $\int f_n g \to \int fg$ for all $g\in L^\infty$.
Since $L^\infty([0,1])\subseteq L^1([0,1])$, part (b) implies part (a).

(b) We find $f\in L^\infty$ such that $\int f_n g \to \int fg$ for all $g\in L^1$.
Each $f_n$ is $1/n$-periodic, so $$\int_0^1 f_n(x)\,dx = \int_0^1 \exp(\sin(2\pi n x))\,dx = n\int_0^{1/n} \exp(\sin(2\pi n x))\,dx = \int_0^1 \exp(\sin(2\pi u))\,du = \int_0^1 f_1(u)\,du.$$ Thus the quantity $\int_0^1 f_n(x)\,dx$ is independent of $n$.
By viewing this as the dual pairing with the constant function 1, we see that if the weak limit $f$ exists it must be equal to the constant $C:=\int_0^1 \exp(\sin(2\pi u))\,du$.

It remains to show that $\int_0^1 f_n g \to C\int_0^1 g$ for every $g\in L^1$.
We use a density argument.
Suppose the convergence holds for all $\phi$ in some family $\mathcal{F}$ dense in $L^1$.
Then for any $g\in L^1$, let $\phi_k$ be a sequence in $\mathcal{F}$ converging to $g$, then we have $$\left|\int f_n g - C\int g\right| \le \left|\int f_n g - \int f_n \phi_k\right| + \left|\int f_n \phi_k - C\int\phi_k\right| + C\left|\int\phi_k-\int g\right| \le 2e\cdot||g-\phi_k||_{L^1} + \left|\int f_n\phi_k - C\int\phi_k\right|$$ because each $f_n$ is bounded uniformly by $e$ and $C\le e$.
For a fixed $k$, take $n\to\infty$ and the second term on the right goes to zero by assumption on the $\phi_k$.
Then take $k\to\infty$ and the first term also goes to zero by construction, so $\int f_n g\to C\int g$.
It remains to prove the convergence for a dense family $\mathcal{F}$.
We take $\mathcal{F}$ to be the set of linear combinations of characteristic functions of closed intervals.
The convergence is linear in $g$, so it suffices to take $g=\chi_{[a,b]}$ and to show that $\int_a^b \exp(\sin(2\pi n x))\,dx \to C(b-a)$ as $n\to\infty$.
Let $a_n=\lceil na\rceil/n$ and $b_n=\lfloor nb\rfloor/n$, so that $0\le a_n-a<1/n$ and $0\le b-b_n<1/n$; for $n>2/(b-a)$ we have $a_n<b_n$.
The interval $[a_n,b_n]$ is the union of $n(b_n-a_n)$ periods of $f_n$, and each period contributes $\int_0^{1/n}\exp(\sin(2\pi n x))\,dx=C/n$.
Hence $$\int_a^b \exp(\sin(2\pi n x))\,dx = \int_a^{a_n}f_n + \int_{b_n}^b f_n + (b_n-a_n)C.$$ Since $0<f_n\le e$, the first two terms lie in $[0,2e/n]$, and $b_n-a_n\to b-a$, so the right side tends to $(b-a)C$ as $n\to\infty$.
$\square$
:::
