---
schema: qual/card@1
id: P-AGH319JACOBIAN
kind: problem
title: An automorphism of $\AA^n$ has constant Jacobian
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Jacobian
  - Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.3.19. Part (b) is a historical status statement: its open-problem formulation requires characteristic zero; in positive characteristic the converse already fails in one variable. Current-status check on 2026-09-17: the characteristic-zero plane case remains open, while Gao, arXiv:2608.00222, records the July 2026 dimension-three counterexample and counterexamples in every dimension greater than two.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked part (a) directly by differentiating a polynomial inverse and taking determinants. This avoids the incorrect claim in some solution notes that every coordinate of a polynomial automorphism must be linear.'
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Garland, An Introduction to the Jacobian Conjecture (UChicago REU
    2018), Proposition 2.9, printed p. 3, which proves part (a) over C by
    the chain rule and the degree of a product; the card now quotes it.
    Checked that the identity is formal in the partial derivatives so that
    it holds over an arbitrary field, which is what the card needs. Verified
    the status claim in the card's remark against the arXiv record of Gao,
    Counterexamples to the Jacobian conjecture in dimensions greater than
    two, arXiv:2608.00222v1 (31 July 2026), which records Alpoge's three-
    dimensional counterexample of 19 July 2026 and leaves dimension two
    open. Not checked: any line of that preprint.
---

::: {.problem}
Let $\phi: \AA^n \to \AA^n$ be a morphism given by $n$ polynomials $f_1,\ldots,f_n$ in the variables $x_1,\ldots,x_n$, and let $J = \det\qty{ \frac{\partial f_i}{\partial x_j} }$ be the \dfn{Jacobian polynomial} of $\phi$.

(a) If $\phi$ is an isomorphism, in which case $\phi$ is called an \dfn{automorphism} of $\AA^n$, show that $J$ is a nonzero constant polynomial.

(b) The converse is an unsolved problem, even for $n = 2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\phi:\AA^n\to\AA^n$ is a polynomial automorphism, then its Jacobian determinant is a unit of $k[x_1,\ldots,x_n]$.

::: pf-proof

Let
$$
\psi:\AA^n\longrightarrow\AA^n
$$
be the inverse polynomial morphism, with coordinate functions $g_1,\ldots,g_n$.
Write $D\phi$ and $D\psi$ for the two Jacobian matrices.
Differentiating
$$
\psi\circ\phi=\operatorname{id}_{\AA^n}
$$
and applying the polynomial chain rule gives
$$
D\psi(\phi(x))\,D\phi(x)=I_n.
$$
Taking determinants yields the polynomial identity
$$
J_\psi(\phi(x))\,J_\phi(x)=1.
$$
Thus $J_\phi$ has a multiplicative inverse in $k[x_1,\ldots,x_n]$.

:::

:::

::: {.pf-step #s2}

Therefore $J$ is a nonzero constant, proving (a).

::: pf-proof

The only units of a polynomial ring over a field are the nonzero constants: if nonzero polynomials $a,b$ satisfy $ab=1$, total degree gives
$$
0=\deg(ab)=\deg a+\deg b,
$$
so both degrees are zero.
Applying this to step [](#s1){.pf-ref} gives
$$
J=J_\phi\in k^\times.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the mathematical assertion in part (a).
Part (b) is a status statement rather than an additional proof obligation; the qualification below records its present scope.

:::

:::

:::

::: {.remark title="Characteristic and current status of the converse"}
The open Jacobian conjecture is a characteristic-zero problem.
In characteristic $p>0$, the converse already fails for $n=1$: the polynomial map
$$
F(x)=x-x^p
$$
has derivative $F'(x)=1$, but $F(0)=F(1)=0$, so it is not an automorphism.

Hartshorne's sentence in part (b) records the status when the book was written.
As of 2026-09-17, the characteristic-zero two-variable case remains open.
The unrestricted higher-dimensional conjecture is no longer open: a counterexample in dimension three was announced in July 2026, and counterexamples in every dimension greater than two are described in Shuhong Gao, *Counterexamples to the Jacobian conjecture in dimensions greater than two*, arXiv:2608.00222.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), gives no solution to 3.19.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 3.19.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.19, PDF p. 38: if any $f_i\in k$ then $\phi$ would not be surjective, and the derivative of a linear nonconstant polynomial is a unit, so the Jacobian is a unit; he marks the converse "SKIP".
The proof above differentiates $\psi\circ\phi=\mathrm{id}$ and takes determinants, which gives the unit $J_\psi\circ\phi$ directly, and then uses that the units of a polynomial ring are the nonzero constants; it does not argue that the $f_i$ are linear, which is false in general.

The complete published argument for (a) is William Garland, *An Introduction to the Jacobian Conjecture* (University of Chicago REU 2018), Proposition 2.9, printed p. 3: "Since $F$ is a polynomial automorphism, we know there exists a polynomial mapping $G:\CC^n\to\CC^n$ which satisfies $G\circ F=\mathrm{Id}_{\CC^n}$. Therefore, note $1=J(\mathrm{Id}_{\CC^n})(z)=J(G\circ F)(z)=J(G)(F(z))\cdot J(F)(z)$ by the Chain Rule. Therefore, $J(F)$ is given by a polynomial which has a multiplicative inverse. Therefore, the degree of $J(F)$ must be $0$, so $J(F)$ must be a constant nonzero polynomial." Garland states the conjecture over $\CC$; the chain-rule identity he uses is formal in the partial derivatives and so holds over any field, which is the form step [](#s1){.pf-ref} states it in.
:::
