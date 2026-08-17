---
schema: qual/card@1
id: E-6ROMA
kind: exercise
title: Fixed points of holomorphic self-maps of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - fixed-points
  - schwarz-lemma
  - rouche
  - blaschke-factors
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $g$ be analytic for $|z|\leq 1$ and $|g(z)| < 1$ for $|z| = 1$.

1.  Show that $g$ has a unique fixed point in $|z| < 1$.

2.  What happens if we replace $|g(z)| < 1$ with $|g(z)|\leq 1$ for
    $|z|=1$? Give an example if (a) is not true or give an proof
    if (a) is still true.

3.  What happens if we simply assume that $f$ is analytic for
    $|z| < 1$ and $|f(z)| < 1$ for $|z| < 1$? Suppose that $f(z)
    \not\equiv  z$. Can f have more than one fixed point in
    $|z| < 1$?

> Hint: The map $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$ may be useful.
:::

:::{.solution title="Part 1"}
Use Rouché: if $\abs{f(z)} < 1$ is strict when $\abs{z} = 1$, then consider $F(z) \da f(z) - z$.
Write the big part as $M(z) = z$ and the small as $m(z) = f(z)$, then on $\abs{z} = 1$
\[
\abs{m(z)} = \abs{f(z)} < 1 = \abs{z} = \abs{M(z)}
,\]
so $M(z)$ and $m(z) + M(z) = f(z) - z$ have the same number of zeros in $\DD$ -- precisely one.
:::

:::{.solution title="Part 2"}
There is still a unique fixed point.
Use the Brouwer fixed point theorem: since $g$ is holomorphic on $\bar{\DD}$, it is in particular continuous.
By the Brouwer fixed point theorem, every continuous map $\bar{\DD} \to \bar{\DD}$ has a fixed point.
If $g$ is nonconstant, then the fixed point is unique by Schwarz: without loss of generality one can assume $f(0) = 0$ by composing with a Blaschke factor.
Apply Schwarz to $f$, then if $f(a) = a$ we have the equality clause and $f(z) = \lambda z$. 
Since $a = f(a) = \lambda a$, $\lambda = 1$ and $f$ is the identity.
If $g$ is constant, then $\abs{g(z)} < 1$ on $\abs{z} = 1$ forces $g\equiv 0$.
:::

:::{.solution title="Part 3"}
Note that there is a major difference between self maps to $\DD$ versus $\bar{\DD}$.
By the argument in part 2, if $f(z)$ is not the identity then $f$ can have at most one fixed point.
Moreover, not every map $f:\DD\to\DD$ need have a fixed point: consider
\[
g: \HH &\to \HH \\
z &\mapsto z+1
.\]
Now conjugate with the Cayley map $C:\HH\to \DD$ to define $f\da CgC\inv:\DD\to \DD$ which has no fixed points at all.
:::
