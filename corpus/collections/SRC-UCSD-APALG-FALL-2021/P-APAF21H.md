---
schema: qual/card@1
id: P-APAF21H
kind: problem
title: Character table of $D_4$ and the Artin--Wedderburn decomposition of $\mathbb{C}[D_4]$
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
Find the character table of the dihedral group $D_4$ of symmetries of a square.
The group algebra of $D_4$ is isomorphic to a direct sum
\[
\mathbb{C}[D_4]\cong\operatorname{Mat}_{n_1}(\mathbb{C})\oplus\cdots\oplus\operatorname{Mat}_{n_r}(\mathbb{C})
\]
of matrix algebras over $\mathbb{C}$.
Determine $r$ and the numbers $n_1,\ldots,n_r>0$.
(Hint: Try showing that $\mathbb{C}[D_4]\cong\operatorname{End}_{D_4}\mathbb{C}[D_4]$ as algebras.
How does the endomorphism ring of $\mathbb{C}[D_4]$ decompose?)
:::

::: {.solution}
Write
\[
D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle.
\]

<1>1. The conjugacy classes are
\[
\{1\},\quad\{r^2\},\quad\{r,r^3\},\quad\{s,r^2s\},\quad\{rs,r^3s\}.
\]
::: {.proof}
Conjugation by $s$ sends $r$ to $r^{-1}=r^3$, so $r$ and $r^3$ are conjugate, while $r^2$ is central. Conjugating a reflection $r^js$ by $r$ changes the exponent by $2$, so the reflections split into the two classes of even and odd exponents. The displayed sets have total size
\[
1+1+2+2+2=8=|D_4|,
\]
so they are all conjugacy classes.
:::

<1>2. There are four one-dimensional characters, determined independently by the choices
\[
r\longmapsto\pm1,
\qquad
s\longmapsto\pm1.
\]
Their values are
\[
\begin{array}{c|rrrrr}
&1&r^2&\{r,r^3\}&\{s,r^2s\}&\{rs,r^3s\}\\ \hline
\chi_{++}&1&1&1&1&1\\
\chi_{+-}&1&1&1&-1&-1\\
\chi_{-+}&1&1&-1&1&-1\\
\chi_{--}&1&1&-1&-1&1
\end{array}.
\]
::: {.proof}
In a one-dimensional representation the relation $srs=r^{-1}$ becomes $r=r^{-1}$, so $r^2=1$. Thus both $r$ and $s$ may independently be sent to $\pm1$, and all four choices satisfy the defining relations. Evaluating them on the five conjugacy classes gives the table.
:::

<1>3. The geometric representation of $D_4$ on $\mathbb R^2\subset\mathbb C^2$ has character
\[
\chi_2=(2,-2,0,0,0).
\]
::: {.proof}
Take
\[
r=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
s=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Then $r$ is rotation by $\pi/2$ and $s$ a reflection. Their traces on the five classes are: $2$ at the identity, $-2$ for $r^2=-I$, $0$ for $r,r^3$, and $0$ for every reflection. Thus the character row is as stated.
Its norm is
\[
\frac18\left(1\cdot4+1\cdot4+2\cdot0+2\cdot0+2\cdot0\right)=1,
\]
so the representation is irreducible.
:::

<1>4. Hence the complete character table is
\[
\begin{array}{c|rrrrr}
&1&r^2&\{r,r^3\}&\{s,r^2s\}&\{rs,r^3s\}\\
\text{class size}&1&1&2&2&2\\ \hline
\chi_{++}&1&1&1&1&1\\
\chi_{+-}&1&1&1&-1&-1\\
\chi_{-+}&1&1&-1&1&-1\\
\chi_{--}&1&1&-1&-1&1\\
\chi_2&2&-2&0&0&0
\end{array}.
\]
::: {.proof}
The five displayed irreducibles have degree squares
\[
1^2+1^2+1^2+1^2+2^2=8=|D_4|.
\]
Therefore they exhaust all irreducible complex representations of $D_4$.
:::

<1>5. As a left $D_4$-module, the regular representation decomposes as
\[
\mathbb C[D_4]
\cong
\chi_{++}\oplus\chi_{+-}\oplus\chi_{-+}\oplus\chi_{--}\oplus 2V_2,
\]
where $V_2$ affords $\chi_2$.
::: {.proof}
In the complex regular representation, every irreducible representation $V$ occurs with multiplicity $\dim V$. The four linear representations therefore occur once each, and the $2$-dimensional representation occurs twice.
:::

<1>6. Consequently
\[
\operatorname{End}_{D_4}(\mathbb C[D_4])
\cong
\mathbb C\oplus\mathbb C\oplus\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
\]
::: {.proof}
For a semisimple representation
\[
W\cong\bigoplus_i m_iV_i
\]
with pairwise nonisomorphic irreducibles, Schur's lemma gives
\[
\operatorname{End}_G(W)\cong\bigoplus_i M_{m_i}(\mathbb C).
\]
Apply this to the multiplicities $1,1,1,1,2$ from <1>5.
:::

<1>7. Therefore
\[
\boxed{\mathbb C[D_4]\cong
\mathbb C^{\oplus4}\oplus M_2(\mathbb C)}.
\]
Thus
\[
\boxed{r=5,\qquad (n_1,\ldots,n_5)=(1,1,1,1,2)}
\]
up to ordering.
::: {.proof}
Right multiplication identifies
\[
\operatorname{End}_{D_4}(\mathbb C[D_4])
\cong\mathbb C[D_4]^{\mathrm{op}}.
\]
The inversion map $g\mapsto g^{-1}$ identifies the group algebra with its opposite algebra. Hence the decomposition in <1>6 is also the Artin--Wedderburn decomposition of $\mathbb C[D_4]$ itself.
:::
:::
