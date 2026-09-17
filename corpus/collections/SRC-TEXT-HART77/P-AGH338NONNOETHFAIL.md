---
schema: qual/card@1
id: P-AGH338NONNOETHFAIL
kind: problem
title: An injective module whose localization map is not surjective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Injective Modules
  - Localization
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the ring, injective extension and requested nonsurjectivity with the retained Hartshorne Chapter III section 3 transcription. The proof exhibits the missing class 1/x_0 and proves the required monomials remain nonzero by explicit quotient maps. It also verifies that A is nonnoetherian and that the associated sheaf is not flasque.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Without the noetherian hypothesis, (3.3) and (3.4) are false.
Let $A=k[x_0, x_1, x_2, \ldots]$ with the relations $x_0^n x_n=0$ for $n=1,2, \ldots$.
Let $I$ be an injective $A$-module containing $A$.
Show that $I \to I_{x_0}$ is not surjective.
:::

::: {.solution}
Write
$$
A=k[x_0,x_1,x_2,\ldots]/(x_0^n x_n:n\ge1),
$$
and use the same symbols for the residue classes of the variables.
Identify $A$ with its given submodule of $I$, so $1\in I$ means the image of $1_A$.

<1>1. For every $n\ge0$, $x_0^n x_{n+1}$ is nonzero in $A$, while $x_0^{n+1}x_{n+1}=0$.
In particular, $A$ is not noetherian.

::: {.proof}
For fixed $n$, define a homomorphism
$$
A\longrightarrow k[t,u]/(t^{n+1}u)
$$
by $x_0\mapsto t$, $x_{n+1}\mapsto u$, and $x_j\mapsto0$ for every other $j\ge1$.
Every defining relation maps to zero: the one with index $n+1$ maps to $t^{n+1}u$, and all the others have a zero factor.
The image of $x_0^n x_{n+1}$ is $t^nu$, which is not in the monomial ideal $(t^{n+1}u)$ of $k[t,u]$.
Thus the element is nonzero in $A$.
Its next multiple by $x_0$ is zero by the defining relation.

Consequently the ideals
$$
\Ann_A(x_0^0)\subsetneq\Ann_A(x_0)\subsetneq\Ann_A(x_0^2)\subsetneq\cdots
$$
form a strictly increasing chain: $x_{n+1}$ belongs to the $(n+1)$st annihilator and not to the $n$th.
This violates the ascending chain condition for a noetherian ring.
:::

<1>2. The class $1/x_0\in I_{x_0}$ is not in the image of $I\to I_{x_0}$.

::: {.proof}
Suppose $z\in I$ satisfies $z/1=1/x_0$.
By the equality criterion for module localization, there is an integer $n\ge0$ such that
$$
x_0^n(x_0z-1)=0,
\qquad\text{hence}\qquad x_0^{n+1}z=x_0^n
$$
in $I$.
Multiply by $x_{n+1}$.
The left side vanishes because $x_0^{n+1}x_{n+1}=0$ in $A$, whereas the right side is the image of the nonzero element $x_0^n x_{n+1}\in A$ from step <1>1.
The inclusion $A\hookrightarrow I$ makes that image nonzero.
This is a contradiction, so the displayed class cannot lift.
The argument works for every module containing $A$, and in particular for the injective module in the statement.
:::

<1>3. The associated sheaf $\widetilde I$ on $X=\Spec A$ is not flasque.

::: {.proof}
For any ring and module, the associated-sheaf construction gives
$$
\Gamma(X,\widetilde I)=I,\qquad
\Gamma(D(x_0),\widetilde I)=I_{x_0},
$$
with restriction the localization map [@Har10a, Proposition II.5.1].
Step <1>2 shows that this restriction is not surjective.
Thus $\widetilde I$ is not flasque even though $I$ is an injective module, proving the failure of the noetherian conclusions invoked in the statement.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 proves the requested nonsurjectivity, with its explicit obstruction established in step <1>1; step <1>3 gives the corresponding sheaf-theoretic counterexample.
:::
:::
