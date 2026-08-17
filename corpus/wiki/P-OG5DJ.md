---
schema: qual/card@1
id: P-OG5DJ
kind: problem
title: "Let $f(x) = x^4 - 4x^2 + 2 \\in \\QQ[x]$."
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - splitting-fields
  - field-extensions
relations: []
review: draft
solved: true
---
Let $f(x) = x^4 - 4x^2 + 2 \in \QQ[x]$.

a.
Find the splitting field $K$ of $f$, and compute $[K: \QQ]$.

b.
Find the Galois group $G$ of $f$, both as an explicit group of automorphisms, and as a familiar abstract group to which it is isomorphic.

c.
Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $k$.

:::{.remark}
Not the nicest proof! Would be better to replace the ad-hoc computations at the end.
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
Note that $g(x) = x^2 - 4x + 2$ has roots $\beta = 2 \pm \sqrt{2}$, and so $f$ has roots 
\[
\alpha_1 &= \sqrt{2 + \sqrt 2} \\
\alpha_2 &= \sqrt{2 - \sqrt 2} \\
\alpha_3 &= -\alpha_1 \\
\alpha_4 &= -\alpha_2
.\]

and splitting field $K = \QQ(\theset{\alpha_i})$.

:::

:::{.proof title="of b"}
$K$ is the splitting field of a separable polynomial and thus Galois over $\QQ$.
Moreover, Since $f$ is irreducible by Eisenstein with $p=2$, the Galois group is a transitive subgroup of $S^4$, so the possibilities are:

- $S_4$
- $A_4$
- $D_4$
- $\ZZ/(2) \cross \ZZ/(2)$
- $\ZZ/(4)$

We can note that $g$ splits over $L \definedas \QQ(\sqrt 2)$, an extension of degree 2.

We can now note that $\min(\alpha, L)$ is given by $p(x) = x^2 - (2 + \sqrt 2)$, and so $[K: L] = 2$.

We then have
\[
[K: \QQ] = [K: L] [L : \QQ] = (2)(2) = 4
.\]

This $\abs{\Gal(K/\QQ)} = 4$, which leaves only two possibilities:

- $\ZZ/(2) \cross \ZZ/(2)$
- $\ZZ/(4)$

We can next check orders of elements.
Take
\[
\sigma &\in \Gal(K/\QQ) \\
\alpha_1 &\mapsto \alpha_2
.\]

Computations show that 

- $\alpha_1^2 \alpha_2^2 = 2$, so $\alpha_1 \alpha_2 = \sqrt 2$
- $\alpha_1^2 = 2 + \sqrt 2 \implies \sqrt 2 = \alpha_1^2 - 2$

and thus
\[
\sigma^2(\alpha_1) 
&= \sigma(\alpha_2) \\
&= \sigma\left(\frac{\sqrt 2}{\alpha_1}\right) \\
&= \frac{\sigma(\sqrt 2)}{\sigma(\alpha_1)} \\
&= \frac{\sigma(\alpha_1^2 - 2)}{\alpha_2} \\
&= \frac{\alpha_2^2 - 2}{\alpha_2} \\
&= \alpha_2 -2\alpha_2\inv \\
&= \alpha_2 - \frac{2\alpha_1}{\sqrt 2} \\
&= \alpha_2 -\alpha_1 \sqrt 2 \\
&\neq \alpha_1
,\]

and so the order of $\sigma$ is strictly greater than 2, and thus 4, and thus $\Gal(K/\QQ) = \theset{\sigma^k \suchthat 1\leq k \leq 4} \cong \ZZ/(4)$.

:::

:::{.proof title="of c"}
?? The subgroup of index 2 $\generators{\sigma^2}$ corresponds to the field extension $Q(\sqrt 2) / \QQ$.
:::

:::

