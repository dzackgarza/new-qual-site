---
schema: qual/card@1
id: E-HAT-3.2-5
kind: problem
title: Hatcher Section 3.2 Exercise 5
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher's corrected Section 3.2 Exercise 5; the stored statement matches the 2004 correction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

# E-HAT-3.2-5

Show the ring $H^*(\mathbb{RP}^\infty; \mathbb{Z}_{2k})$ is isomorphic to $\mathbb{Z}_{2k}[\alpha, \beta] / (2\alpha, 2\beta, \alpha^2 - k\beta)$ where $|\alpha| = 1$ and $|\beta| = 2$.

::: {.solution}
Put $R=\mathbb Z_{2k}$. With the standard CW structure on $\mathbb{RP}^\infty$, there is one cell in each dimension and the cellular boundary is multiplication by $2$ in even dimensions and $0$ in odd dimensions. Hence the cellular cochain differential with coefficients in $R$ is
\[
\delta^q=
\begin{cases}
2,&q\text{ odd},\\
0,&q\text{ even}.
\end{cases}
\]
Therefore
\[
H^q(\mathbb{RP}^\infty;R)\cong
\begin{cases}
R,&q=0,\\
\ker(2:R\to R)=\{0,k\}\cong\mathbb Z_2,&q\text{ odd},\\
R/2R\cong\mathbb Z_2,&q>0\text{ even}.
\end{cases}
\]

Let $\alpha\in H^1$ be represented by the cellular $1$-cocycle taking the value $k$ on the unique $1$-cell, and let $\beta\in H^2$ be the class of the cellular $2$-cochain taking value $1$ on the unique $2$-cell. Then
\[
2\alpha=2\beta=0.
\]
The cellular diagonal used in the proof of Hatcher's Theorem 3.12 shows that the cup product of the basic degree-one cellular cochain with itself represents the basic degree-two cochain. Since our degree-one cocycle has coefficient $k$, its square is represented by $k^2$ times the basic degree-two cochain. Thus
\[
\alpha^2=k^2\beta.
\]
But $\beta$ has additive order $2$, and $k^2\equiv k\pmod 2$, so
\[
\boxed{\alpha^2=k\beta.}
\]

Reduction of coefficients $R\to\mathbb Z_2$ sends $\beta$ to the nonzero class in $H^2(\mathbb{RP}^\infty;\mathbb Z_2)$, so $\beta^j$ is nonzero for every $j\ge1$. Likewise $\alpha\beta^j$ generates the odd-dimensional group in degree $2j+1$. Hence $\alpha,\beta$ generate the whole ring and there are no further relations. Therefore
\[
\boxed{
H^*(\mathbb{RP}^\infty;\mathbb Z_{2k})
\cong
\mathbb Z_{2k}[\alpha,\beta]/(2\alpha,2\beta,\alpha^2-k\beta),
\quad |\alpha|=1,\ |\beta|=2.
}
\]
:::
