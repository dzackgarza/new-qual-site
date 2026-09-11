---
schema: qual/card@1
id: P-APAS15A
kind: problem
title: Character table of the dihedral group $D_5$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
Let $D_5 = \langle r, s : s^2 = r^5 = 1,\ srs = r^{-1} \rangle$ denote the group of symmetries of a regular pentagon.
Find the character table of $D_5$.
:::

::: solution
The elements are
\[
1,r,r^2,r^3,r^4,s,sr,sr^2,sr^3,sr^4.
\]
Since
\[
sr^js=r^{-j},
\]
the nontrivial rotations split into two conjugacy classes
\[
\{r,r^4\},\qquad \{r^2,r^3\}.
\]
Because \(5\) is odd, all reflections are conjugate: indeed
\[
r^k s r^{-k}=sr^{-2k},
\]
and multiplication by \(-2\) permutes the residue classes modulo \(5\). Thus the four conjugacy classes are
\[
C_1=\{1\},\quad C_2=\{r,r^4\},\quad C_3=\{r^2,r^3\},\quad C_4=\{s,sr,sr^2,sr^3,sr^4\}.
\]
Hence \(D_5\) has four irreducible complex characters.

The abelianization is \(C_2\): in an abelian quotient the relation \(srs=r^{-1}\) becomes \(r=r^{-1}\), and since \(r\) has odd order this forces \(r=1\). Therefore there are exactly two linear characters,
\[
\mathbf 1(r)=1,\quad \mathbf 1(s)=1,
\]
and
\[
\varepsilon(r)=1,\quad \varepsilon(s)=-1.
\]

The remaining two irreducibles must have degrees \(d_1,d_2\) satisfying
\[
10=1^2+1^2+d_1^2+d_2^2,
\]
so \(d_1=d_2=2\).

Let \(\zeta=e^{2\pi i/5}\). For \(k=1,2\), define
\[
\rho_k(r)=
\begin{pmatrix}
\zeta^k&0\\0&\zeta^{-k}
\end{pmatrix},
\qquad
\rho_k(s)=
\begin{pmatrix}
0&1\\1&0
\end{pmatrix}.
\]
These matrices satisfy
\[
\rho_k(s)^2=I,\qquad \rho_k(r)^5=I,
\qquad \rho_k(s)\rho_k(r)\rho_k(s)=\rho_k(r)^{-1},
\]
so they define representations of \(D_5\). Their characters are
\[
\chi_k(r^j)=\zeta^{kj}+\zeta^{-kj}=2\cos\frac{2\pi kj}{5},
\qquad
\chi_k(sr^j)=0.
\]
Each \(\rho_k\) is irreducible because any \(r\)-stable line is one of the two coordinate lines, and \(s\) interchanges those lines. The two representations are inequivalent because their values on \(r\) differ.

Set
\[
a=2\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{2},
\qquad
b=2\cos\frac{4\pi}{5}=-\frac{\sqrt5+1}{2}.
\]
Then the full character table is
\[
\begin{array}{c|rrrr}
& C_1&C_2&C_3&C_4\\ \hline
\mathbf1&1&1&1&1\\
\varepsilon&1&1&1&-1\\
\chi_1&2&a&b&0\\
\chi_2&2&b&a&0
\end{array}
\]
with class sizes \(1,2,2,5\), respectively.
:::
