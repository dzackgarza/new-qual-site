---
schema: qual/card@1
id: E-3M6WZ
kind: exercise
title: Unique fractional linear transformation sending one circle to another with
  two prescribed values
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem title="?"}
Let $C$ and $C'$ be two circles and let $z_1 \in C$, $z_2 \notin C$, $z'_1 \in C'$, $z'_2 \notin C'$.
Show that there is a unique fractional linear transformation $f$ with $f(C) = C'$ and $f(z_1) = z'_1$, $f(z_2) = z'_2$.
:::

::: {.solution}
Main idea: both circles can be uniformized in ways that send $z_2, z_2'$ to zero.
Handling $C$:

- $f_1$: Uniformize by translating and scaling $C$ to $S^1$.
  Note that the image of $z_1$ is in $S^1$

- $f_2$: if $z_2$ was not enclosed by $C$, apply $z\mapsto 1/z$ to move $z_2$ into $\DD$.
  Otherwise just take $f_2 = \id$.
  In either case, $z_1\in S^1$ is preserved.

- $f_3$: apply a Blaschke factor $\psi_a(z)$ to move $z_2\to 0$ in $\DD$.
  Since $\psi_a$ preserves $S^1$, $z_1$ is moved to another point in $S^1$.

Define $F\da f_3 \circ f_2 \circ f_1$.
Similarly define $g_1,\cdots, g_3$ and $G$ for $C'$, so $z_2'\to 0$ in $\DD$.
Now $F(z_1), G(z_1')\in S^1$, so there is a rotation $h: z\mapsto \lambda z$ that sends $F(z_1)\to G(z_1')$.

Take the final map to be $f\da G\circ h \circ F\inv$.
:::
