---
schema: qual/card@1
id: P-APAF18B
kind: problem
title: Entrywise $\ell^3$ decay of powers when all eigenvalues satisfy $|\lambda|<1$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $A\in\mathbb{C}^{n\times n}$ be a matrix such that $|\lambda_i|<1$ for all its eigenvalues $\lambda_i$.
Let $B_k=A^k$.
Do we necessarily have
\[
\lim_{k\to\infty}\Biggl(\sum_{i,j=1}^{n}\bigl|(B_k)_{ij}\bigr|^3\Biggr)=0?
\]
If yes, give a proof; if no, give a counterexample.
:::

::: {.solution}
Yes.

<1>1. It is enough to prove that $A^k\to0$ entrywise.
::: {.proof}
If $(A^k)_{ij}\to0$ for every pair $(i,j)$, then for each fixed $(i,j)$,
\[
|(A^k)_{ij}|^3\to0.
\]
There are only $n^2$ terms, so
\[
\sum_{i,j=1}^n |(A^k)_{ij}|^3\longrightarrow0.
\]
:::

<1>2. Put $A=PJP^{-1}$ in Jordan canonical form. Then it is enough to prove that $J^k\to0$ entrywise.
::: {.proof}
One has
\[
A^k=PJ^kP^{-1}.
\]
Each entry of $A^k$ is therefore a fixed finite linear combination of entries of $J^k$. Hence entrywise convergence $J^k\to0$ implies entrywise convergence $A^k\to0$.
:::

<1>3. Let
\[
J_m(\lambda)=\lambda I+N
\]
be a Jordan block of size $m$, where $N^m=0$. Then
\[
J_m(\lambda)^k
=\sum_{r=0}^{m-1}\binom{k}{r}\lambda^{k-r}N^r.
\]
::: {.proof}
The matrices $\lambda I$ and $N$ commute, so the binomial theorem gives
\[
(\lambda I+N)^k
=\sum_{r=0}^{k}\binom{k}{r}\lambda^{k-r}N^r.
\]
Since $N^r=0$ for $r\ge m$, all terms with $r\ge m$ vanish.
:::

<1>4. If $|\lambda|<1$, then
\[
J_m(\lambda)^k\longrightarrow0
\]
entrywise as $k\to\infty$.
::: {.proof}
If $\lambda=0$, then $J_m(0)=N$ and $J_m(0)^k=0$ for every $k\ge m$.

Assume $0<|\lambda|<1$. For every fixed $r<m$,
\[
\left|\binom{k}{r}\lambda^{k-r}\right|
\le \frac{k^r}{r!}|\lambda|^{k-r}
=\frac{|\lambda|^{-r}}{r!}k^r|\lambda|^k.
\]
For every $0<q<1$ and every fixed nonnegative integer $r$,
\[
k^rq^k\to0.
\]
Indeed,
\[
\frac{(k+1)^rq^{k+1}}{k^rq^k}
=q\left(1+\frac1k\right)^r\longrightarrow q<1,
\]
so the sequence eventually decreases geometrically to $0$.
Taking $q=|\lambda|$ shows that every scalar coefficient in <1>3 tends to $0$. Since the sum in <1>3 has only finitely many fixed matrices $N^r$, every entry of $J_m(\lambda)^k$ tends to $0$.
:::

<1>5. Therefore $A^k\to0$ entrywise, and hence
\[
\boxed{\lim_{k\to\infty}\sum_{i,j=1}^{n}|(A^k)_{ij}|^3=0}.
\]
::: {.proof}
Every Jordan block of $J$ has eigenvalue $\lambda$ satisfying $|\lambda|<1$ by hypothesis. Thus <1>4 applies to every block, so $J^k\to0$ entrywise. By <1>2, $A^k\to0$ entrywise, and <1>1 gives the stated limit.
:::
:::
