---
schema: qual/card@1
id: S-SG5NL
kind: solution
title: Solution to P-AE7QC
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-AE7QC
review: draft
---

:::{.solution}
(a) This requires showing the existence of some $f\in L^1$ with $\int f_n g \to \int fg$ for all $g\in L^\infty$. Since $L^\infty([0,1])\subseteq L^1([0,1])$, this conclusion is implied by part (b) below.

(b) We need to find some $f\in L^\infty$ such that $\int f_n g \to \int fg$ for all $g\in L^1$. First note that each $f_n$ is $1/n$-periodic, so we have
$$\int_0^1 f_n(x)\,dx = \int_0^1 \exp(\sin(2\pi n x))\,dx = n\int_0^{1/n} \exp(\sin(2\pi n x))\,dx = \int_0^1 \exp(\sin(2\pi u))\,du = \int_0^1 f_1(u)\,du.$$
Thus the quantity $\int_0^1 f_n(x)\,dx$ is independent of $n$. By viewing this as the dual pairing with the constant function 1, we see that if the weak limit $f$ exists it must be equal to the constant $C:=\int_0^1 \exp(\sin(2\pi u))\,du$.

So we need to show that $\int_0^1 f_n g \to C\int_0^1 g$ for any $g\in L^1$. We do this with a standard density argument. Suppose we knew the desired conclusion for all $\phi$ in some family $\mathcal{F}$ dense in $L^1$. Then for any $g\in L^1$, let $\phi_k$ be a sequence in $\mathcal{F}$ converging to $g$, then we have
$$\left|\int f_n g - C\int g\right| \le \left|\int f_n g - \int f_n \phi_k\right| + \left|\int f_n \phi_k - C\phi_k\right| \le e\cdot||g-\phi_k||_{L^1} + \left|\int f_n\phi_k - C\phi_k\right|$$
because each $f_n$ is bounded uniformly by $e$. For a fixed $k$, take $n\to\infty$ and the second term on the right goes to zero by assumption on the $\phi_k$. Then take $k\to\infty$ and the first term also goes to zero by construction, so the desired result follows. Now we just need to prove the desired result for a dense family $\mathcal{F}$. We take $\mathcal{F}$ to be the set of linear combinations of characteristic functions of closed intervals. Since the desired property is linear, it's enough to verify for the characteristic function $g=\chi_{[a,b]}$. We need to show that $\int_a^b \exp(\sin(2\pi n x))\,dx \to C(b-a)$ as $n\to\infty$. Let $a_n$ be the least number of the form $q/n>a$ and $b_n$ be the greatest number of the form $q/n<b$. Then we write, using the periodicity,
$$\int_a^b \exp(\sin(2\pi n x))\,dx = \left(\int_a^{a_n} + \int_{b_n}^b + (\lfloor(b-a)n\rfloor-2)\int_{a_n}^{a_n+1/n}\right)\exp(\sin(2\pi n x))\,dx$$
$$= e(a_n-a)+e(b-b_n)+(\lfloor(b-a)n\rfloor-2)\int_0^{1/n}\exp(\sin(2\pi n x))\,dx$$
$$= e(a_n-a)+e(b-b_n)+\frac{\lfloor(b-a)n\rfloor-2}{n}C$$
which tends to $(b-a)C$ as $n\to\infty$, so we're done. $\square$
:::
