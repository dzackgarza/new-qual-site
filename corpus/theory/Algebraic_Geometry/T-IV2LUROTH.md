---
schema: qual/card@1
id: T-IV2LUROTH
kind: theorem
title: Lüroth's theorem, and the Lüroth problem in higher dimension
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Curves
  - Function Fields
  - Riemann-Hurwitz
relations:
- kind: uses
  target: T-LKT0U
- kind: related-to
  target: PR-IV2INSEP
review: draft
prompts:
- State Lüroth's theorem.
- Prove it using the genus.
- Where does the proof use that $k$ is algebraically closed?
- Is the analogue true for subfields of $k(t_1, t_2)$? Of $k(t_1,t_2,t_3)$?
---

::: {.theorem title="Lüroth"}
Let $k = \kbar$ and let $L$ be a field with $k \subsetneq L \subseteq k(t)$.
Then $L$ is purely transcendental: $L = k(u)$ for some $u$.
:::

::: {.proof}
$L$ is a subfield of a finitely generated field of transcendence degree $1$, so $\trdeg_k L \leq 1$, and $\trdeg_k L = 1$ because $L \neq k$ and $k$ is algebraically closed, so any element of $L \setminus k$ is transcendental over $k$.
Such an $L$ is itself finitely generated over $k$, hence $L = k(Y)$ for a unique smooth projective curve $Y$.

The inclusion $L \subseteq k(t) = k(\PP^1)$ is a finite extension of function fields, so it is induced by a finite morphism $f : \PP^1 \to Y$.
A finite morphism of curves never decreases the genus, so $g(Y) \leq g(\PP^1) = 0$ and $g(Y) = 0$.
A genus-$0$ curve over $k = \kbar$ is $\PP^1$, so $Y \cong \PP^1$ and $L \cong k(u)$.
:::

::: {.remark title="What the proof actually rests on"}
The one input is $g(X) \geq g(Y)$ for a finite morphism $X \to Y$ of curves, and that is Riemann--Hurwitz read backwards: for separable $f$ of degree $n$,
\[
2 g_X - 2 = n(2 g_Y - 2) + \deg R, \qquad \deg R \geq 0 ,
\]
so $g_X < g_Y$ is impossible.
The inseparable case is not an exception but a separate mechanism: factor $f$ through its purely inseparable part, which preserves the genus, and apply the above to the separable part.
That is the point of [[PR-IV2INSEP]] and it is the step an examiner asks about in characteristic $p$.

Algebraic closedness is used twice, and both uses are worth naming.
It makes every element of $L \setminus k$ transcendental, and it turns $g(Y) = 0$ into $Y \cong \PP^1$ — over a general field a genus-$0$ curve is a conic, which is $\PP^1$ only when it has a rational point.
The purely field-theoretic Lüroth theorem needs neither: over any field $k$, every intermediate field $k \subsetneq L \subseteq k(t)$ is $k(u)$.
The geometric proof above buys the statement back with the curve theory instead of with field theory.
:::

::: {.remark title="The Lüroth problem"}
Restated as geometry, Lüroth says: a curve dominated by $\PP^1$ is rational, that is, unirational implies rational in dimension $1$.
Asking the same in higher dimension is the Lüroth problem, and the answer splits by dimension and by characteristic.

In dimension $2$ over $k = \kbar$ of characteristic $0$, unirational implies rational.
The proof runs through Castelnuovo's criterion, that $q = P_2 = 0$ forces rationality, and it is worth being exact about which half carries the characteristic hypothesis.
Castelnuovo's criterion itself holds in every characteristic, by Zariski and Mumford.
What fails in characteristic $p$ is the other half: a unirational surface need not satisfy $q = P_2 = 0$.
Zariski's surfaces, purely inseparable covers of $\PP^2$, are unirational and not rational, so the dimension-$2$ Lüroth statement is false as soon as $p > 0$ even though the criterion it invokes is not.

In dimension $3$ it is false even over $\CC$.
The three standard counterexamples are the smooth cubic threefold, non-rational because its intermediate Jacobian is not a Jacobian of a curve; the smooth quartic threefold, non-rational because its group of birational self-maps is too small; and the Artin--Mumford double solid, non-rational because it has torsion in $H^3$, which is a birational invariant.
All three are unirational.
Naming one obstruction with its invariant is what the question is testing, since "it is false in dimension $3$" on its own is the part everyone remembers.
:::
