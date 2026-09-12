---
schema: qual/card@1
id: P-APAS20D
kind: problem
title: Conjugacy class sizes from a character table of a group of order $360$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Group Theory
relations: []
review: draft
---

::: problem
Here is the character table for some group of size $360$ (rows are characters, the columns are conjugacy classes):
\[
\begin{array}{c|ccccccc}
 & \gamma_1 & \gamma_2 & \gamma_3 & \gamma_4 & \gamma_5 & \gamma_6 & \gamma_7 \\
\hline
\chi_1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\chi_2 & 5 & -1 & 2 & -1 & 1 & 0 & 0 \\
\chi_3 & 5 & 2 & -1 & -1 & 1 & 0 & 0 \\
\chi_4 & 8 & -1 & -1 & 0 & 0 & \dfrac{1+\sqrt{5}}{2} & \dfrac{1-\sqrt{5}}{2} \\
\chi_5 & 8 & -1 & -1 & 0 & 0 & \dfrac{1-\sqrt{5}}{2} & \dfrac{1+\sqrt{5}}{2} \\
\chi_6 & 9 & 0 & 0 & 1 & 1 & -1 & -1 \\
\chi_7 & 10 & 1 & 1 & 0 & -2 & 0 & 0
\end{array}
\]
Determine the sizes of its conjugacy classes.
For your convenience, the divisors of $360$ are:
\[
1,2,3,4,5,6,8,9,10,12,15,18,20,24,30,36,40,45,60,72,90,120,180,360.
\]
:::

::: solution
If \(g\in G\), column orthogonality for the irreducible character table gives
\[
\sum_{\chi\in\operatorname{Irr}(G)} |\chi(g)|^2=|C_G(g)|.
\]
If \(K_g\) is the conjugacy class of \(g\), then
\[
|K_g|=\frac{|G|}{|C_G(g)|}.
\]
We therefore compute the squared column norms.

For \(\gamma_1\),
\[
1^2+5^2+5^2+8^2+8^2+9^2+10^2=360,
\]
so \(|\gamma_1|=360/360=1\).

For \(\gamma_2\),
\[
1^2+(-1)^2+2^2+(-1)^2+(-1)^2+0^2+1^2=9,
\]
so \(|\gamma_2|=360/9=40\). The same computation for \(\gamma_3\) gives \(|\gamma_3|=40\).

For \(\gamma_4\),
\[
1^2+(-1)^2+(-1)^2+0+0+1^2+0=4,
\]
so \(|\gamma_4|=90\).

For \(\gamma_5\),
\[
1^2+1^2+1^2+0+0+1^2+(-2)^2=8,
\]
so \(|\gamma_5|=45\).

For \(\gamma_6\), let
\[
\alpha=\frac{1+\sqrt5}{2},\qquad \beta=\frac{1-\sqrt5}{2}.
\]
Since \(\alpha+\beta=1\) and \(\alpha\beta=-1\),
\[
\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=3.
\]
Hence the squared column norm is
\[
1+\alpha^2+\beta^2+1=5,
\]
so \(|\gamma_6|=72\). The same holds for \(\gamma_7\).

Thus the conjugacy-class sizes, in the order displayed in the table, are
\[
\boxed{1,40,40,90,45,72,72}.
\]
Their sum is \(360\), as required.
:::
