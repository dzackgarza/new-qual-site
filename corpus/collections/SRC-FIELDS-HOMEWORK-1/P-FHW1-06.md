---
schema: qual/card@1
id: P-FHW1-06
kind: problem
title: Degree of $\QQ(\sqrt n,\sqrt m)$ over $\QQ$
classification:
  areas: [algebra]
  topics: [Field Extensions]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
For all positive integers $n$ and $m$, compute the degree $[\QQ(\sqrt n,\sqrt m):\QQ]$.
:::

::: {.solution}
Write $n=a^2n_0$ and $m=b^2m_0$ with $n_0,m_0$ squarefree positive integers; then $\QQ(\sqrt n)=\QQ(\sqrt{n_0})$ and $\QQ(\sqrt m)=\QQ(\sqrt{m_0})$, because $\sqrt n=a\sqrt{n_0}$.

::: pf

::: {.pf-step #squarefree-parts}
For squarefree $n_0>1$ and squarefree $m_0>1$ the element $\sqrt{m_0}$ lies in $\QQ(\sqrt{n_0})$ exactly when $m_0=n_0$.

::: pf-proof
Write $\sqrt{m_0}=u+v\sqrt{n_0}$ with $u,v\in\QQ$; this is possible inside the field $\QQ(\sqrt{n_0})$, whose elements are exactly the numbers $u+v\sqrt{n_0}$.
Squaring gives $m_0=u^2+v^2n_0+2uv\sqrt{n_0}$.
Since $\sqrt{n_0}$ is irrational for squarefree $n_0>1$, the coefficient $2uv$ vanishes.
If $v=0$ then $\sqrt{m_0}=u$ is rational, which forces $m_0$ to be a square, hence $m_0=1$; so $u=0$ and $m_0=v^2n_0$ with $v\in\QQ$.
Writing $v=r/s$ in lowest terms, $m_0s^2=r^2n_0$, and squarefreeness of $m_0$ and $n_0$ forces $m_0=n_0$.
:::

:::

::: {.pf-step #degree}
With $n_0,m_0$ as above,
$$
[\QQ(\sqrt n,\sqrt m):\QQ]=
\begin{cases}
1, & n_0=m_0=1,\\
2, & \text{exactly one of } n_0,m_0 \text{ is } 1,\ \text{or } n_0=m_0\ne1,\\
4, & \text{otherwise}.
\end{cases}
$$

::: pf-proof
If $n_0=m_0=1$ both generators are rational and the degree is $1$.
Suppose $n_0>1$. Then $[\QQ(\sqrt{n_0}):\QQ]=2$, since $x^2-n_0$ is irreducible by squarefreeness.
The degree in question is $[\QQ(\sqrt{n_0})(\sqrt{m_0}):\QQ(\sqrt{n_0})]\cdot2$, and the first factor is $1$ when $\sqrt{m_0}\in\QQ(\sqrt{n_0})$ and $2$ otherwise, since $\sqrt{m_0}$ is a root of $x^2-m_0\in\QQ[x]\subseteq\QQ(\sqrt{n_0})[x]$.
By step [](#squarefree-parts){.pf-ref} the containment holds exactly when $m_0=n_0$, so the degree is $2$ in that case and $4$ otherwise.
The case $n_0=1<m_0$ is the same argument with the roles exchanged and gives degree $2$.
:::

:::

:::

:::
