---
schema: qual/card@1
id: P-APAF17E
kind: problem
title: Character table of the dihedral group $D_6$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $D_6=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle$ be the dihedral group of symmetries of a regular pentagon.
Calculate the character table of $D_6$.
:::

::: {.remark}
The source describes the group as the symmetries of a regular pentagon, but the printed presentation has $r^6=1$, which is the dihedral group of order $12$, the symmetries of a regular hexagon; the symmetries of a pentagon have $r^5=1$.
The statement is left as the exam printed it, and the presentation governs the calculation.
:::

::: {.solution}
We follow the printed presentation
\[
D_6=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle,
\]
so $|D_6|=12$.

<1>1. The conjugacy classes are
\[
\{1\},\quad \{r^3\},\quad \{r,r^5\},\quad \{r^2,r^4\},
\quad \{s,r^2s,r^4s\},\quad \{rs,r^3s,r^5s\}.
\]
::: {.proof}
Since
\[
sr^ms=r^{-m},
\]
the rotations $r^m$ and $r^{-m}$ are conjugate. Thus the rotation classes are
\[
\{1\},\ \{r^3\},\ \{r,r^5\},\ \{r^2,r^4\}.
\]
For reflections,
\[
r^j(r^ms)r^{-j}=r^{m+2j}s.
\]
Hence conjugation by rotations preserves the parity of $m$ and is transitive on the three even exponents and on the three odd exponents. Conjugation by $s$ sends $r^ms$ to $r^{-m}s$, again preserving parity. Thus the reflections form exactly the two displayed classes. Their sizes sum to
\[
1+1+2+2+3+3=12,
\]
so the list is complete.
:::

<1>2. There are four one-dimensional characters $\chi_{\varepsilon,\delta}$, indexed by $\varepsilon,\delta\in\{\pm1\}$, defined by
\[
\chi_{\varepsilon,\delta}(r)=\varepsilon,
\qquad
\chi_{\varepsilon,\delta}(s)=\delta.
\]
::: {.proof}
In a one-dimensional representation the defining relation becomes
\[
\delta\varepsilon\delta=\varepsilon^{-1}.
\]
Since $\delta^2=1$, this says $\varepsilon=\varepsilon^{-1}$, so $\varepsilon=\pm1$; also $\delta=\pm1$. Conversely, each such pair satisfies all defining relations because $\varepsilon^6=1$, $\delta^2=1$, and $\varepsilon=\varepsilon^{-1}$. Thus these are exactly the four linear characters.
:::

<1>3. Let
\[
\zeta=e^{2\pi i/6}.
\]
For $k=1,2$, define
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
Then $\rho_k$ is an irreducible two-dimensional representation.
::: {.proof}
The matrices satisfy
\[
\rho_k(r)^6=I,
\qquad
\rho_k(s)^2=I,
\qquad
\rho_k(s)\rho_k(r)\rho_k(s)=\rho_k(r)^{-1},
\]
so they define a representation of $D_6$.
For $k=1,2$, the two eigenvalues $\zeta^k$ and $\zeta^{-k}$ of $\rho_k(r)$ are distinct. Any one-dimensional subspace invariant under $r$ must therefore be one of the two coordinate lines, but $\rho_k(s)$ swaps those lines. Hence there is no nonzero proper invariant subspace, so $\rho_k$ is irreducible.
:::

<1>4. The characters of $\rho_k$ satisfy
\[
\chi_k(r^m)=\zeta^{km}+\zeta^{-km}=2\cos\frac{2\pi km}{6},
\qquad
\chi_k(r^ms)=0.
\]
::: {.proof}
The first formula is the trace of the diagonal matrix $\rho_k(r^m)$. The matrix $\rho_k(r^m)\rho_k(s)$ is off-diagonal, so its trace is $0$.
:::

<1>5. With columns ordered as
\[
1,\quad r^3,\quad \{r,r^5\},\quad \{r^2,r^4\},\quad
\{s,r^2s,r^4s\},\quad \{rs,r^3s,r^5s\},
\]
the complete character table is
\[
\begin{array}{c|rrrrrr}
&1&r^3&r^{\pm1}&r^{\pm2}&s\text{-even}&s\text{-odd}\\
\text{class size}&1&1&2&2&3&3\\ \hline
\chi_{+,+}&1& 1& 1& 1& 1& 1\\
\chi_{+,-}&1& 1& 1& 1&-1&-1\\
\chi_{-,+}&1&-1&-1& 1& 1&-1\\
\chi_{-,-}&1&-1&-1& 1&-1& 1\\
\chi_1&2&-2& 1&-1&0&0\\
\chi_2&2& 2&-1&-1&0&0
\end{array}.
\]
::: {.proof}
For the linear characters,
\[
\chi_{\varepsilon,\delta}(r^m)=\varepsilon^m,
\qquad
\chi_{\varepsilon,\delta}(r^ms)=\varepsilon^m\delta,
\]
which gives the first four rows. The last two rows follow from <1>4 by evaluating the relevant cosines.
The six displayed representations are pairwise nonisomorphic irreducibles, and their degree squares sum to
\[
4\cdot1^2+2\cdot2^2=12=|D_6|.
\]
Therefore they exhaust all irreducible representations, so the table is complete.
:::
:::
