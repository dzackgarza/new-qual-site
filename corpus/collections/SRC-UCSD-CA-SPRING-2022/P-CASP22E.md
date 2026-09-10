---
schema: qual/card@1
id: P-CASP22E
kind: problem
title: "Poles of a meromorphic limit appear in the approximating sequence"
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Normal Families
  - Convergence
relations: []
review: draft
---

::: problem
Let $G \subset \mathbb{C}$ be an open set, $\{f_n\}$ a sequence in $M(G)$, and $f$ a meromorphic function such that $f_n \to f$ in $M(G)$.
Suppose $a \in G$ is a pole of $f$.
Show that there is a sequence $\{a_n\}$ in $G$ such that $a_n \to a$ and $f_n$ has a pole at $a_n$ for sufficiently large $n$.
:::

::: solution
Let the pole of $f$ at $a$ have order $m$. Choose $r>0$ so small that
$\overline{B(a,r)}\subset G$ and $a$ is the only pole of $f$ in that disk.
The coefficient of $(z-a)^{-m}$ in the Laurent expansion of $f$ is nonzero,
so
\[
\int_{|z-a|=r}(z-a)^{m-1}f(z)\,dz\ne0.
\]

On the circle $|z-a|=r$, the limit $f$ is finite. Meromorphic convergence is
therefore ordinary uniform convergence there, so for all sufficiently large
$n$,
\[
\int_{|z-a|=r}(z-a)^{m-1}f_n(z)\,dz\ne0.
\]
If such an $f_n$ had no pole in $B(a,r)$, the integrand would be holomorphic
there and the integral would be zero by Cauchy's theorem. Hence every
sufficiently large $f_n$ has a pole in $B(a,r)$.

Apply this argument with radii $r_k\downarrow0$. For each $k$ choose $N_k$ so
that every $n\ge N_k$ has a pole in $B(a,r_k)$, with $N_k$ increasing. For
$N_k\le n<N_{k+1}$ choose one such pole and call it $a_n$. Then
$a_n\to a$, and by construction $a_n$ is a pole of $f_n$ for every
sufficiently large $n$.
:::
