---
schema: qual/card@1
id: T-IV2LUROTH
kind: theorem
title: Lüroth's theorem, and the Lüroth problem in higher dimension
slogan: 'In dimension one, unirational means rational: every intermediate field $k\subsetneq L\subseteq k(t)$ is again $k(u)$.'
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
Let $k$ be an algebraically closed field and let $L$ be a field with $k \subsetneq L \subseteq k(t)$.
Then $L$ is purely transcendental: $L = k(u)$ for some $u$.
:::

::: {.proof}
$L$ is a subfield of a finitely generated field of transcendence degree $1$, so $\trdeg_k L \leq 1$, and $\trdeg_k L = 1$ because $L \neq k$ and $k$ is algebraically closed, so any element of $L \setminus k$ is transcendental over $k$.
Choose $u\in L\sm k$. Since $u$ is a nonconstant rational function of $t$, the extension $k(t)/k(u)$ is finite. Hence the intermediate field $L$ is finite over $k(u)$ and therefore finitely generated over $k$. Thus $L=k(Y)$ for a unique smooth projective curve $Y$.

The inclusion $L \subseteq k(t) = k(\PP^1)$ is a finite extension of function fields, so it is induced by a finite morphism $f : \PP^1 \to Y$.
A finite morphism of curves never decreases the genus, so $g(Y) \leq g(\PP^1) = 0$ and $g(Y) = 0$.
A genus-$0$ curve over an algebraically closed field is $\PP^1$, so $Y \cong \PP^1$ and $L \cong k(u)$.
:::

::: {.remark title="Genus inequality"}
For a finite separable morphism $f\colon X\to Y$ of degree $n$ between smooth projective curves,
$$
2 g_X - 2 = n(2 g_Y - 2) + \deg R, \qquad \deg R \geq 0 ,
$$
so $g_X < g_Y$ is impossible.
The inseparable case is not an exception but a separate mechanism: factor $f$ through its purely inseparable part, which preserves the genus, and apply the above to the separable part.
This is the role of the inseparable factorization in [[PR-IV2INSEP]].

Algebraic closedness enters twice.
It makes every element of $L \setminus k$ transcendental, and it turns $g(Y) = 0$ into $Y \cong \PP^1$ — over a general field a genus-$0$ curve is a conic, which is $\PP^1$ only when it has a rational point.
The purely field-theoretic Lüroth theorem needs neither: over any field $k$, every intermediate field $k \subsetneq L \subseteq k(t)$ is $k(u)$.
The geometric proof above buys the statement back with the curve theory instead of with field theory.
:::

::: {.remark title="The Lüroth problem"}
Restated as geometry, Lüroth says: a curve dominated by $\PP^1$ is rational, that is, unirational implies rational in dimension $1$.
Asking the same in higher dimension is the Lüroth problem, and the answer splits by dimension and by characteristic.

In dimension $2$ over $k = \kbar$ of characteristic $0$, unirational implies rational.
The proof runs through Castelnuovo's criterion, that $q=P_2=0$ forces rationality; the characteristic hypothesis enters in deducing these vanishings from unirationality.
Castelnuovo's criterion itself holds in every characteristic, by Zariski and Mumford.
What fails in characteristic $p$ is the other half: a unirational surface need not satisfy $q = P_2 = 0$.
Zariski's surfaces, purely inseparable covers of $\PP^2$, are unirational and not rational, so the dimension-$2$ Lüroth statement is false as soon as $p > 0$ even though the criterion it invokes is not.

In dimension $3$ the statement is false even over $\CC$.
A smooth cubic threefold is unirational but not rational; Clemens--Griffiths detect irrationality from its intermediate Jacobian. The Artin--Mumford construction gives a unirational threefold whose desingularization is not rational because it has nonzero torsion in $H^3$, a birational obstruction.

Smooth quartic threefolds provide another classical irrationality theorem, by Iskovskikh--Manin, but irrationality alone does not make them counterexamples to the Lüroth problem: a negative Lüroth example must also be unirational.
:::
