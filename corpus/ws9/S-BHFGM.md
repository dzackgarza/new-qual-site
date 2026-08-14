---
schema: qual/card@1
id: S-BHFGM
kind: solution
title: Solution to P-DQNN6
classification:
  areas:
  - real-analysis
  topics:
  - density
  - measure-theory
  - convergence-of-integrals
relations:
- kind: solves
  target: P-DQNN6
review: draft
---

:::{.solution}
By the definition, we see that $\{a_n\}$ is equi-distributed iff for all interval $[c,d]\subset[0,1]$, $\lim_{n\to\infty}\int \chi_{[c,d]}d\mu_n = \int \chi_{[c,d]}dm$.

Then if $\lim_{n\to\infty}\int f d\mu_n = \int f dm$ for all $f\in C[0,1]$. For any interval $[c,d]$, define continuous functions $1\ge f_n\ge 0$ ($n>N$ for some proper $N$) with $f_n=1$ on $[c,d]$ and $\text{supp}(f_n)\subset[c-1/n,d+1/n]$ such that $f_n\downarrow \chi_{[c,d]}$. Then for all $\epsilon>0$, there is a $K$ such that whenever $k>K$, $\mu_k[c,d]\le \int f_n d\mu_k \le \int f_n dm + \epsilon \le \mu[c,d]+2/n+\epsilon$.

Note that this $K$ depend on the interval $[c,d]$. Use this argument for $[c-1/n,c]$ and $[d,d+1/n]$, for the $\epsilon$, for each $n$, there is a $K_n$ such that whenever $k>K_n$, $\int|f_n-\chi_{[c,d]}|d\mu_k \le \int \chi_{[c-1/n,c]}d\mu_k+\int\chi_{[d,d+1/n]}d\mu_k\le 4/n+\epsilon$. In addition, $\int|f_n-\chi_{[c,d]}|dm\le 2/n$ also holds. Now, fix a $n$ big enough such that $6/n<\epsilon$ and $|\int f_n d\mu_k - \int f_n dm| < \epsilon$. This implies that whenever $k>K_n$, $|\int \chi_{[c,d]}d\mu_k - \int \chi_{[c,d]}dm| \le \int|f_n-\chi_{[c,d]}|d\mu_k + |\int f_n d\mu_k - \int f_n dm| + \int |f_n-\chi_{[c,d]}|dm \le 6/n+2\epsilon < 3\epsilon$. We are done.

In the converse, If for all interval $[c,d] \subset [0,1]$, $\lim_{n\to\infty} \int \chi_{[c,d]} d\mu_n = \int \chi_{[c,d]} dm$. Then we pass to all step functions. For any continuous function $f \in C[0,1]$, we can use step functions to approximate $f$ under the norm $\|\cdot\|_\infty$, say for every $\epsilon>0$, there is a $0=x_0<x_1<\dots<x_N=1$ such that for all $n\le N$, $|\max_{x_n\le x\le x_{n+1}} f(x) - \min_{x_n\le x\le x_{n+1}} f(x)|<\epsilon$. Now, define $g=\sum_{n=0}^N a_n \chi_{[x_n,x_{n+1}]}$ where $a_n$ is an arbitrary number between $\min_{x_n\le x\le x_{n+1}} f(x)$ and $\max_{x_n\le x\le x_{n+1}} f(x)$. Thus $\|g-f\|_\infty<\epsilon$. Now, for the $\epsilon$, there is a $K$ such that whenever $k>K$, $|\int g d\mu_k - \int g dm|<\epsilon$ and thus $|\int f d\mu_k-\int f dm|\le |\int f d\mu_k-\int g d\mu_k|+|\int g d\mu_k-\int g dm|+|\int f dm-\int g dm|<2\|f-g\|_\infty+\epsilon<3\epsilon$. We are done.
:::
