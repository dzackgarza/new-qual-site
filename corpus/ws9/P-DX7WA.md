---
schema: qual/card@1
id: P-DX7WA
kind: problem
title: Let $f(z)$ be an analytic function on the entire complex plane $\mathb…
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
Let $f(z)$ be an analytic function on the entire complex plane $\mathbb{C}$ and assume $f(0)\ne 0$. Let $\{a_n\}$ be the zeros of $f$, counted with multiplicity.

a. Let $R>0$ be such that $|f(z)|>0$ on $|z|=R$. Prove
$$\frac{1}{2\pi}\int_0^{2\pi} \log|f(Re^{i\theta})|\,d\theta = \log|f(0)| + \sum_{|a_n|<R} \log\left(\frac{R}{|a_n|}\right).$$

b. Assume $|f(z)|\le Ce^{|z|^\lambda}$ for positive constants $C$ and $\lambda$. Prove that
$$\sum_n \left(\frac{1}{|a_n|}\right)^{\lambda+\epsilon} < \infty$$
for all $\epsilon>0$.
:::
