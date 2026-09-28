---
schema: qual/card@1
id: P-2ZMDH
kind: problem
title: Unique zero of $z-a-qf(z)$, residue formula, and series for $1/F$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Residues
  - Zeros
  - Power Series
relations: []
review: draft
---

::: {.problem}
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

::: {.solution}
Let the circle $K$ have radius $R$ and center $a$. On $K$ the hypothesis gives
\[
|qf(z)|<|z-a|=R.
\]
Hence, by Rouché's theorem, the functions
\[
z-a
\qquad\text{and}\qquad
F(z)=(z-a)-qf(z)
\]
have the same number of zeros in the disk bounded by $K$, counted with
multiplicity. The function $z-a$ has exactly one zero there. Therefore $F$ has
exactly one zero $w$ in the disk, counted with multiplicity. The strict
boundary inequality also shows that $F$ has no zero on $K$. Consequently this
unique zero is simple, so
\[
F'(w)\ne0.
\]

For part (2), $G/F$ is meromorphic in the disk and has exactly one pole there,
the simple pole at $w$. Its residue is
\[
\operatorname{Res}_{z=w}\frac{G(z)}{F(z)}
=\frac{G(w)}{F'(w)}.
\]
The residue theorem therefore gives
\[
\boxed{
\frac{G(w)}{F'(w)}
=\frac1{2\pi i}\int_K\frac{G(z)}{F(z)}\,dz.}
\]

Finally, if $z\in K$, then
\[
\left|\frac{qf(z)}{z-a}\right|<1.
\]
Thus the geometric series is absolutely convergent and
\[
\frac1{F(z)}
=\frac1{z-a}\frac1{1-\frac{qf(z)}{z-a}}
=\frac1{z-a}\sum_{n=0}^\infty
\left(\frac{qf(z)}{z-a}\right)^n.
\]
Hence
\[
\boxed{
\frac1{F(z)}
=\sum_{n=0}^\infty\frac{(qf(z))^n}{(z-a)^{n+1}}.}
\]
:::
