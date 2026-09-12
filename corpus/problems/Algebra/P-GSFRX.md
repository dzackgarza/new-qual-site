---
schema: qual/card@1
id: P-GSFRX
kind: problem
title: Minimal and characteristic polynomials of a $5\times 5$ real matrix with eigenvalues
  $0,1\pm i,1\pm 2i$
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $L \in M_5(\mathbb{R})$ be a $5 \times 5$ real matrix with eigenvalues $0, 1 + i, 1 + 2i$.
Find the characteristic polynomial $\chi_L(x)$ and the minimal polynomial $\mu_L(x)$ of $L$ over $\mathbb{R}$.
:::

::: solution
Because $L$ has real entries, nonreal eigenvalues occur in complex-conjugate pairs. Thus from the given eigenvalues $0$, $1+i$, and $1+2i$, we also obtain $1-i$ and $1-2i$. These are five distinct complex eigenvalues of a $5\times5$ matrix, so each has algebraic multiplicity $1$.

Hence
\[
egin{aligned}
\chi_L(x)
&=x(x-(1+i))(x-(1-i))(x-(1+2i))(x-(1-2i))\
&=xigl((x-1)^2+1igr)igl((x-1)^2+4igr)\
&=x(x^2-2x+2)(x^2-2x+5).
\end{aligned}
\]
Expanding,
\[
\chi_L(x)=x^5-4x^4+11x^3-14x^2+10x.
\]

Every eigenvalue is a root of the minimal polynomial, so $\mu_L$ has at least these five distinct roots. Therefore $\deg\mu_L\ge5$. Since $\mu_L\mid\chi_L$ by Cayley--Hamilton and $\deg\chi_L=5$, we obtain
\[
\mu_L(x)=\chi_L(x)=x(x^2-2x+2)(x^2-2x+5).
\]
:::
