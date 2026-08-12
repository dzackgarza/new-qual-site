---
schema: qual/card@1
id: E-QIB7A
kind: exercise
title: "Assume $u$ is harmonic on open set $O$ and $z_n$ is a sequence in $O$ such\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
(1) Assume $u$ is harmonic on open set $O$ and $z_n$ is a sequence
in $O$ such that $u(z_n) = 0$ and $\lim z_n \in O$. Prove or
disprove that $u$ is identically zero. What if $O$ is a region?

(2) Assume $u$ is harmonic on open set $O$ and $u(z) = 0$ on a
disc in $O$. Prove or disprove that $u$ is identically zero. What if
$O$ is a region?

(3) Formulate and prove a Schwarz reflection principle for
harmonic functions

> cf. Theorem 5.6 on p.60 of Stein et al.

> Hint: Verify the mean value property for your new function obtained by
Schwarz reflection principle.

:::

:::{.solution}
**Part 1**:
This is not true: take the holomorphic function $f(z) = z$, then $u(z) \da \Re(f(z)) = \Re(z)$ is harmonic on nonzero on $\RR$ but zero on $i\RR$.

**Part 2**:
Set $f \da u_x + i u_y$, then $f$ is holomorphic on $O$.
Since $h\equiv 0$ on $\DD_\eps \subseteq O$, $g\equiv 0$ on this disc.
By the identity principle for holomorphic functions, $g\equiv 0$ on $O$.
So $h_x, h_y \equiv 0$, making $h$ constant, and since $h\equiv 0$ on $U$ this forces $h\equiv 0$ on $O$.

**Part 3**:
Let $u$ be harmonic on $S^+$, a region symmetric about $\RR$, and that $u\equiv 0$ on $\RR \intersect S^+$.
Define $S^- = \ts{\bar{z} \st z\in S^+}$, and
\[
U(z) \da 
\begin{cases}
 U(z) &  z\in S^+
\\
 -U(\bar z) & z\in S^-.
\end{cases}
.\]
Then $U$ is a harmonic extension of $u$ to $S \da S^+ \union (S^+ \intersect \RR) \union S^-$.
To see that $U$ is harmonic on $S$, it suffices to check that $U$ satisfies the mean value property on $S$.
Clearly this holds in $S^+$, so for $z_0\in S^+$ we have
\[
U(z_0) 
&= u(z_0) \\
&= {1\over 2\pi} \int_{-\pi}^\pi u(z_0 + re^{it} )\dt \\
&= {1\over 2\pi} \int_{-\pi}^\pi U(z_0 + re^{it} )\dt \\
.\]
So for $w_0\in S^-$, write it as $w_0 = \bar{z_0}$, then
\[
U(z_0)
&\da -u(\bar{z_0}) \\
&= {1\over 2\pi }\int_{-\pi}^\pi - u\qty{\bar{z_0 + re^{it} }} \dt \\
&= {1\over 2\pi }\int_{-\pi}^\pi - u\qty{\bar{z_0} + re^{-it} } \dt \\
&= {1\over 2\pi }\int_{-\pi}^\pi - u\qty{\bar{z_0 + re^{-it} }} \dt \\
&= {1\over 2\pi }\int_{-\pi}^\pi U(z_0 + re^{it} ) \dt
.\]

:::

