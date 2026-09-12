---
schema: qual/card@1
id: P-YFOG7
kind: problem
title: Galois group $D_6$ and intermediate fields of $\QQ(\sqrt[3]{2},\sqrt{3},\zeta_3)/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: problem
Let
\[
L=\QQ(\sqrt[3]2,\sqrt3,\zeta_3),
\]
where $\zeta_3$ is a primitive cube root of unity. Compute $\operatorname{Gal}(L/\QQ)$ and describe the intermediate fields, at least up to conjugacy.
:::

::: solution
Set
\[
a=\sqrt[3]2,
\qquad
b=\sqrt3,
\qquad
\omega=\zeta_3.
\]
The splitting field of $x^3-2$ is $\QQ(a,\omega)$ and has degree $6$ over $\QQ$. The element $b$ does not lie in this field: the only quadratic subfield of the $S_3$-extension $\QQ(a,\omega)/\QQ$ is $\QQ(\sqrt{-3})$, whereas $\QQ(\sqrt3)$ is different. Hence
\[
[L:\QQ]=12.
\]

Define automorphisms
\[
\sigma:a\mapsto\omega a,\quad \omega\mapsto\omega,\quad b\mapsto b,
\]
\[
\tau:a\mapsto a,\quad \omega\mapsto\omega^2,\quad b\mapsto b,
\]
and
\[
\gamma:a\mapsto a,\quad \omega\mapsto\omega,\quad b\mapsto-b.
\]
Then
\[
\sigma^3=\tau^2=\gamma^2=1,
\qquad
\tau\sigma\tau=\sigma^{-1},
\]
and $\gamma$ commutes with both $\sigma$ and $\tau$. Therefore
\[
\operatorname{Gal}(L/\QQ)
\cong S_3\times C_2,
\]
which is also the dihedral group of order $12$ (often denoted $D_6$).

The subgroup/fixed-field correspondence gives the intermediate fields. Representatives of the conjugacy classes of proper nontrivial subgroups are:

\[
\begin{array}{c|c}
H & L^H\\ \hline
\langle\sigma\rangle & \QQ(\omega,b)\\
\langle\tau\rangle & \QQ(a,b)\\
\langle\gamma\rangle & \QQ(a,\omega)\\
\langle\tau\gamma\rangle & \QQ(a,i)\\
\langle\tau,\gamma\rangle & \QQ(a)\\
\langle\sigma,\tau\rangle & \QQ(b)\\
\langle\sigma,\gamma\rangle & \QQ(\omega)\\
\langle\sigma,\tau\gamma\rangle & \QQ(i)
\end{array}
\]

Here
\[
i=\frac{\omega-\omega^2}{b},
\]
which is fixed by $\tau\gamma$.

The conjugates of $\langle\tau\rangle$, $\langle\tau\gamma\rangle$, and $\langle\tau,\gamma\rangle$ give the remaining conjugate intermediate fields:
\[
\QQ(\omega^j a,b),
\qquad
\QQ(\omega^j a,i),
\qquad
\QQ(\omega^j a)
\quad(j=0,1,2).
\]
Together with $\QQ$ and $L$, these account for the full subgroup lattice under the Galois correspondence.
:::
