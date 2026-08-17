---
schema: qual/card@1
id: P-L7G3D
kind: problem
title: "Let $(X, \\mathcal M, \\mu)$ be a measure space and suppose $\\theset{E_n} \\subset \\mathcal M$ satisfies $\\lim _{n \\rightarrow \\infty} \\mu\\left(X \\backslash E_{n}\\right)=0$"
classification:
  areas:
  - real-analysis
  topics:
  - borel-cantelli
  - measure-theory
relations: []
review: draft
solved: true
---
Let $(X, \mathcal M, \mu)$ be a measure space and suppose $\theset{E_n} \subset \mathcal M$ satisfies
\[
\lim _{n \rightarrow \infty} \mu\left(X \backslash E_{n}\right)=0.
\]

Define
\[
G \definedas \theset{x\in X \suchthat x\in E_n \text{ for only finitely many  } n}.
\]

Show that $G \in \mathcal M$ and $\mu(G) = 0$.

:::{.solution}
\envlist

- Claim: $G\in \mcm$.
  - Claim:
  \[  
  G = \qty{ \Intersect_{N=1}^\infty \Union_{n=N}^\infty E_n}^c = \Union_{N=1}^\infty \Intersect_{n=N}^\infty E_n^c
  .\]

    - This follows because $x$ is in the RHS $\iff$ $x\in E_n^c$ for all but finitely many $n$ $\iff$ $x\in E_n$ for at most finitely many $n$.

  - But $\mcm$ is a $\sigma\dash$algebra, and this shows $G$ is obtained by countable unions/intersections/complements of measurable sets, so $G\in \mcm$. 

- Claim: $\mu(G) = 0$.

  - We have
  \[  
  \mu(G)
  &= \mu\qty{\Union_{N=1}^\infty \Intersect_{n=N}^\infty E_n^c} \\
  &\leq \sum_{N=1}^\infty \mu \qty{\Intersect_{n=N}^\infty E_n^c}  \\
  &\leq \sum_{N=1}^\infty \mu(E_M^c) \\ 
  &\definedas \sum_{N=1}^\infty \mu(X\setminus E_N) \\
  &\converges{N\to\infty}\to 0
  .\]

:::{.remark}
Last step seems wrong!
:::
:::

