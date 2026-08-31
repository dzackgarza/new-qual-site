---
schema: qual/card@1
id: P-BTUCW
kind: problem
title: Open mapping theorem for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Argument Principle
  - Zeros
relations: []
review: draft
---

:::{.problem}
Prove the open mapping theorem for holomorphic functions: If $f$ is a non-constant holomorphic function on an open set $U$ in $\mathbb{C}$, then $f(U)$ is also an open set.
:::

:::{.solution}
Idea:

![](../../assets/Complex_Analysis/999_Quals/figures/2022-01-02_02-14-17.png)

Let $f: U\to \CC$.^[Using the argument principle.]
Pick $w_0\in W$ with $f(z_0) = w_0$ for some $z_0\in U$; we want to show that $w_0$ is an interior point of $f(U)$, so we're looking for a disc containing $w_0$ and contained in $f(U)$.

Write 
\[
g_0(z) \da f(z) - w_0
,\]
so $g_0$ is holomorphic and has a zero at $z_0$.
Since zeros of holomorphic functions are isolated, there is some $U' \da \DD_r(z_0)$ where $g_0$ is nonvanishing.
The claim is that if we choose $\eps$ small enough, we can arrange so that $W_\eps \da \DD_\eps(w_0) \subseteq f(U)$.
This will follow if for every $w\in W_\eps$, the equation $f(z) = w$ has a solution in $U$, i.e. 
Define a function that counts the number of zeros:
\[
F(w)
&\da {1\over 2\pi i}\int_{\bd U' } {f(z) \over f(z) - w_1 }\dz\\
&= {1\over 2\pi i}\int_{\bd U' } {\dd{}{z}\qty{f(z) - w} \over f(z) - w }\dz\\
&= \size Z(f(z) - w, U' ) 
,\]
which is the number of zeros of $f(z) - w$ in $U'$ by the argument principle.
Now $F$ is a $\ZZ\dash$valued function, and the only obstruction to continuity is if $f(z) - w = 0$ in the integrand for some $z$.
The claim is that $\eps$ can be chosen such 
\[
z\in \bd U' \implies \abs{f(z) - w} > 0 \qquad \forall w\in W_\eps
.\]
The theorem then follows: $F(w): U' \to W_\eps$ is a continuous and $\ZZ\dash$valued function on the connected set $W_\eps$ (a disc), and a continuous integer-valued function on a connected set is constant (its image is a connected subset of the discrete space $\ZZ$, hence a single point).
Then noting that $F(w_0) = 1$ since $z_0\in U'$ and $w_0\in W_\eps$, we have $F\equiv 1 > 0$ for all $w$.


:::{.proof title="of claim"}
Choose
\[
\eps \da \min_{z\in \bd U'}\abs{f(z) - w_0}
.\]
Now if $\abs{w-w_0} < \eps$ and $\abs{z-z_0} = r$, we have $\abs{f(z) - w} > \eps > 0$.
:::




:::
