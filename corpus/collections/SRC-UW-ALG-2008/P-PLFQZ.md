---
schema: qual/card@1
id: P-PLFQZ
kind: problem
title: Irreducible $\CC G$-modules have dimension at most $\sqrt{|G|}$, with an example
  of dimension $\lfloor\sqrt{|G|}\rfloor$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
- Let $G$ be a group of (finite) order $n$.
  Show that any irreducible left module over the group algebra $\mathbb CG$ has complex dimension at most $\sqrt n$.

- Give an example of a group $G$ of order $n\geq5$ and an irreducible left module over $\mathbb CG$ of complex dimension $\lfloor\sqrt n\rfloor$, the greatest integer to $\sqrt n$.
:::

::: {.solution}
<1>1. Let
\[
V_1,\dots,V_r
\]
be representatives of the irreducible complex representations of $G$, and write
\[
d_i=\dim_{\mathbb C}V_i.
\]
The left regular representation decomposes as
\[
\mathbb C G\cong\bigoplus_{i=1}^r V_i^{\oplus d_i}.
\]
::: {.proof}
By Maschke's theorem, the regular representation is completely reducible. The multiplicity of an irreducible character $\chi_i$ in the regular character $\chi_{\mathrm{reg}}$ is
\[
\langle\chi_{\mathrm{reg}},\chi_i\rangle
=\frac1{|G|}\sum_{g\in G}\chi_{\mathrm{reg}}(g)\overline{\chi_i(g)}.
\]
The regular character satisfies
\[
\chi_{\mathrm{reg}}(1)=|G|=n,
\qquad
\chi_{\mathrm{reg}}(g)=0\quad(g\ne1).
\]
Hence
\[
\langle\chi_{\mathrm{reg}},\chi_i\rangle
=\overline{\chi_i(1)}=d_i.
\]
Thus $V_i$ occurs with multiplicity $d_i$.
:::

<1>2. Therefore
\[
n=\sum_{i=1}^r d_i^2.
\]
::: {.proof}
Take complex dimensions in <1>1. The regular module $\mathbb CG$ has dimension $|G|=n$, while the summand $V_i^{\oplus d_i}$ has dimension $d_i^2$.
:::

<1>3. Every irreducible $\mathbb CG$-module $V$ satisfies
\[
\dim_{\mathbb C}V\le\sqrt n.
\]
::: {.proof}
If $V\cong V_j$, then <1>2 gives
\[
(\dim V)^2=d_j^2\le\sum_{i=1}^r d_i^2=n.
\]
Taking nonnegative square roots yields the claim.
:::

<1>4. Let $G=S_3$, so
\[
n=|S_3|=6
\qquad\text{and}\qquad
\lfloor\sqrt n\rfloor=2.
\]
Consider the subspace
\[
V=\{(z_1,z_2,z_3)\in\mathbb C^3:z_1+z_2+z_3=0\}
\]
of the permutation representation of $S_3$.
Then
\[
\dim_{\mathbb C}V=2.
\]
::: {.proof}
The coordinate-sum map
\[
\mathbb C^3\longrightarrow\mathbb C,
\qquad
(z_1,z_2,z_3)\longmapsto z_1+z_2+z_3
\]
is nonzero and linear, and $V$ is its kernel. Hence $V$ has codimension $1$ in $\mathbb C^3$ and therefore dimension $2$. Permuting coordinates preserves the coordinate sum, so $V$ is $S_3$-stable.
:::

<1>5. The $S_3$-module $V$ in <1>4 is irreducible.
::: {.proof}
Since $\dim V=2$, a proper nonzero invariant subspace would be a one-dimensional invariant line. Suppose such a line existed and let
\[
0\ne v=(a,b,c)\in V
\]
span it. The transpositions $(1\,2)$ and $(2\,3)$ preserve this line. Since each has square equal to the identity, its scalar action on the line is $+1$ or $-1$.

For $(1\,2)$, either
\[
a=b
\]
or
\[
c=0,\qquad a=-b.
\]
For $(2\,3)$, either
\[
b=c
\]
or
\[
a=0,\qquad b=-c.
\]
Checking the four combinations, together with
\[
a+b+c=0,
\]
forces $a=b=c=0$ in every case, contradicting $v\ne0$. Hence no invariant line exists, and $V$ is irreducible.
:::

<1>6. Thus $S_3$ provides the requested sharp example:
\[
\dim_{\mathbb C}V=2=\lfloor\sqrt6\rfloor.
\]
:::
