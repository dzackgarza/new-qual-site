---
schema: qual/card@1
id: P-2ZMDH
kind: problem
title: "Suppose that $f$ is an analytic function in the region $D$ which\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - residues
  - zeros
  - power-series
relations: []
review: draft
solved: false
---

::: problem
Suppose that $f$ is an analytic function in the region $D$ which
contains the point $a$. Let
$$F(z)= z-a-qf(z),\quad \text{where}~ q \ \text{is a complex parameter}.$$

(1) Let $K\subset D$ be a circle with the center at
point $a$ and also we assume that $f(z)\not =0$ for $z\in K$. Prove
that the function $F$ has one and only one zero $z=w$ on the closed
disc $\bar{K}$ whose boundary is the circle $K$ if $\displaystyle{
|q|<\min_{z\in K} \frac{|z-a|}{|f(z)|}.}$\

(2) Let $G(z)$ be an analytic function on the disk $\bar{K}$. Apply
the residue theorem to prove that
$\displaystyle{ \frac{G(w)}{F'(w)}=\frac{1}{2\pi
i}\int_K \frac{G(z)}{F(z)} dz,}$ where $w$ is the zero from (1).\

(3) If $z\in K$, prove that the function
$\displaystyle{\frac{1}{F(z)}}$ can be represented as a convergent
series with respect to $q$: $\displaystyle{
\frac{1}{F(z)}=\sum_{n=0}^{\infty} \frac{(qf(z))^n}{(z-a)^{n+1}}.}$
:::
