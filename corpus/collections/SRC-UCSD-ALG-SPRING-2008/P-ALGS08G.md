---
schema: qual/card@1
id: P-ALGS08G
kind: problem
title: "A simple ring with a minimal right ideal satisfies the minimum condition"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 7 of the official UCSD Spring 2008 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Repaired the socle argument by proving left stability of the sum of copies of a minimal right ideal, using the semisimple direct-sum lemma, and then using cyclicity of A_A to force a finite direct sum.
---

::: problem
Let $A$ be a simple ring with identity element.
Show that if $A$ has a minimal right ideal, then $A$ satisfies the minimum condition for right ideals.
:::

::: {.solution}
<1>1. Let $I$ be a minimal nonzero right ideal of $A$, and let $S$ be the sum of all right ideals of $A$ that are isomorphic to $I$ as right $A$-modules.
Then $S$ is a nonzero two-sided ideal of $A$.
::: {.proof}
By construction, $S$ is a right ideal and $I\subseteq S$, so $S\ne0$.

Let $J\subseteq A$ be a right ideal isomorphic to $I$, and let $a\in A$.
Left multiplication by $a$ defines a homomorphism of right $A$-modules
\[
\lambda_a:J\longrightarrow A,
\qquad
x\longmapsto ax.
\]
Since $J$ is simple, $\ker\lambda_a$ is either $J$ or $0$.
Thus $aJ=0$, or else $aJ$ is a simple right ideal isomorphic to $J$, hence to $I$.
In either case $aJ\subseteq S$.
Because $S$ is the sum of all such $J$, this shows $aS\subseteq S$ for every $a\in A$.
Hence $S$ is also a left ideal, so it is two-sided.
:::

<1>2. The right $A$-module $A_A$ is a sum of simple submodules.
::: {.proof}
The ring $A$ is simple and $S$ from <1>1 is a nonzero two-sided ideal.
Therefore
\[
S=A.
\]
Every summand used to define $S$ is a minimal right ideal, hence a simple right $A$-module.
Thus $A_A$ is a sum of simple submodules.
:::

<1>3. A module that is a sum of simple submodules is a direct sum of simple submodules.
::: {.proof}
Let $M$ be a sum of simple submodules.
Choose, by Zorn's lemma, a maximal family $\{M_\lambda\}_{\lambda\in\Lambda}$ of simple submodules whose sum is direct, and put
\[
N=\bigoplus_{\lambda\in\Lambda}M_\lambda.
\]
Suppose $N\ne M$.
Because $M$ is a sum of simple submodules, there is a simple submodule $T\subseteq M$ with $T\nsubseteq N$.
Now $T\cap N$ is a submodule of the simple module $T$, so it is either $0$ or $T$.
It cannot be $T$, because $T\nsubseteq N$.
Hence $T\cap N=0$, and therefore
\[
N\oplus T
\]
is a strictly larger direct sum of simple submodules, contradicting maximality.
Thus $N=M$.
:::

<1>4. The module $A_A$ is a finite direct sum of simple right ideals.
::: {.proof}
By <1>2 and <1>3, write
\[
A=\bigoplus_{\lambda\in\Lambda} I_\lambda,
\]
where every $I_\lambda$ is a simple right ideal.
Because an element of a direct sum has finite support, there is a finite set $F\subseteq\Lambda$ such that
\[
1\in\bigoplus_{\lambda\in F}I_\lambda.
\]
The finite sum on the right is a right ideal, so
\[
A=1A\subseteq\bigoplus_{\lambda\in F}I_\lambda\subseteq A.
\]
Hence
\[
A=\bigoplus_{\lambda\in F}I_\lambda,
\]
a finite direct sum of simple right $A$-modules.
:::

<1>5. Therefore $A$ satisfies the minimum condition for right ideals.
::: {.proof}
A simple module is Artinian: its only submodules are $0$ and itself.
A finite direct sum of Artinian modules is Artinian, so <1>4 implies that the right module $A_A$ is Artinian.
The submodules of $A_A$ are exactly the right ideals of $A$.
Therefore every descending chain of right ideals stabilizes; equivalently, $A$ satisfies the minimum condition for right ideals.
:::
:::
