---
schema: qual/card@1
id: P-BKS04-1B
kind: problem
title: $y^2+a(x)y+b(x)$ is irreducible over $F(x)$ when $\deg a\le g$ and $\deg b=2g+1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $F$ be a field (of arbitrary characteristic).
Suppose $g$ is a nonnegative integer, and polynomials $a(x),b(x)\in F[x]$ satisfy $\deg a(x)\leq g$ and $\deg b(x)=2g+1$. Prove that the polynomial $y^2+a(x)y+b(x)$ is irreducible over $F(x)$.
:::

::: {.solution}
If instead it factors in $F(x)[y]$ into polynomials of $y$-degree $\geq1$, then by Gauss's lemma, it factors in $F[x][y]=F[x,y]$ into polynomials of $y$-degree $\geq1$. Thus we would have

$$
y^2+a(x)y+b(x)=(y+p(x))(y+q(x))
$$

for some $p(x),q(x)\in F[x]$. Since $p(x)q(x)=b(x)$ has odd degree, $p(x)$ and $q(x)$ have distinct degrees, so

$$
\deg(p(x)+q(x))=\max(\deg p(x),\deg q(x))\geq(\deg p(x)+\deg q(x))/2=(2g+1)/2>g.
$$

This contradicts $\deg a(x)=\deg(p(x)+q(x))\leq g$.
:::
