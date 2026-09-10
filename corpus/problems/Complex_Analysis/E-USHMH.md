---
schema: qual/card@1
id: E-USHMH
kind: problem
title: Product of sines $\sin(k\pi/n)$ via roots of unity
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: exercise
Use $n$th roots of unity to show that $2^{n-1}\sin\frac{\pi}{n}\sin\frac{2\pi}{n}\cdots\sin\frac{(n-1)\pi}{n}=n$.

- ![[_attachments/Pasted image 20210517025227.png]]

- ![[_attachments/Pasted image 20210517025152.png]]

- ![[_attachments/Pasted image 20210517024749.png]]

- ![[_attachments/Pasted image 20210517024557.png]]

- ![[_attachments/Pasted image 20210517023333.png]]

- ![[_attachments/Pasted image 20210517024431.png]]

- ![[_attachments/Pasted image 20210517024807.png]]

- ![[_attachments/Pasted image 20210517030008.png]]

- ![[_attachments/Pasted image 20210517030118.png]]

- ![[_attachments/Pasted image 20210517030226.png]]

- ![[_attachments/Pasted image 20210517030343.png]]

- ![[_attachments/Pasted image 20210517030440.png]]
:::

::: solution
Let $\zeta=e^{2\pi i/n}$. From
\[
z^n-1=(z-1)\prod_{k=1}^{n-1}(z-\zeta^k)
\]
we obtain, after dividing by $z-1$ and setting $z=1$,
\[
n=\prod_{k=1}^{n-1}(1-\zeta^k).
\]
Taking absolute values gives
\[
n=\prod_{k=1}^{n-1}|1-e^{2\pi i k/n}|.
\]
For real $\theta$,
\[
|1-e^{i\theta}|=2\left|\sin\frac\theta2\right|.
\]
Since $0<k\pi/n<\pi$ for $1\le k\le n-1$, all these sines are positive.
Therefore
\[
n=\prod_{k=1}^{n-1}2\sin\frac{k\pi}{n}
=2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n},
\]
as required.
:::
