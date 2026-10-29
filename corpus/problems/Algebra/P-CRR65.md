---
schema: qual/card@1
id: P-CRR65
kind: problem
title: Representations and character table of $D_4$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
(1) Describe the irreducible complex representations and character table of the dihedral group $D_4$ (order 8).

(2) Explicitly construct the 2-dimensional irreducible representation.

(3) Provide its geometric interpretation as symmetries of the square.
:::

::: {.solution}
Write
$$
D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle.
$$

::: pf

::: {.pf-step #classes}
The conjugacy classes of $D_4$ are $\{1\}$, $\{r^2\}$, $\{r,r^3\}$, $\{s,sr^2\}$, $\{sr,sr^3\}$, so $D_4$ has five irreducible complex characters.

::: pf-proof
Conjugation by $s$ inverts $r$, so $r$ and $r^3$ are conjugate and $r^2$ is central.
Conjugation by $r$ sends $sr^k$ to $sr^{k-2}$, so $sr^k$ is conjugate to $sr^{k+2}$, and no element of $D_4$ conjugates $s$ to $sr$, since $r^j(s)r^{-j}=sr^{-2j}$ and $s(s)s=s$.
The number of irreducible complex characters equals the number of conjugacy classes.
:::

:::

::: {.pf-step #linear}
$D_4$ has four one-dimensional characters, obtained by choosing independently $r\mapsto\pm1$ and $s\mapsto\pm1$.

::: pf-proof
The commutator $[s,r]=srs^{-1}r^{-1}=r^{-2}$, so $[D_4,D_4]\supseteq\langle r^2\rangle$.
The quotient $D_4/\langle r^2\rangle$ has order $4$ and every element of it has order at most $2$, so it is abelian and isomorphic to $C_2\times C_2$.
Hence $[D_4,D_4]=\langle r^2\rangle$ and $D_4^{\mathrm{ab}}\cong C_2\times C_2$, whose four characters are the stated ones.
:::

:::

::: {.pf-step #rho}
The assignment
$$
\boxed{\rho(r)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\rho(s)=\begin{pmatrix}1&0\\0&-1\end{pmatrix}}
$$
defines an irreducible two-dimensional representation with character $\chi_5=(2,-2,0,0,0)$ on the classes of step [](#classes){.pf-ref}.

::: pf-proof
The matrices satisfy $\rho(r)^4=\rho(s)^2=I$ and $\rho(s)\rho(r)\rho(s)=\rho(r)^{-1}$, so they define a representation.
The traces of $I$, $\rho(r)^2=-I$, $\rho(r)$, $\rho(s)$ and $\rho(s)\rho(r)$ are $2,-2,0,0,0$.
With class sizes $1,1,2,2,2$,
$$
\langle\chi_5,\chi_5\rangle=\frac18(4+4)=1,
$$
so $\rho$ is irreducible.
:::

:::

::: {.pf-step #table}
The character table of $D_4$ is
$$
\boxed{\begin{array}{c|ccccc}
&1&r^2&\{r,r^3\}&\{s,sr^2\}&\{sr,sr^3\}\\\hline
\chi_1&1&1&1&1&1\\
\chi_2&1&1&-1&1&-1\\
\chi_3&1&1&1&-1&-1\\
\chi_4&1&1&-1&-1&1\\
\chi_5&2&-2&0&0&0
\end{array}}
$$
and $\chi_1,\ldots,\chi_5$ are all the irreducible complex representations.

::: pf-proof
The rows $\chi_1,\ldots,\chi_4$ are the characters of step [](#linear){.pf-ref}, evaluated with $r\mapsto\pm1$ and $s\mapsto\pm1$, and $\chi_5$ is the character of step [](#rho){.pf-ref}.
These are five distinct irreducible characters, and step [](#classes){.pf-ref} shows there are exactly five.
:::

:::

::: pf-step
$\rho(r)$ is rotation of the square with vertices $(\pm1,\pm1)$ by $\pi/2$, and $\rho(s)$ is its reflection across the $x$-axis.

::: pf-proof
$\rho(r)$ sends $(x,y)$ to $(-y,x)$ and $\rho(s)$ sends $(x,y)$ to $(x,-y)$.
Both maps permute the vertices $(\pm1,\pm1)$, so $\rho$ realizes $D_4$ as the symmetry group of the square.
:::

:::

:::

:::
