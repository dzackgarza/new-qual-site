---
schema: qual/card@1
id: P-APAF18D
kind: problem
title: Isomorphism $D_6\cong D_3\times C_2$ and the character table of $D_6$
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
Let $D_n$ be the dihedral group of symmetries of a regular $n$-gon, let $C_n$ be the cyclic group of order $n$, and let $S_n$ be the symmetric group on $n$ letters.

(a) Explain why we have the group isomorphism $D_6\cong D_3\times C_2$.

(b) Write down the character table of $D_6$.
:::

::: {.solution}
Write
\[
D_6=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle.
\]

<1>1. The element $r^3$ is central of order $2$.
::: {.proof}
Clearly $(r^3)^2=r^6=1$ and $r^3\ne1$. It commutes with $r$. Also
\[
sr^3s=(srs)^3=r^{-3}=r^3,
\]
so it commutes with $s$. Since $r,s$ generate $D_6$, one has $r^3\in Z(D_6)$.
:::

<1>2. The subgroup
\[
K=\langle r^2,s\rangle
\]
is isomorphic to $D_3$ and has order $6$.
::: {.proof}
The element $r^2$ has order $3$, while $s$ has order $2$, and
\[
sr^2s=r^{-2}.
\]
Thus $K$ has the presentation
\[
\langle a,b\mid a^3=b^2=1,\ bab=a^{-1}\rangle,
\]
which is the dihedral group $D_3$. Its six elements are
\[
1,r^2,r^4,s,r^2s,r^4s.
\]
:::

<1>3. One has
\[
D_6=K\times\langle r^3\rangle\cong D_3\times C_2.
\]
::: {.proof}
By <1>1, $\langle r^3\rangle$ is central, hence it commutes with $K$. Also
\[
K\cap\langle r^3\rangle=1,
\]
because $K$ contains only the rotations $1,r^2,r^4$, none of which is $r^3$.
Finally, $K\langle r^3\rangle$ contains $s$ and both $r^2$ and $r^3$; since
\[
r=(r^2)^2r^3=r^7=r,
\]
it contains $r$ as well. Hence it contains the generators $r,s$ of $D_6$, so it is all of $D_6$. Therefore the product is direct.
:::

<1>4. The conjugacy classes of $D_6$ are
\[
\begin{array}{c|c}
\text{class}&\text{size}\\ \hline
C_1=\{1\}&1\\
C_2=\{r^3\}&1\\
C_3=\{r,r^5\}&2\\
C_4=\{r^2,r^4\}&2\\
C_5=\{s,r^2s,r^4s\}&3\\
C_6=\{rs,r^3s,r^5s\}&3
\end{array}.
\]
::: {.proof}
Conjugation by $s$ sends $r^j$ to $r^{-j}$, giving the four rotation classes displayed. Conjugating a reflection $r^js$ by $r$ changes the exponent by $2$, so the even-exponent reflections form one class and the odd-exponent reflections form the other. Their sizes are $3$ each.
:::

<1>5. The complete character table of $D_6$ is
\[
\begin{array}{c|rrrrrr}
& C_1&C_2&C_3&C_4&C_5&C_6\\
\text{class size}&1&1&2&2&3&3\\ \hline
\chi_{++}&1&1&1&1&1&1\\
\chi_{+-}&1&1&1&1&-1&-1\\
\chi_{-+}&1&-1&-1&1&1&-1\\
\chi_{--}&1&-1&-1&1&-1&1\\
\rho_1&2&-2&1&-1&0&0\\
\rho_2&2&2&-1&-1&0&0
\end{array}.
\]
::: {.proof}
By <1>3,
\[
D_6\cong D_3\times C_2.
\]
The irreducible characters of a direct product are tensor products of irreducible characters of the factors. The group $D_3\cong S_3$ has two one-dimensional characters and one two-dimensional character, with values
\[
\begin{array}{c|rrr}
&1&\text{3-cycle}&\text{reflection}\\ \hline
1&1&1&1\\
\operatorname{sgn}&1&1&-1\\
\vartheta&2&-1&0
\end{array},
\]
and $C_2$ has the two characters $1$ and $\varepsilon$, where $\varepsilon(r^3)=-1$.
Tensoring these gives six irreducible characters of degrees
\[
1,1,1,1,2,2.
\]
Under the direct-product decomposition, the classes $C_1,C_4,C_5$ have trivial $C_2$ component, whereas $C_2,C_3,C_6$ have nontrivial $C_2$ component. Substituting the $D_3$ class and $C_2$ sign values gives exactly the displayed table. The degree squares sum to
\[
4\cdot1^2+2\cdot2^2=12=|D_6|,
\]
so these are all irreducible characters.
:::
:::
