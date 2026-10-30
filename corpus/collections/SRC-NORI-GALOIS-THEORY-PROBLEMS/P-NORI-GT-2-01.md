---
schema: qual/card@1
id: P-NORI-GT-2-01
kind: problem
title: Kernel of $F^\times/(F^\times)^2\to E^\times/(E^\times)^2$ for a quadratic extension
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 2.1 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The first quotient was transcribed as F^x/(bar{F^x})^2; the statement now reads F^x/(F^x)^2.
---

::: {.problem}
Let F be a field of characteristic $\neq 2$ and let E be a quadratic extension of F . Show that the kernel of the natural homomorphism $F ^ { \times } / ( F ^ { \times } ) ^ { 2 } \to E ^ { \times } / ( E ^ { \times } ) ^ { 2 }$ is a group of order 2.

Deduce that if there is a chain of fields $F = E _ { 0 } \subset E _ { 1 } \subset \ldots \subset E _ { n } = E$ with deg $: ( E _ { i } / E _ { i - 1 } ) = 2$ for $i = 1 , 2 , . . . , n$ , then the kernel of the natural homomorphism $F ^ { \times } / ( { F ^ { \times } } ) ^ { 2 } \to E ^ { \times } / ( E ^ { \times } ) ^ { 2 }$ has order dividing $2 ^ { n }$
:::

::: {.solution}

::: pf

::: pf-step

Write the quadratic extension as
$$
E=F(\sqrt d)
$$
for some $d\in F^\times\setminus(F^\times)^2$.


::: pf-proof

Because $\operatorname{char}F\ne2$, every quadratic extension is separable. If $\alpha\in E\setminus F$, completing the square in its quadratic minimal polynomial shows that $E=F(\sqrt d)$ for some nonsquare $d\in F^\times$.

:::

:::

::: {.pf-step #s1-2}

The square class $[d]\in F^\times/(F^\times)^2$ is a nontrivial element of the kernel of
$$
\iota:F^\times/(F^\times)^2\longrightarrow E^\times/(E^\times)^2.
$$


::: pf-proof

The class is nontrivial because $d$ is not a square in $F$. In $E$ one has
$$
d=(\sqrt d)^2,
$$
so its image in $E^\times/(E^\times)^2$ is trivial.

:::

:::

::: {.pf-step #s1-3}

Let $a\in F^\times$ represent an arbitrary element of $\ker\iota$. Then there exist $x,y\in F$ such that
$$
a=(x+y\sqrt d)^2.
$$


::: pf-proof

Being in the kernel means exactly that $a$ becomes a square in $E$. Every element of $E$ has a unique expression $x+y\sqrt d$ with $x,y\in F$.

:::

:::

::: pf-step

Expanding the equality in step [](#s1-3){.pf-ref} gives
$$
a=x^2+dy^2+2xy\sqrt d,
$$
and hence
$$
xy=0.
$$


::: pf-proof

The left side $a$ lies in $F$. Since $1,\sqrt d$ are linearly independent over $F$, the coefficient of $\sqrt d$ on the right must vanish. Thus $2xy=0$. The characteristic assumption makes $2\ne0$, so $xy=0$.

:::

:::

::: {.pf-step #s1-5}

If $y=0$, then $a=x^2$ and $[a]=1$. If $x=0$, then $a=dy^2$ and $[a]=[d]$.


::: pf-proof

These are the two alternatives forced by $xy=0$. Since $a\ne0$, in the first case $x\ne0$, and in the second $y\ne0$, so the indicated square classes are defined.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\ker\iota=\{1,[d]\},
$$
so
$$
\boxed{\cardinality{\ker\iota}=2.}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} shows both displayed classes lie in the kernel and are distinct; step [](#s1-5){.pf-ref} shows there are no others.

:::

:::

::: {.pf-step #s1-7}

For the tower
$$
F=E_0\subset E_1\subset\cdots\subset E_n=E,
$$
write
$$
V_i=E_i^\times/(E_i^\times)^2
$$
and let
$$
\phi_i:V_{i-1}\to V_i
$$
be the natural map. Then
$$
\cardinality{\ker\phi_i}=2
$$
for every $i$.


::: pf-proof

Each extension $E_i/E_{i-1}$ is quadratic. Since the original field has characteristic different from $2$, every field in the tower does also. Step [](#s1-6){.pf-ref} therefore applies at every stage.

:::

:::

::: {.pf-step #s1-8}

If
$$
\Phi_j=\phi_j\circ\cdots\circ\phi_1:V_0\to V_j,
$$
then
$$
\cardinality{\ker\Phi_j}
\mid
\cardinality{\ker\Phi_{j-1}}\,\cardinality{\ker\phi_j}.
$$


::: pf-proof

Restrict $\Phi_{j-1}$ to $\ker\Phi_j$. Its image lies in $\ker\phi_j$, and its kernel is exactly $\ker\Phi_{j-1}$. Hence the first isomorphism theorem gives an injection
$$
\ker\Phi_j/\ker\Phi_{j-1}\hookrightarrow\ker\phi_j.
$$
Thus the quotient order divides $\cardinality{\ker\phi_j}$, proving the displayed divisibility.

:::

:::

::: {.pf-step #s1-9}

Induction gives
$$
\cardinality{\ker\Phi_n}\mid2^n.
$$


::: pf-proof

For $j=1$, step [](#s1-7){.pf-ref} gives $\cardinality{\ker\Phi_1}=2$. If $\cardinality{\ker\Phi_{j-1}}$ divides $2^{j-1}$, then steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} show that $\cardinality{\ker\Phi_j}$ divides $2^{j-1}\cdot2=2^j$.

:::

:::

::: {.pf-step #s1-10}

Since $\Phi_n$ is the natural map
$$
F^\times/(F^\times)^2\longrightarrow E^\times/(E^\times)^2,
$$
its kernel has order dividing
$$
\boxed{2^n}.
$$


::: pf-proof

The natural map along the entire field inclusion is the composite of the natural maps at each stage, namely $\Phi_n$. Apply step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the first assertion and step [](#s1-10){.pf-ref} proves the deduction for a tower of quadratic extensions.

:::

:::

:::
