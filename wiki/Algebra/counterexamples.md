---
title: Counterexamples
order: 9
problems:
  topics:
  - Counterexamples
---

# Counterexamples

Filed by the statement each one refutes, because that is the form the question takes: "is every $X$ a $Y$", with the answer nearly always no and the work being to name the witness.

## Groups

**Every subgroup of order dividing $\size G$ exists** -- false, and the converse of Lagrange.
$A_5$ has order $60$ and no subgroup of order $30$; $A_4$ has order $12$ and no subgroup of order $6$.

**Every group of order $p^3$ is abelian** -- false: $D_4$ and $Q_8$.
Order $p^2$ is the largest prime power that forces abelian.

**A group with all proper subgroups abelian is abelian** -- false: $A_4$, whose proper subgroups are cyclic or Klein.

**Normality is transitive** -- false.
$\ZZ/2 \normal V_4 \normal A_4$ but $\ZZ/2$ is not normal in $A_4$.

**A quotient of $G$ embeds in $G$** -- false in general; it holds for abelian groups and fails for $Q_8$.

## Rings

The tower and one witness per step is on [[Algebra/rings-and-ideals/which-kind-of-ring|Which kind of ring is this?]].
The three that recur:

**Every irreducible is prime** -- false: $3$ in $\ZZ[\sqrt{-5}]$, where $9 = 3\cdot 3 = (2+\sqrt{-5})(2-\sqrt{-5})$.

**A subring of a PID is a PID** -- false: $\ZZ[x] \subset \QQ[x]$.

**$R$ a PID implies $R[x]$ a PID** -- false: $\gens{2,x}\normal\ZZ[x]$.

## Modules

**Every torsion-free module is free** -- false over a non-PID: $\gens{2,x}\subseteq \ZZ[x]$.

**Every projective module is free** -- false: $\ZZ/2$ over $\ZZ/6$.

**Tensoring preserves injections** -- false: $\ZZ\xrightarrow{2}\ZZ$ tensored with $\ZZ/2$ is the zero map.

**Every short exact sequence splits** -- false: $0\to\ZZ/2\to\ZZ/4\to\ZZ/2\to 0$.

## Linear algebra

The matrix witnesses are on [[Algebra/linear-algebra/matrix-counterexamples|Matrix counterexamples]], and the ones worth having in mind:

**Same characteristic polynomial implies similar** -- false.
$\min$ and $\chi$ together are still not enough: $J_2\oplus J_2$ and $J_2\oplus J_1 \oplus J_1$ share both.

**Every real matrix has a real eigenvalue** -- false: a rotation, with $\chi_M = x^2+1$.

**Diagonalizable over $\RR$ and over $\CC$ agree** -- false, the same rotation.

## Fields

**Every extension is normal** -- false: $\QQ(2^{1/3})/\QQ$.

**Normality is transitive** -- false: $\QQ(2^{1/4})/\QQ(\sqrt2)/\QQ$, and this is the failure the Galois correspondence is built around.

**Every irreducible polynomial is separable** -- false in characteristic $p$: $x^p - t$ over $\FF_p(t)$.
True over perfect fields, which is why the hypothesis is invisible in characteristic zero.

**Every finite extension is simple** -- true in characteristic zero and false in general, the standard witness being $\FF_p(s,t)/\FF_p(s^p,t^p)$.
