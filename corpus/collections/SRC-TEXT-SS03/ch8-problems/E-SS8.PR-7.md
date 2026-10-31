---
schema: qual/card@1
id: E-SS8.PR-7
kind: problem
title: Koebe's construction of a Riemann map
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
relations: []
review: draft
---

::: {.exercise}
A *Koebe domain* is a simply connected proper subdomain $K$ of the unit disc $\DD$ containing $0$. Its inner radius is $r_K=\sup\{\rho\geq0:D(0,\rho)\subset K\}$. A holomorphic injection $f:K\to\DD$ is an *expansion* if $f(0)=0$ and $\abs{f(z)}>\abs z$ for $z\in K\setminus\{0\}$.

(a) Prove that an expansion satisfies $r_{f(K)}\geq r_K$ and $\abs{f'(0)}>1$.

Suppose $K_0$ is a Koebe domain and $f_n:K_n\to K_{n+1}$ are expansions, where $K_{n+1}=f_n(K_n)$. Set $F_n=f_n\circ\cdots\circ f_0:K_0\to\DD$.

(b) Prove that each $F_n$ is an expansion, that $F_n'(0)=\prod_{k=0}^{n}f_k'(0)$, and that $\lim_{n\to\infty}\abs{f_n'(0)}=1$.

(c) Show that if $r_{K_n}\to1$, then $F_n$ converges uniformly on compact subsets of $K_0$ to a conformal map $F:K_0\to\DD$.

For $\alpha\in\DD$, write $\psi_\alpha(z)=(\alpha-z)/(1-\overline\alpha z)$.

(d) Given a Koebe domain $K$, choose $\alpha\in\partial K\cap\DD$ with $\abs{\alpha}=r_K$ and $\beta\in\DD$ with $\beta^2=\alpha$. Let $S$ denote the square root of $\psi_\alpha$ on $K$ such that $S(0)=0$. Why is it well defined? Prove that $f=\psi_\beta\circ S\circ\psi_\alpha:K\to\DD$ is an expansion and that $\abs{f'(0)}=(1+r_K)/(2\sqrt{r_K})$.

(e) Use (d) to construct a sequence with $r_{K_n}\to1$.
:::

::: {.hint}
For (a), write $f(z)=zg(z)$ and use the maximum principle. For (b), use the Schwarz lemma. For (c), show that $r_{F(K_0)}\geq1$. For (d), apply the Schwarz lemma to the inverse map, expressed using $\psi_\alpha$, $\psi_\beta$, and $z\mapsto z^2$.
:::

::: {.remark}
Part (d) is inconsistent as printed: $\psi_\alpha(0)=\alpha\neq0$, so a square root of $\psi_\alpha$ cannot satisfy $S(0)=0$. The composition also requires $S$ to be defined on $\psi_\alpha(K)$. A coherent choice is a square root on $\psi_\alpha(K)$ with $S(\alpha)=\beta$.
:::
